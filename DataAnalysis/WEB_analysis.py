import csv
import numpy as numpy
import matplotlib.pyplot as plt
import statistics

#Loading emerging business enterprises datafile
EBE_file = open("EBE_list.csv", "rU")

#Converting to a DictReader
data_Reader = csv.DictReader(EBE_file)

total_contract_value = []

for row in data_Reader:
    try:
        total_contract_value.append(int(row[data_Reader.fieldnames[28]])+int(row[data_Reader.fieldnames[32]]))
    except Exception:
        pass

print total_contract_value

my_hist = plt.hist(total_contract_value, histtype='bar', color=['red'])

#Show the histogram
plt.show()
