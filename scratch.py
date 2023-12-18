import pandas as pd
from pymatgen.io.cif import CifParser

# Specify the path to the CIF-like file
cif_file_path = "data/raw/magndata/mcif/0.1_LaMnO3.mcif"

# Read the CIF content from the file
with open(cif_file_path, 'r') as file:
    cif_content = file.read()

# Parse CIF content using pymatgen
parser = CifParser.from_string(cif_content)
structure = parser.get_structures()[0]

# Create a dictionary to store occupancy data
data = {
    "Element": [],
    "Occupancy": [],
}

# Extract occupancy information
for site in structure.sites:
    data["Element"].append(site.species_string)
    data["Occupancy"].append(site.properties.get("occupancy", 1.0))

# Create a pandas DataFrame
df_occupancy = pd.DataFrame(data)

# Display the DataFrame
print(df_occupancy)

