import matplotlib.pyplot as plt

from random_walk import Randomwalk

rw = Randomwalk()
while True: #關於這裏嵌套裏面只放個fill函數，爲何結果不會變的問題：因爲一遍過去list已經滿了，第一個判斷就進不去，應該加一個清空語句，試了一下對了！
    rw.fill_walk()
    point_numbers = [i for i in range(rw.num_point)]

    plt.figure(figsize=(10,6)) #英寸，指定畫布大小，還可將本機分辨率傳給dpi
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, s=1)
    plt.scatter(rw.x_values[0],rw.y_values[0],c='green',s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',s=100) #這裏就能看出爲什麽數組要存位置而不是存每次的變化量了，因爲存結果每個只計算一次，求中間的越靠前算得越多，這也是一種優化。
    plt.axis('off')
    # plt.axes().get_xaxis().set_visible(False) # 經過詢問chatgpt，直接改成plt.axis('off')即可
    # plt.axes().get_yaxis().set_visible(False)

    plt.savefig('./image_rw/rw_1w_point_figsize.jpg',bbox_inches='tight')
    plt.show()

    keep_running = input('Make anothor walk? (y/n):')
    if keep_running == 'n':
        break