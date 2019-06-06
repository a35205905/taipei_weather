import csv
import matplotlib.pyplot  as plt

from matplotlib.font_manager import FontProperties
from matplotlib.font_manager import _rebuild


# 重新建立字體索引列表
_rebuild()
# 設定中文字型
plt.rcParams['font.sans-serif']=[u'simhei']
# 圖片大小(寬, 高)
plt.rcParams['figure.figsize'] = (14.0, 6.0)

def main():
    with open('weather.csv', 'r') as f:
        reader = csv.reader(f)
        # 去欄位名稱
        weathers = list(reader)[1:]

    # 依地區分類
    result = {}
    years = 0
    for location, date, temperature in weathers:
        d = date.split(' ')
        if years == 0:
            years = d[0].split('/')[0]
            
        # 去年份
        d[0] = '/'.join(d[0].split('/')[1:])
        date = '\n'.join(d)
        temperature = int(temperature)
        if result.get(location) is None:
            result[location] = {
                'date': [date],
                'temperature': [temperature]
            }
        else:
            result[location].get('date').append(date)
            result[location].get('temperature').append(int(temperature))

    for key, value in result.items():
        plt.plot(value['date'], value['temperature'], label=key)

    plt.xlabel('Date Time')
    plt.ylabel('Temperature')
    plt.title("{} Taipei Weather".format(years))
    # 圖例
    plt.legend()
    # 設定圖例位置
    plt.legend(bbox_to_anchor=(1.01, 1), loc='upper left', borderaxespad=0.)
    # 格線
    plt.grid(True)
    # 產生圖檔
    plt.savefig('weather.png', dpi=300, format='png')
    # 預覽畫面
    plt.show()

if __name__ == '__main__':
    main()