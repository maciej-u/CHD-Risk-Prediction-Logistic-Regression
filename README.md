# Cardiovascular Disease Risk Prediction using Logistic Regression

This project aims to predict the risk of coronary heart disease (CHD) using logistic regression models. The project utilises the Cardiovascular Study Dataset, which contains various health indicators, to train and evaluate the models.

## Project Overview
Cardiovascular heart disease (CHD) is a leading cause of death worldwide. Early prediction of CHD risk can help in timely intervention and prevention. This project focuses on developing logistic regression models to predict the risk of CHD based on various health indicators such as age, blood pressure, cholesterol levels, and more.

The project follows a structured approach, including data cleaning, exploratory data analysis, preprocessing, feature selection, model training, and evaluation. The logistic regression models are built using the scikit-learn library in Python.

## Dataset
The project utilizes the [Cardiovascular Study Dataset](https://www.kaggle.com/datasets/christofel04/cardiovascular-study-dataset-predict-heart-disea/data) from Kaggle. The dataset contains information about patients, including their age, gender, blood pressure, cholesterol levels, and other health indicators. The target variable is the presence or absence of cardiovascular heart disease (CHD).

## Repository Structure
The repository is structured as follows:

- `DA_PY_4_4.ipynb`: Turing College project description and requirements.
- `Predictive_Modeling_Logistic_Regression.ipynb`: Jupyter Notebook containing the whole project, including data cleaning, EDA, preprocessing and logistic regression modelling and evaluation.
- `README.md`: This file, providing an overview of the project.
- `extreme_outliers_function.py`: Python script containing the function for removing extreme outliers.
- `outliers_function.py`: Python script containing the function for identifying outliers.
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `train.csv`: The dataset used for model development.

## Requirements

- Jupyter Notebook
- Python 3.x
- Pandas
- Numpy
- Matplotlib
- Seaborn
- Scikit-learn
- Scipy

## Libraries and Versions
```
- python == 3.12.0
- pandas == 2.2.2
- numpy == 2.0.0
- matplotlib == 3.9.1
- seaborn == 0.13.2
- scikit-learn == 1.5.1
- scipy == 1.14.0
   ```


## Results
The logistic regression models achieved an accuracy of 67% on the test set. The models were evaluated using various metrics such as precision, recall, F1-score, and ROC AUC. The results show the possible application and effectiveness of logistic regression in predicting cardiovascular disease risk based on the given health indicators.

For detailed results and analysis, refer to the Jupyter Notebooks in the repository.