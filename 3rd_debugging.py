
import csv
import numpy as np
import matplotlib.pyplot as plt


""" Original (Incorrect) Code

def plot_data(csv_file_path: str):
    # load data
    results = []
    with open(csv_file_path) as result_csv:
        csv_reader = csv.reader(result_csv, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            results.append(row)
        results = np.stack(results)

    # plot precision-recall curve
    plt.plot(results[:, 1], results[:, 0])
    plt.ylim([-0.05, 1.05])
    plt.xlim([-0.05, 1.05])
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.show()
"""



""" 
Mistake : 
CSV rows were appended as strings 
(["0.376","0.851"]). np.stack kept non-numeric data,
 so plotting used text instead of numbers.

 Precision and recall are plotted in the wrong order

Fix: Convert each value to float when appending 
([float(row[0]), float(row[1])]) and use np.array(results) 
so results is a numeric array. The rest of the code 
(variable names, plotting lines) is unchanged.

"""


#ُSolution :

def plot_data(csv_file_path: str):
    # load data
    results = []
    with open(csv_file_path) as result_csv:
        csv_reader = csv.reader(result_csv, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            if len(row) < 2:       # skip empty or invalid rows - IndexError.
                continue
            # convert strings to floats, keep same variable 'row' and 'results'
            results.append([float(row[0]), float(row[1])])
        results = np.array(results)  # numeric 2D array

    plt.plot(results[:, 0], results[:, 1])  #Precision and recall were plotted in the wrong order
    plt.ylim([-0.05, 1.05])
    plt.xlim([-0.05, 1.05])
    plt.xlabel('Precision')
    plt.ylabel('Recall')
    plt.show()




    # --- Test ---

f = open("data_file.csv", "w")
w = csv.writer(f)
_ = w.writerow(["precision", "recall"])
w.writerows([[0.013,0.951],
             [0.376,0.851],
             [0.441,0.839],
             [0.570,0.758],
             [0.635,0.674],
             [0.721,0.604],
             [0.837,0.531],
             [0.860,0.453],
             [0.962,0.348],
             [0.982,0.273],
             [1.0,0.0]])
f.close()
plot_data("data_file.csv")
plt.show() 