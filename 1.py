import numpy as np
import scipy
import scipy.special
import matplotlib.pyplot as plt
import matplotlib.ticker as mt

#generating 150 random points from {0,1}
#let 0 be heads & 1 be tails

n = np.random.randint(2,size=150)

#Beta function
def beta(a,b,mu):
    x = scipy.special.gamma(a+b)
    y = scipy.special.gamma(a)
    z = scipy.special.gamma(b)
    prior = (x/(y*z))*(mu**(a-1))*((1-mu)**(b-1))
    return prior
    
#plot function
def plot_graph(a,b,name):
    x=[]
    y=[]
    i=0.00001;
    while i<=1:
        x.append(i)
        y.append(beta(a,b,i))
        i += 0.01
    #plt.autoscale()
    plt.xlabel("μ")
    ax = plt.gca()
    ax.set_ylim(0,10)
    
    plt.plot(x,y)
    plt.savefig("figure"+str(name)+".png")
    plt.close(1)

a=4
b=6
name=1

#setting a=a+1 for 0 and b=b+1 for 1
for l in n:
    if l==0 :
        a=a+1
    else:
        b=b+1

    plot_graph(a,b,name)
    name=name+1

#Part B
na = "PartB"
plot_graph(a,b,na)
