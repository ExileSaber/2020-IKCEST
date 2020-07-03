# -------------------------神经网络训练模型---------------------------
import torch
from torch import nn
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd  # 数据处理常用库
import csv

seq = 10


class LSTM(nn.Module):
    def __init__(self):
        super(LSTM, self).__init__()
        self.lstm = nn.LSTM(input_size=1, hidden_size=16, num_layers=1, batch_first=True)
        self.linear = nn.Linear(16 * seq, 1)

    def forward(self, x):
        x, (h, c) = self.lstm(x)
        x = x.reshape(-1, 16 * seq)
        x = self.linear(x)
        return x


def city_A(epoch, method='all people'):
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

    days_ = np.append(np.array(range(21200630, 21200631)), np.array(range(21200701, 21200730)))
    days_ = days_.astype('int')
    print(days_)

    for file in files[0:1]:
        i = 2
        name = names[i]
        dir_ = data_dir + '/' + file + '/' + name
        # print('目前文件为{}'.format(name))
        data = pd.read_csv(dir_, header=0, names=Index[i])
        # print(data[:5])

        city = file.split('_')[-1]

        days = data['data'].unique()
        # print(days)
        region_id = data['region_id'].unique()
        top_10 = {}

        for id in region_id:
            data_ = data[data['region_id'] == id]
            # x = np.array(range(data_.shape[0])).astype('float32')
            y_ = list(data_['num_new_persons'])

            if method == 'all people':
                y__ = []
                for i in range(len(y_)):
                    y__.append(sum(y_[:i+1]))

                # print(y)
                y__ = np.array(y__).astype('float32')
                # print(len(y__))
            elif method == 'new people':
                y__ = np.array(y_).astype('float32')
            else:
                print('--------------------error-------------------')
                print("method取值不是'all people'或者'new people'")
                print('--------------------------------------------')
                exit(-1)

            x = []
            y = []
            for i in range(len(y__) - seq - 1):
                x.append(y__[i:i + seq])
                y.append(y__[i + seq])

            # print(len(y))

            train_x = (torch.tensor(x).float() / 1000.).reshape(-1, seq, 1)
            # print(train_x.shape)
            train_y = (torch.tensor(y).float() / 1000.).reshape(-1, 1)
            test_x_list = x[-1]
            # print(test_x_list)
            test_x = (torch.tensor(x[-1:]).float() / 1000.).reshape(-1, seq, 1)
            test_y = (torch.tensor(y[-1:]).float() / 1000.).reshape(-1, 1)

            print("城市{}，第{}个区域开始训练".format(city, id))
            # 模型训练
            model = LSTM()
            optimzer = torch.optim.Adam(model.parameters(), lr=0.005)
            loss_func = nn.MSELoss()
            model.train()
            l = []
            for epoch in range(epoch):
                output = model(train_x)
                loss = loss_func(output, train_y)
                l.append(loss)
                optimzer.zero_grad()
                loss.backward()
                optimzer.step()
                # if epoch % 100 == 0:
                #     tess_loss = loss_func(model(test_x), test_y)
                #     print("epoch:{}, train_loss:{}, test_loss:{}".format(epoch, loss, tess_loss))

            pred_y = []
            for _ in range(31):
                model.eval()
                # print(_)
                new_y = int((model(test_x).data.reshape(-1)) * 1000)
                pred_y.append(new_y)
                test_x_list = test_x_list[1:]
                test_x_list = np.append(test_x_list, new_y)
                # print(test_x_list)
                test_x = (torch.tensor(test_x_list).float() / 1000.).reshape(-1, seq, 1)

            prediction = list((model(train_x).data.reshape(-1)) * 1000)
            # print(len(prediction))

            # plt.figure(1)
            # plt.plot(y, label='True Value')
            # plt.plot(prediction, label='LSTM fit')
            # plt.plot(np.arange(len(prediction), len(prediction)+30, 1), pred_y[1:], label='LSTM pred')
            # plt.legend(loc='best')
            # plt.title('New daily infections prediction(Hubei province)')
            # plt.xlabel('Day')
            # plt.ylabel('New Confirmed Cases')
            # # plt.figure(2)
            # # plt.plot(l)
            # plt.show()

            the_y = pred_y
            # print(len(the_y))
            number = 0
            for t in range(len(the_y)-1):
                line = list()
                line.append(city)
                line.append(id)
                line.append(days_[t])
                v = the_y[t]
                v = int(the_y[t+1] - v)
                if v >= 0:
                    line.append(v)
                    number += 1
                else:
                    line.append(0)
                    number += 1
                f = open('submission_a.csv', 'a', newline='')
                csv_writer = csv.writer(f)
                csv_writer.writerow(line)
            print("城市{}，第{}个区域训练结束，训练预测的数据条数{}-------".format(city, id, number))

