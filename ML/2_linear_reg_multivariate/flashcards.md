### **Card 1**  
**Front**: What is multiple linear regression?  
**Back**:  
A regression model with multiple independent variables predicting one dependent variable:  
`y = b + m₁x₁ + m₂x₂ + ... + mₙxₙ`  

---

### **Card 2**  
**Front**: How do you handle missing values in a DataFrame column using median?  
**Back**:  
`df['column'] = df['column'].fillna(df['column'].median())`  

---

### **Card 3**  
**Front**: How to select all columns except one as features for training?  
**Back**:  
`df.drop('target_column', axis=1)`  
Returns DataFrame without the specified column  

---

### **Card 4**  
**Front**: What does `reg.coef_` return in multiple linear regression?  
**Back**:  
An array of coefficients - one for each feature in the order they were provided  

---

### **Card 5**  
**Front**: How to manually calculate predictions using coefficients and intercept?  
**Back**:  
`prediction = intercept + (feature1 * coef1) + (feature2 * coef2) + ...`  

---

### **Card 6**  
**Front**: What's the correct format for prediction input with multiple features?  
**Back**:  
`model.predict([[feature1, feature2, feature3]])`  
Double brackets for 2D array format  

---

### **Card 7**  
**Front**: What are independent variables called in machine learning?  
**Back**:  
Features or predictors  

---

### **Card 8**  
**Front**: What is the dependent variable called in machine learning?  
**Back**:  
Target or response variable  

---

### **Card 9**  
**Front**: How to get the median of a DataFrame column?  
**Back**:  
`df['column_name'].median()`  

---

### **Card 10**  
**Front**: What does data preprocessing typically involve?  
**Back**:  
Handling missing values, feature scaling, encoding categorical variables  
