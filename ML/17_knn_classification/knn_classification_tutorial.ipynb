{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h2 style='color:blue' align=\"center\">KNN (K Nearest Neighbors) Classification: Machine Tutorial Using Python Sklearn</h2>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from sklearn.datasets import load_iris\n",
    "iris = load_iris()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<img height=300 width=300 src=\"iris_petal_sepal.png\" />"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['sepal length (cm)',\n",
       " 'sepal width (cm)',\n",
       " 'petal length (cm)',\n",
       " 'petal width (cm)']"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "iris.feature_names"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['setosa', 'versicolor', 'virginica'], dtype='<U10')"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "iris.target_names"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
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
       "      <th>sepal length (cm)</th>\n",
       "      <th>sepal width (cm)</th>\n",
       "      <th>petal length (cm)</th>\n",
       "      <th>petal width (cm)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>5.1</td>\n",
       "      <td>3.5</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0.2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>4.9</td>\n",
       "      <td>3.0</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0.2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>4.7</td>\n",
       "      <td>3.2</td>\n",
       "      <td>1.3</td>\n",
       "      <td>0.2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4.6</td>\n",
       "      <td>3.1</td>\n",
       "      <td>1.5</td>\n",
       "      <td>0.2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5.0</td>\n",
       "      <td>3.6</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0.2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)\n",
       "0                5.1               3.5                1.4               0.2\n",
       "1                4.9               3.0                1.4               0.2\n",
       "2                4.7               3.2                1.3               0.2\n",
       "3                4.6               3.1                1.5               0.2\n",
       "4                5.0               3.6                1.4               0.2"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.DataFrame(iris.data,columns=iris.feature_names)\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
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
       "      <th>sepal length (cm)</th>\n",
       "      <th>sepal width (cm)</th>\n",
       "      <th>petal length (cm)</th>\n",
       "      <th>petal width (cm)</th>\n",
       "      <th>target</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>5.1</td>\n",
       "      <td>3.5</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0.2</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>4.9</td>\n",
       "      <td>3.0</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0.2</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>4.7</td>\n",
       "      <td>3.2</td>\n",
       "      <td>1.3</td>\n",
       "      <td>0.2</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4.6</td>\n",
       "      <td>3.1</td>\n",
       "      <td>1.5</td>\n",
       "      <td>0.2</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5.0</td>\n",
       "      <td>3.6</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0.2</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)  \\\n",
       "0                5.1               3.5                1.4               0.2   \n",
       "1                4.9               3.0                1.4               0.2   \n",
       "2                4.7               3.2                1.3               0.2   \n",
       "3                4.6               3.1                1.5               0.2   \n",
       "4                5.0               3.6                1.4               0.2   \n",
       "\n",
       "   target  \n",
       "0       0  \n",
       "1       0  \n",
       "2       0  \n",
       "3       0  \n",
       "4       0  "
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['target'] = iris.target\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
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
       "      <th>sepal length (cm)</th>\n",
       "      <th>sepal width (cm)</th>\n",
       "      <th>petal length (cm)</th>\n",
       "      <th>petal width (cm)</th>\n",
       "      <th>target</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>50</th>\n",
       "      <td>7.0</td>\n",
       "      <td>3.2</td>\n",
       "      <td>4.7</td>\n",
       "      <td>1.4</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>51</th>\n",
       "      <td>6.4</td>\n",
       "      <td>3.2</td>\n",
       "      <td>4.5</td>\n",
       "      <td>1.5</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>52</th>\n",
       "      <td>6.9</td>\n",
       "      <td>3.1</td>\n",
       "      <td>4.9</td>\n",
       "      <td>1.5</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>53</th>\n",
       "      <td>5.5</td>\n",
       "      <td>2.3</td>\n",
       "      <td>4.0</td>\n",
       "      <td>1.3</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>54</th>\n",
       "      <td>6.5</td>\n",
       "      <td>2.8</td>\n",
       "      <td>4.6</td>\n",
       "      <td>1.5</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)  \\\n",
       "50                7.0               3.2                4.7               1.4   \n",
       "51                6.4               3.2                4.5               1.5   \n",
       "52                6.9               3.1                4.9               1.5   \n",
       "53                5.5               2.3                4.0               1.3   \n",
       "54                6.5               2.8                4.6               1.5   \n",
       "\n",
       "    target  \n",
       "50       1  \n",
       "51       1  \n",
       "52       1  \n",
       "53       1  \n",
       "54       1  "
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[df.target==1].head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
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
       "      <th>sepal length (cm)</th>\n",
       "      <th>sepal width (cm)</th>\n",
       "      <th>petal length (cm)</th>\n",
       "      <th>petal width (cm)</th>\n",
       "      <th>target</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>100</th>\n",
       "      <td>6.3</td>\n",
       "      <td>3.3</td>\n",
       "      <td>6.0</td>\n",
       "      <td>2.5</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>101</th>\n",
       "      <td>5.8</td>\n",
       "      <td>2.7</td>\n",
       "      <td>5.1</td>\n",
       "      <td>1.9</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>102</th>\n",
       "      <td>7.1</td>\n",
       "      <td>3.0</td>\n",
       "      <td>5.9</td>\n",
       "      <td>2.1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>103</th>\n",
       "      <td>6.3</td>\n",
       "      <td>2.9</td>\n",
       "      <td>5.6</td>\n",
       "      <td>1.8</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>104</th>\n",
       "      <td>6.5</td>\n",
       "      <td>3.0</td>\n",
       "      <td>5.8</td>\n",
       "      <td>2.2</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)  \\\n",
       "100                6.3               3.3                6.0               2.5   \n",
       "101                5.8               2.7                5.1               1.9   \n",
       "102                7.1               3.0                5.9               2.1   \n",
       "103                6.3               2.9                5.6               1.8   \n",
       "104                6.5               3.0                5.8               2.2   \n",
       "\n",
       "     target  \n",
       "100       2  \n",
       "101       2  \n",
       "102       2  \n",
       "103       2  \n",
       "104       2  "
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[df.target==2].head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
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
       "      <th>sepal length (cm)</th>\n",
       "      <th>sepal width (cm)</th>\n",
       "      <th>petal length (cm)</th>\n",
       "      <th>petal width (cm)</th>\n",
       "      <th>target</th>\n",
       "      <th>flower_name</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>5.1</td>\n",
       "      <td>3.5</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0.2</td>\n",
       "      <td>0</td>\n",
       "      <td>setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>4.9</td>\n",
       "      <td>3.0</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0.2</td>\n",
       "      <td>0</td>\n",
       "      <td>setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>4.7</td>\n",
       "      <td>3.2</td>\n",
       "      <td>1.3</td>\n",
       "      <td>0.2</td>\n",
       "      <td>0</td>\n",
       "      <td>setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4.6</td>\n",
       "      <td>3.1</td>\n",
       "      <td>1.5</td>\n",
       "      <td>0.2</td>\n",
       "      <td>0</td>\n",
       "      <td>setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5.0</td>\n",
       "      <td>3.6</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0.2</td>\n",
       "      <td>0</td>\n",
       "      <td>setosa</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)  \\\n",
       "0                5.1               3.5                1.4               0.2   \n",
       "1                4.9               3.0                1.4               0.2   \n",
       "2                4.7               3.2                1.3               0.2   \n",
       "3                4.6               3.1                1.5               0.2   \n",
       "4                5.0               3.6                1.4               0.2   \n",
       "\n",
       "   target flower_name  \n",
       "0       0      setosa  \n",
       "1       0      setosa  \n",
       "2       0      setosa  \n",
       "3       0      setosa  \n",
       "4       0      setosa  "
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['flower_name'] =df.target.apply(lambda x: iris.target_names[x])\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
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
       "      <th>sepal length (cm)</th>\n",
       "      <th>sepal width (cm)</th>\n",
       "      <th>petal length (cm)</th>\n",
       "      <th>petal width (cm)</th>\n",
       "      <th>target</th>\n",
       "      <th>flower_name</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>45</th>\n",
       "      <td>4.8</td>\n",
       "      <td>3.0</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0.3</td>\n",
       "      <td>0</td>\n",
       "      <td>setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>46</th>\n",
       "      <td>5.1</td>\n",
       "      <td>3.8</td>\n",
       "      <td>1.6</td>\n",
       "      <td>0.2</td>\n",
       "      <td>0</td>\n",
       "      <td>setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>47</th>\n",
       "      <td>4.6</td>\n",
       "      <td>3.2</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0.2</td>\n",
       "      <td>0</td>\n",
       "      <td>setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>48</th>\n",
       "      <td>5.3</td>\n",
       "      <td>3.7</td>\n",
       "      <td>1.5</td>\n",
       "      <td>0.2</td>\n",
       "      <td>0</td>\n",
       "      <td>setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>49</th>\n",
       "      <td>5.0</td>\n",
       "      <td>3.3</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0.2</td>\n",
       "      <td>0</td>\n",
       "      <td>setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50</th>\n",
       "      <td>7.0</td>\n",
       "      <td>3.2</td>\n",
       "      <td>4.7</td>\n",
       "      <td>1.4</td>\n",
       "      <td>1</td>\n",
       "      <td>versicolor</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>51</th>\n",
       "      <td>6.4</td>\n",
       "      <td>3.2</td>\n",
       "      <td>4.5</td>\n",
       "      <td>1.5</td>\n",
       "      <td>1</td>\n",
       "      <td>versicolor</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>52</th>\n",
       "      <td>6.9</td>\n",
       "      <td>3.1</td>\n",
       "      <td>4.9</td>\n",
       "      <td>1.5</td>\n",
       "      <td>1</td>\n",
       "      <td>versicolor</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>53</th>\n",
       "      <td>5.5</td>\n",
       "      <td>2.3</td>\n",
       "      <td>4.0</td>\n",
       "      <td>1.3</td>\n",
       "      <td>1</td>\n",
       "      <td>versicolor</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>54</th>\n",
       "      <td>6.5</td>\n",
       "      <td>2.8</td>\n",
       "      <td>4.6</td>\n",
       "      <td>1.5</td>\n",
       "      <td>1</td>\n",
       "      <td>versicolor</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)  \\\n",
       "45                4.8               3.0                1.4               0.3   \n",
       "46                5.1               3.8                1.6               0.2   \n",
       "47                4.6               3.2                1.4               0.2   \n",
       "48                5.3               3.7                1.5               0.2   \n",
       "49                5.0               3.3                1.4               0.2   \n",
       "50                7.0               3.2                4.7               1.4   \n",
       "51                6.4               3.2                4.5               1.5   \n",
       "52                6.9               3.1                4.9               1.5   \n",
       "53                5.5               2.3                4.0               1.3   \n",
       "54                6.5               2.8                4.6               1.5   \n",
       "\n",
       "    target flower_name  \n",
       "45       0      setosa  \n",
       "46       0      setosa  \n",
       "47       0      setosa  \n",
       "48       0      setosa  \n",
       "49       0      setosa  \n",
       "50       1  versicolor  \n",
       "51       1  versicolor  \n",
       "52       1  versicolor  \n",
       "53       1  versicolor  \n",
       "54       1  versicolor  "
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[45:55]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [],
   "source": [
    "df0 = df[:50]\n",
    "df1 = df[50:100]\n",
    "df2 = df[100:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
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
    "**Sepal length vs Sepal Width (Setosa vs Versicolor)**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.collections.PathCollection at 0x2d5f7f3a460>"
      ]
     },
     "execution_count": 57,
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
    "plt.xlabel('Sepal Length')\n",
    "plt.ylabel('Sepal Width')\n",
    "plt.scatter(df0['sepal length (cm)'], df0['sepal width (cm)'],color=\"green\",marker='+')\n",
    "plt.scatter(df1['sepal length (cm)'], df1['sepal width (cm)'],color=\"blue\",marker='.')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Petal length vs Pepal Width (Setosa vs Versicolor)**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.collections.PathCollection at 0x2d5f75af700>"
      ]
     },
     "execution_count": 58,
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
    "plt.xlabel('Petal Length')\n",
    "plt.ylabel('Petal Width')\n",
    "plt.scatter(df0['petal length (cm)'], df0['petal width (cm)'],color=\"green\",marker='+')\n",
    "plt.scatter(df1['petal length (cm)'], df1['petal width (cm)'],color=\"blue\",marker='.')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Train test split**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [],
   "source": [
    "X = df.drop(['target','flower_name'], axis='columns')\n",
    "y = df.target"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "120"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(X_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "30"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(X_test)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Create KNN (K Neighrest Neighbour Classifier)**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "knn = KNeighborsClassifier(n_neighbors=10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "KNeighborsClassifier(n_neighbors=10)"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "knn.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9666666666666667"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "knn.score(X_test, y_test)"
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
       "array([0])"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "knn.predict([[4.8,3.0,1.5,0.3]])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Plot Confusion Matrix**"
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
       "array([[11,  0,  0],\n",
       "       [ 0, 12,  1],\n",
       "       [ 0,  0,  6]], dtype=int64)"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.metrics import confusion_matrix\n",
    "y_pred = knn.predict(X_test)\n",
    "cm = confusion_matrix(y_test, y_pred)\n",
    "cm"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(42.0, 0.5, 'Truth')"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 504x360 with 2 Axes>"
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
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sn\n",
    "plt.figure(figsize=(7,5))\n",
    "sn.heatmap(cm, annot=True)\n",
    "plt.xlabel('Predicted')\n",
    "plt.ylabel('Truth')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Print classification report for precesion, recall and f1-score for each classes**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       1.00      1.00      1.00        11\n",
      "           1       1.00      0.92      0.96        13\n",
      "           2       0.86      1.00      0.92         6\n",
      "\n",
      "    accuracy                           0.97        30\n",
      "   macro avg       0.95      0.97      0.96        30\n",
      "weighted avg       0.97      0.97      0.97        30\n",
      "\n"
     ]
    }
   ],
   "source": [
    "from sklearn.metrics import classification_report\n",
    "\n",
    "print(classification_report(y_test, y_pred))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Do not forget to work on exercise, exercise link is below** \n",
    "\n",
    "https://github.com/codebasics/py/blob/master/ML/17_knn_classification/knn_exercise.md\n"
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
