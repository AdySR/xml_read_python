from io import StringIO
import xml.etree.ElementTree as ET
import pandas as pd


xml_data = open('./sample2.xml', 'r').read()  # Read file
root = ET.XML(xml_data)
print(root)

all_records =[]

for i, child in enumerate(root):
    record ={}
    for subchild in child:
        record[subchild.tag] =subchild.text
    all_records.append(record)

df = pd.DataFrame(all_records)

print(df)
