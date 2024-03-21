import numpy as np
import json
import subprocess


#create chem-comp vector
with open('romerodata/curie/processed_curie.json') as f:
    processed_curie = json.load(f)

comp_list = []
for key in processed_curie:
    comp_list.append(processed_curie[key]["composition"])
#comp_list.pop(726)
comp_array = np.array(comp_list)

#print(comp_array[726])
#np.savetxt('Magnetic_Classification/rhysdata/chemical_comps.txt', comp_array, fmt='%s')
#subprocess.run(['open', 'Magnetic_Classification/rhysdata/chemical_comps.txt'])


#create curie temp vector
with open('romerodata/curie/processed_curie.json') as f:
    processed_curie = json.load(f)

temp_list = []
for key in processed_curie:
    temp_list.append(processed_curie[key]["curie_temperature"])
#temp_list.pop(726)
temp_array = np.array(temp_list)


#print(temp_array[726])
#np.savetxt('Magnetic_Classification/rhysdata/curie_temps.txt', temp_array, fmt='%s')
#subprocess.run(['open', 'Magnetic_Classification/rhysdata/curie_temps.txt'])