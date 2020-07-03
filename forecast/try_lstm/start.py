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

time = 6000
# method 只有all people 和 new people两个选择。all people以每天总人数来预测，new people以每天新增人数来预测
method = 'new people'

city_A(time, method)
city_B(time, method)
city_C(time, method)
city_D(time, method)
city_E(time, method)
city_F(time, method)
city_G(time, method)
city_H(time, method)
city_I(time, method)
city_J(time, method)
city_K(time, method)
all_city()
