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
