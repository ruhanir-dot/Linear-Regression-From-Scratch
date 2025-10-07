import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv("C:\\Users\\Ruhani R\\Downloads\\Lungs.csv")

# m is our b_1 (slope), b is our b_0 (intercept)

# E --> the function we want to minimize
def loss_function(m,b,points): 
    total_error = 0 
    for i in range(len(points)): # writing our function E
        x = points.iloc[i].age 
        y = points.iloc[i].FEV
        total_error += (y - (m * x + b)) ** 2 
    total_error / float(len(points))

def gradient_descent(m_now, b_now, points, L):
    