This directory contains the original files and scripts to parse them.

The scripts should be run in the following order:

- initial_parse.py -> neel_data.json, left_over_neel_data.txt
- I then manually correct left_over_neel_data.txt -> left_over_neel_data_reformated.txt
- second_parse.py -> neel_data_afterLeftOver.json
- composition_processing.py -> processed_neel.json