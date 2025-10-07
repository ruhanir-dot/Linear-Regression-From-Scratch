import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv("C:\\Users\\Ruhani R\\Downloads\\Lungs.csv")

# utilizing y = mx + b notation
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
    m_gradient = 0 # starting our gradient for slope and intercept
    b_gradient = 0
    
    n = len(points)

    for i in range(n): 
        x = points.iloc[i].age 
        y = points.iloc[i].FEV

        m_gradient += -(2/n) * x * (y - (m_now * x + b_now))
        b_gradient += -(2/n) * (y - (m_now * x + b_now))
    
    m = m_now - m_gradient * L 
    b = b_now - b_gradient * L 
    
    return m,b

m = 0 
b = 0 
L = 0.0001
epochs = 100 

for i in range(epochs): 
    m,b = gradient_descent(m,b,data,L)

print(m,b)

plt.scatter(data.age, data.FEV, color = "black")
plt.plot(list(range(4,19)), [m * x + b for x in range(4,19)], color = "red")

