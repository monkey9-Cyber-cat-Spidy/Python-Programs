import pandas as pd
import numpy as np

data_list = [10, 20, 30, 40]
s_from_list = pd.Series(data_list)
print(s_from_list)

data_array = np.array([5, 6, 7, 8])
s_from_array = pd.Series(data_array)
print(s_from_array)

data_dict = {'a': 1, 'b': 2, 'c': 3}
s_from_dict = pd.Series(data_dict)
print(s_from_dict)

data_dict_lists = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']
}
df_from_dict_lists = pd.DataFrame(data_dict_lists)
print(df_from_dict_lists)

data_list_of_dicts = [
    {'Name': 'David', 'Age': 40, 'City': 'Tokyo'},
    {'Name': 'Eve', 'Age': 28, 'City': 'Rome'}
]
df_from_list_of_dicts = pd.DataFrame(data_list_of_dicts)
print(df_from_list_of_dicts)

data_2d_array = np.array([[1, 2, 3], [4, 5, 6]])
df_from_array = pd.DataFrame(data_2d_array, columns=['ColA', 'ColB', 'ColC'])
print(df_from_array)

s = pd.Series([100, 200, 300], name='Values')
df_from_series = s.to_frame()
print(df_from_series)
