# 🩺 MediPredict AI – Multi-Disease Prediction System

**MediPredict AI** is a machine learning-based web application designed to demonstrate disease prediction for Chronic Kidney Disease (CKD) and Heart Disease. Built using Python and Flask, the application provides an interactive interface where users can enter health-related parameters and receive model-generated predictions.

🌐 **Live Demo:** https://multidisease-fo6v.onrender.com/

## ✨ Features

* **CKD Prediction:** Predicts the likelihood of Chronic Kidney Disease using health-related input parameters.
* **Heart Disease Prediction:** Estimates the likelihood of heart disease based on user-provided parameters.
* **Model Performance:** Displays the performance information of the trained machine learning models.
* **Interactive Web Interface:** Simple interface built with HTML, CSS, and JavaScript.
* **Flask Backend:** Processes form inputs and connects them to trained machine learning models.
* **Pre-trained Models:** Uses saved `.pkl` model files for predictions.

## 🛠️ Technologies Used

| Technology   | Purpose                                |
| ------------ | -------------------------------------- |
| Python       | Backend development and ML integration |
| Flask        | Web application framework              |
| Scikit-learn | Machine learning models                |
| Pandas       | Data processing                        |
| NumPy        | Numerical operations                   |
| Joblib       | Model loading and serialization        |
| HTML         | Web page structure                     |
| CSS          | Styling and layout                     |
| JavaScript   | Client-side interactivity              |
| Render       | Web application hosting                |

## 🤖 Machine Learning Models

The project explores the following algorithms:

* Logistic Regression
* Decision Tree
* Random Forest

The selected model differs by prediction task. The current project results report:

* **CKD:** Random Forest — test accuracy of 100%
* **Heart Disease:** Logistic Regression — test accuracy of 88.52%

*These are reported results from the project's evaluation. Actual performance depends on the dataset, train-test split, preprocessing, and evaluation methodology. In particular, 100% test accuracy does not establish clinical reliability.*

## 📂 Project Structure

```text
Multidisease/
│
├── app.py
├── ckd_model.pkl
├── heart_model.pkl
├── requirements.txt
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── ckd.html
│   ├── heart.html
│   ├── performance.html
│   └── about.html
│
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── script.js
```

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/somcode14/Multidisease.git
cd Multidisease
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

On macOS or Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the Flask application

```bash
python app.py
```

Open the local URL shown in your terminal, typically:

```text
http://127.0.0.1:5000/
```

## 📊 Application Pages

* **Home:** Introduction and access to the prediction modules.
* **CKD Prediction:** Form for entering kidney-disease-related parameters.
* **Heart Disease Prediction:** Form for entering heart-health parameters.
* **Model Performance:** Overview of the model evaluation results.
* **About:** Information about the project.

## 🎯 Project Objectives

* Apply machine learning algorithms to healthcare-related datasets.
* Integrate trained models into a Flask web application.
* Provide an interactive interface for exploring model predictions.
* Understand the process of model training, serialization, backend integration, and deployment.

## 🔮 Future Improvements

* Improve model evaluation using cross-validation and additional metrics.
* Add clearer input validation and error handling.
* Enhance responsive design for mobile devices.
* Add explainability features to help users understand model predictions.
* Explore secure user authentication and prediction history.
* Evaluate models on appropriate external datasets before considering real-world use.

## ⚠️ Disclaimer

MediPredict AI is an **educational machine learning project**. It is not a clinically validated medical device and must not be used to diagnose diseases, make treatment decisions, or replace consultation with a qualified healthcare professional.

## 👩‍💻 Author

**Soma Kar**

B.Tech — Computer Science and Engineering (Artificial Intelligence and Machine Learning)

C. V. Raman Global University, Bhubaneswar

* GitHub: https://github.com/somcode14

---

⭐ If you find this project interesting, feel free to explore the repository and share feedback.
