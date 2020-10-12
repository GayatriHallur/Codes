#Importing libraries
import numpy as np


def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()

def tanh_derivative(z):
    return 1 - np.power(np.tanh(z), 2)

def forward_prop(model,a0):  
    W1, b1, W2, b2, W3, b3 = model['W1'], model['b1'], model['W2'], model['b2'], model['W3'],model['b3'] 
    z1 = a0.dot(W1) + b1  
    a1 = np.tanh(z1)
    z2 = a1.dot(W2) + b2
    a2 = np.tanh(z2)
    z3 = a2.dot(W3) + b3
    a3 = softmax(z3)
    cache = {'a0':a0,'z1':z1,'a1':a1,'z2':z2,'a2':a2,'a3':a3,'z3':z3}    
    return cache

def backword_prop(model,cache,y):
    W1, b1, W2, b2, W3, b3 = model['W1'], model['b1'], model['W2'], model['b2'],model['W3'],model['b3'] 
    a0,a1, a2,a3 = cache['a0'],cache['a1'],cache['a2'],cache['a3'] 
    m = y.shape[0] 
    dz3 = a3-y
    dW3 = 1/m*(a2.T).dot(dz3) 
    dz2 = np.multiply(dz3.dot(W3.T) ,tanh_derivative(a2))  
    dW2 = 1/m*(a1.T).dot(dz2)
    db3 = 1/m*np.sum(dz3, axis=0)
    dW2 = 1/m*np.dot(a1.T, dz2)
    db2 = 1/m*np.sum(dz2, axis=0) 
    dz1 = np.multiply(dz2.dot(W2.T),tanh_derivative(a1))
    dW1 = 1/m*np.dot(a0.T,dz1)        
    db1 = 1/m*np.sum(dz1,axis=0) 
    grads = {'dW3':dW3, 'db3':db3, 'dW2':dW2,'db2':db2,'dW1':dW1,'db1':db1}
    return grads

def input_parameters():
    W1 = np.random.rand(3,3)
    W2 = np.random.rand(3,3)
    W3 = np.random.rand(3,3)
    b1 = np.random.rand(1,3)
    b2 = np.random.rand(1,3)
    b3 = np.random.rand(1,3)
    y = np.random.rand(3,3)
    a0 = np.random.rand(3,3)
    model = {'W1':W1,'W2':W2,'W3':W3,'b1':b1,'b2':b2,'b3':b3}
    return model


if __name__=="__main__":
    model = input_parameters()
    a0 = np.random.rand(3,3)
    y = np.random.rand(3,3)
    cache = forward_prop(model,a0)
    grades = backword_prop(model,cache,y)

