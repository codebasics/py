{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h2 style='color:purple' align='center'>Training And Testing Available Data</h2>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p><b>We have a dataset containing prices of used BMW cars. We are going to analyze this dataset\n",
    "and build a prediction function that can predict a price by taking mileage and age of the car\n",
    "as input. We will use sklearn train_test_split method to split training and testing dataset</b></p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mileage</th>\n",
       "      <th>Age(yrs)</th>\n",
       "      <th>Sell Price($)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>69000</td>\n",
       "      <td>6</td>\n",
       "      <td>18000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>35000</td>\n",
       "      <td>3</td>\n",
       "      <td>34000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>57000</td>\n",
       "      <td>5</td>\n",
       "      <td>26100</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>22500</td>\n",
       "      <td>2</td>\n",
       "      <td>40000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>46000</td>\n",
       "      <td>4</td>\n",
       "      <td>31500</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Mileage  Age(yrs)  Sell Price($)\n",
       "0    69000         6          18000\n",
       "1    35000         3          34000\n",
       "2    57000         5          26100\n",
       "3    22500         2          40000\n",
       "4    46000         4          31500"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "df = pd.read_csv(\"carprices.csv\")\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Car Mileage Vs Sell Price ($)**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.collections.PathCollection at 0x2882746dd30>"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\nWc7/B/NG8AYrTXDmAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x288273dfdd8>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.scatter(df['Mileage'],df['Sell Price($)'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Car Age Vs Sell Price ($)**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.collections.PathCollection at 0x28826e06240>"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x2882732b358>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.scatter(df['Age(yrs)'],df['Sell Price($)'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Looking at above two scatter plots, using linear regression model makes sense as we can clearly see a linear relationship between our dependant (i.e. Sell Price) and independant variables (i.e. car age and car mileage)**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p style='color:purple'><b>The approach we are going to use here is to split available data in two sets</b></p>\n",
    "    <ol>\n",
    "        <b>\n",
    "        <li>Training: We will train our model on this dataset</li>\n",
    "        <li>Testing: We will use this subset to make actual predictions using trained model</li>\n",
    "        </b>\n",
    "     </ol>\n",
    "<p style='color:purple'><b>The reason we don't use same training set for testing is because our model has seen those samples before, using same samples for making predictions might give us wrong impression about accuracy of our model. It is like you ask same questions in exam paper as you tought the students in the class.\n",
    "</b></p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "X = df[['Mileage','Age(yrs)']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "y = df['Sell Price($)']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mileage</th>\n",
       "      <th>Age(yrs)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>79000</td>\n",
       "      <td>7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>69000</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>83000</td>\n",
       "      <td>7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>35000</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>69000</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>91000</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>72000</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>28000</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>52000</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>46000</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>52000</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>57000</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>59000</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>25400</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Mileage  Age(yrs)\n",
       "11    79000         7\n",
       "17    69000         5\n",
       "10    83000         7\n",
       "1     35000         3\n",
       "0     69000         6\n",
       "8     91000         8\n",
       "7     72000         6\n",
       "16    28000         2\n",
       "6     52000         5\n",
       "4     46000         4\n",
       "19    52000         5\n",
       "2     57000         5\n",
       "5     59000         5\n",
       "15    25400         3"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mileage</th>\n",
       "      <th>Age(yrs)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>22500</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>59000</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>82450</td>\n",
       "      <td>7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>58780</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>67000</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>87600</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Mileage  Age(yrs)\n",
       "3     22500         2\n",
       "12    59000         5\n",
       "14    82450         7\n",
       "13    58780         4\n",
       "9     67000         6\n",
       "18    87600         8"
      ]
     },
     "execution_count": 18,
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
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "11    19500\n",
       "17    19700\n",
       "10    18700\n",
       "1     34000\n",
       "0     18000\n",
       "8     12000\n",
       "7     19300\n",
       "16    35500\n",
       "6     32000\n",
       "4     31500\n",
       "19    28200\n",
       "2     26100\n",
       "5     26750\n",
       "15    35000\n",
       "Name: Sell Price($), dtype: int64"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_train"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3     40000\n",
       "12    26000\n",
       "14    19400\n",
       "13    27500\n",
       "9     22000\n",
       "18    12800\n",
       "Name: Sell Price($), dtype: int64"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_test"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Lets run linear regression model now**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.linear_model import LinearRegression\n",
    "clf = LinearRegression()\n",
    "clf.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mileage</th>\n",
       "      <th>Age(yrs)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>22500</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>59000</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>82450</td>\n",
       "      <td>7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>58780</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>67000</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>87600</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Mileage  Age(yrs)\n",
       "3     22500         2\n",
       "12    59000         5\n",
       "14    82450         7\n",
       "13    58780         4\n",
       "9     67000         6\n",
       "18    87600         8"
      ]
     },
     "execution_count": 25,
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
   "execution_count": 26,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 38166.23426912,  25092.95646646,  16773.29470749,  24096.93956163,\n",
       "        22602.44614295,  15559.98266172])"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "clf.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3     40000\n",
       "12    26000\n",
       "14    19400\n",
       "13    27500\n",
       "9     22000\n",
       "18    12800\n",
       "Name: Sell Price($), dtype: int64"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.92713129118963111"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "clf.score(X_test, y_test)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**random_state argument**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mileage</th>\n",
       "      <th>Age(yrs)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>72000</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>83000</td>\n",
       "      <td>7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>59000</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>52000</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>22500</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>87600</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Mileage  Age(yrs)\n",
       "7     72000         6\n",
       "10    83000         7\n",
       "5     59000         5\n",
       "6     52000         5\n",
       "3     22500         2\n",
       "18    87600         8"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=10)\n",
    "X_test"
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
   "version": "3.6.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
