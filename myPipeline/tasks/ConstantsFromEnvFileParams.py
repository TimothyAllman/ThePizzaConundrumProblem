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
from pathlib import Path
import pickle
import datetime as dt


# %%
INPUT_DATE_AS_A_DATETIME = dt.strptime(MY_DATE, "%Y-%m-%d")
# pickle/store stuff to use later
Path(str(product["THING_1"])).parent.mkdir(exist_ok=True, parents=True)
Path(str(product["THING_1"])).write_bytes(pickle.dumps(INPUT_DATE_AS_A_DATETIME))
# print output
INPUT_DATE_AS_A_DATETIME

# %%
INPUT_DATE_AS_STRING = INPUT_DATE_AS_A_DATETIME.strftime("%Y-%m-%d")
# pickle/store stuff to use later
Path(str(product["INPUT_DATE_AS_STRING"])).parent.mkdir(exist_ok=True, parents=True)
Path(str(product["INPUT_DATE_AS_STRING"])).write_bytes(pickle.dumps(INPUT_DATE_AS_STRING))
# print output
INPUT_DATE_AS_STRING
