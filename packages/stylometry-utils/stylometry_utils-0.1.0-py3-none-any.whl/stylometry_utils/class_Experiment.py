from sklearn import preprocessing, metrics
from pathlib import Path
import os
from requests import get

import pandas as pd
from typing import Tuple, Union
from sklearn.model_selection import train_test_split

MODEL_SAVEPATH = "/content/drive/MyDrive/simo/"


class Experiment:

    def __init__(self, dataset_path: Path, target_col: str, split: bool = True, test_size: float = 0.2,
                 model_savepath=MODEL_SAVEPATH, dropna: bool = False):
        self.scaler = preprocessing.StandardScaler()
        self.lbl_enc = preprocessing.LabelEncoder()

        self.dataset_path = dataset_path
        self.test_size = test_size
        self.target_col = target_col
        self.dataset_name = dataset_path.name
        self.model_savepath = model_savepath

        self.X, self.y = self.load_dataset(self.dataset_path)
        if split:
            self.X_train, self.X_test, self.y_train, self.y_test = self.split_dataset()

        # check if on colab or local
        if os.getcwd() == "/content":
            self.nb_name = get('http://172.28.0.2:9000/api/sessions').json()[0]['name'].split(".")[0]
        else:
            self.nb_name = Path(__file__).name

    def load_dataset(self, dataset_path: Path) -> Tuple:
        """
        Loads in memory a csv or xlsx or xls dataset.

        :param dataset_path: Path of the dataset
        :return: X and y tuple (y is determined by the self.target_col attr)
        """
        file_format = dataset_path.suffix
        valid = {".csv", ".xlsx", ".xls"}
        if file_format not in valid:
            raise ValueError(f"results: status must be one of {valid}.")
        else:
            print(f"Loading dataset {dataset_path.name}")
            if file_format == ".csv":
                dataset = pd.read_csv(dataset_path)
                print("Dataset head\n")
                print(dataset.head())
            elif file_format == ".xlsx" or file_format == ".xls":
                dataset = pd.read_excel(dataset_path)
                print("Dataset head\n")
                print(dataset.head())

            X = dataset.drop(self.target_col, axis=1)
            y = self.lbl_enc.fit_transform(dataset[self.target_col].values)

        return X, y

    def split_dataset(self, test_size: float = None) -> Tuple:
        """
        Split the dataset using sklearn train_test_split

        :param test_size: size in decimal of the holdout data
        :return: tuple of X_train, X_test, y_train, y_test
        """
        if not test_size:
            X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, random_state=42,
                                                                test_size=self.test_size, shuffle=True)
            return X_train, X_test, y_train, y_test
        else:
            X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, random_state=42, test_size=test_size,
                                                                shuffle=True)
            return X_train, X_test, y_train, y_test

    @staticmethod
    def drop_na(X: pd.DataFrame, how: str = "any", axis: int = 0) -> pd.DataFrame:
        """
        Drops nan rows (default) or columns using pandas dropna method.

        :param X: dataframe without target column. Returned by :meth:`Experiment.load_dataset`
        :param how: Determine if row or column is removed from DataFrame, when we have at least one NA or all NA.
        :param axis:Determine if rows or columns which contain missing values are removed. *0, or ‘index’ : Drop rows which contain missing values. *1, or ‘columns’ : Drop columns which contain missing value.
        :return: X with dropped nans
        """
        print("DROPPING NAN")
        X_drop = X.dropna(axis=axis, how=how)

        return X_drop

    def use_scaler(self) -> pd.DataFrame:
        """
        Use standard scaler from sklearn on X.

        :return: scaled X
        """
        X = self.scaler.fit_transform(self.X)
        return X

    def show_class_distribution(self):
        """
        Show how many instances of each class are in the dataset

        """
        listy = list(self.lbl_enc.inverse_transform(self.y))
        print("Dataset class distribution:")
        for i in set(listy):
            print(i, listy.count(i))

    def print_cm(self, yvalid: Union[pd.Series, list], predicted: Union[pd.Series, list], target_names=None):
        """
        Shows confusion matrix.

        :param yvalid: Ground truth labels
        :param predicted: predicted labels
        :param target_names: list of class labels
        """
        if not target_names:
            target_names = []
        cm = metrics.confusion_matrix(yvalid, predicted)
        disp = metrics.ConfusionMatrixDisplay(cm, display_labels=target_names)
        disp.plot(xticks_rotation="vertical")

    def print_report(self, predicted, yvalid, target_names=None):
        """
        Shows skelarn report.

        :param predicted: predicted labels
        :param yvalid: Ground truth labels
        :param target_names: list of class labels
        :return:
        """
        report_dict = metrics.classification_report(yvalid, predicted, target_names=[str(x) for x in target_names],
                                                    output_dict=True)
        report_text = metrics.classification_report(yvalid, predicted, target_names=[str(x) for x in target_names])
        print(report_text)
        self.print_cm(yvalid, predicted, target_names=target_names)
        return report_dict

    def load_test_dataset(self, testdataset_path: Path, dropna: bool = False, how: str = "any", axis: int = 0) -> Tuple:
        """
        Load a third party test dataset to be used for verifying model robustness.

        :param testdataset_path: path of the test dataset
        :param dropna: Whether to drop na values or not
        :param how: Determine if row or column is removed from DataFrame, when we have at least one NA or all NA.
        :param axis:Determine if rows or columns which contain missing values are removed. *0, or ‘index’ : Drop rows which contain missing values. *1, or ‘columns’ : Drop columns which contain missing value.
        :return:
        """
        X, y = self.load_dataset(testdataset_path)
        target_names = self.lbl_enc.inverse_transform(list(set(y)))
        if dropna:
            self.drop_na(X)

        return X, y, target_names
