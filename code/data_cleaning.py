import pandas as pd
import os

current_file_path = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(current_file_path))
data_raw_folder = os.path.join(project_root, 'data', 'raw')



df = pd.read_csv(os.path.join(data_raw_folder, 'Electric_Vehicle_Population_Data.csv'))
df.dropna(inplace=True)


df.to_csv(os.path.join(project_root, "data", "Data_Cleaned.csv"), index=False)