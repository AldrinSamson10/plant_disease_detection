PlantAI – AI Based Plant Disease Detection System

PlantAI is a web-based application that uses artificial intelligence to detect plant leaf diseases through image analysis. Users can upload or capture a plant leaf image, and the system predicts the disease, severity level, and provides basic treatment and prevention guidance. The goal is early detection and better crop health support.

--------------------------------------------------

Features

- Image-based plant disease detection
- Deep learning model for disease classification
- Confidence score with severity level
- Disease library with images and descriptions
- Severity and action guide
- Crop care and prevention advisory
- Responsive and user-friendly interface

--------------------------------------------------

Technology Stack

Backend:
Python, Flask

AI and Machine Learning:
TensorFlow, Keras (CNN model)

Frontend:
HTML, CSS, JavaScript

Data Handling:
JSON

--------------------------------------------------

Project Structure

plant_disease_detection/
│
├── app.py
│
├── model/
│   ├── plant_disease_model.h5
│   └── labels.txt
│
├── content/
│   └── disease_info.json
│
├── static/
│   ├── css/
│   │   ├── dashboard.css
│   │   └── main.css
│   │
│   ├── js/
│   │   └── detect.js
│   │
│   └── images/
│       └── diseases/
│           ├── healthy.jpg
│           ├── powdery_mildew.jpg
│           ├── leaf_rust.jpg
│           └── early_blight.jpg
│
├── templates/
│   ├── dashboard.html
│   ├── detect.html
│   ├── library.html
│   ├── action_guide.html
│   └── about.html
│
└── README.md

--------------------------------------------------

How the System Works

1. The user uploads or captures a plant leaf image.
2. The image is preprocessed and passed to a trained deep learning model.
3. The model predicts the disease class and confidence score.
4. Disease details, severity level, treatment, and prevention information are displayed.

--------------------------------------------------

Limitations

- Prediction accuracy depends on image clarity and lighting.
- Only trained disease classes can be detected.
- This system is not a replacement for professional agricultural diagnosis.

--------------------------------------------------

Developer Information

Developed by: Aldrin Samson

LinkedIn:
https://www.linkedin.com/in/aldrin-samson

GitHub:
https://github.com/AldrinSamson10

--------------------------------------------------

License

This project is intended for learning, demonstration, and portfolio purposes.