"""

"""

from __future__ import print_function
import csv
from os.path import dirname, join

from ..utils import Bunch
import numpy as np

def info(data_name):
    """
    获得数据的详细描述
    :param data_name: 数据集名称
    :return: 返回该数据集的详细描述信息
    """
    module_path = dirname(__file__)
    data_name = data_name + ".rst"
    with open(join(module_path, 'data', data_name)) as rst_file:
        fdescr = rst_file.read()
    return fdescr

def load(data_name, X_names=[], y_name=None):
    """
    加载数据集
    :param data_name: 数据集名称
    :param X_names: 选择加载该数据集的哪几列，该参数是一个特征列表
    :param y_name: 选择哪一列作为标签
    :return: 返回数据集
    """
    if data_name == "iris":
        return load_iris(X_names=X_names, y_name=y_name)
    elif data_name == "boston_house_prices":
        return load_boston_house_prices(X_names=X_names, y_name=y_name)


def load_data(module_path, data_file_name, X_names=[], y_name=None):
    """
    加载数据集
    :param module_path:数据集的路径
    :param data_file_name:数据集文件名
    :param X_names:数据集特征名
    :param y_name:数据集标签名
    :return:X,y,X_names,y_name分别是数据集、标签、数据集特征名、数据集标签名
    """
    with open(join(module_path, 'data', data_file_name)) as csv_file:
        data_file = csv.reader(csv_file)
        field = next(data_file)

        if y_name == None: # 不指定标签列，则最后一列为标签列
            y_name = field[len(field) - 1]

        if len(X_names) == 0: # 不指定特征列，则合并所有除标签以外的特征列
            X_names = field[:field.index(y_name)] + field[field.index(y_name)+1:]

        X, y = [], []

        for item in data_file:
            X_list = []
            for i in X_names:
                X_list.append(item[field.index(i)])
            X.append(X_list)
            y.append(item[field.index(y_name)])

        X = np.asarray(X, dtype=np.float64)
        y = np.asarray(y)

    return X, y, X_names, y_name, field

def load_iris(return_X_y=False, X_names=[], y_name=None):
    """
    加载鸢尾花数据集
    :param return_X_y: 该参数表示是否返回X和y
    :param X_names: 数据集特征名
    :param y_name: 数据集标签名
    :return: 返回一个Bunch，这是一个数据集模型
    """
    module_path = dirname(__file__)
    X, y, X_names, y_name, field = load_data(module_path, 'iris.csv')

    with open(join(module_path, 'data', 'iris.rst')) as rst_file:
        fdescr = rst_file.read()

    if return_X_y:
        return X, y

    return Bunch(X=X, y=y,
                 X_names=X_names,
                 DESCR=fdescr,
				 y_name=y_name,
                 field = field)


def load_boston_house_prices(return_X_y=False, X_names=[], y_name=None):
    """
    加载鸢尾花数据集
    :param return_X_y:该参数表示是否返回X和y
    :param X_names:数据集特征名
    :param y_name:数据集标签名
    :return:返回一个Bunch，这是一个数据集模型
    """
    module_path = dirname(__file__)
    X, y, X_names, y_name, field = load_data(module_path, 'boston_house_prices.csv', X_names, y_name)

    with open(join(module_path, 'data', 'boston_house_prices.rst')) as rst_file:
        fdescr = rst_file.read()

    if return_X_y:
        return X, y

    return Bunch(X=X, y=y,
                 X_names=X_names,
                 DESCR=fdescr,
				 y_name=y_name,
                 field = field)


def main():
    iris = load("iris")
    # print (iris.X_names)
    # print (iris.y)
    # print (iris.get_blance())
    # iris.blance()
    # print(iris.get_blance())
    print(len(iris.X))


    # X_train, X_test, y_train , y_test = iris.split()
    # print (X_train)
    # print (type(iris.y))
    # boston_house_prices = load_boston_house_prices()
    # print(boston_house_prices.get_blance())
    # print (len(boston_house_prices.y))
    # print (boston_house_prices.y)
    # print (boston_house_prices.y)
    # pass

if __name__ == "__main__":
    main()
