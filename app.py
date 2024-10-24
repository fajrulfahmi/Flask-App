from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)

# Muat model dari file pickle secara langsung tanpa os.path.join
with open('model/water_usage_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def index():
    return render_template('index.html')

# Rute untuk prediksi (yang Anda beri komentar di atas)
@app.route('/predict', methods=['POST'])
def predict_water_consumption():
    # Ambil data dari POST request dalam format JSON
    data = request.json
    waterFlowRate = data['waterFlowRate']
    temp = data['temp']
    humidity = data['humidity']
    numResidents = data['numResidents']
    specialEvent = data['specialEvent']

    # Siapkan data untuk prediksi
    input_data = np.array([[waterFlowRate, temp, humidity, numResidents, specialEvent]])

    # Lakukan prediksi
    predicted_consumption = model.predict(input_data)

    # Format respon dalam JSON
    response = {
        'predicted_consumption': predicted_consumption[0],
        'percent_change_from_previous_day': 5.5  # Misalnya perubahan konsumsi dari hari sebelumnya
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
