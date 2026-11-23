# Sensor Data Analysis Tool

A Python program that generates simulated sensor readings or loads them
from a CSV file, calculates statistics and displays two graphs.

## Requirements

Python 3, NumPy and Matplotlib.

## Installation

Open the project folder in VS Code and open the terminal.

Create a virtual environment:
python3 -m venv .venv

Activate it:
source .venv/bin/activate

Install the required libraries:
python -m pip install -r requirements.txt


## Run


python sensor_monitor.py


Choose one of the following options:

1: Generate new readings. Enter the sensor type, number of readings,
  minimum value, maximum value and alert threshold.
2: Load an existing CSV file. Enter the sensor type, alert threshold
  and CSV filename.

Generated readings are rounded to two decimal places and automatically
saved to `readings.csv` in the current working folder.
Generating new readings overwrites this file.

## Results

The program displays:

- Number of readings.
- Mean, minimum, maximum and standard deviation.
- Number and values of readings strictly above the alert threshold.
- A line plot with the alert threshold.
- A histogram showing the distribution of readings.

Close both graph windows to finish the program.

## CSV format

The CSV uses the columns `sample` and `reading`.
The loading function reads numerical values from the `reading` column.
An example data file is included as `readings.csv`.

## Error handling

Invalid numerical input, non-positive reading counts, incorrect limits
and file access errors produce messages and return to the main menu.