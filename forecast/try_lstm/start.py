import tensorflow as tf  # 专门用来做机器学习的库
from city_a import city_A
from city_b import city_B
from city_c import city_C
from city_d import city_D
from city_e import city_E
from city_f import city_F
from city_g import city_G
from city_h import city_H
from city_i import city_I
from city_j import city_J
from city_k import city_K

from all_city import all_city

time = 2000  # 运行轮数
seq = 8  # 预测时每次输入到网络中的数据长度

# method 只有all people 和 new people两个选择。all people以每天总人数来预测，new people以每天新增人数来预测
method = 'all people'

city_A(time, seq, method)
city_B(time, seq, method)
city_C(time, seq, method)
city_D(time, seq, method)
city_E(time, seq, method)
city_F(time, seq, method)
city_G(time, seq, method)
city_H(time, seq, method)
city_I(time, seq, method)
city_J(time, seq, method)
city_K(time, seq, method)
all_city()
