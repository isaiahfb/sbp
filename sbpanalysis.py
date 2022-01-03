import matplotlib
import csv
import matplotlib.pyplot as plt
import numpy as np
import datetime


#row 1427 end of Apr 18
#row 757 beginning of Apr 12
#row 88 beginning of Apr 5
 
file_CSV = open('sbpdata.csv')
data_CSV = csv.reader(file_CSV)
list_CSV = list(data_CSV)
list_CSV_t = np.transpose(list_CSV)


def countgraph(col, max):
    plt.plot([datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f') for date in list_CSV_t[0][87:756]], [int(x) for x in list_CSV_t[col][87:756]], color ='b')
    plt.ylim(0, max)
    dates = []
    for x in range(87, 756, 24):
        dates.append(datetime.datetime.strptime(list_CSV_t[0][x], '%Y-%m-%d %H:%M:%S.%f'))
    for date in dates:
        plt.axvline(x=date, color = 'k')
    plt.show()

def percentall(start, end):
    plt.plot([datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f') for date in list_CSV_t[0][start:end]], [float(x)/280 for x in list_CSV_t[2][start:end]], color ='r')
    plt.plot([datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f') for date in list_CSV_t[0][start:end]], [float(x)/56 for x in list_CSV_t[5][start:end]], color ='g')
    plt.plot([datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f') for date in list_CSV_t[0][start:end]], [float(x)/144 for x in list_CSV_t[8][start:end]], color ='b')
    plt.ylim(0, 1)
    dates = []
    for x in range(start, end, 24):
        dates.append(datetime.datetime.strptime(list_CSV_t[0][x], '%Y-%m-%d %H:%M:%S.%f'))
    for date in dates:
        plt.axvline(x=date, color = 'k')
    plt.show()

def onedaycomp(start):
    end = start+96
    plt.plot([datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f') for date in list_CSV_t[0][start:end]], [float(x) for x in list_CSV_t[2][start:end]], color ='r')
    plt.plot([datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f') for date in list_CSV_t[0][start:end]], [float(x) for x in list_CSV_t[5][start:end]], color ='g')
    plt.plot([datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f') for date in list_CSV_t[0][start:end]], [float(x) for x in list_CSV_t[8][start:end]], color ='b')
    plt.plot([datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f') for date in list_CSV_t[0][start:end]], [float(x) for x in list_CSV_t[2][start+669:end+669]], color ='r')
    plt.plot([datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f') for date in list_CSV_t[0][start:end]], [float(x) for x in list_CSV_t[5][start+669:end+669]], color ='g')
    plt.plot([datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f') for date in list_CSV_t[0][start:end]], [float(x) for x in list_CSV_t[8][start+669:end+669]], color ='b')
    #plt.ylim(0, 280)
    dates = []
    for x in range(start, end, 4):
        dates.append(datetime.datetime.strptime(list_CSV_t[0][x], '%Y-%m-%d %H:%M:%S.%f'))
    for date in dates:
        plt.axvline(x=date, color = 'k')
    plt.show()

#onedaycomp(87)
#onedaycomp(183)
#onedaycomp(278)
#onedaycomp(373)
#onedaycomp(469)
#onedaycomp(565)
#onedaycomp(661)
#percentall(756, 1426)
#countgraph(2, 280)
#countgraph(5, 56)
#countgraph(8, 144)

