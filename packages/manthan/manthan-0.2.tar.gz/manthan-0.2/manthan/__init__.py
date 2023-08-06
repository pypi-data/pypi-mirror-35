import numpy as np

def mean_absolute_percentage_error(y_true, y_pred): 
#    y_true[y_true==0] = np.nextafter(0,1) # Set to lowest presicion value
    y_true[y_true==0] = y_true[y_true>0].min() # Set to min value to avoid divide overflow
    y_true, y_pred = np.array(y_true), np.array(y_pred[y_pred != 0])
    return np.mean(np.abs((y_true - y_pred) / y_true))

def weighted_absolute_percentage_error(y_true, y_pred): 
    return np.abs(y_true - y_pred).sum()/y_true.sum()