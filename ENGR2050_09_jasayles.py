# ENGR2050_09_jasayles.py
# Ethan Sayles
# April 6, 2017
import numpy as np
from matplotlib import pyplot as plt
from scipy import stats as st



        
#Class to plot the points and best fit lines of data
class Plot():
    def __init__(self, file):
        self.file = file
    def  read_data(self):           #Function to read the data into two lists
        x = []
        y = []
        f = open(self.file, 'r')
        for line in f:
            pari = line.split(",")
            x.append(float(pari[0]))
            y.append(float(pari[1]))
        f.close()
        self.data = [x, y]
    def show(self):                 #Function to show the data points, and the best fit lines
        self.read_data()
        y = self.data[1]
        x = self.data[0]
        Xs = np.arange(0, max(x), .1)
        
        line_data = st.linregress(x, y)     #Finding the best fit line using scipy
        m1 = line_data[0]
        b1 = line_data[1]
        r_squared = line_data[2] ** 2
        
        
        plt.plot(y, x,  'ro',  label = 'Data Points')                                     #Plotting the data points and the best fit lines
        plt.plot(m1 * Xs + b1 , Xs,label = "R_squared = %f" %(r_squared))
        #plt.plot(m2*Xs+b2, Xs, label = "Numpy linalg best fit line")
        plt.title("Best Fit Line",  fontsize = 20)
        plt.xlabel("x",  fontsize=10)
        plt.ylabel("y",  fontsize=10)
        print ("The coefficient of determination for the blue function is %f" %(r_squared))
        plt.legend()
        plt.show()
        

#Conditional to check for test cases
if __name__ == '__main__':
    f ="ENGR2050_qz2-1_6.dat"
    plot = Plot(f)   
    plot.show()


        
    

    
