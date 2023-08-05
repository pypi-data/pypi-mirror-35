"""

"""

from datasets import load_iris
from datasets import load_boston_house_prices


def test_bunch_dir():
    # check that dir (important for autocomplete) shows attributes
    data = load_iris()
    print ("X" in dir(data))


def test_load_iris():
    # res = load_iris()
    # print (res)

    X_y_tuple = load_iris(return_X_y=True)
    print (X_y_tuple[0])


def test_load_boston_house_prices():
    res = load_boston_house_prices(X_index = ['ZN', 'NOX', 'DIS'])
    print (res.y)

    # X_y_tuple = load_boston_house_prices(return_X_y=True)
    # print (X_y_tuple[1])


def main():
    # test_bunch_dir()
    # test_load_iris()
    test_load_boston_house_prices()


if __name__ == "__main__":
    main()