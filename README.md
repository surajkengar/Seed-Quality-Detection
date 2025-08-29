# Seed-Quality-Detection

A **desktop application** that detects the quality of seeds using **deep learning (CNN)** and a user-friendly **Tkinter GUI**.  
Includes **login/registration** system, **image preprocessing**, and **real-time prediction** with a trained model.

---

## 🚀 Features
- User Authentication (Sign-In / Sign-Up with SQLite)
- Tkinter GUI with background images & smooth navigation
- Upload & Preprocess images (grayscale, thresholding)
- CNN-based Prediction (Excellent / Average / Bad seed quality)
- Model Training via `VITModel.py` (saves `seed_model.h5`)
- Performance plots (accuracy & loss curves)

---

## 🛠 Tech Stack
- **Frontend:** Tkinter, Pillow  
- **Backend:** Python, SQLite  
- **Deep Learning:** TensorFlow, Keras, NumPy, OpenCV  
- **Visualization:** Matplotlib, scikit-learn  

---

## 📂 Project Structure
- `GUI_main.py` → Entry page (Sign-In, Sign-Up, Logout)
- `registration.py` → Register new users with validation
- `login.py` → Sign-In and database authentication
- `GUI_Master_old.py` → Main GUI for detection
- `model_CNN.py` → CNN model training
- `seed_model.h5` → Saved trained model
- `assets/` → Backgrounds and screenshots
