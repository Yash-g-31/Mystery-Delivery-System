# FastBox Delivery Simulation

## Overview

FastBox is a Python-based simulation program that models a delivery system where agents pick up packages from warehouses and deliver them to destinations. The program assigns packages to the nearest available agent based on Euclidean distance, with tie-breaking by total distance traveled. It calculates efficiency metrics and generates a report identifying the most efficient agent.

## Features

- **Agent Assignment**: Assigns packages to the closest agent from the warehouse location.
- **Distance Calculation**: Uses Euclidean distance for all calculations.
- **Efficiency Metrics**: Computes total distance traveled and efficiency (distance per package delivered).
- **Report Generation**: Outputs a JSON report with agent statistics and the best-performing agent.

## Requirements

- Python 3.x
- Standard library modules: `json`, `math` (no external dependencies required)

## Input Format

The program reads input from a JSON file (default: `test_case_7.json`). The JSON structure should include:

- `agents`: A dictionary of agent IDs mapped to their initial [x, y] coordinates.
- `warehouses`: A dictionary of warehouse IDs mapped to their [x, y] coordinates.
- `packages`: A list of packages, each with:
  - `warehouse`: The ID of the warehouse where the package is located.
  - `destination`: The [x, y] coordinates of the delivery destination.

Example input structure:
```json
{
  "agents": {
    "agent1": [0, 0],
    "agent2": [10, 10]
  },
  "warehouses": {
    "warehouse1": [5, 5]
  },
  "packages": [
    {
      "warehouse": "warehouse1",
      "destination": [15, 15]
    }
  ]
}
```

## How to Run

1. Ensure you have a valid input JSON file in the same directory (e.g., `test_case_7.json`).
2. Run the program:
   ```
   python main.py
   ```
3. The program will process the data and generate `report.json`.

To run with a different test case, modify the file path in `main.py` (line 3) to point to another JSON file, such as `test_case_1.json` to `test_case_10.json` or `base_case.json`.

## Output

The program generates `report.json` with the following structure:

- For each agent: `packages_delivered`, `total_distance` (rounded to 2 decimals), and `efficiency` (distance per package).
- `best_agent`: The ID of the agent with the lowest efficiency (most efficient).

Example output:
```json
{
  "agent1": {
    "packages_delivered": 2,
    "total_distance": 25.46,
    "efficiency": 12.73
  },
  "best_agent": "agent1"
}
```

## Algorithm Details

1. Load agents, warehouses, and packages from the input JSON.
2. For each package:
   - Find the nearest agent to the package's warehouse.
   - If distances are equal, choose the agent with less total distance traveled.
   - Update the agent's total distance (to warehouse + to destination).
   - Move the agent to the destination.
   - Increment packages delivered.
3. Calculate efficiency for each agent.
4. Identify the best agent (lowest efficiency).
5. Save the report to `report.json`.


## Troubleshooting

- **File Not Found Error**: Ensure the specified JSON file exists in the directory.
- **Invalid JSON**: Verify the input JSON matches the expected format.
- **No Packages Delivered**: If an agent has 0 packages, efficiency is set to 0.0.
- **Distance Calculations**: All distances use Euclidean formula; ensure coordinates are numeric.

