import os
import pandas as pd
from pymatgen.io.cif import CifParser

# Specify the folder containing .mcif files
folder_path = "/Users/rhyscampbell/Documents/projects/Magnetic_Classification/data/raw/magndata/mcif"

# Initialize an empty list to store DataFrames
dataframes = []

# Iterate through .mcif files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".mcif"):
        # Create the full path to the .mcif file
        file_path = os.path.join(folder_path, filename)

        # Parse the .mcif file
        parser = CifParser(file_path)
        structure = parser.get_structures()[0]  # Assuming there is only one structure in the CIF file

        # Extract atomic coordinates
        atomic_coordinates = []
        for site in structure.sites:
            atomic_coordinates.append({"Element": site.specie, "x": site.coords[0], "y": site.coords[1], "z": site.coords[2]})

        # Create a DataFrame for the atomic coordinates
        df = pd.DataFrame(atomic_coordinates)

        # Add any additional information you want to the DataFrame
        df["Formula"] = structure.composition.reduced_formula
        df["Space Group"] = structure.get_space_group_info()[1]

        # Append the DataFrame to the list
        dataframes.append(df)

# Concatenate all DataFrames into a single DataFrame
final_dataframe = pd.concat(dataframes, ignore_index=True)

# Print the final DataFrame
print(final_dataframe.head())

