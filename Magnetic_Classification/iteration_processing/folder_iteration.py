import numpy as np
import pandas as pd
from pymatgen.io.cif import CifParser
import os

for filename in os.listdir('/Users/rhyscampbell/Documents/projects/Magnetic_Classification/magndata/mcif'):
   print(filename)
   try:
      with open(os.path.join('Magnetic_Classification/magndata/mcif', filename)) as file:
         molecule = file.read()
      parser = CifParser.from_str(molecule)
      structure = parser.parse_structures()[0]
      #print(structure)
      composition = structure.composition
      print(composition)
   except:
      pass