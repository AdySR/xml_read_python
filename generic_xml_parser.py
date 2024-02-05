import csv
import xmltodict
from module_flatten_json import flatten_json
import pandas as pd


# Reading xml file
with open(r"CDXFSchema12142023\CDXFSchema12142023\NB XML_GL653063380-00_082223_v2.xml", 'r') as file:
    filedata = file.read()
    
# Converting xml to python dictionary (ordered dict)    
data_dict = xmltodict.parse(filedata)

# print(data_dict)

flatten_dict = flatten_json(data_dict)

df_json= pd.DataFrame(flatten_dict , ['key'])

df_json.to_csv('./df_json.csv')
# print(df_json.size)
# print(flatten_dict)

# print(type(flatten_dict))
# str = str(data_dict)


# with open('./out.txt','w') as fileout:
#     fileout.write(str)

# fileout.close()
file.close()
