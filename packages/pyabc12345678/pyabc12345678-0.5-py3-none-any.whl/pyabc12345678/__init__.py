def index():
    print(""" 
        1aQ1) Design a simple linear neural network model.
              Calculate the output of neural net where input X = 0.2, w = 0.3 and bias b 0.45.
        1aQ2) Calculate the output of neural net for given data.
              Calculate the output of neural net where input X = [x1, x2, x3] = [0.3, 0.5, 0.6]
              & Weight W = [w1, w2, w3] = [0.2, 0.1, -0.3].
        1b) Calculate the output of neural net using both binary and bipolar sigmoidal function.
            
        2a) Generate AND/NOT function using McCulloch- Pitts neural net.
        2b) Generate XOR function using McCulloch-Pitts neural net.
    
        3a) WAP to implement Hebb’s rule. L and U pattern..
        3b) WAP to implement of delta rule.
    
        4a) WAP for Back Propagation Algorithm. 
        4b) WAP for error Backpropagation algorithm.
    
        5a) WAP for Hopfield network.
        5b) WAP for radial basis function.
    
        6a) Kohonen self-organizing map.
        6b) Hopfield network.
    
        7a) Implement membership and identity operators | in, not in.
        7b) Implement membership and identity operators is, is not.
    
        8a) Find ratios using fuzzy logic.
        8b) Solve tipping problem using fuzzy logic.

          """)
          
#index()



def prog(num):
    if(num=="1aQ1"):
        print(""" 

x = float(input("Enter the input: "))
w = float(input("Enter the weight: "))
b = float(input("Enter the bias: "))

Yin = x*w + b
print("Yin: ",Yin)

if Yin < 0:
  out = 0
elif Yin > 1:
  out = 1
else:
  out = Yin

print("Output: ",out)



              """) 
        
    elif(num=="1aQ2"):
        print("""

import numpy as np

n = int(input("Enter the number of elements: "))
x = np.zeros(n)
w = np.zeros(n)

print("Enter the inputs")
for i in range(0,n):
  x[i] = float(input())

print("Enter the weights")
for i in range(0,n):
  w[i] = float(input())

yin_temp = np.zeros(n)
yin_temp = (x*w)

yin = yin_temp.sum()
yin = round(yin,2) 
print("Net Input: ",yin)

if yin < 0:
  out = 0
elif yin > 1:
  out = 1
else:
  out = yin

print("Output: ",out)

                """)
        
    elif(num=="1b"):
        print(""".

import math
import numpy as np

n = int(input("Enter the number of elements: "))
x = np.zeros((n,))
w = np.zeros((n,))

print("Enter the inputs")
for i in range(0,n):
  x[i] = float(input())

print("Enter the weights")
for i in range(0,n):
  w[i] = float(input())

b = float(input("Enter Bias: "))


yin_temp = np.zeros(n)
yin_temp = (x*w)
yin = yin_temp.sum() + b
yin = round(yin,2) 
print("Net Input: ",yin)

binary_sigmoidal = (1/(1+(math.e**(-yin))))
print("Binary Sigmoidal: ",(round(binary_sigmoidal,3)))

bipolar_sigmoidal = (2/(1+(math.e**(-yin)))) - 1
print("Bipolar Sigmoidal: ",(round(bipolar_sigmoidal,3)))

""")
    
    elif(num=="2a"):
        print("""
import numpy as np
print("ANDNOT using MP Neuron")
x1 = np.array([0,0,1,1])
x2 = np.array([0,1,0,1])

print("Considering all weights as Excitatory")
w1 = w2 =1
yin = x1*w1 + x2*w2
print("x1 x2 yin")
for i in range(0,4):
    print(x1[i]," ",x2[i], " ", yin[i])

print("Considering one weight as Excitatory and other as Inhibitory")
w1 = 1
w2 = -1
yin = x1*w1 + x2*w2
print("x1 x2 yin")
for i in range(0,4):
    print(x1[i]," ",x2[i], " ", yin[i])

theta = 1
print("Considering Threshold as 1")
print("Applying Threshold")
y = np.zeros(4).astype(int)
for i in range(0,4):
    if yin[i] >= 1:
        y[i] = 1
    else:
        y[i] = 0


print("x1 x2   y")
for i in range(0,4):
    print(x1[i]," ",x2[i], " ", y[i])


""")

    elif(num=="2b"):
        print("""
#Implementing XOR Uing MP

import numpy as np
x1 = np.array([0,0,1,1])
x2 = np.array([0,1,0,1])

print("Calculating zin1 = x1*w11 + x2*w21")
print("Considering one weight as excitatory and other as inhibitory")
w11 = 1
w21 = -1
zin1 = x1*w11 + x2*w21
print("x1 x2 zin1")
for i in range(0,4):
    print(x1[i]," ",x2[i], " ", zin1[i])

print("Calculating zin2 = x1*w12 + x2*w22")
print("Considering one weight as excitatory and other as inhibitory")
w12 = -1
w22 = 1
zin2 = x1*w12 + x2*w22
print("x1 x2 zin2")
for i in range(0,4):
    print(x1[i]," ",x2[i], " ", zin2[i])

print("Applying Threshold for zin1 and zin2")
z1 = np.zeros(4).astype(int)
z2 = np.zeros(4).astype(int)

for i in range(0,4):
    if zin1[i] >= 1:
        z1[i] = 1
    else:
        z1[i] = 0
        
    if zin2[i] >= 1:
        z2[i] = 1
    else:
        z2[i] = 0

print("x1 x2   z1  z2")
for i in range(0,4):
    print(x1[i]," ",x2[i], " ", z1[i]," ", z2[i])

print("Calculating yin = z1*v1 + z2*v2")
print("Considering both weight as excitatory")
v1 = v2 = 1
yin = z1*v1 + z2*v2

print("x1 x2   yin")
for i in range(0,4):
    print(x1[i]," ",x2[i], " ", yin[i])

print("Applying Threshold for yin")
y = np.zeros(4).astype(int)

for i in range(0,4):
    if yin[i] >= 1:
        y[i] = 1
    else:
        y[i] = 0

print("x1 x2   y")
for i in range(0,4):
    print(x1[i]," ",x2[i], " ", y[i])

""")
        
    elif(num=="3a"):
        print("""

import numpy as np
x1=np.array([1,-1,-1,1,-1,-1,1,1,1])
x2=np.array([1,-1,1,1,-1,1,1,1,1])
b=0
y=np.array([1,-1])

wtold=np.zeros(9)
wtnew=np.zeros(9)
#print("--",wtold)
wtnew=wtnew.astype(int)
wtold=wtold.astype(int)
bais=0

print("First input with target=1")
wtnew = wtold+x1*y[0]
wtold=wtnew
b=b+y[0]
print("new wt=", wtnew)
print("Bias value",b)

print("\nSecond input with target=-1")
wtnew = wtold+x2*y[1]
b=b+y[1]

print("New wt=",wtnew)
print("Bias value",b)

""")
        
    elif(num=="3b"):
        print("""
import numpy as np
import time
np.set_printoptions(precision=2)
x=np.zeros((3,))
weights=np.zeros((3,))
desired=np.zeros((3,))
actual=np.zeros((3,))
for i in range(0,3):
    x[i]=float(input("Intial inputs:"))

for i in range(0,3):
    weights[i]=float(input("Intial weights:"))

for i in range(0,3):
    desired[i]=float(input("Desired output:"))

a=float(input("Enter learning rate:"))

actual=x*weights
print("actual",actual)
print("desired",desired)

while True:
  if np.array_equal(desired,actual):
    break     #no change
  else:
    for i in range(0,3):
        weights[i]=weights[i]+a*(desired[i]-actual[i])

  actual=x*weights
  print("weights",weights)
  print("actual",actual)
  print("desired",desired)

print("*"*30)
print("Final output")
print("Corrected weights",weights)
print("actual",actual)
print("desired",desired)


#Initial input = 1,1,1
#initial weight = 1,1,1
#desired output = 2,3,4
#learning rate = 1

""")
        
    elif(num=="4a"):
        print("""
import numpy as np
X=np.array(([2,9],[1,5],[3,6]),dtype=float)
Y=np.array(([92],[86],[89]),dtype=float)

#scale units
X=X/np.amax(X,axis=0)
Y=Y/100;

class NN(object):
  def __init__(self):
    self.inputsize=2
    self.outputsize=1
    self.hiddensize=3
    self.W1=np.random.randn(self.inputsize,self.hiddensize)
    self.W2=np.random.randn(self.hiddensize,self.outputsize)
    
  def forward(self,X):
    self.z=np.dot(X,self.W1)
    self.z2=self.sigmoidal(self.z)
    self.z3=np.dot(self.z2,self.W2)
    op=self.sigmoidal(self.z3)
    return op;

  def sigmoidal(self,s):
    return 1/(1+np.exp(-s))

obj=NN()
op=obj.forward(X)
print("actual output\n"+str(op))
print("expected output\n"+str(Y))

""")
        
    elif(num=="4b"):
        print("""
import numpy as np
X=np.array(([2,9],[1,5],[3,6]),dtype=float)
Y=np.array(([92],[86],[89]),dtype=float)

X=X/np.amax(X,axis=0)
Y=Y/100;

class NN(object):
  def __init__(self):
    self.inputsize=2
    self.outputsize=1
    self.hiddensize=3
    self.W1=np.random.randn(self.inputsize,self.hiddensize)
    self.W2=np.random.randn(self.hiddensize,self.outputsize)

  def forward(self,X):
    self.z=np.dot(X,self.W1)
    self.z2=self.sigmoidal(self.z)
    self.z3=np.dot(self.z2,self.W2)
    op=self.sigmoidal(self.z3)
    return op;

  def sigmoidal(self,s):
    return 1/(1+np.exp(-s))

  def sigmoidalprime(self,s):
    return s* (1-s)

  def backward(self,X,Y,o):
    self.o_error=Y-o
    self.o_delta=self.o_error * self.sigmoidalprime(o)
    self.z2_error=self.o_delta.dot(self.W2.T)
    self.z2_delta=self.z2_error * self.sigmoidalprime(self.z2)
    self.W1 = self.W1 + X.T.dot(self.z2_delta)
    self.W2= self.W2+ self.z2.T.dot(self.o_delta)

  def train(self,X,Y):
    o=self.forward(X)
    self.backward(X,Y,o)

obj=NN()
for i in range(2000):
  obj.train(X,Y)

print("input\n"+str(X))
print("\n\nActual output\n"+str(Y))
print("\n\nPredicted output\n"+str(obj.forward(X)))
print("\n\nloss"+str(np.mean(np.square(Y-obj.forward(X)))))

""")
        
    elif(num=="5a"):
        print(""" """)
        
    elif(num=="5b"):
        print(""" """)
        
    elif(num=="6a"):
        print(""" """)
        
    elif(num=="6b"):
        print(""" """)
        
    elif(num=="7a"):
        print(""" """)
        
    elif(num=="7b"):
        print(""" """)
        
    elif(num=="8a"):
        print(""" """)
        
    elif(num=="8b"):
        print(""" """)
    
    


#a = input("Enter Prog num")
#prog(a)





    
    


















