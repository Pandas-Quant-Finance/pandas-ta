import pandas as pd
from pandas_ta import monkey_patch_dataframe

print("pandas version", pd.__version__)
monkey_patch_dataframe()