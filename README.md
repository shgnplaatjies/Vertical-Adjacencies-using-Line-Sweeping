# Vertical Adjacencies using Line Sweeping

This repository contains Python scripts for generating data, computing vertical adjacencies of rectangles using a brute force approach, and measuring the performance of the algorithm.

## Contents

- `graph_gen.py`: Generates sample data of rectangles and saves the results in CSV files.
- `rectangledata.py`: Generates rectangles data for testing.
- `brute_force.py`: Implements a brute force approach to compute vertical adjacencies between rectangles.
- `timings.csv`: Stores the timing results of the algorithm for different input sizes.
- `adjacencies.csv`: Stores the computed vertical adjacencies of rectangles for different input sizes.
- `rectangles.csv`: Stores the generated rectangles data for different input sizes.

## Usage

### 1. Generate Sample Data

To generate sample data for testing, run the following command:

```bash
python graph_gen.py
```

### 2. Compute Vertical Adjacencies

To compute vertical adjacencies using a brute force approach, execute the following command:

```bash
python brute_force.py
```

### 3. Analyze Performance

The performance of the algorithm is measured and stored in `timings.csv`. You can analyze the timing results to understand the algorithm's efficiency.

## Dependencies

- Python 3.x
- NumPy
- Matplotlib
- CSV module
