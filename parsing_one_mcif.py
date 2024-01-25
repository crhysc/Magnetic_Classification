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
    "Occupancy": [],
    "Space Group Name (H-M Alt)": [],
    "International Table Number": [],
    "Transform Pp abc": [],
    "Cell Length a": [],
    "Cell Length b": [],
    "Cell Length c": [],
    "Cell Angle alpha": [],
    "Cell Angle beta": [],
    "Cell Angle gamma": [],
}

# Extract atom site information
for site in structure.sites:
    data["Element"].append(site.species_string)
    data["Type Symbol"].append(site.species_string.split()[0])  # Assuming the type symbol is the first part of the species string
    data["Fractional x"].append(site.frac_coords[0])
    data["Fractional y"].append(site.frac_coords[1])
    data["Fractional z"].append(site.frac_coords[2])
    data["Occupancy"].append(site.properties.get("occupancy", 1.0))

# Extract parent space group information
parent_space_group = structure.get_space_group_info()
print("Parent Space Group Info:", parent_space_group)

# Fill in crystallographic information (or "N/A" if not available)
data["Space Group Name (H-M Alt)"] = [parent_space_group.symbol] if parent_space_group.symbol else ["N/A"]
data["International Table Number"] = [parent_space_group.number] if parent_space_group.number else ["N/A"]
data["Transform Pp abc"] = [parent_space_group.transform_pbc] if parent_space_group.transform_pbc else ["N/A"]
data["Cell Length a"] = [structure.lattice.a] if structure.lattice.a else ["N/A"]
data["Cell Length b"] = [structure.lattice.b] if structure.lattice.b else ["N/A"]
data["Cell Length c"] = [structure.lattice.c] if structure.lattice.c else ["N/A"]
data["Cell Angle alpha"] = [structure.lattice.alpha] if structure.lattice.alpha else ["N/A"]
data["Cell Angle beta"] = [structure.lattice.beta] if structure.lattice.beta else ["N/A"]
data["Cell Angle gamma"] = [structure.lattice.gamma] if structure.lattice.gamma else ["N/A"]

# Create a pandas DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)
