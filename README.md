# Student Performance Prediction

This project predicts students' academic performance using machine learning models. It takes various features such as demographics, parental education, and test preparation status to predict the students' scores. The project includes **data preprocessing**, **exploratory data analysis (EDA)**, and **model training** pipelines.

---

## 📂 Project Structure

```
├── application.py              # Main application entry point
├── model_training.ipynb        # Jupyter Notebook for model training
├── eda_studens_performance.ipynb # EDA on dataset
├── exception.py                # Custom exception handling
├── requirements.txt            # Python dependencies
├── setup.py                    # Project setup file
└── README.md                   # Project documentation
```

---

## 🚀 Features

- **Exploratory Data Analysis (EDA):**  
  Visualizes distributions and relationships between variables.
- **Machine Learning Models:**  
  Implements and trains models like `CatBoost`, `XGBoost`, and `Scikit-learn` regressors.
- **Custom Exception Handling:**  
  Handles errors gracefully for better debugging.
- **Reusable Pipeline:**  
  Modularized code for data preprocessing, training, and inference.

---

## 🛠 Tech Stack

- **Programming Language:** Python 3.x  
- **Libraries:**  
  `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `catboost`, `xgboost`, `dill`

---

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/student-performance-prediction.git
   cd student-performance-prediction
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage

1. **Run EDA:**  
   Open `eda_studens_performance.ipynb` in Jupyter Notebook and execute cells to visualize data insights.

2. **Train Model:**  
   Open `model_training.ipynb` and run the training pipeline to generate a trained model.

3. **Run Application:**  
   ```bash
   python application.py
   ```

---

## 📊 Example Outputs

- Feature distribution plots  
- Correlation heatmaps  
- Model performance metrics (e.g., RMSE, R² score)  

_(You can add screenshots of graphs or console outputs here for better visualization.)_

---

## 🤝 Contributing

Contributions are welcome!  
1. Fork the repository  
2. Create a new branch (`feature/your-feature`)  
3. Commit your changes  
4. Open a pull request  

---

## 📜 License

This project is licensed under the **MIT License** – you are free to use, modify, and distribute with attribution.


