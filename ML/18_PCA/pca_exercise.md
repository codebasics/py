Download heart disease dataset heart.csv in [Exercise](https://github.com/codebasics/py/tree/master/ML/18_PCA/Exercise) folder and do following, (credits of dataset:  https://www.kaggle.com/fedesoriano/heart-failure-prediction)

1. Load heart disease dataset in pandas dataframe
1. Remove outliers using Z score. Usual guideline is to remove anything that has Z score > 3 formula or Z score < -3
1. Convert text columns to numbers using label encoding and one hot encoding
1. Apply scaling
1. Build a classification model using various methods (SVM, logistic regression, random forest) and check which model gives you the best accuracy
1. Now use PCA to reduce dimensions, retrain your model and see what impact it has on your model in terms of accuracy. Keep in mind that many times doing PCA reduces the accuracy but computation is much lighter and that's the trade off you need to consider while building models in real life


[Solution Link](https://github.com/codebasics/py/blob/master/ML/18_PCA/Exercise/PCA_heart_disease_prediction_exercise_solution.ipynb)



 