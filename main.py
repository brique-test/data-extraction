import datetime
import pandas as pd


def calculate_values(df):
    print(df.max())
    print(df.min())
    print(df.mean())
    print(df.std())
    print(df.median())


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
