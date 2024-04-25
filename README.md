# Gout Prediction Calculator

This program predicts the probability of a patient developing gout based on their demographic and medical parameters.

## Research Overview

This prediction model is based on the research article titled "A machine learning-based prediction model for gout in hyperuricemics – a nationwide cohort study" by Shay Brikman et al. The study presents a machine learning model for predicting gout diagnosis among hyperuricemic patients using demographic characteristics, clinical diagnoses, medication prescriptions, and laboratory results. The research contains both full and compact models. This repository presents the compact model.

## Authors
- Shay Brikman MD, 1 2
- Liel Serfaty, 3
- Ran Abuhasira MD, PhD, 4 5 6
- Naomi Schlesinger MD, 7
- Amir Bieber MD, MA, 1
- Nadav Rappoport PhD, 3
1. Rheumatic Diseases Unit, Emek Medical Center, Afula, Israel.
2. Rappaport Faculty of Medicine, Technion, Haifa, Israel.
3. Department of Software and Information Systems Engineering, Ben-Gurion University of the Negev, Be'er Sheva, Israel 
4. Clinical Research Center, Soroka University Medical Center, Be'er Sheva, Israel.
5. Faculty of Health Sciences, Ben-Gurion University of the Negev, Be'er Sheva, Israel.
6. Department of Internal Medicine B, Rabin Medical Center, Beilinson Campus, Petah Tikva, Israel.
7. Division of Rheumatology, Department of Medicine, Spencer Fox Eccles School of Medicine, University of Utah, Salt Lake City, UT, USA.


## Libraries Required

- Python==3.x
- pandas
- joblib==1.4.0
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

