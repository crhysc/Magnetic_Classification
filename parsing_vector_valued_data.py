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

# Extract relevant information
ids = []
kxkykz = []

for prop_vector in structure.site_properties['_parent_propagation_vector']:
    ids.append(prop_vector['id'])
    kxkykz.append(prop_vector['kxkykz'])

# Create a Pandas DataFrame
df = pd.DataFrame({'id': ids, 'kxkykz': kxkykz})

# Print the DataFrame
print(df)
