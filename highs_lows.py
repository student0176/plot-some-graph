import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = './csv_and_json/death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f) #reader是一個iterator，將一行按逗號弄成list后讀進來
    header_row = next(reader)
    # for index,column in enumerate(header_row):
    #     print(index,column) # 這裏查看行的索引，0123分別對應年月日，max、mean、min
    highs = []
    lows = []
    dates = []
    for row in reader: # 第一行都是表頭，已經給了header_row，所以這裏拿到的是數據
        try:
            high_value = int(row[1])
            low_value = int(row[3])
            date_value = datetime.strptime(row[0], '%Y-%m-%d')
        except ValueError:
            print(dates[-1],'missing data')
        else:
            highs.append(high_value)
            lows.append(low_value)
            dates.append(date_value)

    # print(highs)

    fig = plt.figure(figsize=(10,6))
    plt.plot(dates,highs,c='red',alpha=0.5)
    plt.plot(dates,lows,c='blue',alpha=0.5)
    plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1) #alpha為透明度（默認爲1，為0完全透明）
    plt.title('Daily high and low tempretures - 2014', fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate() # 傾斜，防重叠
    plt.ylabel('Tempreture (F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.savefig('./image_tempreture/death_valley.jpg',bbox_inches='tight')
    plt.show()