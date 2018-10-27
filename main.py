import datetime
import pandas as pd


def calculate_values(df):
    print(f'\nTotal number of rows: {df.shape[0]}\n')
    print(f'\nMax value of each columns:\n{df.max()}\n')
    print(f'\nMin value of each columns:\n{df.min()}\n')
    print(f'\nAverage value of each columns:\n{df.mean()}\n')
    print(f'\nStandard deviation value of each columns:\n{df.std()}\n')
    print(f'\nMedian value of each columns:\n{df.median()}\n')


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    print(f'start_time: {start_time}')
    data_frame = pd.read_csv('test.csv',
                             delimiter=',',
                             encoding='utf-8',
                             skipinitialspace=True)
    calculate_values(data_frame)
    taken_time = datetime.datetime.now() - start_time
    print(f'-----Total elapsed time: {taken_time.total_seconds()} seconds-----')
