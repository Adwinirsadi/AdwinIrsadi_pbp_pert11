// Dataset selection
let selectedDataset = 'diabetes';

const datasetButtons = document.querySelectorAll('.dataset-btn');
const diabetesForm = document.getElementById('diabetesForm');
const strokeForm = document.getElementById('strokeForm');

// Handle dataset selection
datasetButtons.forEach(btn => {
  btn.addEventListener('click', function() {
    selectedDataset = this.getAttribute('data-dataset');
    
    // Update active button
    datasetButtons.forEach(b => b.classList.remove('active'));
    this.classList.add('active');
    
    // Show/hide forms
    if (selectedDataset === 'diabetes') {
      diabetesForm.classList.add('active');
      strokeForm.classList.remove('active');
    } else {
      diabetesForm.classList.remove('active');
      strokeForm.classList.add('active');
    }
    
    // Clear results
    document.getElementById('resultBox').classList.add('hidden');
  });
});

// Diabetes Form Submission
diabetesForm.addEventListener('submit', async function(event) {
  event.preventDefault();

  const data = {
    Pregnancies: Number(document.getElementById('Pregnancies').value),
    Glucose: Number(document.getElementById('Glucose').value),
    BloodPressure: Number(document.getElementById('BloodPressure').value),
    SkinThickness: Number(document.getElementById('SkinThickness').value),
    Insulin: Number(document.getElementById('Insulin').value),
    BMI: Number(document.getElementById('BMI').value),
    DiabetesPedigreeFunction: Number(document.getElementById('DiabetesPedigreeFunction').value),
    Age: Number(document.getElementById('Age').value)
  };

  try {
    const response = await fetch('http://127.0.0.1:5000/predict/diabetes', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    });

    const result = await response.json();
    displayResult(result);

  } catch (error) {
    displayError('API belum berjalan atau tidak dapat diakses. Pastikan server Flask berjalan di http://127.0.0.1:5000');
  }
});

// Stroke Form Submission
strokeForm.addEventListener('submit', async function(event) {
  event.preventDefault();

  const data = {
    gender: document.getElementById('gender').value,
    age: Number(document.getElementById('age').value),
    hypertension: Number(document.getElementById('hypertension').value),
    heart_disease: Number(document.getElementById('heart_disease').value),
    ever_married: document.getElementById('ever_married').value,
    work_type: document.getElementById('work_type').value,
    Residence_type: document.getElementById('Residence_type').value,
    avg_glucose_level: Number(document.getElementById('avg_glucose_level').value),
    bmi: Number(document.getElementById('bmi').value),
    smoking_status: document.getElementById('smoking_status').value
  };

  try {
    const response = await fetch('http://127.0.0.1:5000/predict/stroke', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    });

    const result = await response.json();
    displayResult(result);

  } catch (error) {
    displayError('API belum berjalan atau tidak dapat diakses. Pastikan server Flask berjalan di http://127.0.0.1:5000');
  }
});

// Display result
function displayResult(result) {
  const resultBox = document.getElementById('resultBox');
  const resultText = document.getElementById('resultText');
  const probabilityText = document.getElementById('probabilityText');
  const riskLevelText = document.getElementById('riskLevelText');

  if (result.status === 'success') {
    resultBox.classList.remove('hidden');
    resultText.innerHTML = '<strong>Hasil:</strong> ' + result.result;
    probabilityText.innerHTML = '<strong>Probabilitas Risiko:</strong> ' + (result.probability * 100).toFixed(2) + '%';
    riskLevelText.innerHTML = '<strong>Tingkat Risiko:</strong> <span style="color: ' + getRiskColor(result.risk_level) + '; font-weight: bold;">' + result.risk_level + '</span>';
  } else {
    displayError('Terjadi kesalahan: ' + result.message);
  }
}

// Display error
function displayError(errorMessage) {
  const resultBox = document.getElementById('resultBox');
  const resultText = document.getElementById('resultText');
  const probabilityText = document.getElementById('probabilityText');
  const riskLevelText = document.getElementById('riskLevelText');

  resultBox.classList.remove('hidden');
  resultText.innerHTML = '<strong>Kesalahan:</strong> ' + errorMessage;
  probabilityText.innerText = '';
  riskLevelText.innerText = '';
}

// Get risk level color
function getRiskColor(riskLevel) {
  if (riskLevel === 'Tinggi') {
    return '#d9534f'; // Red
  } else if (riskLevel === 'Sedang') {
    return '#f0ad4e'; // Orange
  } else {
    return '#5cb85c'; // Green
  }
}