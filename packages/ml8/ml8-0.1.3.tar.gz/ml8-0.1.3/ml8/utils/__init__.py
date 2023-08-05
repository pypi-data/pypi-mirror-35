"""


"""

from sklearn import model_selection
from imblearn.combine import SMOTEENN
from sklearn import tree
from sklearn import metrics
import pydot
from sklearn.externals.six import StringIO
import os
from sklearn.neighbors import KNeighborsClassifier
import math

class Bunch(dict):
    """Container object for datasets

    Dictionary-like object that exposes its keys as attributes.

    >>> b = Bunch(a=1, b=2)
    >>> b['b']
    2
    >>> b.b
    2
    >>> b.a = 3
    >>> b['a']
    3
    >>> b.c = 6
    >>> b['c']
    6

    """

    def __init__(self, **kwargs):
        super(Bunch, self).__init__(kwargs)

    def __setattr__(self, key, value):
        self[key] = value

    def __dir__(self):
        return self.keys()

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(key)

    def __setstate__(self, state):
        # Bunch pickles generated with scikit-learn 0.16.* have an non
        # empty __dict__. This causes a surprising behaviour when
        # loading these pickles scikit-learn 0.17: reading bunch.key
        # uses __dict__ but assigning to bunch.key use __setattr__ and
        # only changes bunch['key']. More details can be found at:
        # https://github.com/scikit-learn/scikit-learn/issues/6196.
        # Overriding __setstate__ to be a noop has the effect of
        # ignoring the pickled __dict__
        pass

    def train_test_split(self, test_size=0.25, random_state=0):
        """
        划分训练集和测试集
        :param test_size:
        :param random_state:
        :return:
        """
        X_train, X_test, y_train, y_test = model_selection.train_test_split(self.X, self.y, test_size=test_size, random_state=random_state)
        return X_train, X_test, y_train, y_test

    def blance(self):
        """
        样本采样方法，该方法是一个集成算法，包含smote算法和enn算法
        :return:
        """
        sm = SMOTEENN()
        self.X, self.y = sm.fit_sample(self.X, self.y)
        return self.get_blance()

    def get_blance(self):
        """
        获得平衡度，这里用标准差来衡量，该参数只在样本具有分类属性时有意义，因为计算的是不同类型的样本的偏差
        计算公式为：s = sqrt(∑(X-M)^2 / (n-1))
        :return:返回一个浮点数字，该数字越小，数据平衡度越强，表示数据越均衡
        """
        y_list = list(self.y)

        y_dict = {}
        for i in y_list:
            if i not in y_dict:
                y_dict[i] = 1
            else:
                y_dict[i] += 1
        sum = 0
        for i in y_dict:
            sum += y_dict[i]
        m = sum / len(y_dict)

        # get s
        sig = 0.
        for i in y_dict:
            sig += (y_dict[i] - m) ** 2
        s = math.sqrt(sig / len(y_list))

        return s



class Classify(dict):
    """

    """

    def __init__(self, **kwargs):
        super(Classify, self).__init__(kwargs)

    def __setattr__(self, key, value):
        self[key] = value

    def __dir__(self):
        return self.keys()

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(key)

    def __setstate__(self, state):
        pass

    def fit(self, **kwargs):
        """
        训练模型，通过传入不同参数进行不同的模型训练
        :return:返回训练好的模型
        """
        if self.model_type == "DT":
            self.model = tree.DecisionTreeClassifier(criterion=self.criterion, splitter=self.splitter, max_depth=self.max_depth,
                                                   min_samples_split=self.min_samples_split, min_samples_leaf=self.min_samples_leaf,
                                                   min_weight_fraction_leaf=self.min_weight_fraction_leaf,
                                                   max_features=self.max_features, random_state=self.random_state,
                                                   max_leaf_nodes=self.max_leaf_nodes,min_impurity_decrease=self.min_impurity_decrease,
                                                   min_impurity_split=self.min_impurity_split, class_weight=self.class_weight, presort=self.presort).fit(self.X_train, self.y_train)

        elif self.model_type == "KNN":
            self.model = KNeighborsClassifier().fit(self.X_train, self.y_train)
            print ()

    def predict(self, X_test):
        """
        预测
        :param X_test: 测试集
        :return: 预测的结果
        """
        y_predict = self.model.predict(X_test)
        self.y_predict = y_predict
        return y_predict

    def test(self, X_test, y_test, target_names=None):
        """
        性能评估
        :param X_test: 测试集
        :param y_test: 测试集的标签
        :param target_names:样本的类别
        :return:
        """
        y_predict = self.predict(X_test)
        self.accuracy_score = metrics.accuracy_score(y_predict, y_test)
        self.confusion_matrix = metrics.confusion_matrix(y_test, y_predict)
        self.classification_report = metrics.classification_report(y_test, y_predict, target_names=target_names)

    def generate_tree(self, path='.', name='DT.pdf'):
        """
        打印决策树模型生成的决策树，保存成pdf格式
        :param path: 保存文件的路径
        :param name: 需要保存的文件名
        :return:
        """
        if self.model_type == 'DT':
            dot_data = StringIO()
            tree.export_graphviz(self.model, out_file=dot_data)
            graph = pydot.graph_from_dot_data(dot_data.getvalue())
            path = os.path.join(path, name)
            graph[0].write_pdf(path)
            print (path)


