import pickle
import numpy as np
from pandas import DataFrame as df
from models.patient import Patient


def predict(patients: df):
    model = pickle.load(open('finalized_model.sav', 'rb'))
    patients_classified = df()
    for patient in patients.iterrows():
        patient = patient[1]
        input_data_as_numpy_array = np.asarray(patient)
        input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
        prediction = model.predict(input_data_reshaped)
        patient['outcome'] = prediction[0]
        patients_classified = patients_classified.append(patient, ignore_index=True)
        if prediction[0] == '0':
            print('not diabetic')
        else:
            print('diabetic')

    return patients_classified


if __name__ == "__main__":
    patients = [Patient(5, 166, 9, 964, 9, 6, 0.587, 44),
                Patient(2, 197, 70, 45, 543, 30.5, 0.158, 53)]
    patients = df.from_records([p.to_dict() for p in patients])
    patients = patients.drop(columns='outcome', axis=1)
    predict(patients)

