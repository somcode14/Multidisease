from flask import Flask, render_template, request
import pandas as pd
import joblib

# ============================================================
# FLASK APP
# ============================================================

app = Flask(__name__)


# ============================================================
# LOAD TRAINED MODELS
# ============================================================

try:
    ckd_model = joblib.load("ckd_model.pkl")
    heart_model = joblib.load("heart_model.pkl")

    print("CKD model loaded successfully.")
    print("Heart disease model loaded successfully.")

except Exception as e:
    print("Error loading models:", e)
    ckd_model = None
    heart_model = None


# ============================================================
# HOME PAGE
# ============================================================

@app.route("/")
def home():
    return render_template("home.html")


# ============================================================
# CKD PREDICTION
# ============================================================

@app.route("/ckd", methods=["GET", "POST"])
def ckd():

    prediction = None
    probability = None
    error = None

    if request.method == "POST":

        try:

            # --------------------------------------------
            # GET CKD INPUTS
            # --------------------------------------------

            data = {
                "age": float(request.form["age"]),
                "bp": float(request.form["bp"]),
                "sg": float(request.form["sg"]),
                "al": float(request.form["al"]),
                "su": float(request.form["su"]),

                "rbc": request.form["rbc"],
                "pc": request.form["pc"],
                "pcc": request.form["pcc"],
                "ba": request.form["ba"],

                "bgr": float(request.form["bgr"]),
                "bu": float(request.form["bu"]),
                "sc": float(request.form["sc"]),
                "sod": float(request.form["sod"]),
                "pot": float(request.form["pot"]),
                "hemo": float(request.form["hemo"]),
                "pcv": float(request.form["pcv"]),
                "wbcc": float(request.form["wbcc"]),
                "rbcc": float(request.form["rbcc"]),

                "htn": request.form["htn"],
                "dm": request.form["dm"],
                "cad": request.form["cad"],
                "appet": request.form["appet"],
                "pe": request.form["pe"],
                "ane": request.form["ane"]
            }

            # --------------------------------------------
            # CREATE DATAFRAME
            # --------------------------------------------

            input_df = pd.DataFrame([data])

            # --------------------------------------------
            # PREDICT
            # --------------------------------------------

            result = ckd_model.predict(input_df)[0]

            # --------------------------------------------
            # PROBABILITY
            # --------------------------------------------

            if hasattr(ckd_model, "predict_proba"):

                probabilities = ckd_model.predict_proba(input_df)[0]

                classes = list(ckd_model.classes_)

                if 1 in classes:

                    probability = round(
                        probabilities[classes.index(1)] * 100,
                        2
                    )

            # --------------------------------------------
            # RESULT
            # --------------------------------------------

            if result == 1:

                prediction = "Higher Risk of Chronic Kidney Disease"

            else:

                prediction = "Lower Risk of Chronic Kidney Disease"

        except Exception as e:

            error = str(e)

    return render_template(
        "ckd.html",
        prediction=prediction,
        probability=probability,
        error=error
    )


# ============================================================
# HEART DISEASE PREDICTION
# ============================================================

@app.route("/heart", methods=["GET", "POST"])
def heart():

    prediction = None
    probability = None
    error = None

    if request.method == "POST":

        try:

            # --------------------------------------------
            # GET HEART INPUTS
            # --------------------------------------------

            data = {

                "age": float(request.form["age"]),

                "sex": int(request.form["sex"]),

                "cp": int(request.form["cp"]),

                "trestbps": float(
                    request.form["trestbps"]
                ),

                "chol": float(
                    request.form["chol"]
                ),

                "fbs": int(
                    request.form["fbs"]
                ),

                "restecg": int(
                    request.form["restecg"]
                ),

                "thalach": float(
                    request.form["thalach"]
                ),

                "exang": int(
                    request.form["exang"]
                ),

                "oldpeak": float(
                    request.form["oldpeak"]
                ),

                "slope": int(
                    request.form["slope"]
                ),

                "ca": int(
                    request.form["ca"]
                ),

                "thal": int(
                    request.form["thal"]
                )
            }

            # --------------------------------------------
            # CREATE DATAFRAME
            # --------------------------------------------

            input_df = pd.DataFrame([data])

            # --------------------------------------------
            # PREDICT
            # --------------------------------------------

            result = heart_model.predict(input_df)[0]

            # --------------------------------------------
            # PROBABILITY
            # --------------------------------------------

            if hasattr(heart_model, "predict_proba"):

                probabilities = heart_model.predict_proba(input_df)[0]

                classes = list(heart_model.classes_)

                if 1 in classes:

                    probability = round(
                        probabilities[classes.index(1)] * 100,
                        2
                    )

            # --------------------------------------------
            # RESULT
            # --------------------------------------------

            if result == 1:

                prediction = "Higher Risk of Heart Disease"

            else:

                prediction = "Lower Risk of Heart Disease"

        except Exception as e:

            error = str(e)

    return render_template(
        "heart.html",
        prediction=prediction,
        probability=probability,
        error=error
    )


# ============================================================
# MODEL PERFORMANCE
# ============================================================

@app.route("/performance")
def performance():

    return render_template("performance.html")


# ============================================================
# ABOUT PAGE
# ============================================================

@app.route("/about")
def about():

    return render_template("about.html")


# ============================================================
# ERROR HANDLERS
# ============================================================

@app.errorhandler(404)
def page_not_found(error):

    return render_template("home.html"), 404


@app.errorhandler(500)
def internal_server_error(error):

    return """
    <h2>Internal Server Error</h2>
    <p>Please check the Flask terminal for details.</p>
    """, 500


# ============================================================
# RUN APPLICATION
# ============================================================

if __name__ == "__main__":

    print("\n======================================")
    print("       MEDIPREDICT AI")
    print(" Multi-Disease Prediction System")
    print("======================================")
    print("Server running at:")
    print("http://127.0.0.1:5000")
    print("======================================\n")

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )