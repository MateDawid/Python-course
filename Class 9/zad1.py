import pandas as pd

df = pd.read_csv(r'E:\[PROGRAMOWANIE]\Python\Akademia Kodu\Class 9\2019.csv') #data frame
#print(df.head()) #wyświetla pierwsze dane
#print(df.columns) #wyświetla listę kolumn
print(type(df))
max_index = 0 #indeks z elementem maksymalnym
min_index = 0 #indeks z elementem minimalnym
for index in df.index:
    if (df['Score'][index]>df['Score'][max_index]):
        max_index = index
    if (df['Score'][index]<df['Score'][min_index]):
        min_index = index
print(df['Country or region'][max_index],df['Score'][max_index])
print(df['Country or region'][min_index],df['Score'][min_index])