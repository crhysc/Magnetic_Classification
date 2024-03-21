This directory contains the original files and scripts to parse them.

The scripts should be run in the following order:

- initial_parse.py ->curie_data.json, left_over_curie_data.txt
- I then manually correct left_over_curie_data.txt -> left_over_curie_data_reformated.txt
- second_parse.py -> curie_data_afterLeftOver.json
- composition_processing.py -> processed_curie.json