# 🔥 Fire Weather Index (FWI) Prediction System

A machine learning web application that predicts the **Fire Weather Index (FWI)** using meteorological data, helping assess wildfire risk levels in real time.

---

## 📌 Overview

Wildfires are a growing global threat driven by climate change. This system leverages the **Algerian Forest Fires Dataset** and regression-based ML models to predict FWI values from weather inputs, classifying danger levels to support disaster management and early warning systems.

The dataset contains **244 instances** of meteorological data collected during the fire season (June–September 2012) from two regions in Algeria:
- **Bejaia** (northeast)
- **Sidi Bel-Abbes** (northwest)

---

## 🚀 Features

- Predicts FWI value from weather inputs via a web form
- Classifies wildfire danger into 6 levels (Very Low → Extreme)
- Trained on multiple regression models with performance comparison
- Flask-powered backend with StandardScaler normalization
- Nature-themed responsive frontend

---

## 🛠️ Tech Stack

| Layer | Tools |
|---|---|
| Backend | Python, Flask, Gunicorn |
| ML | Scikit-learn, NumPy, Pandas |
| Frontend | HTML, CSS |
| Dev Env | Jupyter Notebook |

---

## 📂 Project Structure

```
fwi-prediction/
├── .ebextensions/
│   └── python.config                               # AWS Elastic Beanstalk config
├── dataset/
│   └── Algerian_forest_fires_cleaned_dataset.csv   # Cleaned dataset
├── models/
│   ├── ridge.pkl                                   # Trained Ridge Regression model
│   └── scaler.pkl                                  # Fitted StandardScaler
├── notebooks/
│   ├── 2.0-EDA And FE Algerian Forest Fires.ipynb  # Exploratory Data Analysis
│   ├── 3.0-Model Training.ipynb                    # Model training & evaluation
│   └── Algerian_forest_fires_cleaned_dataset.csv
├── templates/
│   ├── index.html                                  # Landing page
│   └── home.html                                   # Prediction form & result
├── application.py                                  # Flask app entry point
├── requirements.txt
└── README.md
```

---

## 📊 Input Features

| Feature | Description |
|---|---|
| `Temperature` | Ambient temperature (°C) |
| `RH` | Relative Humidity (%) |
| `WS` | Wind Speed (km/h) |
| `Rain` | Rainfall (mm) |
| `FFMC` | Fine Fuel Moisture Code |
| `DMC` | Duff Moisture Code |
| `ISI` | Initial Spread Index |
| `Classes` | Fire / Not Fire (encoded: 1 / 0) |
| `Region` | Geographic region (encoded: 0 / 1) |

---

## 🤖 Models Trained

| Model | MAE | R² Score |
|---|---|---|
| Linear Regression | 0.584 | 0.9835 |
| **Ridge Regression** | 0.746 | 0.9498 |
| Lasso Regression | 1.146 | 0.9498 |
| ElasticNet Regression | 0.730 | 0.9789 |

> **Ridge Regression** was selected for deployment due to its regularization and generalization balance.

---

## 🔥 FWI Danger Classification

| FWI Range | Danger Level |
|---|---|
| < 5.2 | 🟢 Very Low |
| 5.2 – 11.2 | 🟡 Low |
| 11.2 – 21.3 | 🟠 Moderate |
| 21.3 – 38.0 | 🔴 High |
| 38.0 – 50.0 | 🟣 Very High |
| > 50.0 | ⚫ Extreme |

---

## ⚙️ Data Preprocessing

1. **Cleaning** — Removed irrelevant columns (day, month)
2. **Encoding** — Fire → 1, Not Fire → 0
3. **Standardization** — Applied `StandardScaler` (zero mean, unit variance)

---

## 🏃 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/your-username/fwi-prediction.git
cd fwi-prediction
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run locally
```bash
python application.py
```
Visit `http://localhost:5000`

### 4. Production (Gunicorn)
```bash
gunicorn -w 4 application:app
```

### 5. Deploy to AWS Elastic Beanstalk
```bash
# Initialize EB (first time)
eb init -p python-3.11 fwi-prediction

# Create environment and deploy
eb create fwi-env
eb open

# For subsequent deploys
eb deploy
```

> The `.ebextensions/python.config` handles WSGI configuration automatically.

---

## 📦 Requirements

```
flask
numpy
pandas
scikit-learn
gunicorn
```

---

## 🌍 Applications

- Real-time wildfire risk assessment for emergency responders
- Disaster management and resource allocation
- Environmental and forest monitoring
- Agriculture and land management decisions
- Climate change research

---

## 🔮 Future Extensions

- Integrate real-time IoT / satellite weather data
- Upgrade to neural network models for higher accuracy
- Build a mobile app for on-the-go alerts
- Expand to global regions with localized datasets
- Automated firefighting system integration

---

## 📄 Dataset

**Algerian Forest Fires Dataset** — UCI Machine Learning Repository  
244 instances | 11 meteorological attributes | June–September 2012

---

## 🙏 Acknowledgements

- FWI classification ranges based on the **Algerian Forest Fire Weather Index System** and the **European Forest Fire Information System (EFFIS)**
- Dataset sourced from the UCI ML Repository