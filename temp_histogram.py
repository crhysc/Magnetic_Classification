import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_json('data/raw/romerodata/curie/processed_curie.json')

curie_temps = []

for key, value in data.items():
    curie_temp_i = value.get("curie_temperature")
    if curie_temp_i is not None:
        curie_temps.append(curie_temp_i)

# Create a histogram
plt.hist(curie_temps, bins=100, color='blue', alpha=0.7)

# Add labels and a title
plt.xlabel('Curie Temperatures')
plt.ylabel('Frequency')
plt.title('Frequency of Curie Temperatures in MAGNDATA')

# Show the plot
plt.show()

