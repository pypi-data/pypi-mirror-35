"""

"""

def run_demo_iris():
    print ("鸢尾花数据集样例\n")
    from ml8.datasets import load
    from ml8.classifier import DecisionTreeClassifier
    from ml8.datasets import model_selection
    from ml8 import metrics

    iris = load("iris")     # 加载数据集
    X = iris.X              # 获得数据集数据
    print ("X的前五条数据：\n", X[:5])
    print ("\n")

    y = iris.y              # 获得数据集的标签
    print("y的前五条数据:\n", y[:5])
    print("\n")

    print("X的维度是：", X.shape)    # 数据维度
    print("y的维度是：", y.shape)    # 标签维度
    print("\n")

    dt = DecisionTreeClassifier(max_depth=3)    # 构建决策树，指定决策树的最大深度为3
    print ("输出模型")
    print(dt)
    print("\n")

    X_train, X_test, y_train, y_test = model_selection.train_test_split(X=X, y=y, test_size=0.25)   # 划分训练集和测试集

    print ("使用模型训练数据：")
    dt.fit(X_train, y_train)    # 训练模型
    print("\n")

    print("测试集的预测结果为：\n", dt.predict(X_test))   # 使用测试集测试模型并输出测试结果
    print("\n")

    print("准确率：\n", metrics.accuracy_score(y_test, dt.predict(X_test))) # 输出模型准确率
    print("\n")

    print("混淆矩阵：\n", metrics.confusion_matrix(y_test, dt.predict(X_test)))  # 输出混淆矩阵
    print("\n")

    print("精确率、召回率和f1值：\n", metrics.classification_report(y_test, dt.predict(X_test)))  # 输出精确率、召回率和F1的值
    print("\n")

def run_demo_boston():
    pass

def run_demo_galton():
    pass