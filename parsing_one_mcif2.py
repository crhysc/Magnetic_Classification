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

# Create lists to store data
elements = []
type_symbols = []
fractional_x = []
fractional_y = []
fractional_z = []
occupancies = []

# Extract atom site information
for site in structure.sites:
    elements.append(site.species_string)
    type_symbols.append(site.species_string.split()[0])
    fractional_x.append(site.frac_coords[0])
    fractional_y.append(site.frac_coords[1])
    fractional_z.append(site.frac_coords[2])
    occupancies.append(site.properties.get("occupancy", 1.0))

# Create a pandas DataFrame
data = {
    "Element": elements,
    "Type Symbol": type_symbols,
    "Fractional x": fractional_x,
    "Fractional y": fractional_y,
    "Fractional z": fractional_z,
    "Occupancy": occupancies,
}

df = pd.DataFrame(data)

# Display the DataFrame
print(df)
