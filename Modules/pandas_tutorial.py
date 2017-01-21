import pandas as pd

stats = {
    'Month': ['Jan', 'Feb', 'March', 'April'],
    'Expenses': [2350, 3400, 2700, 2200],
    'Income': [4000, 4000, 4000, 4000]
}

df = pd.DataFrame(stats)
# df = df.set_index('Month')
print(df.Month)