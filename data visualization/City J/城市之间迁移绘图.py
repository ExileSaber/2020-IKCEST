import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

data = np.load(file="Data/city_to_city.npy")
shape = data.shape
print(data)

num = 11

the_list = np.zeros((shape[0], num))
for k in range(shape[0]):
    data_1 = data[k]
    for i in range(num):
        the_list[k, i] = sum(data[k, i, :])

x = range(shape[0])
for i in range(num):
    y = the_list[:, i]
    plt.plot(x, y)

legend = ['J->A', 'J->B', 'J->C', 'J->D', 'J->E', 'J->F', 'J->G', 'J->H', 'J->I', '->J', 'J->K']
plt.legend(legend)
plt.title('J城市与周边城市人口流动图')
plt.savefig(
    r'D:\python\venv\2020year\2020 IKCEST\data visualization\Plot\city_J\JK城市与周边城市人口流动图')
plt.show()
