import pandas as pd

data_frame = pd.DataFrame()

print(data_frame)

if (len(data_frame) == 0):
    print('data_frame is empty, as expected\n')
else:
    print('data_frame is not empty, unexpected\n')

data_frame = pd.read_csv('Inlämning 4/Test.csv', sep=',', dtype='category')
print(data_frame)

for column in data_frame.columns:
    print("-------------column-------------\n" + str(column) + "\n")
    print(
        "-------------data_frame[column]-------------\n" + str(data_frame[column]) + "\n")
    print("-------------data_frame[column].cat.categories-------------\n" +
          str(data_frame[column].cat.categories) + "\n")
    print("-------------data_frame[column].astype('category').cat.codes-------------\n" +
          str(data_frame[column].astype('category').cat.codes) + "\n")
for column in data_frame.columns:
    print("--------" + str(column) + "--------")
    for part in data_frame[column].astype('category').cat.codes:
        print(part, '\n')


data_frame = pd.read_csv('Inlämning 4/Test.csv', sep=',', dtype='category')
for column in data_frame.columns:
    print(f'-------------column-------------\n{str(column)}\n')

for idx, row in data_frame.iterrows():
    if idx % 2 == 0:
        print(f'-------------row-------------\n{str(row)}\n')

print(data_frame[data_frame.columns[0]].cat.categories)
for column in data_frame.columns:
    print(f'-------------categories-------------\n')
    print(str(data_frame[column].cat.categories)), '\n'
