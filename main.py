import datetime
import pandas as pd


# dataframe을 받아 결과값을 출력하는 함수
def calculate_values(df):
    print(f'\nTotal number of rows: {df.shape[0]}\n')
    print(f'\nMax value of each columns:\n{df.max()}\n')
    print(f'\nMin value of each columns:\n{df.min()}\n')
    print(f'\nAverage value of each columns:\n{df.mean()}\n')
    print(f'\nStandard deviation value of each columns:\n{df.std()}\n')
    print(f'\nMedian value of each columns:\n{df.median()}\n')


if __name__ == '__main__':
    # 시작 시간 기록
    start_time = datetime.datetime.now()
    print(f'start_time: {start_time}')

    # dataframe 생성
    # skipinitialspace=True 옵션을 사용해 파일 내의 띄어쓰기를 모두 무시
    data_frame = pd.read_csv('test.csv',
                             delimiter=',',
                             encoding='utf-8',
                             skipinitialspace=True)
    # 함수 실행
    calculate_values(data_frame)

    # 총 소요 시간 계산
    taken_time = datetime.datetime.now() - start_time
    print(f'-----Total elapsed time: {taken_time.total_seconds()} seconds-----')
