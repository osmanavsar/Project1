import pandas as pd
pd.options.display.max_rows = 1000
pd.options.display.max_columns = 1000

region = pd.read_csv(r'C:\Users\Osman\Desktop\saglik.txt', sep=",")
print(region)

print()

hospital = pd.read_csv(r'C:\Users\Osman\Desktop\hastane.txt', sep=",")
print(hospital)


