import xmlschema
from pprint import pprint
from module_flatten_json import flatten_json
import pandas as pd


xs = xmlschema.XMLSchema('./xsd_sample1.xsd')
dict_xsd = xs.to_dict('./xsd_sample1.xsd')

# print(dict_xsd)

flatten_json_data = flatten_json(dict_xsd)
df_json= pd.DataFrame(flatten_json_data , ['key'])

df_json.to_csv(r'./df_json.csv')
print(df_json)
