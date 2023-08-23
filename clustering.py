import matplotlib.pyplot as plt
import random
import numpy as np
import pandas as pd
f = "DataPoints-Project02.csv"
class MyPoint:
    def __init__(self):
        list1=[]
        num_points1=-1
        ff=open(f,"r")
        for row in ff.readlines():
            list1.append(row.split(","))
            num_points1+=1
        list1.pop(0)
        for item in list1:
            item.pop(0)
        self.num_points=num_points1
        self.x_values=[]
        self.y_values=[]
        for item in list1:
            self.x_values.append(float(item[0]))
            self.y_values.append(float(item[1]))

    def read_mycsv(self):
        f_csv=pd.read_csv(f,sep=",",header=0,index_col=0)
        print(f_csv)

    def get_data(self):
        data=[]
        for i in range(self.num_points):
            data.append([self.x_values[i],self.y_values[i]])
        return data


    def show(self):
        list_of_colors=[]
        for i in range (self.num_points):
            list_of_colors.append((self.x_values[i],self.y_values[i],0.4))
        plt.scatter(self.x_values,self.y_values,c=list_of_colors)
        plt.show()

    def distance(p1, p2):
        d=0
        for i in range(len(p1)):
            d+=(p1[i]-p2[i])**2
        return d**0.5

class Clustering:
    def __init__(self, data, k):
        self.data = data
        self.k = k
        self.centroids = random.sample(self.data, self.k)
        self.clusters = {}
        for i in range(self.k):
            self.clusters[i] = []

    def Lioyd_algorithm(self, max_iterating=100):
        for i in range(max_iterating):
            for clusterID in range(self.k):
                self.clusters[clusterID] = []
            for point in self.data:
                distances = [MyPoint.distance(point, self.centroids[j]) for j in range(self.k)]
                ind = distances.index(min(distances))
                self.clusters[ind].append(point)
            for cluster in self.clusters:
                self.centroids[cluster] = np.average(self.clusters[cluster], axis=0)



a=MyPoint()
a.read_mycsv()
a.show()
mydata=MyPoint.get_data(a)
myclustering=Clustering(mydata,7)
myclustering.Lioyd_algorithm()
for cluster in myclustering.clusters:
    for point in myclustering.clusters[cluster]:
        plt.scatter(point[0],point[1],c=[(point[0],point[1],0.4)],s=10)
        plt.scatter(myclustering.centroids[cluster][0],myclustering.centroids[cluster][1],
                    c=[(myclustering.centroids[cluster][0],myclustering.centroids[cluster][1],0.4)],s=1000)
plt.show()