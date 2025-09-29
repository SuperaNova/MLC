
# Team MatchaLabubuClairo

something our info or something

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/your-username/project-name/)

---

# Project Structure

```bash
MLC/
│── data/               # Datasets (not tracked in git, add to .gitignore)
│── notebooks/          # Jupyter notebooks (.ipynb)
│── requirements.txt    # Python dependencies
│── .gitignore
│── README.md
```

---

# Local Setup

## Clone the repo
```bash
git clone https://github.com/SuperaNova/MLC.git
cd MLC
```

## Create virtual environment
```bash
python -m venv venv
```

---
# Activate environment
## On Windows:
```bash
venv\Scripts\activate
```
## On Mac/Linux:
```bash
source venv/bin/activate
```

## Install dependencies
```bash
pip install -r requirements.txt
```

## Start Jupyter
```bash
jupyter notebook
```

---

# Google Colab Setup

1. Open [Google Colab](https://colab.research.google.com/).
2. Select **GitHub** tab and search for this repo:
   `https://github.com/SuperaNova/MLC`
3. Open the notebook you want.
4. At the top of the Colab notebook, install dependencies:

   ```python
   !pip install -r requirements.txt
   ```

---

# Dependencies

All required libraries are in `requirements.txt`.
Update it if you add new packages:

```bash
pip freeze > requirements.txt
```

---

# Notes

* Keep datasets in `data/` (ignored by git).
* Use `notebooks/` for all experiments.
* When working in Colab, re-run `!pip install -r requirements.txt` if a new dependency is added.

