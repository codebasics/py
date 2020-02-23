"""
Introducing pandas using namespace pd,
such that you can call pandas class using pd instead of pandas.
"""

import pandas as pd

# Dict object, with arbitrary data.
stats = {
    'Month': ['Jan', 'Feb', 'March', 'April'],
    'Expenses': [2350, 3400, 2700, 2200],
    'Income': [4000, 4000, 4000, 4000]
}

# stats is now a pandas data frame object.
df = pd.DataFrame(stats)
# df = df.set_index('Month')
print(df.Month)
