import pandas as pd


def all_city():
    data_1 = pd.read_csv(r'D:\python\venv\2020year\2020 IKCEST\train_data_all\submission.csv', header=None)

    data_2 = pd.read_csv(r'D:\python\venv\2020year\2020 IKCEST\forecast\try_lstm\submission_a.csv', header=None)
    data_3 = pd.read_csv(r'D:\python\venv\2020year\2020 IKCEST\forecast\try_lstm\submission_b.csv', header=None)
    data_4 = pd.read_csv(r'D:\python\venv\2020year\2020 IKCEST\forecast\try_lstm\submission_c.csv', header=None)
    data_5 = pd.read_csv(r'D:\python\venv\2020year\2020 IKCEST\forecast\try_lstm\submission_d.csv', header=None)
    data_6 = pd.read_csv(r'D:\python\venv\2020year\2020 IKCEST\forecast\try_lstm\submission_e.csv', header=None)
    data_7 = pd.read_csv(r'D:\python\venv\2020year\2020 IKCEST\forecast\try_lstm\submission_f.csv', header=None)
    data_8 = pd.read_csv(r'D:\python\venv\2020year\2020 IKCEST\forecast\try_lstm\submission_g.csv', header=None)
    data_9 = pd.read_csv(r'D:\python\venv\2020year\2020 IKCEST\forecast\try_lstm\submission_h.csv', header=None)
    data_10 = pd.read_csv(r'D:\python\venv\2020year\2020 IKCEST\forecast\try_lstm\submission_i.csv', header=None)
    data_11 = pd.read_csv(r'D:\python\venv\2020year\2020 IKCEST\forecast\try_lstm\submission_j.csv', header=None)
    data_12 = pd.read_csv(r'D:\python\venv\2020year\2020 IKCEST\forecast\try_lstm\submission_k.csv', header=None)

    data_ = pd.concat([data_2, data_3, data_4, data_5, data_6, data_7, data_8, data_9, data_10, data_11, data_12],
                      axis=0, ignore_index=True)
    print(data_.shape)

    data = pd.merge(data_1, data_, on=[0, 1, 2], how='inner')
    print(data[:5])

    data.drop(['3_x'], axis=1, inplace=True)  # inplace=True会就地修改

    data = data.drop_duplicates([0, 1, 2])
    print(data.shape)

    data.to_csv('submission.csv', index=None, header=None)


# all_city()