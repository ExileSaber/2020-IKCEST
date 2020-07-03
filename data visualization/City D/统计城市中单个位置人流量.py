import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
pd.set_option('display.max_columns', 10000, 'display.max_rows', 10000)
'''
1.统计每个区域内的人流量
2.统计流动的迁移总强度
'''

data_dir = 'D:/python/venv/2020year/2020 IKCEST/train_data_all'
file = 'city_D'
names = ['density.csv', 'grid_attr.csv', 'infection.csv', 'migration.csv', 'transfer.csv', 'weather.csv']

Index = [
    ['data', 'hour', 'grid_x', 'grid_y', 'Population_flow_index'],
    ['grid_x', 'grid_y', 'region_id'],
    ['city', 'region_id', 'data', 'num_new_persons'],
    ['data', 'departure_city', 'arrival_city', 'migration_scale_index'],
    ['hour', 'start_grid_x', 'start_grid_y', 'end_grid_x', 'end_grid_y', 'transfer_intensity'],
    ['data', 'hour', 'temperature', 'humidity', 'wind_direction', 'wind_speed', 'wind_force', 'weather']
]

i = 0
dir_1 = data_dir + '/' + file + '/' + names[i]
data_1 = pd.read_csv(dir_1, names=Index[i])
print(data_1.shape)

i = 1
dir_2 = data_dir + '/' + file + '/' + names[i]
data_2 = pd.read_csv(dir_2, names=Index[i])
print(data_2.shape)

data = pd.merge(data_1, data_2)
print(data[:20])
print(data.shape)

days = data['data'].unique()
print(days)
region_id = data['region_id'].unique()

the_list = []
for day in days:
    d_1 = data[data['data'] == day]
    sum_mean_list = []
    for id in region_id:
        d_2 = d_1[d_1['region_id'] == id]
        sum_index = sum(list(d_2['Population_flow_index']))
        mean_index = sum_index/len(list(d_2['Population_flow_index']))
        sum_mean_list.append([sum_index, mean_index])
    the_list.append(sum_mean_list)


np.save(file="Data/the_list.npy", arr=the_list)
# x = range(len(days))
# the_list = np.array(the_list)
# y = the_list[:, 0, 0]
# print(y)
# plt.plot(x, y)
# plt.xticks(x, days, rotation=60)
# plt.show()


