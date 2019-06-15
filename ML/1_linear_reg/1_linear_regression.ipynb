{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h2 style=\"color:green\" align=\"center\">Machine Learning With Python: Linear Regression With One Variable</h2>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3 style=\"color:purple\">Sample problem of predicting home price in monroe, new jersey (USA)</h3>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Below table represents current home prices in monroe township based on square feet area, new jersey"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<img src=\"homepricetable.JPG\" style=\"width:370px;height:250px\">"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Problem Statement**: Given above data build a machine learning model that can predict home prices based on square feet area\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You can represent values in above table as a scatter plot (values are shown in red markers). After that one can draw a straight line that best fits values on chart. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<img src=\"scatterplot.JPG\" style=\"width:600px;height:370px\">"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You can draw multiple lines like this but we choose the one where total sum of error is minimum"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<img src=\"equation.PNG\" style=\"width:600px;height:370px\" >"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You might remember about linear equation from your high school days math class. Home prices can be presented as following equation,\n",
    "\n",
    "home price = m * (area) + b\n",
    "\n",
    "Generic form of same equation is,"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<img src=\"linear_equation.png\" >"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "from sklearn import linear_model\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
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
       "      <th>area</th>\n",
       "      <th>price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2600</td>\n",
       "      <td>550000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>3000</td>\n",
       "      <td>565000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3200</td>\n",
       "      <td>610000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3600</td>\n",
       "      <td>680000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4000</td>\n",
       "      <td>725000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   area   price\n",
       "0  2600  550000\n",
       "1  3000  565000\n",
       "2  3200  610000\n",
       "3  3600  680000\n",
       "4  4000  725000"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_csv('homeprices.csv')\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.collections.PathCollection at 0x25c8eb78d68>"
      ]
     },
     "execution_count": 3,
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
    "%matplotlib inline\n",
    "plt.xlabel('area')\n",
    "plt.ylabel('price')\n",
    "plt.scatter(df.area,df.price,color='red',marker='+')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
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
       "      <th>area</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2600</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>3000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3600</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   area\n",
       "0  2600\n",
       "1  3000\n",
       "2  3200\n",
       "3  3600\n",
       "4  4000"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_df = df.drop('price',axis='columns')\n",
    "new_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    550000\n",
       "1    565000\n",
       "2    610000\n",
       "3    680000\n",
       "4    725000\n",
       "Name: price, dtype: int64"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "price = df.price\n",
    "price"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None,\n",
       "         normalize=False)"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Create linear regression object\n",
    "reg = linear_model.LinearRegression()\n",
    "reg.fit(new_df,price)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**(1) Predict price of a home with area = 3300 sqr ft**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([628715.75342466])"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "reg.predict([[3300]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([135.78767123])"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "reg.coef_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "180616.43835616432"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "reg.intercept_"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Y = m * X + b (m is coefficient and b is intercept)**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "628715.7534151643"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "3300*135.78767123 + 180616.43835616432"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**(1) Predict price of a home with area = 5000 sqr ft**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([859554.79452055])"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "reg.predict([[5000]])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3 style=\"color:purple\">Generate CSV file with list of home price predictions</h3>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
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
       "      <th>area</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2300</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   area\n",
       "0  1000\n",
       "1  1500\n",
       "2  2300"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "area_df = pd.read_csv(\"areas.csv\")\n",
    "area_df.head(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 316404.10958904,  384297.94520548,  492928.08219178,\n",
       "        661304.79452055,  740061.64383562,  799808.21917808,\n",
       "        926090.75342466,  650441.78082192,  825607.87671233,\n",
       "        492928.08219178, 1402705.47945205, 1348390.4109589 ,\n",
       "       1144708.90410959])"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "p = reg.predict(area_df)\n",
    "p"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
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
       "      <th>area</th>\n",
       "      <th>prices</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1000</td>\n",
       "      <td>3.164041e+05</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1500</td>\n",
       "      <td>3.842979e+05</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2300</td>\n",
       "      <td>4.929281e+05</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3540</td>\n",
       "      <td>6.613048e+05</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4120</td>\n",
       "      <td>7.400616e+05</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>4560</td>\n",
       "      <td>7.998082e+05</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>5490</td>\n",
       "      <td>9.260908e+05</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>3460</td>\n",
       "      <td>6.504418e+05</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>4750</td>\n",
       "      <td>8.256079e+05</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>2300</td>\n",
       "      <td>4.929281e+05</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>9000</td>\n",
       "      <td>1.402705e+06</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>8600</td>\n",
       "      <td>1.348390e+06</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>7100</td>\n",
       "      <td>1.144709e+06</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    area        prices\n",
       "0   1000  3.164041e+05\n",
       "1   1500  3.842979e+05\n",
       "2   2300  4.929281e+05\n",
       "3   3540  6.613048e+05\n",
       "4   4120  7.400616e+05\n",
       "5   4560  7.998082e+05\n",
       "6   5490  9.260908e+05\n",
       "7   3460  6.504418e+05\n",
       "8   4750  8.256079e+05\n",
       "9   2300  4.929281e+05\n",
       "10  9000  1.402705e+06\n",
       "11  8600  1.348390e+06\n",
       "12  7100  1.144709e+06"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "area_df['prices']=p\n",
    "area_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "area_df.to_csv(\"prediction.csv\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3>Exercise</h3>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p >Predict canada's per capita income in year 2020. There is an exercise folder here on github at same level as this notebook, download that and you will find canada_per_capita_income.csv file. Using this build a regression model and predict the per capita income fo canadian citizens in year 2020</p>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3>Answer</h3>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "41288.69409442"
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
