import random
import csv
import numpy as np
import matplotlib.pyplot as plt


def get_user_input():
    sensor_type = input("Enter sensor type: ").strip()
    if sensor_type == "":
        raise ValueError("Sensor type cannot be empty.")

    count = int(input("Enter number of readings: "))
    if count <= 0:
        raise ValueError("Number of readings must be greater than zero.")

    minimum = float(input("Enter minimum sensor value: "))
    maximum = float(input("Enter maximum sensor value: "))
    if minimum >= maximum:
        raise ValueError("Minimum must be less than maximum.")

    threshold = float(input("Enter alert threshold: "))
    return sensor_type, count, minimum, maximum, threshold

def generate_readings(count, minimum, maximum):
    random.seed(7)
    readings = []

    for _ in range(count):
        value = random.uniform(minimum, maximum)
        readings.append(value)

    return np.array(readings)

def calculate_statistics(readings):
    print("\nNumber of readings:", len(readings))
    print(f"Mean: {np.mean(readings):.2f}")
    print(f"Minimum: {np.min(readings):.2f}")
    print(f"Maximum: {np.max(readings):.2f}")
    print(f"Standard deviation: {np.std(readings):.2f}")

def find_outliers(readings, threshold):
    high_readings = readings[readings > threshold]

    print("Alert threshold:", threshold)
    print("Number of readings above threshold:", len(high_readings))
    print("Values above threshold:")

    for value in high_readings:
        print(f"{value:.2f}")

    return high_readings

def save_readings(filename, readings):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["sample", "reading"])

        for sample_number, value in enumerate(readings, start=1):
            writer.writerow([sample_number, value])


def load_readings(filename):
    readings = []

    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            readings.append(float(row["reading"]))

    if len(readings) == 0:
        raise ValueError("The CSV file contains no readings.")

    return np.array(readings)
