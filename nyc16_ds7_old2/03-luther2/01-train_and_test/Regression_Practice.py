#@@@@@@@@@@@@@@@@@@@@
#Regression Practice:
#Jeremy Kedziora
#4/15/2016
#@@@@@@@@@@@@@@@@@@@@



import pandas as pd    #import pandas to read in out write out data
import statsmodels.api as sm    #import statsmodels for the stats models
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats    #import for stats functions


#fake data to play around with
#x_1 = np.random.normal(0,1,2000)
#x_2 = np.random.uniform(0,1,2000)
#x_3 = np.random.uniform(-1,3,2000)
#x_4 = np.random.normal(0,1,2000)
#x_5 = np.random.normal(0,3,2000)
#x_6 = np.random.uniform(0,1,2000)

#b_0 = 1.02    #constant
#b_1 = 0.56    #x1 effect
#b_2 = -0.9    #x2 effect
#b_3 = -1.1    #x3 effect
#b_4 = 0.29    #x4 effect
#b_5 = 0    #x5 effect
#b_6 = 0    #x6 effect
#b_7 = -1.5    #x_4^2 effect
#b_8 = 1.2    #x_4^3 effect

#y = b_0 + b_1*x_1 + b_2*x_2 + b_3*x_3 + b_4*x_4 + b_5*x_5 + b_6*x_6 + b_7*(x_4**2.0) + b_8*(x_4**3.0) + np.random.normal(0,1,2000)    #generate the dependent variable
#pd.DataFrame(np.array([x_1,x_2,x_3,x_4,x_5,x_6,y]).T).to_csv('/Users/seniordatascientist/Desktop/Metis Codes/Data/Practice_data.csv')    #write out



Data = pd.read_csv('/Users/seniordatascientist/Desktop/Metis Codes/Data/Practice_data.csv')    #read in data
y = Data['Dep_Variable']    #extract dependent variable
X = Data.drop('Dep_Variable',1)    #remove it from the data and keep everything else
X['Ind_Variable_4**2'] = X['Ind_Variable_4']**2.0    #include a squared term on x_4
X['Ind_Variable_4**3'] = X['Ind_Variable_4']**3.0    #include a cubed term on x_4
X['Intercept'] = [1.0]*X.shape[0]    #include the intercept




#plot the relationships
#The density of y
ys = np.linspace(min(y),max(y),200)    #set the x range

#compute the density for the first data
density_y = scipy.stats.gaussian_kde(y)    #use the scipy density calculator
density_y.covariance_factor = lambda : .25    #set the covariance factor so that plots analogous to R's are plotted
density_y._compute_covariance()    #recompute using the new covariance factor

plt.figure(figsize = (20,8))    #initiate the plot
plt.plot(ys,density_y(ys),'b--',lw=4)    #generate the plot
plt.fill(ys,density_y(ys),'b',alpha=0.3)    #fill in the curves
plt.xlabel('y',fontsize=30)    #add an x label
plt.ylabel('density of y',fontsize=30)    #add a y label
plt.text(np.mean(y),max(density_y(ys))/2.0,r'$\widehat{y}$',fontsize=30)    #add LaTeX text for location of the mean
#plt.title('A Simple Density',fontsize=40)    #add a title to the plot
plt.grid(True)
plt.savefig('/Users/seniordatascientist/Desktop/Metis Codes/Density_of_y.pdf')    #save the plot to file
plt.show()    #and then show the plot



#The variables vs y
plt.figure(figsize = (20,10))    #initiate the plot

plt.subplot(2,3,1)    #plot subplot 1,1 in the 3x3 area
plt.plot(X['Ind_Variable_1'],y,'bs',lw=4)    #generate the plot
plt.xlabel(r'$x_1$',fontsize=10)    #add an x label
plt.ylabel(r'$y$',fontsize=10)    #add a y label

plt.subplot(2,3,2)    #plot subplot 1,2 in the 3x3 area
plt.plot(X['Ind_Variable_2'],y,'bs',lw=4)    #generate the plot
plt.xlabel(r'$x_2$',fontsize=10)    #add an x label
plt.ylabel(r'$y$',fontsize=10)    #add a y label

plt.subplot(2,3,3)    #plot subplot 1,3 in the 3x3 area
plt.plot(X['Ind_Variable_3'],y,'bs',lw=4)    #generate the plot
plt.xlabel(r'$x_3$',fontsize=10)    #add an x label
plt.ylabel(r'$y$',fontsize=10)    #add a y label

plt.subplot(2,3,4)    #plot subplot 2,1 in the 3x3 area
plt.plot(X['Ind_Variable_4'],y,'bs',lw=4)    #generate the plot
plt.xlabel(r'$x_4$',fontsize=10)    #add an x label
plt.ylabel(r'$y$',fontsize=10)    #add a y label

plt.subplot(2,3,5)    #plot subplot 2,2 in the 3x3 area
plt.plot(X['Ind_Variable_5'],y,'bs',lw=4)    #generate the plot
plt.xlabel(r'$x_5$',fontsize=10)    #add an x label
plt.ylabel(r'$y$',fontsize=10)    #add a y label

plt.subplot(2,3,6)    #plot subplot 2,3 in the 3x3 area
plt.plot(X['Ind_Variable_6'],y,'bs',lw=4)    #generate the plot
plt.xlabel(r'$x_6$',fontsize=10)    #add an x label
plt.ylabel(r'$y$',fontsize=10)    #add a y label

plt.savefig('/Users/seniordatascientist/Desktop/Metis Codes/Variable_relationships.pdf')    #save the plot to file




#split into training and test sets:
mask = np.random.rand(X.shape[0]) < 0.75    #choose 3/4 of the data for training and the rest for test
X_train = X[mask]    #take the training independent variable data
X_test = X[~mask]    #and the test independent variable data
y_train = y[mask]    #take the training dependent variable data
y_test = y[~mask]    #and the training dependent variable data

#train the model
model = sm.OLS(y_train, X_train)    #define the statsmodels model object
results = model.fit()    #fit the model
results.summary()    #summarize

#consider in the test set
r2_adj = 1 - ((sum((y_test-results.predict(X_test))**2.0)/(len(X_test) - len(results.params) - 1))
                /(sum((y_test - np.mean(y_test))**2.0)/(len(X_test) - 1)))    #compute the adjusted r2 in the test set

