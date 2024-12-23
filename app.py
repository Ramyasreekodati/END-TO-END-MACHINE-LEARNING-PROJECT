from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import os
from werkzeug.security import generate_password_hash, check_password_hash
import numpy as np
import pandas as pd
from src.wine_quality.pipeline.prediction import PredictionPipeline  # Ensure this exists

app = Flask(__name__, static_folder='project_folder/static', template_folder='project_folder/templates')

# Use a fixed secret key for development; replace with a secure key in production
app.secret_key = 'your_secret_key'

# Dummy user data (replace with a database in production)
users = {
    "ramyasreekodati@gmail.com": generate_password_hash("password123")
}

# ----------------------------- ROUTES ---------------------------------

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        try:
            name = request.form.get('name')
            email = request.form.get('email')
            password = request.form.get('password')
            
            if not name or not email or not password:
                return jsonify({"error": "All fields are required"}), 400

            if email in users:
                return jsonify({"error": "User already exists"}), 400

            users[email] = generate_password_hash(password)
            return redirect('/signin')
        except Exception as e:
            print(f"Error during signup: {e}")
            return jsonify({"error": "Internal Server Error"}), 500
    return render_template('signup.html')


@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        
        if email in users and check_password_hash(users[email], password):
            session["user"] = email
            return redirect(url_for("home"))
        else:
            return jsonify({"error": "Invalid credentials"}), 400
    
    return render_template("signin.html")

@app.route("/")
def home():
    if "user" not in session:
        return redirect(url_for("signin"))
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if "user" not in session:
        return redirect(url_for("signin"))
    
    try:
        features = {
            "fixed acidity": float(request.form["fixed_acidity"]),
            "volatile acidity": float(request.form["volatile_acidity"]),
            "citric acid": float(request.form["citric_acid"]),
            "residual sugar": float(request.form["residual_sugar"]),
            "chlorides": float(request.form["chlorides"]),
            "free sulfur dioxide": float(request.form["free_sulfur_dioxide"]),
            "total sulfur dioxide": float(request.form["total_sulfur_dioxide"]),
            "density": float(request.form["density"]),
            "pH": float(request.form["pH"]),
            "sulphates": float(request.form["sulphates"]),
            "alcohol": float(request.form["alcohol"]),
            "Id": 0
        }

        data_df = pd.DataFrame([features])

        prediction_pipeline = PredictionPipeline()
        prediction = prediction_pipeline.predict(data_df)

        return render_template("result.html", prediction=prediction)

    except Exception as e:
        print(f"Error during prediction: {e}")
        return jsonify({"error": "Something went wrong"}), 500

@app.route("/train", methods=["GET"])
def train():
    try:
        os.system("python main.py")
        return "Training Successful!"
    except Exception as e:
        print(f"Error during training: {e}")
        return jsonify({"error": "Training failed"}), 500

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("signin"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2021, debug=True)
