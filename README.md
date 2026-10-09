# MediPredict AI – Multi-Disease Prediction System

🌐 **Live Demo:** https://multidisease-fo6v.onrender.com/

## About the Project

MediPredict AI is a machine learning-based web application that predicts the likelihood of Chronic Kidney Disease (CKD) and Heart Disease using health-related parameters.

The project integrates trained machine learning models with a Flask backend and an interactive web interface.

## Features

* **CKD Prediction:** Generates predictions using health-related input parameters.
* **Heart Disease Prediction:** Estimates the likelihood of heart disease.
* **Model Performance:** Displays model evaluation results.
* **Interactive Interface:** Simple and user-friendly web pages.
* **Online Deployment:** Accessible through a public URL.

## Technologies Used

* Python
* Flask
* Scikit-learn
* Pandas and NumPy
* Joblib
* HTML, CSS, JavaScript
* Render
* Git and GitHub

## Machine Learning Algorithms

* Logistic Regression
* Decision Tree
* Random Forest

## Model Performance

| Disease       | Selected Model      | Reported Accuracy |
| ------------- | ------------------- | ----------------: |
| CKD           | Random Forest       |              100% |
| Heart Disease | Logistic Regression |            88.52% |

*Note: These are reported test results and do not establish clinical reliability.*

## Project Structure

```text
Multidisease/
├── app.py
├── ckd_model.pkl
├── heart_model.pkl
├── requirements.txt
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── ckd.html
│   ├── heart.html
│   ├── performance.html
│   └── about.html
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── script.js
```

## Workflow

<img width="1312" height="1199" alt="image" src="https://github.com/user-attachments/assets/81ce656e-c741-4e1f-ae91-e353493ea8f6" />


## How It Works

1. Users enter health-related parameters through the web interface.
2. Flask receives and processes the submitted inputs.
3. The appropriate pre-trained machine learning model generates a prediction.
4. The application displays the prediction result.

## Future Improvements

* Improve model validation and evaluation.
* Add model explainability.
* Enhance input validation and error handling.
* Improve mobile responsiveness.
* Explore additional disease prediction modules.

## Disclaimer

This project is developed for educational purposes only. It is not a clinically validated medical device and must not be used for medical diagnosis or treatment decisions.

