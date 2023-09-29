import numpy as np
import random
import json



def generate_str():
    num_choice = ["0", "1"]
    num_list = [np.random.choice(num_choice) for i in range(8)]
    return ' '.join(num_list)


many_strings = []
for s in range(200):
    many_strings.append(generate_str())



json_data = json.dumps(many_strings)
json_data