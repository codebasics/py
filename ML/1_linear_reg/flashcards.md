### **Card 1**  
**Front**: What is the mathematical equation for linear regression?  
**Back**:  
`y = mx + b`  
Where: y = dependent variable, x = independent variable, m = slope/coefficient, b = intercept  

---

### **Card 2**  
**Front**: Which sklearn module contains the LinearRegression class?  
**Back**:  
`from sklearn import linear_model`  

---

### **Card 3**  
**Front**: What method trains a linear regression model on data?  
**Back**:  
`model.fit(X, y)`  
Where X = feature matrix, y = target vector  

---

### **Card 4**  
**Front**: How do you make predictions with a trained linear regression model?  
**Back**:  
`model.predict(X_new)`  
Where X_new = new feature values to predict  

---

### **Card 5**  
**Front**: What do the coef_ and intercept_ attributes store in a linear regression model?  
**Back**:  
- `coef_`: Slope coefficients (m values)  
- `intercept_`: Y-intercept (b value)  

---

### **Card 6**  
**Front**: How can you manually calculate predictions using coef_ and intercept_?  
**Back**:  
`prediction = (X * model.coef_) + model.intercept_`  
For single feature: `prediction = X * coef_ + intercept_`  

---

### **Card 7**  
**Front**: What matplotlib function creates a scatter plot?  
**Back**:  
`plt.scatter(x, y)`  
Plots x values against y values as points  

---

### **Card 8**  
**Front**: How do you remove a column from a pandas DataFrame?  
**Back**:  
`df.drop('column_name', axis=1)`  
or `df.drop('column_name', axis='columns')`  

---

### **Card 9**  
**Front**: How do you add a new column with predictions to a DataFrame?  
**Back**:  
`df['new_column_name'] = predictions_array`  

---

### **Card 10**  
**Front**: What method exports a DataFrame to a CSV file?  
**Back**:  
`df.to_csv("filename.csv")`  
Saves DataFrame as comma-separated values file  