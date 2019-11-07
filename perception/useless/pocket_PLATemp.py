#coding=utf-8
# calculate error count
import numpy as np
def calError(self, X, Y, W):
    score = np.dot(X, W)
    Y_pred = np.ones_like(Y)
    Y_pred[score < 0] = -1
    err_cnt = np.sum(Y_pred != Y)
    return err_cnt

def pocket_pla_1(self, X_train, Y_train, X_test, Y_test):
    Iteration = 2000  # number of iteration
    Update = 50
    Errors = []  # list store error rate every iteration

    for iter in range(Iteration):
        np.random.seed(iter)  # set random seed, different by iteration
        permutation = np.random.permutation(X_train.shape[0])  # random select index
        X_train = X_train[permutation]  # random order X_train
        Y_train = Y_train[permutation]  # random order Y_train, as the same as X_train

        # look through the 50 iterations
        W = np.zeros(X_train.shape[1])  # weights initialization
        min_err = self.calError(X_train, Y_train, W)  # set initial W can make minimal error
        for i in range(Update):
            score = np.dot(X_train[i, :], W)  # score
            if score * Y_train[i] <= 0:  # classification error
                tmp = W + np.dot(X_train[i, :].T, Y_train[i])  # new tmp, wait to decide replace W
                tmp_err = self.calError(X_train, Y_train, tmp)  # calculate new error
                if tmp_err < min_err:
                    W = tmp  # update W
                    min_err = tmp_err  # update min_err

        # get W to test data
        Y_pred_test = np.dot(X_test, W)  # calculate score
        Y_pred_test[Y_pred_test > 0] = 1  # positive
        Y_pred_test[Y_pred_test < 0] = -1  # negative
        error = np.mean(Y_pred_test != Y_test)
        Errors.append(error)  # store error to list

    # mean of errors
    error_mean = np.mean(Errors)

    return error_mean