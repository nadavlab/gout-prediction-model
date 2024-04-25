# Gout Prediction Calculator

This program predicts the probability of a patient developing gout based on their demographic and medical parameters.

## Research Overview

This prediction model is based on the research article titled "A machine learning-based prediction model for gout in hyperuricemics – a nationwide cohort study" by Shay Brikman et al. The study presents a machine learning model for predicting gout diagnosis among hyperuricemic patients using demographic characteristics, clinical diagnoses, medication prescriptions, and laboratory results.

## Libraries Required

- Python 3.x
- pandas
- joblib
- xgboost

## How to Run

1. Ensure you have Python 3.x installed on your system.
2. Install the required libraries by running: `pip install pandas joblib xgboost`.
3. Download or clone the repository to your local machine.
4. Open a terminal or command prompt.
5. Navigate to the directory containing the `main.py` file.
6. Run the following command:

    ```
    python main.py -age <age> -ua <serum urate level> -hyperlipidemia <True/False> -nsaid <True/False> -diuretic <True/False>
    ```

    Replace `<age>` with the patient's age, `<serum urate level>` with the patient's serum urate level (mg/dL), and `<True/False>` with the corresponding values for hyperlipidemia, NSAID usage, and diuretic usage.

7. The program will print the predicted probability of the patient developing gout.

## Calculator Link

[Click here to access the Gout Prediction Calculator](https://github.com/yourusername/yourrepository/main.py)

