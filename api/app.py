from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np
import os

# Membuat aplikasi Flask
app = Flask(__name__)
CORS(app)

# Menentukan lokasi file model dan scaler
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load Diabetes Model
DIABETES_MODEL_PATH = os.path.join(BASE_DIR, "..", "model", "diabetes_model.pkl")
DIABETES_SCALER_PATH = os.path.join(BASE_DIR, "..", "model", "scaler.pkl")

with open(DIABETES_MODEL_PATH, "rb") as file:
    diabetes_model = pickle.load(file)

with open(DIABETES_SCALER_PATH, "rb") as file:
    diabetes_scaler = pickle.load(file)

# Load Stroke Model
STROKE_MODEL_PATH = os.path.join(BASE_DIR, "..", "model", "stroke_model.pkl")
STROKE_ENCODERS_PATH = os.path.join(BASE_DIR, "..", "model", "stroke_label_encoders.pkl")

with open(STROKE_MODEL_PATH, "rb") as file:
    stroke_model = pickle.load(file)

with open(STROKE_ENCODERS_PATH, "rb") as file:
    stroke_label_encoders = pickle.load(file)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "success",
        "message": "API Prediksi Risiko Kesehatan (Diabetes & Stroke)",
        "endpoints": {
            "diabetes": {
                "path": "/predict/diabetes",
                "method": "POST",
                "description": "Prediksi risiko diabetes"
            },
            "stroke": {
                "path": "/predict/stroke",
                "method": "POST",
                "description": "Prediksi risiko stroke"
            }
        }
    })


@app.route("/predict/diabetes", methods=["POST"])
def predict_diabetes():
    try:
        # Mengambil data JSON dari request
        data = request.get_json()

        # Daftar field yang wajib dikirim dari aplikasi web
        required_fields = [
            "Pregnancies",
            "Glucose",
            "BloodPressure",
            "SkinThickness",
            "Insulin",
            "BMI",
            "DiabetesPedigreeFunction",
            "Age"
        ]

        # Validasi apakah seluruh field tersedia
        for field in required_fields:
            if field not in data:
                return jsonify({
                    "status": "error",
                    "message": f"Field '{field}' wajib diisi"
                }), 400

        # Mengubah input JSON menjadi array numerik
        input_data = np.array([[
            float(data["Pregnancies"]),
            float(data["Glucose"]),
            float(data["BloodPressure"]),
            float(data["SkinThickness"]),
            float(data["Insulin"]),
            float(data["BMI"]),
            float(data["DiabetesPedigreeFunction"]),
            float(data["Age"])
        ]])

        # Melakukan scaling data sesuai scaler dari proses training
        input_scaled = diabetes_scaler.transform(input_data)

        # Melakukan prediksi
        prediction = diabetes_model.predict(input_scaled)[0]

        # Mengambil probabilitas kelas 1 atau risiko diabetes
        probability = diabetes_model.predict_proba(input_scaled)[0][1]

        # Interpretasi hasil prediksi
        if prediction == 1:
            result = "Berisiko Diabetes"
        else:
            result = "Tidak Berisiko Diabetes"

        # Menentukan tingkat risiko berdasarkan probabilitas
        if probability >= 0.70:
            risk_level = "Tinggi"
        elif probability >= 0.40:
            risk_level = "Sedang"
        else:
            risk_level = "Rendah"

        # Mengirim response ke aplikasi web
        return jsonify({
            "status": "success",
            "dataset": "diabetes",
            "prediction": int(prediction),
            "result": result,
            "probability": round(float(probability), 4),
            "risk_level": risk_level
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


@app.route("/predict/stroke", methods=["POST"])
def predict_stroke():
    try:
        # Mengambil data JSON dari request
        data = request.get_json()

        # Daftar field yang wajib dikirim dari aplikasi web
        required_fields = [
            "gender",
            "age",
            "hypertension",
            "heart_disease",
            "ever_married",
            "work_type",
            "Residence_type",
            "avg_glucose_level",
            "bmi",
            "smoking_status"
        ]

        # Validasi apakah seluruh field tersedia
        for field in required_fields:
            if field not in data:
                return jsonify({
                    "status": "error",
                    "message": f"Field '{field}' wajib diisi"
                }), 400

        # Encode categorical features
        input_data = []
        categorical_features = ['gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status']
        feature_order = ['gender', 'age', 'hypertension', 'heart_disease', 'ever_married', 'work_type', 'Residence_type', 'avg_glucose_level', 'bmi', 'smoking_status']

        for feature in feature_order:
            if feature in categorical_features:
                le = stroke_label_encoders[feature]
                input_data.append(le.transform([data[feature]])[0])
            else:
                input_data.append(float(data[feature]))

        input_array = np.array([input_data])

        # Melakukan prediksi
        prediction = stroke_model.predict(input_array)[0]

        # Mengambil probabilitas kelas 1 atau risiko stroke
        probability = stroke_model.predict_proba(input_array)[0][1]

        # Interpretasi hasil prediksi
        if prediction == 1:
            result = "Berisiko Stroke"
        else:
            result = "Tidak Berisiko Stroke"

        # Menentukan tingkat risiko berdasarkan probabilitas
        if probability >= 0.70:
            risk_level = "Tinggi"
        elif probability >= 0.40:
            risk_level = "Sedang"
        else:
            risk_level = "Rendah"

        # Mengirim response ke aplikasi web
        return jsonify({
            "status": "success",
            "dataset": "stroke",
            "prediction": int(prediction),
            "result": result,
            "probability": round(float(probability), 4),
            "risk_level": risk_level
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


# Backward compatibility - default endpoint untuk diabetes
@app.route("/predict", methods=["POST"])
def predict():
    return predict_diabetes()


if __name__ == "__main__":
    app.run(debug=True, port=5000)