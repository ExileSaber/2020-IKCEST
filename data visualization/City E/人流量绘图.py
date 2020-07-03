import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


days = [21200506, 21200509, 21200513, 21200516, 21200520, 21200523, 21200527, 21200530, 21200603, 21200606, 21200610,
        21200613, 21200617, 21200620, 21200624, 21200627]
data = np.load(file="Data/the_list.npy")
shape = data.shape
print(shape)

sum_top_10 = {}
mean_top_10 = {}

for i in range(shape[2]):
    for j in range(shape[1]):
        x = range(shape[0])
        y = data[:, j, i]

        if i == 0:
            if len(sum_top_10.keys()) < 10:
                sum_top_10[j] = max(y)
            else:
                if max(y) > min(sum_top_10.values()):
                    sum_top_10[j] = max(y)
                    m = min(sum_top_10.keys(), key=(lambda x: sum_top_10[x]))
                    sum_top_10.pop(m)
        else:
            if len(mean_top_10.keys()) < 10:
                mean_top_10[j] = max(y)
            else:
                if max(y) > min(mean_top_10.values()):
                    mean_top_10[j] = max(y)
                    m = min(mean_top_10.keys(), key=(lambda x: mean_top_10[x]))
                    mean_top_10.pop(m)

        print(y)
        plt.plot(x, y)
    plt.xticks(x, days, rotation=60)
    if i == 0:
        plt.title('E城市区域人流量总数')
        plt.savefig(
            r'D:\python\venv\2020year\2020 IKCEST\data visualization\Plot\city_E\E城市区域人流量总数')
    else:
        plt.title('E城市区域人流量平均数')
        plt.savefig(
            r'D:\python\venv\2020year\2020 IKCEST\data visualization\Plot\city_E\E城市区域人流量平均数')
    plt.show()

print('=================')

sum_top_10_list = sorted(sum_top_10.items(), key=lambda x: x[1])
print(sum_top_10_list)

mean_top_10_list = sorted(mean_top_10.items(), key=lambda x: x[1])
print(mean_top_10_list)

sum_top_10_id = sorted(sum_top_10, key=lambda x: sum_top_10[x])
mean_top_10_id = sorted(mean_top_10, key=lambda x: mean_top_10[x])

for id in sum_top_10_id:
    x = range(shape[0])
    y = data[:, id, 0]
    plt.plot(x, y)
plt.legend(sum_top_10_id)
plt.xticks(x, days, rotation=60)
plt.title('E城市top10区域人流量总数')
plt.savefig(
    r'D:\python\venv\2020year\2020 IKCEST\data visualization\Plot\city_E\E城市top10区域人流量总数数')
plt.show()

for id in mean_top_10_id:
    x = range(shape[0])
    y = data[:, id, 1]
    plt.plot(x, y)
plt.legend(mean_top_10_id)
plt.xticks(x, days, rotation=60)
plt.title('E城市top10区域人流量平均数')
plt.savefig(
    r'D:\python\venv\2020year\2020 IKCEST\data visualization\Plot\city_E\E城市top10区域人流量平均数')
plt.show()
