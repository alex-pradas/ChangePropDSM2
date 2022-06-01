## Background
This script was created to solve Arindam's need to substitute X's on DSM's for actual values.

## Instructions for Arindam

### Set up python environment

1. Ensure you have python installed in your computer. You can open a terminal and type ``python -V`` 
and it will tell you the python version. I created it using Python 3.10 but other versions will likely work.
2. Create a new python or conda environment, install the python packages listed in ``requirements.txt``

### Preparing the inputs

3. Create a new folder anywhere in your PC where you have writing rights
4. In that folder, create a subfolder called data.
5. In `data`, put all DSM's .cvs files that you want to change from X to numbers
6. In `data`, put an Excel file named `Values.xlsx` containing the CP values for each pair.
   - The name has to be specific so use the template.
7. copy main.py to `data`

### Running the script

7. Open a terminal on the working folder location
8. Activate the python/conda environment
9. Run python main.py
   - A new folder called `output` will appear with your data in it
   - If you have an existing `output` folder, it will be deleted and recreated.

## Other
- This repo contains a dummy set of outputs in case you don't even want to run it.
- This code has NOT been properly tested.

Good luck!
