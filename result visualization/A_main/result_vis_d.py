# -------------------------神经网络训练模型---------------------------
import numpy as np  # 数据处理常用库
import pandas as pd  # 数据处理常用库
import matplotlib.pyplot as plt
import os

NUM = 89


def city_D(dir):
    # 设置模型
    # 学习率
    learning_rate = 0.01  # 类似于每次梯度下降移动步长

    data_dir = 'D:/python/venv/2020year/2020 IKCEST/train_data_all'
    files = ['city_A', 'city_B', 'city_C', 'city_D', 'city_E', 'city_F', 'city_G',
             'city_H', 'city_I', 'city_J', 'city_K']
    names = ['density.csv', 'grid_attr.csv', 'infection.csv', 'migration.csv', 'transfer.csv', 'weather.csv']

    Index = [
        ['data', 'hour', 'grid_x', 'grid_y', 'Population_flow_index'],
        ['grid_x', 'grid_y', 'region_id'],
        ['city', 'region_id', 'data', 'num_new_persons'],
        ['data', 'departure_city', 'arrival_city', 'migration_scale_index'],
        ['hour', 'start_grid_x', 'start_grid_y', 'end_grid_x', 'end_grid_y', 'transfer_intensity'],
        ['data', 'hour', 'temperature', 'humidity', 'wind_direction', 'wind_speed', 'wind_force', 'weather']
    ]

    # days_ = np.append(np.array(range(21200615, 21200631)), np.array(range(21200701, 21200715)))
    # days_ = days_.astype('int')
    # print(days_)

    for file in files[3:4]:
        i = 2
        name = names[i]
        dir_ = data_dir + '/' + file + '/' + name
        print('目前文件为{}'.format(name))
        data = pd.read_csv(dir_, header=0, names=Index[i])
        data_2 = pd.read_csv('D:/python/venv/2020year/2020 IKCEST/result/{}/submission.csv'.format(dir), header=None, names=Index[i])
        city = file.split('_')[-1]
        data_2 = data_2[data_2['city'] == city]

        print(data[:5])

        days = data['data'].unique()
        # print(days)
        region_id = data['region_id'].unique()

        # 创建存储路径
        save_path = r'D:\python\venv\2020year\2020 IKCEST\result visualization\{}\{}'.format(dir, city)
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        for id in region_id:
            data_ = data[data['region_id'] == id]
            data_2_ = data_2[data_2['region_id'] == id]
            x = np.array(range(data_.shape[0])).astype('float32')
            y_ = list(data_['num_new_persons'])
            y = []
            for i in range(len(y_)):
                y.append(sum(y_[:i+1]))

            # print(y)
            y = np.array(y).astype('float32')
            max_y = y.max()
            y = y.reshape((len(y), 1))
            x = x.reshape((len(x), 1))

            st = NUM - data_2_.shape[0]
            x_2 = np.array(range(st, NUM))
            y_2 = []
            y_0 = np.array(data_2_['num_new_persons'])
            for i in range(len(y_0)):
                y_2.append(sum(y_0[:i+1]) + max_y)

            plt.cla()
            plt.plot(x, y, color='blue')
            plt.plot(x_2, y_2, color='red')
            name_ = "city {}，id{}".format(city, id)
            plt.title(name_)

            plt.savefig(
                r'D:\python\venv\2020year\2020 IKCEST\result visualization\{}\{}\{}'.format(dir, city, id))
