# Modeling Viral Dynamics: Predicting YouTube Video Popularity

This repository contains a complete, ready-to-run skeleton for the project:

**"Modeling Viral Dynamics: Predicting YouTube Video Popularity Using Platform Metrics and External Search Interest"**

## How to use

1. Create a virtual environment and install requirements:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

2. Download the Kaggle dataset `USvideos.csv` (from `datasnaek/youtube-new`) and place it into:

   ```text
   data/raw/USvideos.csv
   ```

3. Open the project in VS Code and run the notebooks in the following order:

   - `notebooks/01_eda.ipynb` – exploratory data analysis
   - `notebooks/02_feature_engineering.ipynb` – feature engineering and label creation
   - `notebooks/03_modeling.ipynb` – machine learning models

After running `02_feature_engineering.ipynb`, a processed feature file will be written to:

```text
data/processed/features.csv
```

which is then consumed by the modeling notebook.
