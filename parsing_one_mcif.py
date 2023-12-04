import pandas as pd
from pymatgen.io.cif import CifParser

# Specify the path to the CIF-like file
cif_file_path = "data/raw/magndata/mcif/0.1_LaMnO3.mcif"

# Read the CIF content from the file
with open(cif_file_path, 'r') as file:
    cif_content = file.read()

# Parse CIF content using pymatgen
parser = CifParser.from_str(cif_content)
structure = parser.get_structures()[0]

# Create a dictionary to store the data
data = {
    "Element": [],
    "Type Symbol": [],
    "Fractional x": [],
    "Fractional y": [],
    "Fractional z": [],
}

# Extract atom site information
for site in structure.sites:
    data["Element"].append(site.species_string)
    data["Type Symbol"].append(site.species_string.split()[0])  # Assuming the type symbol is the first part of the species string
    data["Fractional x"].append(site.frac_coords[0])
    data["Fractional y"].append(site.frac_coords[1])
    data["Fractional z"].append(site.frac_coords[2])
    
# Create a pandas DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)