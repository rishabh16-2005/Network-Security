from ruamel.yaml import YAML 
import pandas as pd 
data = pd.read_csv('Network_Data/phisingData.csv')

yaml_data = {
    'columns':[{col:str(data[col].dtype)} for col in data.columns],
    'numerical_columns' : [col for col in data.columns if pd.api.types.is_numeric_dtype(data[col])]
}

yaml = YAML()
yaml.indent(mapping=2, sequence=4, offset=2)  # perfect indentation
with open('data_schema/schema.yaml', 'w') as f:
    yaml.dump(yaml_data, f)

