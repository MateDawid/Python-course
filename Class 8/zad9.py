import pandas as p
df = p.read_csv(r'E:\[PROGRAMOWANIE]\Python\Akademia Kodu\Class 9\2019.csv')
print(df.columns)
print(type(df))
max_index = 0
min_index = 0
for index in df.index:
    if df['Score'][index] > df['Score'][max_index]:
        max_index = index
    if df['Score'][index] < df['Score'][min_index]:
        min_index = index
print(f"Najszczęśliwszym państwem jest {df['Country or region'][max_index]}.")
print(f"Najmniej szczęśliwym państwem jest {df['Country or region'][min_index]}.")