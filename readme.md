# AI Lab Experiments

This repository contains various AI lab experiments implementing different algorithms and concepts.

## Prerequisites

Before running the experiments, make sure you have Python 3.x installed. Then install the required libraries using pip:

```bash
pip install sympy
```
```
pip install pgmpy
```
```
pip install networkx
```
```
pip install matplotlib
```

## Experiments

### Experiment 3: Graph Traversal Algorithms (BFS and DFS)
#### Files: 
- `exp3_BFS.py`: Breadth-First Search implementation
- `exp3_DFS.py`: Depth-First Search implementation

#### Execution:
```bash
python exp3_BFS.py  # Run BFS algorithm
```
```bash
python exp3_DFS.py  # Run DFS algorithm
```
Both files contain a sample graph implementation and will show the traversal order of nodes.

### Experiment 4: A* Path Finding Algorithm
#### File: `exp4.py`

#### Description:
Implements the A* pathfinding algorithm with multiple path detection capability using a 2D maze.

#### Execution:
```bash
python exp4.py
```
The program will find optimal paths in a predefined maze using heuristic-based search.

### Experiment 6: Logical Reasoning (Propositional Logic)
#### File: `exp6.py`

#### Description:
Implements logical reasoning using propositional logic to prove the classic "Socrates is mortal" syllogism.

#### Execution:
```bash
python exp6.py
```
The program will demonstrate logical entailment using SymPy's logic module.

### Experiment 7: Goal Stack Planning
#### File: `exp7.py`

#### Description:
Implements a goal stack planning algorithm for block arrangement problems.

#### Execution:
```bash
python exp7.py
```
The program will demonstrate goal-based planning for block arrangement.

### Experiment 8: Bayesian Networks (Monty Hall Problem)
#### File: `exp8.py`

#### Description:
Implements a Bayesian Network for the Monty Hall problem using pgmpy.

#### Execution:
```bash
python exp8.py
```
The program will:
1. Create a Bayesian network
2. Display probability distributions
3. Generate a network visualization (saved as 'Data.png')
4. Calculate posterior probabilities




