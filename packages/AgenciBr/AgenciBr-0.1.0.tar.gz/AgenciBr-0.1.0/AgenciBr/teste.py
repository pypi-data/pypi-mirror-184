import pandas as pd
from datetime import datetime
import numpy as np


print(pd.date_range(start=datetime(1980,1,1), end="1/1/1990").to_numpy())