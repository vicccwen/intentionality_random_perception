import numpy as np
import random

def generate_str(string):
    num_choice = ["0", "1"]
    return [np.random.choice(num_choice) for i in range(len(string))]