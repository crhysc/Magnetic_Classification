import numpy as np
import pandas as pd
from pymatgen.io.cif import CifParser
import os

for filename in os.listdir('magndata/mcif'):
    with open(os.path.join('magndata/mcif', filename)) as file:
       molecule = file.read()
    parser = CifParser.from_str(molecule)
    structure = parser.parse_structures()[0]
    print(structure)