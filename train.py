import csv
import pickle
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
import pandas as pd
import os

from models.patient import Patient


def start_training():
    patients = []
    with open('./Data/diabetes.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            patients.append(Patient(row[0], row[1], row[2],
                                    row[3], row[4], row[5],
                                    row[6], row[7], row[8]))
    patients = pd.DataFrame.from_records([p.to_dict() for p in patients])

    # drop the header line
    diabetes_data = patients.drop(index=0, axis=0)
    x_axis = diabetes_data.drop(columns='outcome', axis=1)
    y_axis = diabetes_data['outcome']
    x_train, x_test, y_train, y_test = train_test_split(x_axis, y_axis, test_size=0.2, stratify=y_axis, random_state=2)
    classifier = svm.SVC(kernel='linear')
    classifier.fit(x_train, y_train)

    x_train_prediction = classifier.predict(x_train)
    training_data_accuracy = accuracy_score(x_train_prediction, y_train)
    print('Accuracy score of training is :', training_data_accuracy)

    x_test_prediction = classifier.predict(x_test)
    test_data_accuracy = accuracy_score(x_test_prediction, y_test)
    print('Accuracy score of test is :', test_data_accuracy)

    # export using pickle
    export_model(classifier)


def export_model(classifier):
    model = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'finalized_model.sav')
    pickle.dump(classifier, open(model, 'wb'))
    pickle.load(open('finalized_model.sav', 'rb'))


if __name__ == "__main__":
    start_training()
