# -*- coding: utf-8 -*-
from sklearn.metrics import f1_score
y_true = [0, 1, 2, 0, 1, 2]
y_pred = [0, 2, 1, 0, 0, 1]
print('True   :', y_true)
print('Predict:',y_pred)

print('F1 (Macro Averaging)',f1_score(y_true, y_pred, average='macro'))  

print('F1 (Micro Averaging)',f1_score(y_true, y_pred, average='micro')) 

print('F1 (Weighted averaging)',f1_score(y_true, y_pred, average='weighted'))  

print('F1 (No averaging)',f1_score(y_true, y_pred, average=None))