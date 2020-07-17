{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h2 style=\"color:blue\" align=\"center\">Handwritten digits classification using neural network</h2>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In this notebook we will classify handwritten digits using a simple neural network which has only input and output layers. We will than add a hidden layer and see how the performance of the model improves"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "import tensorflow as tf\n",
    "from tensorflow import keras\n",
    "import matplotlib.pyplot as plt\n",
    "%matplotlib inline\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "(X_train, y_train) , (X_test, y_test) = keras.datasets.mnist.load_data()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "60000"
      ]
     },
     "execution_count": 4,
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
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10000"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(28, 28)"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train[0].shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0],\n",
       "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0],\n",
       "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0],\n",
       "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0],\n",
       "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0],\n",
       "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   3,\n",
       "         18,  18,  18, 126, 136, 175,  26, 166, 255, 247, 127,   0,   0,\n",
       "          0,   0],\n",
       "       [  0,   0,   0,   0,   0,   0,   0,   0,  30,  36,  94, 154, 170,\n",
       "        253, 253, 253, 253, 253, 225, 172, 253, 242, 195,  64,   0,   0,\n",
       "          0,   0],\n",
       "       [  0,   0,   0,   0,   0,   0,   0,  49, 238, 253, 253, 253, 253,\n",
       "        253, 253, 253, 253, 251,  93,  82,  82,  56,  39,   0,   0,   0,\n",
       "          0,   0],\n",
       "       [  0,   0,   0,   0,   0,   0,   0,  18, 219, 253, 253, 253, 253,\n",
       "        253, 198, 182, 247, 241,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0],\n",
       "       [  0,   0,   0,   0,   0,   0,   0,   0,  80, 156, 107, 253, 253,\n",
       "        205,  11,   0,  43, 154,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0],\n",
       "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,  14,   1, 154, 253,\n",
       "         90,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0],\n",
       "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, 139, 253,\n",
       "        190,   2,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0],\n",
       "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  11, 190,\n",
       "        253,  70,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0],\n",
       "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  35,\n",
       "        241, 225, 160, 108,   1,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0],\n",
       "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "         81, 240, 253, 253, 119,  25,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0],\n",
       "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,  45, 186, 253, 253, 150,  27,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0],\n",
       "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,  16,  93, 252, 253, 187,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0],\n",
       "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0,   0, 249, 253, 249,  64,   0,   0,   0,   0,   0,\n",
       "          0,   0],\n",
       "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,  46, 130, 183, 253, 253, 207,   2,   0,   0,   0,   0,   0,\n",
       "          0,   0],\n",
       "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  39,\n",
       "        148, 229, 253, 253, 253, 250, 182,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0],\n",
       "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  24, 114, 221,\n",
       "        253, 253, 253, 253, 201,  78,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0],\n",
       "       [  0,   0,   0,   0,   0,   0,   0,   0,  23,  66, 213, 253, 253,\n",
       "        253, 253, 198,  81,   2,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0],\n",
       "       [  0,   0,   0,   0,   0,   0,  18, 171, 219, 253, 253, 253, 253,\n",
       "        195,  80,   9,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0],\n",
       "       [  0,   0,   0,   0,  55, 172, 226, 253, 253, 253, 253, 244, 133,\n",
       "         11,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0],\n",
       "       [  0,   0,   0,   0, 136, 253, 253, 253, 212, 135, 132,  16,   0,\n",
       "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0],\n",
       "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0],\n",
       "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0],\n",
       "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
       "          0,   0]], dtype=uint8)"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train[0]"
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
       "<matplotlib.image.AxesImage at 0x1fe79cb99e8>"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 288x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.matshow(X_train[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_train[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train = X_train / 255\n",
    "X_test = X_test / 255"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        ],\n",
       "       [0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        ],\n",
       "       [0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        ],\n",
       "       [0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        ],\n",
       "       [0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        ],\n",
       "       [0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.01176471, 0.07058824, 0.07058824,\n",
       "        0.07058824, 0.49411765, 0.53333333, 0.68627451, 0.10196078,\n",
       "        0.65098039, 1.        , 0.96862745, 0.49803922, 0.        ,\n",
       "        0.        , 0.        , 0.        ],\n",
       "       [0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.11764706, 0.14117647,\n",
       "        0.36862745, 0.60392157, 0.66666667, 0.99215686, 0.99215686,\n",
       "        0.99215686, 0.99215686, 0.99215686, 0.88235294, 0.6745098 ,\n",
       "        0.99215686, 0.94901961, 0.76470588, 0.25098039, 0.        ,\n",
       "        0.        , 0.        , 0.        ],\n",
       "       [0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.19215686, 0.93333333, 0.99215686,\n",
       "        0.99215686, 0.99215686, 0.99215686, 0.99215686, 0.99215686,\n",
       "        0.99215686, 0.99215686, 0.98431373, 0.36470588, 0.32156863,\n",
       "        0.32156863, 0.21960784, 0.15294118, 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        ],\n",
       "       [0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.07058824, 0.85882353, 0.99215686,\n",
       "        0.99215686, 0.99215686, 0.99215686, 0.99215686, 0.77647059,\n",
       "        0.71372549, 0.96862745, 0.94509804, 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        ],\n",
       "       [0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.31372549, 0.61176471,\n",
       "        0.41960784, 0.99215686, 0.99215686, 0.80392157, 0.04313725,\n",
       "        0.        , 0.16862745, 0.60392157, 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        ],\n",
       "       [0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.05490196,\n",
       "        0.00392157, 0.60392157, 0.99215686, 0.35294118, 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        ],\n",
       "       [0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.54509804, 0.99215686, 0.74509804, 0.00784314,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        ],\n",
       "       [0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.04313725, 0.74509804, 0.99215686, 0.2745098 ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        ],\n",
       "       [0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.1372549 , 0.94509804, 0.88235294,\n",
       "        0.62745098, 0.42352941, 0.00392157, 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        ],\n",
       "       [0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.31764706, 0.94117647,\n",
       "        0.99215686, 0.99215686, 0.46666667, 0.09803922, 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        ],\n",
       "       [0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.17647059,\n",
       "        0.72941176, 0.99215686, 0.99215686, 0.58823529, 0.10588235,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        ],\n",
       "       [0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.0627451 , 0.36470588, 0.98823529, 0.99215686, 0.73333333,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        ],\n",
       "       [0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.97647059, 0.99215686, 0.97647059,\n",
       "        0.25098039, 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        ],\n",
       "       [0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.18039216,\n",
       "        0.50980392, 0.71764706, 0.99215686, 0.99215686, 0.81176471,\n",
       "        0.00784314, 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        ],\n",
       "       [0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.15294118, 0.58039216, 0.89803922,\n",
       "        0.99215686, 0.99215686, 0.99215686, 0.98039216, 0.71372549,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        ],\n",
       "       [0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.09411765, 0.44705882, 0.86666667, 0.99215686, 0.99215686,\n",
       "        0.99215686, 0.99215686, 0.78823529, 0.30588235, 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        ],\n",
       "       [0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.09019608, 0.25882353,\n",
       "        0.83529412, 0.99215686, 0.99215686, 0.99215686, 0.99215686,\n",
       "        0.77647059, 0.31764706, 0.00784314, 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        ],\n",
       "       [0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.07058824, 0.67058824, 0.85882353, 0.99215686,\n",
       "        0.99215686, 0.99215686, 0.99215686, 0.76470588, 0.31372549,\n",
       "        0.03529412, 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        ],\n",
       "       [0.        , 0.        , 0.        , 0.        , 0.21568627,\n",
       "        0.6745098 , 0.88627451, 0.99215686, 0.99215686, 0.99215686,\n",
       "        0.99215686, 0.95686275, 0.52156863, 0.04313725, 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        ],\n",
       "       [0.        , 0.        , 0.        , 0.        , 0.53333333,\n",
       "        0.99215686, 0.99215686, 0.99215686, 0.83137255, 0.52941176,\n",
       "        0.51764706, 0.0627451 , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        ],\n",
       "       [0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        ],\n",
       "       [0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        ],\n",
       "       [0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        ]])"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train_flattened = X_train.reshape(len(X_train), 28*28)\n",
    "X_test_flattened = X_test.reshape(len(X_test), 28*28)"
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
       "(60000, 784)"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train_flattened.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.01176471, 0.07058824, 0.07058824,\n",
       "       0.07058824, 0.49411765, 0.53333333, 0.68627451, 0.10196078,\n",
       "       0.65098039, 1.        , 0.96862745, 0.49803922, 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.11764706, 0.14117647, 0.36862745, 0.60392157,\n",
       "       0.66666667, 0.99215686, 0.99215686, 0.99215686, 0.99215686,\n",
       "       0.99215686, 0.88235294, 0.6745098 , 0.99215686, 0.94901961,\n",
       "       0.76470588, 0.25098039, 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.19215686, 0.93333333,\n",
       "       0.99215686, 0.99215686, 0.99215686, 0.99215686, 0.99215686,\n",
       "       0.99215686, 0.99215686, 0.99215686, 0.98431373, 0.36470588,\n",
       "       0.32156863, 0.32156863, 0.21960784, 0.15294118, 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.07058824, 0.85882353, 0.99215686, 0.99215686,\n",
       "       0.99215686, 0.99215686, 0.99215686, 0.77647059, 0.71372549,\n",
       "       0.96862745, 0.94509804, 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.31372549, 0.61176471, 0.41960784, 0.99215686, 0.99215686,\n",
       "       0.80392157, 0.04313725, 0.        , 0.16862745, 0.60392157,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.05490196,\n",
       "       0.00392157, 0.60392157, 0.99215686, 0.35294118, 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.54509804,\n",
       "       0.99215686, 0.74509804, 0.00784314, 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.04313725, 0.74509804, 0.99215686,\n",
       "       0.2745098 , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.1372549 , 0.94509804, 0.88235294, 0.62745098,\n",
       "       0.42352941, 0.00392157, 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.31764706, 0.94117647, 0.99215686, 0.99215686, 0.46666667,\n",
       "       0.09803922, 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.17647059,\n",
       "       0.72941176, 0.99215686, 0.99215686, 0.58823529, 0.10588235,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.0627451 , 0.36470588,\n",
       "       0.98823529, 0.99215686, 0.73333333, 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.97647059, 0.99215686,\n",
       "       0.97647059, 0.25098039, 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.18039216, 0.50980392,\n",
       "       0.71764706, 0.99215686, 0.99215686, 0.81176471, 0.00784314,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.15294118,\n",
       "       0.58039216, 0.89803922, 0.99215686, 0.99215686, 0.99215686,\n",
       "       0.98039216, 0.71372549, 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.09411765, 0.44705882, 0.86666667, 0.99215686, 0.99215686,\n",
       "       0.99215686, 0.99215686, 0.78823529, 0.30588235, 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.09019608, 0.25882353, 0.83529412, 0.99215686,\n",
       "       0.99215686, 0.99215686, 0.99215686, 0.77647059, 0.31764706,\n",
       "       0.00784314, 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.07058824, 0.67058824, 0.85882353,\n",
       "       0.99215686, 0.99215686, 0.99215686, 0.99215686, 0.76470588,\n",
       "       0.31372549, 0.03529412, 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.21568627, 0.6745098 ,\n",
       "       0.88627451, 0.99215686, 0.99215686, 0.99215686, 0.99215686,\n",
       "       0.95686275, 0.52156863, 0.04313725, 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.53333333, 0.99215686, 0.99215686, 0.99215686,\n",
       "       0.83137255, 0.52941176, 0.51764706, 0.0627451 , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        ])"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train_flattened[0]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3 style='color:purple'>Very simple neural network with no hidden layers</h3>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<img src=\"digits_nn.jpg\" />"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 1/5\n",
      "1875/1875 [==============================] - 3s 1ms/step - loss: 0.4886 - accuracy: 0.8775\n",
      "Epoch 2/5\n",
      "1875/1875 [==============================] - 3s 1ms/step - loss: 0.3060 - accuracy: 0.9156\n",
      "Epoch 3/5\n",
      "1875/1875 [==============================] - 2s 1ms/step - loss: 0.2848 - accuracy: 0.9214\n",
      "Epoch 4/5\n",
      "1875/1875 [==============================] - 2s 1ms/step - loss: 0.2747 - accuracy: 0.9243\n",
      "Epoch 5/5\n",
      "1875/1875 [==============================] - 2s 1ms/step - loss: 0.2677 - accuracy: 0.9262\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<tensorflow.python.keras.callbacks.History at 0x1fe24f47a90>"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model = keras.Sequential([\n",
    "    keras.layers.Dense(10, input_shape=(784,), activation='sigmoid')\n",
    "])\n",
    "\n",
    "model.compile(optimizer='adam',\n",
    "              loss='sparse_categorical_crossentropy',\n",
    "              metrics=['accuracy'])\n",
    "\n",
    "model.fit(X_train_flattened, y_train, epochs=5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "313/313 [==============================] - 0s 985us/step - loss: 0.2670 - accuracy: 0.9257\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[0.26697656512260437, 0.9257000088691711]"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.evaluate(X_test_flattened, y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1.7270680e-05, 1.3593615e-10, 4.5622761e-05, 7.5602829e-03,\n",
       "       1.3076769e-06, 7.5061922e-05, 1.7646971e-09, 6.9968843e-01,\n",
       "       7.8440302e-05, 8.1232190e-04], dtype=float32)"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_predicted = model.predict(X_test_flattened)\n",
    "y_predicted[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.image.AxesImage at 0x1fe2322e3c8>"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 288x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.matshow(X_test[0])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**np.argmax finds a maximum element  from an array and returns the index of it**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.argmax(y_predicted[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [],
   "source": [
    "y_predicted_labels = [np.argmax(i) for i in y_predicted]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[7, 2, 1, 0, 4]"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_predicted_labels[:5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<tf.Tensor: shape=(10, 10), dtype=int32, numpy=\n",
       "array([[ 960,    0,    0,    2,    0,    5,   10,    2,    1,    0],\n",
       "       [   0, 1109,    3,    2,    0,    1,    4,    2,   14,    0],\n",
       "       [   7,    7,  929,   11,    5,    4,   15,    8,   42,    4],\n",
       "       [   3,    0,   23,  910,    0,   27,    6,   11,   23,    7],\n",
       "       [   1,    1,    2,    1,  915,    0,   16,    4,   10,   32],\n",
       "       [  11,    2,    2,   27,    9,  773,   23,    4,   33,    8],\n",
       "       [   7,    3,    5,    1,    7,    7,  925,    2,    1,    0],\n",
       "       [   1,    6,   25,    5,    8,    0,    0,  941,    2,   40],\n",
       "       [   7,    5,    7,   18,    9,   22,   11,    8,  880,    7],\n",
       "       [  11,    7,    1,   10,   32,    6,    0,   18,    9,  915]])>"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cm = tf.math.confusion_matrix(labels=y_test,predictions=y_predicted_labels)\n",
    "cm"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(69.0, 0.5, 'Truth')"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 720x504 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import seaborn as sn\n",
    "plt.figure(figsize = (10,7))\n",
    "sn.heatmap(cm, annot=True, fmt='d')\n",
    "plt.xlabel('Predicted')\n",
    "plt.ylabel('Truth')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3 style='color:purple'>Using hidden layer</h3>"
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
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 1/5\n",
      "1875/1875 [==============================] - 3s 2ms/step - loss: 0.2925 - accuracy: 0.9191\n",
      "Epoch 2/5\n",
      "1875/1875 [==============================] - 3s 2ms/step - loss: 0.1366 - accuracy: 0.9602\n",
      "Epoch 3/5\n",
      "1875/1875 [==============================] - 3s 2ms/step - loss: 0.0981 - accuracy: 0.9703\n",
      "Epoch 4/5\n",
      "1875/1875 [==============================] - 3s 2ms/step - loss: 0.0764 - accuracy: 0.9768\n",
      "Epoch 5/5\n",
      "1875/1875 [==============================] - 3s 2ms/step - loss: 0.0618 - accuracy: 0.9812\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<tensorflow.python.keras.callbacks.History at 0x1fe230e7128>"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model = keras.Sequential([\n",
    "    keras.layers.Dense(100, input_shape=(784,), activation='relu'),\n",
    "    keras.layers.Dense(10, activation='sigmoid')\n",
    "])\n",
    "\n",
    "model.compile(optimizer='adam',\n",
    "              loss='sparse_categorical_crossentropy',\n",
    "              metrics=['accuracy'])\n",
    "\n",
    "model.fit(X_train_flattened, y_train, epochs=5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "313/313 [==============================] - 0s 1ms/step - loss: 0.0966 - accuracy: 0.9716\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[0.09658893942832947, 0.9715999960899353]"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.evaluate(X_test_flattened,y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(69.0, 0.5, 'Truth')"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 720x504 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "y_predicted = model.predict(X_test_flattened)\n",
    "y_predicted_labels = [np.argmax(i) for i in y_predicted]\n",
    "cm = tf.math.confusion_matrix(labels=y_test,predictions=y_predicted_labels)\n",
    "\n",
    "plt.figure(figsize = (10,7))\n",
    "sn.heatmap(cm, annot=True, fmt='d')\n",
    "plt.xlabel('Predicted')\n",
    "plt.ylabel('Truth')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3 style='color:purple'>Using Flatten layer so that we don't have to call .reshape on input dataset</h3>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 1/10\n",
      "1875/1875 [==============================] - 3s 2ms/step - loss: 0.2959 - accuracy: 0.9185\n",
      "Epoch 2/10\n",
      "1875/1875 [==============================] - 3s 2ms/step - loss: 0.1368 - accuracy: 0.9603\n",
      "Epoch 3/10\n",
      "1875/1875 [==============================] - 3s 2ms/step - loss: 0.0995 - accuracy: 0.9703\n",
      "Epoch 4/10\n",
      "1875/1875 [==============================] - 3s 2ms/step - loss: 0.0771 - accuracy: 0.9772\n",
      "Epoch 5/10\n",
      "1875/1875 [==============================] - 3s 2ms/step - loss: 0.0628 - accuracy: 0.9806\n",
      "Epoch 6/10\n",
      "1875/1875 [==============================] - 3s 2ms/step - loss: 0.0519 - accuracy: 0.9841\n",
      "Epoch 7/10\n",
      "1875/1875 [==============================] - 3s 2ms/step - loss: 0.0442 - accuracy: 0.9865\n",
      "Epoch 8/10\n",
      "1875/1875 [==============================] - 3s 2ms/step - loss: 0.0369 - accuracy: 0.9886\n",
      "Epoch 9/10\n",
      "1875/1875 [==============================] - 3s 2ms/step - loss: 0.0300 - accuracy: 0.9910\n",
      "Epoch 10/10\n",
      "1875/1875 [==============================] - 3s 2ms/step - loss: 0.0264 - accuracy: 0.9917\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<tensorflow.python.keras.callbacks.History at 0x1fe24629e80>"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model = keras.Sequential([\n",
    "    keras.layers.Flatten(input_shape=(28, 28)),\n",
    "    keras.layers.Dense(100, activation='relu'),\n",
    "    keras.layers.Dense(10, activation='sigmoid')\n",
    "])\n",
    "\n",
    "model.compile(optimizer='adam',\n",
    "              loss='sparse_categorical_crossentropy',\n",
    "              metrics=['accuracy'])\n",
    "\n",
    "model.fit(X_train, y_train, epochs=10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "313/313 [==============================] - 0s 1ms/step - loss: 0.0813 - accuracy: 0.9779\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[0.08133944123983383, 0.9779000282287598]"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.evaluate(X_test,y_test)"
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
 "nbformat_minor": 4
}
