# DiabeteAI

This project implements an AI model that predicts if patients are more susceptible to be 
diabetic or not.

This model is trained using a CSV dataset of patients that have or not the diabetes, and then 
be able to perform predictions on other patients.

### Built With


[![My Skills](https://skillicons.dev/icons?i=py)](https://skillicons.dev)

<!-- GETTING STARTED -->
## Getting Started

To start off, pull the project locally, and download all dependencies.

### Prerequisites

You need to have python and pip package manager installed, then run the command :
  ```sh
  pip install -r requirements.txt
  ```

## Usage

Before the algorithm can work on performing predictions, it needs to be trained
first.

You can use the file `train.py` that takes a sample csv file of patients. Keep or replace the 
file as needed if other patients are to be added or removed.

Once the file executed, it will export a trained model using the `pickle`
library to facilitate the model's persistence.

Then predictions may be performed using the `predict.py` script, that takes patients
as parameters, and loads the saved pickle model to analyze the patient's
data and returns a new dataframe of given patients in addition to a new
column that holds the prediction's outcome.

`outcome=0 if the patient is not diabetic`

`outcome=1 if the patient is diabetic`
