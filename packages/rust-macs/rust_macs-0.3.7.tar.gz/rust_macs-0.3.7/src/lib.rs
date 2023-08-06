use pyo3::prelude::*;

use rand::seq::{index::sample, SliceRandom};
use rand::{Rng, thread_rng};
use rand::distributions::{WeightedIndex, Distribution};

type Node = usize;
type AntType = usize;

#[derive(Debug)]
struct Graph {
    distance_matrix: Vec<Vec<f32>>,
    ant_passage_matrix: Vec<Vec<Vec<bool>>>,
    probability_matrix: Vec<Vec<Vec<f32>>>,

    /// (Symmetrical) Pheromone table of ant s from node i to node j
    /// Access using pheromones\[s]\[i]\[j]
    pheromones: Vec<Vec<Vec<f32>>>,

}


impl Graph {
    fn new(distance_matrix: &Vec<Vec<f32>>, n_types: usize, n_nodes: usize, init_pheromones: f32) -> Self {
        Self {
            distance_matrix: distance_matrix.clone(),
            ant_passage_matrix: vec![vec![vec![false; n_nodes]; n_nodes]; n_types],
            probability_matrix: vec![vec![vec![0.0; n_nodes]; n_nodes]; n_types],
            pheromones: vec![vec![vec![init_pheromones; n_nodes]; n_nodes]; n_types],
        }
    }

    fn greedy_path(&self, source: Node, dest: Node) -> (Vec<Node>, f32) {
        let mut current_node = source;
        let mut visited = vec![current_node];
        while current_node != dest {
            let candidates = self.find_candidate_nodes(current_node, self.distance_matrix.len(), &visited);
            current_node = self._greedy_next_node(current_node, &candidates);
            visited.push(current_node);
        }
        let cost = self.evaluate_path_cost(&visited);
        (visited, cost)
    }

    fn _greedy_next_node(&self, current: Node, candidates: &Vec<Node>) -> Node {
        let mut best_edge_dist = f32::INFINITY;
        let candidates = match candidates.len() == 0 {
            true => self._find_neighbours(current),
            false => candidates.clone()
        };
        let mut best_neighbour: Node = *candidates.last().unwrap();

        for i in candidates {
            if i != current {
                let edge_dist = self.distance_matrix[current][i];
                if edge_dist <= best_edge_dist {
                    best_edge_dist = edge_dist;
                    best_neighbour = i;
                }
            }
        }
        best_neighbour
    }

    fn _find_neighbours(&self, current: Node) -> Vec<Node> {
        let mut candidates: Vec<Node> = vec![];
        let n_nodes = self.distance_matrix[current].len();
        for i in sample(&mut thread_rng(), n_nodes, n_nodes) {
            if self.distance_matrix[current][i] != 0. {
                candidates.push(i);
            }
        }
        candidates
    }

    fn evaluate_join_paths(&self, joint_paths: &Vec<(Vec<Node>, f32, f32)>, disjoint_val_method: i8)
                           -> Vec<(Vec<Node>, f32, f32)> {
        let mut paths = vec![];
        let mut costs = vec![];
        for (path, _, _) in joint_paths {
            paths.push(path.clone());
            costs.push(self.evaluate_path_cost(path));
        }
        let disjoint_vals = self.evaluate_disjoint_values(&paths, disjoint_val_method);
        let ret: Vec<(Vec<Node>, f32, f32)>= paths.iter()
            .zip(disjoint_vals.iter())
            .zip(costs.iter())
            .map(|((x, &y), &z)| (x.clone(), y, z))
            .collect();
        /*
        println!("{:?}", paths);
        println!("{:?}", costs);
        println!("{:?}", disjoint_vals);
        println!("{:?}", ret);
         */
        ret
    }

    /// Compute the disjoint value of each path
    fn evaluate_disjoint_values(&self, paths: &Vec<Vec<Node>>, disjoint_val_method: i8) -> Vec<f32> {
        let mut disj_values = vec![];
        let mut passage_matrix: Vec<Vec<Vec<bool>>> = vec![vec![vec![false; self.distance_matrix.len()];
                                                                self.distance_matrix.len()]; paths.len()];
        // Convert path to edges and compute the passage matrix
        let mut edges_paths: Vec<Vec<(Node, Node)>> = vec![];
        for s in 0..paths.len() {
            edges_paths.push( Graph::path_nodes_to_path_edges(&paths[s]));
            for edge in &edges_paths[s] {
                passage_matrix[s][edge.0][edge.1] = true;
                passage_matrix[s][edge.1][edge.0] = true;
            }
        }
        for s in 0..paths.len() {
            let mut sum = 0.;
            let mut nb_shared_edges = 0;
            for edge in &edges_paths[s] {
                let mut n_others = 0;
                for s2 in 0..paths.len() {
                    if s != s2 && passage_matrix[s2][edge.0][edge.1] {
                        n_others += 1;
                    }
                }
                if n_others != 0 {
                    nb_shared_edges += 1;
                }

                if disjoint_val_method == 1 {
                    sum += n_others as f32;
                } else {
                    sum += self.distance_matrix[edge.0][edge.1] * n_others as f32;
                }
            }
            if disjoint_val_method == 1 {
                sum /= nb_shared_edges as f32;
            }
            disj_values.push(sum);
        }
        disj_values
    }

    fn evaluate_path_cost(&self, path: &Vec<Node>) -> f32 {
        let edges = Graph::path_nodes_to_path_edges(path);
        let mut cost = 0.;
        for edge in edges {
            cost += self.distance_matrix[edge.0][edge.1];
        }
        cost
    }

    fn path_nodes_to_path_edges(path_nodes: &Vec<Node>) -> Vec<(Node, Node)>{
        let mut edges: Vec<(Node, Node)> = vec![];
        for k in 1..path_nodes.len() {
            edges.push((path_nodes[k-1], path_nodes[k]))
        }
        edges
    }

    fn update_passage_on_path_for_type(&mut self, a_type: AntType, path: &Vec<Node>) {
        let path_edges = Graph::path_nodes_to_path_edges(path);
        self.reset_ant_passage_matrix_for_type(a_type);
        for edge in path_edges {
            self.update_passage_on_edge(a_type, edge.0, edge.1);
        }
        //todo!()?
    }

    fn update_passage_on_edge(&mut self, a_type: AntType, from: Node, to: Node) {
        self.ant_passage_matrix[a_type][from][to] = true;
        self.ant_passage_matrix[a_type][to][from] = true;
    }

    fn apply_local_pheromones(&mut self, from: Node, to: Node, ant_type: AntType, rho: f32, tau_0: f32) {
        self.pheromones[ant_type][from][to] *= 1.-rho;
        self.pheromones[ant_type][from][to] += rho*tau_0;

        self.pheromones[ant_type][to][from] *= 1.-rho;
        self.pheromones[ant_type][to][from] += rho*tau_0;
    }

    /// Apply global pheromones rule on edge (from, to) (and thus also (to, from)
    fn apply_global_pheromones(&mut self, from: Node, to: Node, ant_type: AntType, rho: f32, delta_tau: f32) {
        let new_val = (1. - rho) * self.pheromones[ant_type][from][to] + rho*delta_tau;
        self.pheromones[ant_type][from][to] = new_val;
        self.pheromones[ant_type][to][from] = new_val;
    }

    /// Compute the probability matrix where entry \[s]\[i]\[j] corresponds to the probability
    /// of an ant of type s to go to node j from node i.
    fn compute_probability_matrix(&mut self, beta: f32, gamma: f32) {
        for s in 0..self.probability_matrix.len() { // Loop over types
            self.compute_prob_matrix_for_type(beta, gamma, s);
        }
    }

    fn compute_prob_matrix_for_type(&mut self, beta: f32, gamma: f32, s: AntType) {
        for i in 0..self.probability_matrix[s].len() {
            let mut denum: f32 = 0.;
            for j in 0..self.probability_matrix[s][i].len() {
                if self.distance_matrix[i][j] != 0. { // Don't compute for impossible nodes
                    let heuristic: f32 = 1. / self.distance_matrix[i][j];
                    let other_pheromones = self._compute_other_types_pheromones(i, j, s);
                    let numerator: f32 = self.pheromones[s][i][j] * heuristic.powf(beta) * other_pheromones.powf(gamma);
                    self.probability_matrix[s][i][j] = numerator;
                    denum += numerator;
                }
                /*else {
                    self.probability_matrix[s][i][j] = 0.;
                }*/
            }
            for j in 0..self.probability_matrix[s][i].len() {
                self.probability_matrix[s][i][j] = self.probability_matrix[s][i][j] / denum;
            }
        }
    }

    /// Compute the the sum of the pheromones on an edge that are not from a given type
    fn _compute_other_types_pheromones(&self, from: Node, to: Node, a_type: AntType) -> f32 {
        let mut other_pheromones = 0.;
        for other_type in 0..self.pheromones.len() {
            if other_type != a_type {
                other_pheromones += self.pheromones[other_type][from][to];
            }
        }
        other_pheromones
    }

    fn reset_ant_passage_matrix(&mut self) {
        for s in 0..self.ant_passage_matrix.len() {
            self.reset_ant_passage_matrix_for_type(s);
        }
    }

    fn reset_ant_passage_matrix_for_type(&mut self, a_type: AntType) {
        for i in 0..self.ant_passage_matrix[a_type].len() {
            for j in 0..self.ant_passage_matrix[a_type][i].len() {
                self.ant_passage_matrix[a_type][i][j] = false;
            }
        }
    }

    fn find_candidate_nodes(&self, current_node: Node, cl_size: usize, visited: &Vec<Node>) -> Vec<Node> {
        let mut candidates = vec![];
        let n_nodes = self.distance_matrix[current_node].len();
        for i in sample(&mut thread_rng(), n_nodes, n_nodes) {
            if self.distance_matrix[current_node][i] != 0. && !visited.contains(&i) {
                candidates.push(i);
                if candidates.len() == cl_size {
                    break;
                }
            }
        }
        candidates
    }
}

#[derive(Debug)]
struct Ant {
    a_type: AntType,
    current_node: Node,
    path: Vec<Node>
}

impl Ant {

    fn choose_node_from_current(&self, graph: &Graph, candidates: &Vec<Node>, q0: f32) -> Node {
        let q = thread_rng().gen::<f32>();

        // TODO : change
        return if q <= q0 {
            // Exploit
            let mut best: (f32, Node) = (-f32::INFINITY, 0);
            for &candidate in candidates {
                let candidate_prob = graph.probability_matrix[self.a_type][self.current_node][candidate];
                if candidate_prob >= best.0 {
                    best = (candidate_prob, candidate);
                }
            }
            best.1
        } else {
            // Explore

            // Use probability of each candidate as weight for sampling
            let candidate_weights: Vec<f32> = candidates.iter().map(|&c| {
                graph.probability_matrix[self.a_type][self.current_node][c]
            }).collect();
            let dist = WeightedIndex::new(&candidate_weights).unwrap();
            let mut rng = thread_rng();
            candidates[dist.sample(&mut rng)]
        }
    }

    fn choose_random_neighbour_from_current(&self, graph: &Graph) -> Node {
        let candidates: Vec<Node> = graph.distance_matrix[self.current_node].iter()
            .enumerate()
            .filter(|(_, &dist)| dist!= 0.)
            .map(|(idx, _)| idx)
            .collect();
        *candidates.choose(&mut thread_rng()).unwrap()
    }

    fn move_to_node(&mut self, node: Node) {
        self.path.push(node);
        self.current_node = node;
    }

    // Evaluate the current tour of the ant and return its cost and disjoint value
    fn evaluate_tour(&self, graph: &Graph, disjoint_val_method: i8) -> (f32, f32) {
        //println!("Evaluating the disjoint value with method {disjoint_val_method} for path \n{:?}", self.path);
        //println!("With other ants : {:?}", graph.ant_passage_matrix);
        let mut tour_cost = 0.;
        let mut tour_disjoint_value = 0.;
        let mut n_shared_edges = 0;
        for node_idx in 0..(self.path.len()-1) {
            let edge = (self.path[node_idx], self.path[node_idx+1]);
            let edge_cost = graph.distance_matrix[edge.0][edge.1];

            // Compute number of other ants type on an edge
            let mut other_ants_on_edge = 0;
            for s in 0..graph.ant_passage_matrix.len() {
                if s != self.a_type && graph.ant_passage_matrix[s][edge.0][edge.1]  {
                    other_ants_on_edge += 1;
                }
            }

            if other_ants_on_edge != 0 {
                n_shared_edges += 1;
            }

            tour_cost += edge_cost;
            if disjoint_val_method == 1 {
                // Compute the average number of ants per shared edge
                tour_disjoint_value += other_ants_on_edge as f32;
            } else {
                // Compute the cost of shared edges weighted by nb of sharers
                tour_disjoint_value += edge_cost*other_ants_on_edge as f32;
            }
        }
        if disjoint_val_method == 1 && n_shared_edges != 0{
            tour_disjoint_value /= n_shared_edges as f32;
        }
        //println!("Found {tour_cost}, {tour_disjoint_value}");
        //println!("=================");
        (tour_cost, tour_disjoint_value)
    }

    fn build_tour(&mut self, graph: &mut Graph, dest: Node, cl_size: usize, q0: f32, rho: f32, tau0: f32) {
        loop {
            let candidates: Vec<Node> = graph.find_candidate_nodes(self.current_node, cl_size, &self.path);
            let next_node: Node = match candidates.len() != 0 {
                true => self.choose_node_from_current(graph, &candidates, q0),
                false => self.choose_random_neighbour_from_current(graph)
            };
            graph.apply_local_pheromones(self.current_node, next_node, self.a_type, rho, tau0);

            self.move_to_node(next_node);
            if next_node == dest {
                break;
            }
        }
    }

    fn reset_path(&mut self) {
        self.path.clear();
    }

}

#[derive(Debug)]
struct MacsOptimizer {
    n_ants: usize,
    n_types: usize,
    ants: Vec<Vec<Ant>>,
    init_pheromones: f32,
    beta: f32,
    q0: f32,
    q0_increase: f32,
    q0_max: f32,
    gamma: f32,
    rho: f32,

    graph: Graph,

    /// Array containing the best path of each type of ant, its cost and its disjoint value
    best_paths: Vec<(Vec<Node>, f32, f32)>,
}

impl MacsOptimizer {
    fn new(n_ants: usize, n_types: usize, init_pheromones: f32, beta: f32, q0: f32, gamma: f32, rho: f32,
           distance_matrix: &Vec<Vec<f32>>, q0_increase: f32, q0_max: f32) -> Self {
        let n_nodes: usize = distance_matrix.len();

        // Create ants and pheromones
        let mut ants: Vec<Vec<Ant>> = vec![];
        let mut pheromones = vec![vec![vec![init_pheromones; n_nodes]; n_nodes]; n_types];
        for i in 0..n_types {
            let mut ants_i = vec![];
            for _ in 0..n_ants {
                ants_i.push(Ant {
                    a_type: i,
                    path: vec![],
                    current_node: 0
                });
            }
            ants.push(ants_i);

            for j in 0..n_nodes {
                pheromones[i][j][j] = 0.0; // No edge going from a node to itself
            }
        }

        let mut res = Self {
            n_ants, n_types, ants, init_pheromones, beta, q0, gamma, rho, q0_increase, q0_max,
            graph: Graph::new(&distance_matrix, n_types, n_nodes, init_pheromones),
            best_paths: vec![(vec![], f32::INFINITY, f32::INFINITY); n_types],
        };
        res.graph.compute_probability_matrix(beta, gamma);
        res
    }

    fn optimize(&mut self, source: usize, dest: usize, t_max: usize, cl_len: usize,
                disjoint_val_method: i8) -> &Vec<(Vec<Node>, f32, f32)> {
        let mut q0_increase_tstep = t_max;
        if self.q0_increase != 0. {
            q0_increase_tstep = (t_max as f32 * self.q0_increase/ (self.q0_max - self.q0)) as usize;
        }

        self._init_ants(source);

        //"Initial run of the ants based on heuristics"
        self._build_first_path(source, dest, disjoint_val_method);

        // Main loop
        for t in 0..t_max {
            if t % q0_increase_tstep == 0 {
                self.q0 += self.q0_increase;
            }
            //println!("Iteration {t} for optimizer with {} ants for each of the {} types", self.n_ants, self.n_types);
            // Build tour for each ant
            for k in 0..self.n_ants {
                for s in 0..self.n_types {
                    //print!("\tAnt {k}, type {s} started...");
                    let ant: &mut Ant = &mut self.ants[s][k];
                    //print!(" initial values are {:?}", ant);
                    ant.reset_path();
                    ant.move_to_node(source);
                    ant.build_tour(&mut self.graph, dest, cl_len, self.q0, self.rho,
                                   self.init_pheromones);
                    self.graph.compute_probability_matrix(self.beta, self.gamma);
                    //print!(" finished with tour {:?}", ant.path);
                    //println!();
                }
            }

            //println!("Fininshed running each ant");

            // Parse paths and find the best for each type
            for s in 0..self.ants.len() {
                for k in 0..self.ants[s].len() {
                    let ant = &self.ants[s][k];
                    let (path_cost, path_disjoint_val) = ant.evaluate_tour(&self.graph, disjoint_val_method);

                    /*
                    if t==0 {
                        //println!("First best path for anttype {s} is {:?}", ant.path);
                        self.best_paths[s].0 = ant.path.clone();
                        self.graph.update_passage_on_path_for_type(s, &ant.path);
                    }
                     */
                    // Compare with current best path for type s
                    if Self::better_path_found(self.best_paths[s].2, self.best_paths[s].1, path_cost, path_disjoint_val) {
                        self.best_paths[s] = (ant.path.clone(), path_cost, path_disjoint_val);
                        self.graph.update_passage_on_path_for_type(s, &ant.path);
                    }
                }
            }

            //self.best_paths = self.graph.evaluate_join_paths(&self.best_paths, disjoint_val_method);
            //println!("Recomputed best paths to {:?}", self.best_paths);
            //self.graph.reset_ant_passage_matrix();
            //println!("Current best paths : {:?}", self.best_paths);

            // Global pheromone update for next iteration
            for s in 0..self.n_types {
                self._apply_global_pheromones(s);
                //self._apply_global_pheromones_only_best_tour(s);
            }
        }
        self.best_paths = self.graph.evaluate_join_paths(&self.best_paths, disjoint_val_method);

        &self.best_paths
    }

    fn _build_first_path(&mut self, source: usize, dest: usize, disjoint_val_method: i8) {
        let (best_path, best_len) = self.graph.greedy_path(source, dest);
        let best_disjoint_val = self.graph
            .evaluate_disjoint_values(&vec![best_path.clone(); self.n_types], disjoint_val_method);
        for s in 0..self.n_types {
            // Initial run based on heuristic
            self.best_paths[s] = (best_path.clone(), best_len, best_disjoint_val[s]);
            self.graph.update_passage_on_path_for_type(s, &best_path);
        }
    }

    fn _init_ants(&mut self, source: usize) {
        for s in 0..self.n_types {
            for k in 0..self.n_ants {
                self.ants[s][k].move_to_node(source);
            }
        }
    }

    fn _apply_global_pheromones_only_best_tour(&mut self, ant_type: AntType) {
        let edges = Graph::path_nodes_to_path_edges(
            &self.best_paths[ant_type].0);
        let delta_tau = 1./ self.best_paths[ant_type].1;

        for edge in edges {
            self.graph.apply_global_pheromones(edge.0, edge.1, ant_type, self.rho, delta_tau);
        }
    }

    fn _apply_global_pheromones(&mut self, ant_type: AntType) {
        // Loop through every edge and apply the global pheromone update for given ant_type
        for i in 0..self.graph.pheromones[ant_type].len() {
            for j in 0..self.graph.pheromones[ant_type][i].len() {
                // If edge ij is in best path of ant_type then delta_tau = 1/L
                if i < j {
                    /*
                    let delta_tau: f32 = match self.edge_in_best_path(ant_type, i, j) {
                        true => 1. / self.best_paths[ant_type].1, // Length of best path
                        false => 0.
                    }; */
                    // TODO : remove?
                    let delta_tau = 1./ self.best_paths[ant_type].1;
                    self.graph.apply_global_pheromones(i, j, ant_type, self.rho, delta_tau);
                }
            }
        }
        self.graph.compute_probability_matrix(self.beta, self.gamma)
    }

    fn better_path_found(best_disjoint_val: f32, best_disjoint_val_path_cost: f32, path_cost: f32, path_disjoint_val: f32) -> bool {
        path_disjoint_val < best_disjoint_val || (path_disjoint_val == best_disjoint_val && path_cost < best_disjoint_val_path_cost)
    }

    fn edge_in_best_path(&self, a_type: AntType, from: Node, to: Node) -> bool {
        let path = &self.best_paths[a_type].0;
        let path_edges: Vec<(Node, Node)> = path.iter()
            .enumerate()
            .skip(1)
            .map(|(idx, &node)| {
                (path[idx-1], node)
            })
            .collect();
        path_edges.contains(&(from, to)) || path_edges.contains(&(to, from))
    }
}

#[pyfunction]
fn optimize_macs(distance_matrix: Vec<Vec<f32>>, n_ants: usize, n_types: usize,
                 init_pheromones: f32, beta: f32, q0: f32, gamma: f32, rho: f32, source: usize,
                 dest: usize, t_max: usize, cl_len: usize, disjoint_val_method: i8,
                 q0_increase: Option<f32>, q0_max: Option<f32>) -> PyResult<Vec<(Vec<Node>, f32, f32)>> {
    let q0_increase = q0_increase.unwrap_or(0.);
    let q0_max = q0_max.unwrap_or(0.);
    let mut macs = MacsOptimizer::new(n_ants, n_types, init_pheromones, beta, q0, gamma,
        rho, &distance_matrix, q0_increase, q0_max);
    let best_paths = macs.optimize(source, dest, t_max, cl_len, disjoint_val_method);
    Ok(best_paths.clone())
}

/// A Python module implemented in Rust.
#[pymodule]
fn rust_macs(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(optimize_macs, m)?)?;
    Ok(())
}