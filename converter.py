import re
import pandas as pd

def convert_csv_to_dc_txt(path_to_csv, outputpath):
    df = pd.read_csv(path_to_csv)
    complete_string = ""

    for idx, row in df.iterrows():

        values = [str(x) for x in list(row.values)]
        columns = [str(x)+":" for x in list(df.columns)]
        both = " ".join([" ".join(x) for x in zip(columns, values)])
        both = both.replace("\n\n", "")
        complete_string += both + " \n\n "
        
    f = open(outputpath, "w")
    f.write(complete_string)
    f.close()

convert_csv_to_dc_txt("depremyardim/depremyardim_v1.csv", "txt/depremyardim_v1.txt")    
convert_csv_to_dc_txt("depremyardim/depremyardim_v2.csv", "txt/depremyardim_v2.txt")    
convert_csv_to_dc_txt("depremyardim/depremyardim_v3.csv", "txt/depremyardim_v3.txt")    
convert_csv_to_dc_txt("depremyardim/depremyardim_v4.csv", "txt/depremyardim_v4.txt")
convert_csv_to_dc_txt("depremyardim/depremyardim_v5.csv", "txt/depremyardim_v5.txt")