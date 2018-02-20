import csv
import numpy as np
import matplotlib.pyplot as plt 
import statistics

my_data_file = open("EBE_data.csv", "rU")

data_reader = csv.DictReader(my_data_file)

total_contract_value = []

for row in data_reader:
	try:
		#value1 = int(row[data_reader.fieldnames[27]])
		value1 = int(row['Job_Exp1_Value_of_Contract'])/10000000;
		value2 = int(row['Job_Exp2_Value_of_Contract'])/10000000;
		value3 = int(row['Job_Exp3_Value_of_Contract'])/10000000;
		value4 = int(row['Job_Exp4_Value_of_Contract'])/10000000;
		#print(value1)
		total_contract_value.append(value1+value2+value3+value4)
	except Exception:
		pass

#print(total_contract_value)

#Calculating the quartiles
quarts = np.percentile(total_contract_value, [25,50,75])
iqr = quarts[2] + quarts[0]
upper_bound = quarts[2] + (1.5*iqr)
lower_bound = quarts[0] + (1.5*iqr)

#Calculate mean and standard deviation
data_mean = statistics.mean(total_contract_value)
std_dev = np.std(total_contract_value)

#build data points for showing std deviations
mean_measures = []

for i in range(4):
	mean_measures.append(data_mean+(i*std_dev))
	mean_measures.append(data_mean-(i*std_dev))


num_bins =10
#Create histogram
histogram = plt.hist(total_contract_value, 1000, normed=False, histtype='bar', color=['red'])


#Plotting quartile lines in green
plt.vlines(quarts, 0, 5000, color=['g','g','g'], linestyle='dashed', linewidth=1)
plt.vlines([upper_bound, lower_bound], 0, 5000, color=['b','b','b'], linestyle='dashed', linewidth=1)

#plot mean lines in yellow
plt.vlines(mean_measures, 0, 5000, color=['y','y','y'], linestyle='dashed', linewidth=1)


#Show the histogram
plt.show()