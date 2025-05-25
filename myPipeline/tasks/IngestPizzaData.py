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
upstream = []

# This is a placeholder, leave it as None
product = None


# %%
# your code here...

# %%
# python imports
import polars as pl

from thepizzaconundrumproblem.ConstantsDataModule import _PI
from thepizzaconundrumproblem.PizzaFromNySliceDataModule import _NY_REGULAR_BASE_PIZZA, PizzaFromNySliceLargeBaseDto, PizzaFromNySliceRegularDto
from thepizzaconundrumproblem.PizzaFromRomansDataModule import _ROMANS_THICK_BASE_PIZZA

# %%


# %%
_MY_LIST_OF_ALL_PIZZAS_DF = pl.from_dicts(
    [
        vars(_NY_REGULAR_BASE_PIZZA),
        vars(PizzaFromNySliceLargeBaseDto()),
        _ROMANS_THICK_BASE_PIZZA.__dict__,
    ],
)
_MY_LIST_OF_ALL_PIZZAS_DF

# %%
