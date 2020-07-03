每个city_*.py 文件对应每个城市的预测，生成对应城市的submission_*.csv文件

all_city.py 用于合并最后的预测结果，将submission_*.csv合并为submission.csv文件

## 只用直接运行start.py 文件就好

### 最后生成的submission.csv 文件需自己移动到result目录下自己新建的文件夹下，或者改一下all_city,py 中submission.csv 的存储目录
### 生成的submission_*.csv 文件需要自己将其全部删除才能进行下一轮训练

* start.py 中time 表示运行轮数，method 有两种选择
