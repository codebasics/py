{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h2 style=\"color:green\" align=\"center\">Predicting if a person would buy life insurnace based on his age using logistic regression</h2>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Above is a binary logistic regression problem as there are only two possible outcomes (i.e. if person buys insurance or he/she doesn't). "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from matplotlib import pyplot as plt\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>bought_insurance</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>22</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>25</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>47</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>52</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>46</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   age  bought_insurance\n",
       "0   22                 0\n",
       "1   25                 0\n",
       "2   47                 1\n",
       "3   52                 0\n",
       "4   46                 1"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_csv(\"insurance_data.csv\")\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.collections.PathCollection at 0x20a8cb15d30>"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.scatter(df.age,df.bought_insurance,marker='+',color='red')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train, X_test, y_train, y_test = train_test_split(df[['age']],df.bought_insurance,train_size=0.8)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>46</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>62</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>26</th>\n",
       "      <td>23</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>58</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25</th>\n",
       "      <td>54</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    age\n",
       "4    46\n",
       "8    62\n",
       "26   23\n",
       "17   58\n",
       "24   50\n",
       "25   54"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.linear_model import LogisticRegression\n",
    "model = LogisticRegression()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\ProgramData\\Anaconda3\\lib\\site-packages\\sklearn\\linear_model\\logistic.py:433: FutureWarning: Default solver will be changed to 'lbfgs' in 0.22. Specify a solver to silence this warning.\n",
      "  FutureWarning)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,\n",
       "          intercept_scaling=1, max_iter=100, multi_class='warn',\n",
       "          n_jobs=None, penalty='l2', random_state=None, solver='warn',\n",
       "          tol=0.0001, verbose=0, warm_start=False)"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>25</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>47</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    age\n",
       "16   25\n",
       "21   26\n",
       "2    47"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [],
   "source": [
    "y_predicted = model.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0.40569485, 0.59430515],\n",
       "       [0.26002994, 0.73997006],\n",
       "       [0.63939494, 0.36060506],\n",
       "       [0.29321765, 0.70678235],\n",
       "       [0.36637568, 0.63362432],\n",
       "       [0.32875922, 0.67124078]])"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.predict_proba(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.0"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.score(X_test,y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 1, 0, 1, 1, 1], dtype=int64)"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_predicted"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>46</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>62</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>26</th>\n",
       "      <td>23</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>58</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25</th>\n",
       "      <td>54</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    age\n",
       "4    46\n",
       "8    62\n",
       "26   23\n",
       "17   58\n",
       "24   50\n",
       "25   54"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_test"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**model.coef_ indicates value of m in y=m*x + b equation**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0.04150133]])"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.coef_"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**model.intercept_ indicates value of b in y=m*x + b equation**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([-1.52726963])"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.intercept_"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Lets defined sigmoid function now and do the math with hand**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "import math\n",
    "def sigmoid(x):\n",
    "  return 1 / (1 + math.exp(-x))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [],
   "source": [
    "def prediction_function(age):\n",
    "    z = 0.042 * age - 1.53 # 0.04150133 ~ 0.042 and -1.52726963 ~ -1.53\n",
    "    y = sigmoid(z)\n",
    "    return y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.4850044983805899"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "age = 35\n",
    "prediction_function(age)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**0.485 is less than 0.5 which means person with 35 age will *not* buy insurance**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.568565299077705"
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "age = 43\n",
    "prediction_function(age)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**0.485 is more than 0.5 which means person with 43 will buy the insurance**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h2 style=\"color:purple\">Exercise</h2>\n",
    "\n",
    "Download employee retention dataset from here: https://www.kaggle.com/giripujar/hr-analytics. \n",
    "1. Now do some exploratory data analysis to figure out which variables have direct and clear impact on employee retention (i.e. whether they leave the company or continue to work)\n",
    "2. Plot bar charts showing impact of employee salaries on retention\n",
    "3. Plot bar charts showing corelation between department and employee retention\n",
    "4. Now build logistic regression model using variables that were narrowed down in step 1\n",
    "5. Measure the accuracy of the model"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
