# Smart Issue Aggregator (ML-Powered)

**Status:** *In Development (Phase: Data Engineering & Preprocessing)*

An AI-powered tool designed to solve the "Choice Paralysis" problem for open-source contributors. Unlike standard filters, this project aims to use Machine Learning to identify "beginner-friendly" GitHub issues based on their textual content, even if they lack the specific `good first issue` label.

##  Architecture
1.  **Data Ingestion:** A Python pipeline that scrapes public repositories (e.g., ArduPilot) using the GitHub API.
2.  **Dataset Construction:** Automatically labels issues as `Positive` (Good First Issue) or `Negative` (Hard/Complex) to create a balanced training set.
3.  **Preprocessing:** Uses Pandas for data cleaning and TF-IDF (Term Frequency-Inverse Document Frequency) to vectorize issue descriptions for the model.

##  Tech Stack
* **Language:** Python 3.10+
* **API:** PyGithub (GitHub REST API wrapper)
* **Data Science:** Pandas, Scikit-learn, CSV

##  Project Structure
* `fetch_data.py`: Connects to GitHub, fetches issues, and generates `all_issues.csv`.
* `train_model.py`: Loads the raw CSV, cleans missing values, encodes labels, and performs TF-IDF vectorization.
* `all_issues.csv`: The raw dataset containing Title, Body, and Labels.

##  How to Run
1.  **Install Dependencies:**
    ```bash
    pip install PyGithub pandas scikit-learn
    ```
2.  **Fetch Data:**
    ```bash
    python fetch_data.py
    ```
3.  **Process Data:**
    ```bash
    python train_model.py
    ```

## 🔮 Next Steps
* Train a Logistic Regression Classifier on the vectorized data.
* Evaluate model accuracy.
* Build a Flask API to serve predictions.
