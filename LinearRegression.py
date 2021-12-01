import numpy as np
import matplotlib.pyplot as plt


# origin: https://blog.csdn.net/arli_xu/article/details/100145495
# used for creating linear equation for x-y point dataset


def compute_cost(a,b,points):
    # can be used for analysis
    total_cost=0
    M =len(points)
    for i in range(M):
        x=points[i,0]
        y=points[i,1]
        total_cost += (y-a*x-b)**2
    return total_cost/M 


def average(data):
     sum=0
     num=len(data)
     for i in range(num):
         sum += data[i]
     return sum/num


def fit(points):
    M = len(points)
    x_bar=np.mean(points[:,0])
    sum_yx= 0
    sum_x2=0
    sum_delta =0
    for i in range(M):
        x=points[i,0]
        y=points[i,1]
        sum_yx += y*(x-x_bar)
        sum_x2 += x**2
    
    w = sum_yx/(sum_x2-M*(x_bar**2))
    
    for i in range(M):
        x=points[i,0]
        y=points[i,1] 
        sum_delta += (y-w*x)
    b = sum_delta / M
    return w,b


def main():
    points = np.genfromtxt("data.csv",delimiter=",")
    x=points[:,0]
    y=points[:,1]

    a,b =fit(points)
    print ("a is :",a)
    print ("b is :",b)
    cost = compute_cost(a,b,points)
    print("cost is :" ,cost)
    pred_y= a*x+b

    plt.scatter(x,y,marker='.')
    plt.plot(x,pred_y,c='r')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


if __name__ == "__main__":
    main()