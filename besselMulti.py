from math import sin,cos
import numpy as np
import matplotlib.pyplot as plt

def up(x,l):
    j0=sin(x)/x
    if l==0: return j0
    j1=(j0-cos(x))/x
    if l==1: return j1
    # else use recusion relation
    l=l-1
    return (2*l+1)/x * up(x,l) - up(x,l-1)

def down(x,n):
    lMax=50
    j=[0]*(lMax+2)     # maximum order for downward calculation
    j[lMax+1] = j[lMax] = 1.    # start with "something"
    for k in range(lMax,0,-1):
        j[k-1] = ((2.*k + 1.)/x)*j[k] - j[k+1]   # recur. rel
    scale = ((sin(x))/x)/j[0];		         #   scale the result  
    return(j[n]*scale)

if __name__ == "__main__":

    xmax=40.0
    xmin=0.1
    step=0.1
    xvalues=np.arange(xmin,xmax+step,step)
    


    fig, ax = plt.subplots(4, 1, figsize=(10,10) )
    fig.suptitle('J_n(x) with Up/Down Calculations')
    for ji, j in enumerate([0, 3, 5, 8]):
        jval_up=np.array( [up(x, j) for x in xvalues], dtype=np.float64)
        jval_down=np.array([down(x, j) for x in xvalues], dtype=np.float64)
        #print(xvalues)
        
        #Label the axes for both plots and assign data
        ax[ji].plot(xvalues, jval_up, c='g', ls='--', label='Up' )
        ax[ji].plot(xvalues, jval_down, c='r', ls='dashdot', label='Down' )


        ax[ji].set(xlabel="x", ylabel=f"J_{j}(x)")
        ax[ji].legend()
        

    #Create and save the plots
    plt.tight_layout()

    plt.savefig("./bessel.png")

    plt.show()