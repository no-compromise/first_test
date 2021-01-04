import pandas as pd

pasazieri = pd.read_csv('titanic.csv')

iba_s_vekom = pasazieri[pasazieri['Age'].notna()]


print(pasazieri.shape)
print(iba_s_vekom.shape)