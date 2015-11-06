#! /usr/bin/python

from pylab import *

def autosubplot(data_dict):
    
    subplot_num = len(data_dict)
    if subplot_num == 1:
        fig, axs = subplots()
    elif subplot_num >= 2:
        fig, axs = subplots(1, subplot_num)
    
    #if subplot_num%2==0: #if number of subplots is even, 
    for idx, key in enumerate(data_dict):
        print idx
        print key
        if subplot_num == 1:
            axs.plot(data_dict[key]['x'], data_dict[key]['y'])
        else:
            axs[idx].plot(data_dict[key]['x'], data_dict[key]['y'])


if __name__=='__main__':
    x = arange(0,20,0.1)
    y = x**2
    z = cos(pi*x)
    j = 2*x + 3
    data_dict1 = {'data1':{'x':x,'y':y}}
    data_dict2 = {'data1':{'x':x,'y':y},'data2':{'x':x,'y':z}}
    data_dict3 = {'data1':{'x':x,'y':y},'data2':{'x':x,'y':z},'data3':{'x':x,'y':j}}
    autosubplot(data_dict1)
    autosubplot(data_dict2)
    autosubplot(data_dict3)
    show()
