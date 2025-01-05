# ---
# jupyter:
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# Add description here
#
# *Note:* You can open this file as a notebook (JupyterLab: right-click on it in the side bar -> Open With -> Notebook)


# %%
# Uncomment the next two lines to enable auto reloading for imported modules
# # %load_ext autoreload
# # %autoreload 2
# For more info, see:
# https://docs.ploomber.io/en/latest/user-guide/faq_index.html#auto-reloading-code-in-jupyter

# %% tags=["parameters"]
# If this task has dependencies, list them them here
# (e.g. upstream = ['some_task']), otherwise leave as None.
upstream = None

# This is a placeholder, leave it as None
product = None


# %%
# your code here...


# %%
# python imports
from pathlib import Path
import pickle

# %%
# unpickle shared variables

# %% [markdown]
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <h1> Path to base folders (we generate on each run/play/iteration) <h1/>
# %%
# this is the main folder, everything else gets placed inside here
_ABSOLUTE_PATH_TO_MY_FOLDER = str(Path(product["ABSOLUTE_PATH_TO_MY_FOLDER"]))
_ABSOLUTE_PATH_TO_MY_FOLDER

# %%
# folder where we place images/pngs of graphs and tables
_ABSOLUTE_PATH_TO_IMAGES_FOLDER = f"{_ABSOLUTE_PATH_TO_MY_FOLDER}/images"
# remember to create the actual path/folder as the above is just a string
Path(_ABSOLUTE_PATH_TO_IMAGES_FOLDER).mkdir(exist_ok=True, parents=True)

# %%
# folder where we place excel view of dataframes
_ABSOLUTE_PATH_TO_EXCEL_OUTPUT_FOLDER = f"{_ABSOLUTE_PATH_TO_MY_FOLDER}/excelOutput"
# remember to create the actual path/folder as the above is just a string
Path(_ABSOLUTE_PATH_TO_EXCEL_OUTPUT_FOLDER).mkdir(exist_ok=True, parents=True)

# %%
# fodler where we place reports
_ABSOLUTE_PATH_TO_REPORTS_FOLDER = f"{_ABSOLUTE_PATH_TO_MY_FOLDER}/reports"
# remember to create the actual path/folder as the above is just a string
Path(_ABSOLUTE_PATH_TO_REPORTS_FOLDER).mkdir(exist_ok=True, parents=True)

# %%


# %%

# %%
# %% [markdown]
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <h1> .xlsx files names <h1/>
# %%
ABSOLUTE_PATH_TO_DATA_1_XLSX = f"{_ABSOLUTE_PATH_TO_IMAGES_FOLDER}/ABSOLUTE_PATH_TO_DATA_1_XLSX"
# pickle it to use it later
Path(product["ABSOLUTE_PATH_TO_DATA_1_XLSX"]).parent.mkdir(exist_ok=True, parents=True)
Path(product["ABSOLUTE_PATH_TO_DATA_1_XLSX"]).write_bytes(pickle.dumps(ABSOLUTE_PATH_TO_DATA_1_XLSX))
# print output
ABSOLUTE_PATH_TO_DATA_1_XLSX

# %%
ABSOLUTE_PATH_TO_DATA_2_XLSX = f"{_ABSOLUTE_PATH_TO_IMAGES_FOLDER}/ABSOLUTE_PATH_TO_DATA_2_XLSX"
# pickle it to use it later
Path(product["ABSOLUTE_PATH_TO_DATA_2_XLSX"]).parent.mkdir(exist_ok=True, parents=True)
Path(product["ABSOLUTE_PATH_TO_DATA_2_XLSX"]).write_bytes(pickle.dumps(ABSOLUTE_PATH_TO_DATA_2_XLSX))
# print output
ABSOLUTE_PATH_TO_DATA_2_XLSX


# %% [markdown]
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <h1> images/pngs <h1/>
# %%
_ABSOLUTE_PATH_TO_GRAPH_1_PLOTLY_PNG = f"{_ABSOLUTE_PATH_TO_IMAGES_FOLDER}/ABSOLUTE_PATH_TO_GRAPH_1_PLOTLY_PNG"
# pickle it to use it later
Path(product["ABSOLUTE_PATH_TO_GRAPH_1_PLOTLY_PNG"]).parent.mkdir(exist_ok=True, parents=True)
Path(product["ABSOLUTE_PATH_TO_GRAPH_1_PLOTLY_PNG"]).write_bytes(pickle.dumps(_ABSOLUTE_PATH_TO_GRAPH_1_PLOTLY_PNG))
# print output
_ABSOLUTE_PATH_TO_GRAPH_1_PLOTLY_PNG
