### **Card 1**  
**Front**: What is the Mean Squared Error (MSE) formula?  
**Back**:  
`MSE = (1/n) * Σ(y_actual - y_predicted)²`  
Where n = number of samples  

---

### **Card 2**  
**Front**: What is a cost function in machine learning?  
**Back**:  
A function that measures how wrong the model's predictions are.  
MSE is a common cost function for regression.  

---

### **Card 3**  
**Front**: What is gradient descent?  
**Back**:  
An optimization algorithm that minimizes the cost function by iteratively adjusting parameters in the direction of steepest descent.  

---

### **Card 4**  
**Front**: What is the learning rate (α) in gradient descent?  
**Back**:  
A hyperparameter that controls the step size during parameter updates.  
Too small = slow convergence, too large = may overshoot minimum.  

---

### **Card 5**  
**Front**: What are the gradient descent update rules for linear regression?  
**Back**:  
`m_new = m - α * ∂J/∂m`  
`b_new = b - α * ∂J/∂b`  
Where J is the cost function  

---

### **Card 6**  
**Front**: What do partial derivatives represent in gradient descent?  
**Back**:  
- `∂J/∂m` = rate of cost change with respect to slope  
- `∂J/∂b` = rate of cost change with respect to intercept  

---

### **Card 7**  
**Front**: What are the partial derivative formulas for MSE cost function?  
**Back**:  
`∂J/∂m = (-2/n) * Σ x(y - (mx + b))`  
`∂J/∂b = (-2/n) * Σ (y - (mx + b))`  

---

### **Card 8**  
**Front**: What happens if learning rate is too large?  
**Back**:  
Overshooting the minimum, causing divergence or oscillation around the optimal values.  

---

### **Card 9**  
**Front**: What happens if learning rate is too small?  
**Back**:  
Very slow convergence, requiring many iterations to reach the minimum.  

---

### **Card 10**  
**Front**: How do you know when gradient descent has converged?  
**Back**:  
When the cost function stops decreasing significantly between iterations.  

---

### **Card 11**  
**Front**: What is the typical range for learning rate values?  
**Back**:  
Usually between 0.001 and 0.1, but depends on the specific problem and data scale.  

---

### **Card 12**  
**Front**: Why do we square the errors in MSE?  
**Back**:  
To handle negative errors and penalize larger errors more heavily.