######################################
#
#Shreya Vaidyanathan (sv2525)
#Investigative Techniques Assignment - Data Analysis
#
#####################################
#
#Obtained a data set (from Open Data NYC) of all the certified Minority and/or Women owned business enterprises (M_WBE__LBE__and_EBE_Certified_Business_List) in the city of New York.
#I found that there was huge disparity in the utilization of these contracts and the values of the contracts themselves range from few hundreds to millions of USD.
#
#My goal here is to inspect the value of contracts each business carried out and see the range of values it covers for the available data set. 
#The data set provided the detailed description of each of these businesses - Eg. Name, Contact details, type of service offered, and the contracts they have taken up in the past. 
#It also includes the contract values (in USD) for upto 4 contracts that these business enterprises have worked on and the amount of the job they completed.
#In this script, I am trying to see mean, median, standard deviation of the total contract values for all these businesses and showcase them in a histogram.
#
#As a further extension, I would like to calculate the values for only those businesses operating in a particular domain, burough/zipcode -- to see if there is a pattern within that subset of contracts.
####################################################

import csv
import numpy as np
import matplotlib.pyplot as plt 
import statistics

#Opening my data set
my_data_file = open("EBE_data.csv", "rU")

data_reader = csv.DictReader(my_data_file)

#Creating an array to store the sum of all the values of contracts for every business that is listed
total_contract_value = []

for row in data_reader:
	try:
		#value1 = int(row[data_reader.fieldnames[27]])
		value1 = int(row['Job_Exp1_Value_of_Contract']);
		value2 = int(row['Job_Exp2_Value_of_Contract']);
		value3 = int(row['Job_Exp3_Value_of_Contract']);
		value4 = int(row['Job_Exp4_Value_of_Contract']);
		#print(value1)
		total_contract_value.append(value1+value2+value3+value4)
	except Exception:
		pass

#Total value of the contracts for each business (or row)
print(total_contract_value)

#Calculating the quartiles in the data set
quarts = np.percentile(total_contract_value, [25,50,75])
iqr = quarts[2] + quarts[0]
upper_bound = quarts[2] + (1.5*iqr)
lower_bound = quarts[0] + (1.5*iqr)

#Calculate mean and standard deviation
data_mean = statistics.mean(total_contract_value)
standard_dev = np.std(total_contract_value)

#Print the mean of the value of contracts
print(data_mean);

#Print the standard deviation
print(standard_dev)

#build data points for showing std deviations
mean_measures = []
for i in range(4):
	mean_measures.append(data_mean+(i*standard_dev))
	mean_measures.append(data_mean-(i*standard_dev))


num_bins =10		#To try and seperate the values from getting sorted into only one column of the histogram.

#Create the histogram
histogram = plt.hist(total_contract_value, 1000, normed=False, histtype='bar', color=['red'])

#Plotting quartile lines in green
plt.vlines(quarts, 0, 5000, color=['g','g','g'], linestyle='dashed', linewidth=1)
plt.vlines([upper_bound, lower_bound], 0, 5000, color=['b','b','b'], linestyle='dashed', linewidth=1)

#plot mean lines in yellow
plt.vlines(mean_measures, 0, 5000, color=['y','y','y'], linestyle='dashed', linewidth=1)

#Show the histogram
plt.show()

