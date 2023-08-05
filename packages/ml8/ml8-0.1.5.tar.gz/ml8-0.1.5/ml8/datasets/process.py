
from sklearn.model_selection import train_test_split


def split(return_X_y=False, X=None, y=None, test_size=0.25, random_state=0):
    X_train, X_test, y_train,  y_test = train_test_split(X, y, test_size=test_size,random_state=random_state)

if __name__ == "__main__":
    pass
