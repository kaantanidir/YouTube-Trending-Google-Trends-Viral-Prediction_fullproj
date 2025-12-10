# Predicting Short-Term Popularity Growth of YouTube Trending Videos Using Platform Metrics and Machine Learning

## 1. Overview & Motivation

YouTube is one of the most influential media platforms in the world. Videos sometimes go “viral” in a very short time, but it is not always clear which factors drive this rapid popularity.

This project aims to model and predict short-term popularity growth of YouTube trending videos by combining internal platform metrics (views, likes, comments, category, channel information) with external search interest signals from Google Trends.

The objective is to determine which features best predict next-day view growth and to build machine learning models that classify or regress “high-growth” outcomes.

---

## 2. Research Questions

- **RQ1:** Which video- and channel-level features (category, publication time, engagement ratios) are associated with higher short-term popularity growth?  
- **RQ2:** Does Google search interest improve prediction accuracy?  
- **RQ3:** Can a supervised ML model reliably predict high next-day growth?

---

## 3. Data Sources

### 3.1 YouTube Trending Dataset (Primary)
CSV dataset (Kaggle) including:  
video_id, title, channel_title, category_id, publish_time, views, likes, dislikes, comment_count, tags, description.

### 3.2 Google Trends Dataset (Enrichment)
Daily search interest scores exported as CSV:  
date, interest_score (0–100).

---

## 4. Data Collection & Integration Plan

### YouTube Data Processing
- Download CSV files from Kaggle.  
- Filter to a specific timeframe (e.g., several months).  
- Engineer derived metrics:  
  - like_to_view_ratio  
  - comment_to_view_ratio  
  - days_since_publication  
  - one-hot encoded categories  

### Google Trends Processing
- Export daily interest scores for selected topic keywords.  
- Convert date fields into a standard format.

### Dataset Integration
- Merge YouTube and Google Trends on the “date” field.  
- Handle missing values and scale features as necessary.

---

## 5. Planned Methods

### 5.1 Exploratory Data Analysis (EDA)
- View, like, and comment distributions  
- Category-level engagement comparisons  
- Publication time and growth patterns  

### 5.2 Feature Engineering
- Next-day view growth  
- Growth rate = (views_next_day – views_today) / views_today  
- High-growth label (upper 75th percentile)  
- Ratios: like/view, comment/view  
- One-hot encoding  
- Google Trends score  

### 5.3 Statistical Analysis
- Correlations between features and growth  
- Hypothesis tests comparing high vs low trends days  

### 5.4 Machine Learning
Tasks: binary classification or regression  
Models: Logistic Regression, Random Forest, Gradient Boosting  
Evaluation metrics: accuracy, F1-score, ROC-AUC, RMSE, MAE  
Model interpretation via feature importances

---

## 6. Expected Findings

- External search interest from Google Trends may significantly improve predictions.  
- Certain video categories may show higher growth tendencies.  
- Engagement ratios are expected to be strong predictors.

---

## 7. Limitations and Future Work

### Current Limitations
- Trending dataset reflects only already popular content  
- Google Trends measures general topic interest, not individual video interest  

### Future Directions
- NLP on titles, descriptions, and tags  
- Multi-country dataset expansion  
- More advanced time-series modeling approaches  

---

## 8. Project Structure (Directory Layout)

The recommended folder structure is below (GitHub will render this as plain text without converting it into a code block):

youtube-viral-dynamics  
│  
├── data  
│   ├── raw  
│   │   ├── USvideos.csv
│   │   ├── google_trends.csv  
│   ├── processed  
│       ├── youtube_merged.csv  
│       ├── features.csv
│  
├── notebooks  
│   ├── 01_eda.ipynb
│   ├── 02_feature_engineering.ipynb 
│   ├── 03_modeling.ipynb  
│  
├── src  
│   ├── data_preparation.py  
│   ├── feature_engineering.py  
│   ├── modeling.py  
│  
├── reports  
│   ├── figures  
│   └── final_report.md  
│  
├── requirements.txt  
└── README.md

---

## 9. Reproducibility

All code is written in Python, and all dependencies are listed in `requirements.txt`.  
The entire data pipeline is implemented through Jupyter notebooks and is fully reproducible end-to-end once the raw dataset is provided.

To reproduce the project:

### 1. Clone the repository
```bash
git clone https://github.com/kaantanidir/YouTube-Trending-Google-Trends-Viral-Prediction_fullproj.git
cd YouTube-Trending-Google-Trends-Viral-Prediction_fullproj
```
### 2. (Optional) Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate       # macOS / Linux
venv\Scripts\activate          # Windows
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Download the Kaggle dataset

Place the following file in the raw data folder:
```bash
data/raw/USvideos.csv
```
### 5. Run the notebooks in order

- **00_fetch_google_trends.ipynb**
– Fetches and saves google_trends_category.csv
– Skips the download if the file already exists (prevents API rate limits)

- **01_eda.ipynb**
– Explores the raw YouTube dataset

- **02_feature_engineering.ipynb**
– Generates features.csv and features_with_trends.csv
– Integrates Google Trends signals and computes rolling averages

- **03_modeling.ipynb**
– Trains ML models and evaluates performance using a time-based split


Once these steps are completed, all results in the repository can be reproduced exactly.
---

## 10. AI Usage Disclosure

AI tools may be used for:
- Drafting and refining documentation  
- Brainstorming ideas  
- Suggesting code components  

All AI usage will be documented in a dedicated ai_usage.md file, as required by the course.

---

## 11. Project Timeline

| Date | Milestone |
|------|-----------|
| October 31 | Submission of proposal (this README.md) |
| November 28 | Data collection, cleaning, and EDA |
| January 2 | ML model development and evaluation |
| January 9 | Final submission (23:59 deadline) |

---

## 12. Author

**Kaan Tanıdır**  
Department of Computer Science and Engineering  
Sabancı University  
Fall 2025–2026

```

which is then consumed by the modeling notebook.
