# The name of the folder where all inputs are stored
IN_DIR = "data"
# Folder name where all new data will be written to
OUT_DIR = "output"
# Name of the file where change propagation values are stored
CP_VALUES = "Values.xlsx"

import pandas as pd
from pathlib import Path


def merge_1_file(filename):
    """Creates a new csv file with the Change propagation values and substitutes on the DSM "X" spots """
    dsm = pd.read_csv(filename, dtype="string")
    dsm = dsm.set_index("HIERARCHY ID", drop=False)
    element = dsm[["ELEMENT NAME", "HIERARCHY ID"]].set_index("HIERARCHY ID").to_dict()["ELEMENT NAME"]

    cp = pd.read_excel(f"{IN_DIR}/{CP_VALUES}")

    def find_cp_value(a, b, cp):
        """Looks for a couple of element text description and returns the change propagation value
        Inputs:
            a: Name of the first element to look
            b: Name of the second element to look
            cp: pandas DataFrame containing the names of the first two columns and the change propagation value in the third

        This funcion assumes that the dataframe is named "Element 1", "Element 2" and "Value"

        """
        possible = cp[(cp["Element 1"] == a) & (cp["Element 2"] == b)]
        if len(possible) == 1:
            return str(possible["Value"].tolist()[0])
        else:
            possible = cp[(cp["Element 1"] == b) & (cp["Element 2"] == a)]
            if len(possible) == 1:
                return str(possible["Value"].tolist()[0])
            else:
                raise ValueError(f"Could not find on {CP_VALUES} a Change Propagation value for the combination: \n"
                                 f"- '{a}' \n"
                                 f"- '{b}'\n"
                                 f"The combination was found on {filename.name}")

    for row in dsm["HIERARCHY ID"].to_list():
        for col in dsm["HIERARCHY ID"].to_list():
            if isinstance(dsm.at[row, col], str):
                dsm.loc[row, [col]] = find_cp_value(element[row], element[col], cp)

    out_filename = Path(OUT_DIR) / filename.name
    dsm.to_csv(out_filename, index=False)


def rm_tree(pth):
    pth = Path(pth)
    for child in pth.glob('*'):
        if child.is_file():
            child.unlink()
        else:
            rm_tree(child)
    pth.rmdir()


def main():
    p_out = Path(OUT_DIR)
    # deleting and recreate output folder if not exist
    print(f"deleting and recreating {p_out}")
    rm_tree(p_out)
    p_out.mkdir(parents=True, exist_ok=True)

    for file in Path(".").glob(f"{IN_DIR}/**/*.csv"):
        print(f"updating {file}")
        merge_1_file(file)
    print("\n*** Done! ***\n")




if __name__ == "__main__":
    main()
