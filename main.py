import argparse
import pandas as pd
import joblib
import xgboost as xgb
import warnings
warnings.filterwarnings('ignore')
def get_patient_data(age, su, hyperlipidemia, nsaid, diuretic):
    scaler = joblib.load('./scaler_cv_0.pkl')
    df = pd.DataFrame(columns=scaler.feature_names_in_)
    age_loc = df.columns.get_loc('Age')
    su_loc = df.columns.get_loc('UA_II')
    df.loc[0, 'Age'] = age
    df.loc[0, 'UA_II'] = su
    df.fillna(1, inplace=True)
    df = scaler.transform(df)
    patient_data = [df[0][su_loc], df[0][age_loc], int(hyperlipidemia), int(nsaid), int(diuretic)]
    patient_data.extend([0, 0, 0, 0, 0])  # Dummy values for additional features
    patient_data = pd.DataFrame([patient_data], columns=['UA_II', 'Age', 'hyperlipidemia', 'NSAIDS', 'Diuretics',
                                                         'HA1C_BOOL', 'SEDIMENTATION_BOOL', 'HYPERTENSION',
                                                         'Enalapril', 'UREA_max'])
    return patient_data


def load_model(model_path):
    model = xgb.Booster()
    model.load_model(model_path)
    return model


def make_prediction(model, features):
    dmatrix = xgb.DMatrix(features)
    return model.predict(dmatrix)


def main():
    parser = argparse.ArgumentParser(description='Gout Prediction Calculator')
    parser.add_argument('-age', type=int, help='Age of the patient')
    parser.add_argument('-ua', type=float, help='Serum Urate Level (mg/dL) of the patient')
    parser.add_argument('-hyperlipidemia', type=bool, help='Has the patient been diagnosed with Hyperlipidemia?')
    parser.add_argument('-nsaid', type=bool, help='Is there a record of NSAIDs purchase for the patient?')
    parser.add_argument('-diuretic', type=bool, help='Is there a record of Diuretics purchase for the patient?')
    args = parser.parse_args()

    patient_data = get_patient_data(args.age, args.ua, args.hyperlipidemia, args.nsaid, args.diuretic)
    model = load_model('./json_xgboost_save_model.json')
    preds = make_prediction(model, patient_data)
    preds = preds * 100
    preds = "{:.2f}%".format(preds[0])
    print(f'The patient has a {preds} chance of developing gout')


if __name__ == "__main__":
    main()
