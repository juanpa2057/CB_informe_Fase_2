# %% [markdown]
# 

# %%
# this cell enables relative path imports
import os
from dotenv import load_dotenv
import pickle
load_dotenv()
_PROJECT_PATH: str = os.environ["_project_path"]
_PICKLED_DATA_FILENAME: str = os.environ["_pickled_data_filename"]
#_CSV_DATA_FILENAME: str = os.environ["_csv_data_filename"]



import sys
from pathlib import Path
project_path = Path(_PROJECT_PATH)
sys.path.append(str(project_path))

# %%
# import all your modules here
import time
import json
import pandas as pd

import config_v2 as cfg
from library_ubidots_v2 import Ubidots as ubi

# %%
#blob_name = r"data/data_weekly_report.pkl"
#downloader.upload_pkl_file(bancolombia_pkl,blob_name, blob_container)

# %%
# set your constants here
baseline=cfg.BASELINE
study=cfg.STUDY
#study = ['2025-01-01', '2025-02-01']

# %%
print(study)
print(baseline)

# %%
df_devices = ubi.get_available_devices_v2(label='bancolombia-f2', level='group', page_size=1000)
df_vars = ubi.get_available_variables(list(df_devices['device_id']))

# %%
df_devices

# %%
#df_vars = ubi.get_available_variables(['65b00756bd7602000b6876b8'])

# %%
df_vars

# %%
df_vars = df_vars[df_vars['variable_label'].isin(cfg.WHITELISTED_VAR_LABELS)]
VAR_IDS_TO_REQUEST = list(df_vars['variable_id'])
VAR_ID_TO_LABEL = dict(zip(df_vars['variable_id'], df_vars['variable_label']))

# %%
#leer el archivo data_weekly_report.pkl y guardarlo en un dataframe llamado df1
df1 = pd.read_pickle(r'C:\Digitalizacion\Bancolombia\CB_informe_Fase_2\data\data_weekly_report.pkl')


# %%
df1.info()

# %%
#study = ['2025-06-02', '2025-06-09']

# %%
CHUNK_SIZE = 10
DATE_INTERVAL_REQUEST = {'start': study[0], 'end': study[1]}
df = None
lst_responses = []
n_vars = len(VAR_IDS_TO_REQUEST)
print(f"Making request for the following interval: Study:{study[0]}, Study:{study[1]}")
for idx in range(0, ubi.ceildiv(len(VAR_IDS_TO_REQUEST), CHUNK_SIZE)):
    idx_start = idx * CHUNK_SIZE
    idx_end = (idx + 1) * CHUNK_SIZE
    chunk = VAR_IDS_TO_REQUEST[idx_start:idx_end]
    response = ubi.make_request(
        chunk, 
        DATE_INTERVAL_REQUEST, 
    )
    if response.status_code == 204 or response.status_code >= 500:
        print(f"Empty response for chunk {idx}")
        time.sleep(10)
        response = ubi.make_request(
        chunk, 
        DATE_INTERVAL_REQUEST,)
    current_idx = idx_end+1
    if (current_idx > n_vars):
        current_idx = n_vars
    print(f"Progress: {100*(current_idx)/n_vars:0.1f}%")
    print(f"Response status code: {response.status_code}")
    if (response.status_code != 204) and  (len(response.json()['results']) >0 ):
        lst_responses.append(response)
    else: 
        print(f"Empty response for chunk {idx}")
df = ubi.parse_response(lst_responses, VAR_ID_TO_LABEL)

# %%
#Unir el dataframe dfprogress: 30.5%Response status code: 200Progress: 34.8%Response status code: 200Progress: 39.1%Response status code: 200Progress: 43.3%Response status code: 200 y df1 en uno que se llame df_full / esto es para mas adelante
df = pd.concat([df1, df], axis=0, ignore_index=False)

# para quitar el indixe de "datatime" y volverlo columna 
df.reset_index(inplace=True)

# Quitar duplicados 
df = df.drop_duplicates()

# Establecer la columna "datetime" como el índice
df.set_index('datetime', inplace=True)


# %%
pd.to_pickle(df, project_path / 'data'/ _PICKLED_DATA_FILENAME)

# %%
df.index[(df.index.month == 1)&(df.index.year == 2025)].unique()

# %%



