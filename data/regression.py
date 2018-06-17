import numpy as np
from data_holder import DataHolder

holder = DataHolder(11, 350)
holder.load_data('data.txt')
np_x = np.array(holder.x)
np_y = np.array(holder.y)

X = np_x  # transpose so input vectors are along the rows
X = np.c_[X, np.ones(X.shape[0])]  # add bias term
beta_hat = np.linalg.lstsq(X, np_y)[0]
y_hat = np.dot(X, beta_hat)
sqerr = (np_y - y_hat) ** 2
print(sqerr.sum() / 350)
