import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', 10000, 'display.max_rows', 10000)


data_dir = 'D:/python/venv/2020year/2020 IKCEST/train_data_all'
file = 'city_C'
names = ['density.csv', 'grid_attr.csv', 'infection.csv', 'migration.csv', 'transfer.csv', 'weather.csv']
'''
infection.csv
城市中每个区域每天增长人数
'''
'''
migration.csv
城市之间的人口迁移，有一个迁移指数不知道定义
迁移指数：可能就是一个衡量城市之间迁移强度的指标

density.csv
网格人流量指数

transfer.csv
网格关联强度

grid_attr.csv
网格归属区域

weather.csv
城市天气数据
'''
Index = [
    ['data', 'hour', 'grid_x', 'grid_y', 'Population_flow_index'],
    ['grid_x', 'grid_y', 'region_id'],
    ['city', 'region_id', 'data', 'num_new_persons'],
    ['data', 'departure_city', 'arrival_city', 'migration_scale_index'],
    ['hour', 'start_grid_x', 'start_grid_y', 'end_grid_x', 'end_grid_y', 'transfer_intensity'],
    ['data', 'hour', 'temperature', 'humidity', 'wind_direction', 'wind_speed', 'wind_force', 'weather']
]

i = 3
name = names[i]
dir = data_dir + '/' + file + '/' + name
print('目前文件为{}'.format(name))
data = pd.read_csv(dir, header=0, names=Index[i])
# print(data[:5])

days = data['data'].unique()
print(len(days))
cities = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']

the_list = np.zeros((len(days), 11, 11))
# print(the_list)

for k in range(len(days)):
    day = days[k]
    data_1 = data[data['data'] == day]
    for i in range(len(cities)):
        city_1 = cities[i]
        data_2 = data_1[data_1['departure_city'] == city_1]
        if data_2.empty:
            continue
        for j in range(len(cities)):
            city_2 = cities[j]
            data_3 = data_2[data_2['arrival_city'] == city_2]
            # print(data_3)
            if data_3.empty:
                continue
            the_list[k, i, j] = float(data_3['migration_scale_index'])

print(the_list)
np.save(file="Data/city_to_city.npy", arr=the_list)
