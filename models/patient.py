class Patient:
    pregnancies = 0
    glucose = 0
    blood_pressure = 0
    skin_thickness = 0
    insulin = 0
    bmi = 0
    diabetes_pedigree_function = 0
    age = 0
    outcome = 0

    def __init__(self, pregnancies, glucose, blood_pressure, skin_thickness,
                 insulin, bmi, diabetes_pedigree_function, age, outcome=0):
        self.pregnancies = pregnancies
        self.glucose = glucose
        self.blood_pressure = blood_pressure
        self.skin_thickness = skin_thickness
        self.insulin = insulin
        self.bmi = bmi
        self.diabetes_pedigree_function = diabetes_pedigree_function
        self.age = age
        self.outcome = outcome

    def to_dict(self):
        return {
            'pregnancies': self.pregnancies,
            'glucose': self.glucose,
            'blood_pressure': self.blood_pressure,
            'skin_thickness': self.skin_thickness,
            'insulin': self.insulin,
            'bmi': self.bmi,
            'diabetes_pedigree_function': self.diabetes_pedigree_function,
            'age': self.age,
            'outcome': self.outcome,
        }
