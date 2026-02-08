# ================= SAFETY FIRST =================
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

# ================= IMPORTS ======================
import json
import numpy as np
from flask import (
    Flask,
    render_template,
    request,
    send_from_directory,
    redirect,
    url_for
)
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# ================= APP INIT =====================
app = Flask(__name__)

# ================= PATH CONFIG ==================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER  = os.path.join(BASE_DIR, "uploads")
MODEL_FOLDER   = os.path.join(BASE_DIR, "model")
CONTENT_FOLDER = os.path.join(BASE_DIR, "content")

MODEL_PATH  = os.path.join(MODEL_FOLDER, "plant_disease_model.h5")
LABELS_PATH = os.path.join(MODEL_FOLDER, "labels.txt")

CONFIDENCE_THRESHOLD = 60.0

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ================= LOAD DATA ====================
with open(os.path.join(CONTENT_FOLDER, "disease_info.json"), "r") as f:
    disease_info = json.load(f)

model = load_model(MODEL_PATH)

with open(LABELS_PATH, "r") as f:
    labels = [line.strip() for line in f.readlines()]

# ================= ROUTES =======================

# ✅ HOME → DASHBOARD
@app.route("/")
def home():
    return render_template("dashboard.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# ✅ FIXED: Library is now DYNAMIC
@app.route("/library")
def library():
    highlight = request.args.get("highlight")
    return render_template(
        "library.html",
        diseases=disease_info,
        highlight=highlight
    )


@app.route("/action-guide")
def action_guide():
    with open(os.path.join(CONTENT_FOLDER, "action_guide.json")) as f:
        guides = json.load(f)
    return render_template("action_guide.html", guides=guides)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


# ================= DETECT =======================
@app.route("/detect", methods=["GET", "POST"])
def detect():
    result = None
    image_url = None

    if request.method == "POST":
        file = request.files.get("image")

        if not file or file.filename == "":
            return render_template("detect.html")

        # ---------- SAVE IMAGE ----------
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(file_path)
        image_url = f"/uploads/{file.filename}"

        # ---------- IMAGE PREPROCESS ----------
        img = image.load_img(file_path, target_size=(224, 224))
        img_array = image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # ---------- MODEL PREDICTION ----------
        predictions = model.predict(img_array)[0]
        idx = int(np.argmax(predictions))
        confidence = float(predictions[idx]) * 100
        predicted_label = labels[idx]

        # ---------- CONFIDENCE CHECK ----------
        if confidence < CONFIDENCE_THRESHOLD:
            result = {
                "disease": "Uncertain Prediction",
                "confidence": f"{confidence:.2f}%",
                "description": (
                    "The model is not confident enough to identify the leaf condition. "
                    "Please upload a clearer plant leaf image."
                ),
                "treatment": "Ensure the image is a clear close-up of a leaf.",
                "prevention": "Use good lighting and avoid background distractions."
            }
        else:
            info = disease_info.get(predicted_label, {})
            result = {
                "disease": predicted_label,
                "confidence": f"{confidence:.2f}%",
                "description": info.get("description", "Information not available."),
                "treatment": info.get("treatment", "Information not available."),
                "prevention": info.get("prevention", "Information not available.")
            }

        # 🔥 OPTIONAL BUT POWERFUL
        # Uncomment this if you want auto-jump to library
        # return redirect(url_for("library", highlight=predicted_label))

    return render_template("detect.html", result=result, image_url=image_url)


# ================= RUN APP ======================
if __name__ == "__main__":
    app.run(debug=True)