
import statsmodels.api as sm
from statsmodels.sandbox.regression.predstd import wls_prediction_std
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import HuberRegressor
from statsmodels.regression.quantile_regression import QuantReg
from statsmodels.tools.tools import add_constant
from IPython.display import display
import pandas as pd
import numpy as np
import ezhc as hc

plt.style.use('ggplot')

def hc_plot(title, series, x_name, y_name):
        g = hc.Highcharts()
        g.xAxis.title.text = x_name
        g.yAxis.title.text = y_name
        g.plotOptions = {
            'line': {
                'marker': {
                    'enabled': False
                }
            }
        }
        g.title = title
        g.series=series

        display(g.plot())

def OLS_stat_m(y, x, intercept=False, fit_test_ratio=0, summary=True, plot=True):
        
    split = int(round(len(x) * fit_test_ratio, 0))
    if split is 0:
        if intercept is True:
            x = sm.add_constant(x)
        model = sm.OLS(y, x)
        fit = model.fit()
        prstd, iv_l, iv_u = wls_prediction_std(fit)
        if summary:
            print(fit.summary())

        if plot:
            plt.figure(figsize=(12, 6))
            fig, ax = plt.subplots(figsize=(12, 6))
            ax.plot(x, y, 'o', label="data", color='black')
            ax.plot(x, fit.fittedvalues, 'r', label="OLS")
            ax.plot(x, iv_u, 'r')
            ax.plot(x, iv_l, 'r')
            ax.legend(loc='best')
        return fit, fit.params, fit.rsquared, prstd, iv_l, iv_u, pd.DataFrame(y - fit.fittedvalues, index=y.index)
    else:
        X_train = x.values[:split - 1]
        Y_train = y.values[:split - 1]
        X_test = x.values[split:]
        Y_test = y.values[split:]
        model = sm.OLS(Y_train, X_train)
        fit = model.fit()
        prstd, iv_l, iv_u = wls_prediction_std(fit)
        Y_pred = fit.predict(X_test)
        if summary:
            print(fit.summary())

        if plot:
            plt.figure(figsize=(12, 6))
            plt.scatter(X_train, Y_train, color='red')
            plt.scatter(X_test, Y_test, color='black')
            plt.plot(X_test, Y_pred, color='blue', linewidth=3)

    return fit, fit.params, fit.rsquared, prstd, iv_l, iv_u, pd.DataFrame(Y_test - Y_pred, index=list(y.index)[split:])


def OLS_scikit(Y, X, intercept=False, fit_test_ratio=0, plot=True):
    """
    Y: pd.Series
    X: pd.DataFrame
    """
    split = int(round(len(X)*fit_test_ratio, 0))
    xName = X.columns[0] if isinstance(X, pd.DataFrame) else X.name 
    yName = Y.columns[0] if isinstance(Y, pd.DataFrame) else Y.name

    if split is 0:
        X_train = X.values.reshape(len(X), 1)
        Y_train = Y.values.reshape(len(Y), 1)
        regr = linear_model.LinearRegression(fit_intercept=intercept)
        regr.fit(X_train, Y_train)
        Y_pred = regr.predict(X_train)
        if plot is True:
            data1 = [[X_train[i][0], Y_train[i][0]] for i in range(len(X_train))]
            data2 = [[X_train[i][0], Y_pred[i][0]] for i in range(len(X_train))]
            series = [
                {
                    'name':'Train',
                    'data':data1,
                    'type':'scatter'
                },
                {
                    'name':'OLS',
                    'data':data2,
                },
            ]
            hc_plot('OLS Scikit', series, xName, yName)
        return regr, regr.coef_,mean_squared_error(Y_train, Y_pred),r2_score(Y_train, Y_pred), pd.DataFrame(Y_train - Y_pred, index = Y.index)
    else:
        X_train=X.values[:split-1]
        Y_train=Y.values[:split-1]
        X_train = X_train.reshape(len(X_train), 1)
        Y_train = Y_train.reshape(len(X_train), 1)
        X_test = X.values[split:]
        Y_test = Y.values[split:]
        X_test = X_test.reshape(len(X_test), 1)
        Y_test = Y_test.reshape(len(Y_test), 1)
        regr = linear_model.LinearRegression(fit_intercept=intercept)
        regr.fit(X_train, Y_train)
        Y_pred = regr.predict(X_test)
        if plot is True:
            data1 = [[X_train[i][0], Y_train[i][0]] for i in range(len(X_train))]
            data2 = [[X_test[i][0], Y_test[i][0]] for i in range(len(X_test))]
            data3 = [[X_test[i][0], Y_pred[i][0]] for i in range(len(X_test))]
            series = [
                {
                    'name':'Train',
                    'data':data1,
                    'type':'scatter'
                },
                {
                    'name':'Test',
                    'data':data2,
                    'type':'scatter'
                },
                {
                    'name':'OLS',
                    'data':data3,
                },
            ]
            hc_plot('OLS Scikit', series, xName, yName)
        return regr, regr.coef_,mean_squared_error(Y_test, Y_pred),r2_score(Y_test, Y_pred), pd.DataFrame(Y_test - Y_pred, index=list(Y.index)[split:])


def RANSAC_scikit(Y, X, intercept=False, fit_test_ratio=0, plot=True):
    
    split = int(round(len(X) * fit_test_ratio, 0))
    xName = X.columns[0] if isinstance(X, pd.DataFrame) else X.name 
    yName = Y.columns[0] if isinstance(Y, pd.DataFrame) else Y.name

    if split is 0:
        X_train = X.values.reshape(len(X), 1)
        Y_train = Y.values.reshape(len(Y), 1)
        regr = linear_model.RANSACRegressor()
        regr.fit(X_train, Y_train)
        Y_pred = regr.predict(X_train)
        if plot is True:
            data1 = [[X_train[i][0], Y_train[i][0]] for i in range(len(X_train))]
            data2 = [[X_train[i][0], Y_pred[i][0]] for i in range(len(X_train))]
            x, y = X_train[regr.inlier_mask_], Y_train[regr.inlier_mask_]
            data3 = [[x[i][0], y[i][0]] for i in range(len(x))]
            series = [
                {
                    'name':'Outlier',
                    'data':data1,
                    'type':'scatter'
                },
                {
                    'name':'Pred',
                    'data':data2,
                },
                {
                    'name':'Train',
                    'data':data3,
                    'type':'scatter'
                },
            ]
            hc_plot('RANSAC Scikit',series, xName, yName)
            
            # plt.scatter(X_train, Y_train, color='yellow')
            # plt.scatter(X_train[regr.inlier_mask_], Y_train[regr.inlier_mask_], color='red')
            # plt.plot(X_train, Y_pred, color='blue', linewidth=3)
        return regr, regr.estimator_.coef_, mean_squared_error(Y_train, Y_pred), r2_score(Y_train,
                                                                                          Y_pred), pd.DataFrame(
            Y_train - Y_pred, index=Y.index), \
               regr.inlier_mask_
    else:
        X_train = X.values[:split - 1]
        Y_train = Y.values[:split - 1]
        X_train = X_train.reshape(len(X_train), 1)
        Y_train = Y_train.reshape(len(X_train), 1)
        X_test = X.values[split:]
        Y_test = Y.values[split:]
        X_test = X_test.reshape(len(X_test), 1)
        Y_test = Y_test.reshape(len(Y_test), 1)
        regr = linear_model.RANSACRegressor()
        regr.fit(X_train, Y_train)
        Y_pred = regr.predict(X_test)
        if plot is True:
            data1 = [[X_train[i][0], Y_train[i][0]] for i in range(len(X_train))]
            x, y = X_train[regr.inlier_mask_], Y_train[regr.inlier_mask_]
            data2 = [[x[i][0], y[i][0]] for i in range(len(x))]
            data3 = [[X_test[i][0], Y_test[i][0]] for i in range(len(X_test))]
            data4 = [[X_test[i][0], Y_pred[i][0]] for i in range(len(X_test))]
            
            series = [
                {
                    'name':'Outlier',
                    'data':data1,
                    'type':'scatter'
                },
                {
                    'name':'Train',
                    'data':data2,
                    'type':'scatter'
                },
                {
                    'name':'Test',
                    'data':data3,
                    'type':'scatter'
                },
                {
                    'name':'RANSAC',
                    'data':data4,
                }
            ]
            hc_plot('RANSAC Scikit',series, xName, yName)

            # plt.scatter(X_train, Y_train, color='yellow')
            # plt.scatter(X_train[regr.inlier_mask_], Y_train[regr.inlier_mask_], color='red')
            # plt.scatter(X_test, Y_test, color='black')
            # plt.plot(X_test, Y_pred, color='blue', linewidth=3)
        return regr, regr.estimator_.coef_, mean_squared_error(Y_test, Y_pred), r2_score(Y_test, Y_pred), pd.DataFrame(
            Y_test - Y_pred, index=list(Y.index)[split:]), \
               regr.inlier_mask_


def Huber_scikit(Y, X, intercept=False, fit_test_ratio=0, plot=True, alpha=0, max_iter=1000, eps=1.3):

    split = int(round(len(X) * fit_test_ratio, 0))
    xName = X.columns[0] if isinstance(X, pd.DataFrame) else X.name 
    yName = Y.columns[0] if isinstance(Y, pd.DataFrame) else Y.name
    if split is 0:
        X_train = X.values.reshape(len(X), 1)
        Y_train = Y.values
        regr = HuberRegressor(fit_intercept=intercept, alpha=alpha, max_iter=max_iter,
                              epsilon=eps)
        regr.fit(X_train, Y_train)
        Y_pred = regr.predict(X_train)
        if plot is True:
            x, y = X_train[regr.outliers_], Y_train[regr.outliers_]
            data1 = [[X_train[i][0], Y_train[i]] for i in range(len(X_train))]
            data2 = [[X_train[i][0], Y_pred[i]] for i in range(len(X_train))]
            data3 = [[x[i][0], y[i]] for i in range(len(x))]
            series = [
                {
                    'name':'Train',
                    'data':data1,
                    'type':'scatter'
                },
                {
                    'name':'Huber',
                    'data':data2,
                },
                {
                    'name':'Outlier',
                    'data':data3,
                    'type':'scatter'
                },
            ]
            hc_plot('Huber Scikit',series, xName, yName)
            
            # plt.scatter(X_train, Y_train, color='red')
            # plt.scatter(X_train[regr.outliers_], Y_train[regr.outliers_], color='yellow')
            # plt.plot(X_train, Y_pred, color='blue', linewidth=3)
        return regr, regr.coef_, mean_squared_error(Y_train, Y_pred), r2_score(Y_train, Y_pred), pd.DataFrame(
            Y_train - Y_pred, index=Y.index), \
               regr.outliers_
    else:
        X_train = X.values[:split - 1]
        Y_train = Y.values[:split - 1]
        X_train = X_train.reshape(len(X_train), 1)
        X_test = X.values[split:]
        Y_test = Y.values[split:]
        X_test = X_test.reshape(len(X_test), 1)
        regr = HuberRegressor(fit_intercept=intercept, alpha=0.0, max_iter=100,
                              epsilon=eps)
        regr.fit(X_train, Y_train)
        Y_pred = regr.predict(X_test)
        if plot is True:
            x, y = X_train[regr.outliers_], Y_train[regr.outliers_]
            data1 = [[X_train[i][0], Y_train[i]] for i in range(len(X_train))]
            data2 = [[x[i][0], y[i]] for i in range(len(x))]
            data3 = [[X_test[i][0], Y_test[i]] for i in range(len(X_test))]
            data4 = [[X_test[i][0], Y_pred[i]] for i in range(len(X_test))]
            
            series = [
                {
                    'name':'Train',
                    'data':data1,
                    'type':'scatter'
                },
                {
                    'name':'Outlier',
                    'data':data2,
                    'type':'scatter'
                },
                {
                    'name':'Test',
                    'data':data3,
                    'type':'scatter'
                },
                {
                    'name':'Huber',
                    'data':data4,
                }
            ]
            hc_plot('Huber Scikit',series, xName, yName)

            # plt.scatter(X_train, Y_train, color='red')
            # plt.scatter(X_train[regr.outliers_], Y_train[regr.outliers_], color='yellow')
            # plt.scatter(X_test, Y_test, color='black')
            # plt.plot(X_test, Y_pred, color='blue', linewidth=3)
        return regr, regr.coef_, mean_squared_error(Y_test, Y_pred), r2_score(Y_test, Y_pred), pd.DataFrame(
            Y_test - Y_pred, index=list(Y.index)[split:]), \
               regr.outliers_

        # http://www.gmelli.org/RKB/sklearn.linear_model.HuberRegressor


def TheilSen_scikit(Y, X, intercept=False, fit_test_ratio=0, plot=True):

    split = int(round(len(X) * fit_test_ratio, 0))
    xName = X.columns[0] if isinstance(X, pd.DataFrame) else X.name 
    yName = Y.columns[0] if isinstance(Y, pd.DataFrame) else Y.name

    if split is 0:
        X_train = X.values.reshape(len(X), 1)
        Y_train = Y.values
        regr = linear_model.TheilSenRegressor(fit_intercept=intercept)
        regr.fit(X_train, Y_train)
        Y_pred = regr.predict(X_train)
        Y_pred = [y[0] for y in Y_pred]
        if plot is True:
            data1 = [[X_train[i][0], Y_train[i]] for i in range(len(X_train))]
            data2 = [[X_train[i][0], Y_pred[i]] for i in range(len(X_train))]
            series = [
                {
                    'name':'Train',
                    'data':data1,
                    'type':'scatter'
                },
                {
                    'name':'TheilSen',
                    'data':data2,
                },
            ]
            hc_plot('Theilsen Scikit', series, xName, yName)

            # plt.scatter(X_train, Y_train, color='red')
            # # plt.scatter(X_train[regr.inlier_mask_], Y_train[regr.inlier_mask_],  color='red')
            # plt.plot(X_train, Y_pred, color='blue', linewidth=3)
        return regr, regr.coef_, mean_squared_error(Y_train, Y_pred), r2_score(Y_train, Y_pred), pd.DataFrame(
            Y_train - Y_pred, index=Y.index), \
               regr.breakdown_
    else:
        X_train = X.values[:split - 1]
        Y_train = Y.values[:split - 1]
        X_train = X_train.reshape(len(X_train), 1)
        X_test = X.values[split:]
        Y_test = Y.values[split:]
        X_test = X_test.reshape(len(X_test), 1)
        regr = linear_model.TheilSenRegressor(fit_intercept=intercept)
        regr.fit(X_train, Y_train)
        Y_pred = regr.predict(X_test)
        Y_pred = [y[0] for y in Y_pred]
        if plot is True:
            data1 = [[X_train[i][0], Y_train[i]] for i in range(len(X_train))]
            data2 = [[X_test[i][0], Y_test[i]] for i in range(len(X_test))]
            data3 = [[X_test[i][0], Y_pred[i]] for i in range(len(X_test))]
            series = [
                {
                    'name':'Train',
                    'data':data1,
                    'type':'scatter'
                },
                {
                    'name':'Test',
                    'data':data2,
                    'type':'scatter'
                },
                {
                    'name':'TheilSen',
                    'data':data3,
                },
            ]
            hc_plot('Theilsen Scikit', series, xName, yName)

            # plt.scatter(X_train, Y_train, color='red')
            # # plt.scatter(X_train[regr.inlier_mask_], Y_train[regr.inlier_mask_],  color='red')
            # plt.scatter(X_test, Y_test, color='black')
            # plt.plot(X_test, Y_pred, color='blue', linewidth=3)
        return regr, regr.coef_, mean_squared_error(Y_test, Y_pred), r2_score(Y_test, Y_pred), pd.DataFrame(
            Y_test - Y_pred, index=list(Y.index)[split:]), \
               regr.breakdown_


def quantile_regression_stat_m(Y, X, intercept=False, quantile=[0.5], fit_test_ratio=0, plot=True, summary=False):

    split = int(round(len(X) * fit_test_ratio, 0))

    if split is 0:
        if intercept is True:
            X_train = add_constant(X, prepend=True, has_constant='skip')
        else:
            X_train = X

        Y_train = Y
        regr = QuantReg(Y_train, X_train)
        R = {}
        Y_pred = {}
        for q in quantile:
            R[q] = regr.fit(q=q, vcov='robust', kernel='epa', bandwidth='hsheather', max_iter=1000, p_tol=1e-06)
            Y_pred[q] = R[q].predict(X_train)
            if summary is True:
                print(R[q].summary())
        if plot is True:
            plt.figure(figsize=(12, 6))
            for q in quantile:
                if q != 0.5:
                    plt.plot(X_train, Y_pred[q], linestyle='dotted', color='blue')
                else:
                    plt.plot(X_train, Y_pred[q], color='blue')

            plt.scatter(X_train, Y_train, color='red')
        return R, Y_pred
    else:
        if intercept is True:
            X = add_constant(X, prepend=True, has_constant='skip')
        X_train = X.values[:split - 1]
        Y_train = Y.values[:split - 1]
        X_test = X.values[split:]
        Y_test = Y.values[split:]
        regr = QuantReg(Y_train, X_train)
        R = {}
        Y_pred = {}
        for q in quantile:
            R[q] = regr.fit(q=q, vcov='robust', kernel='epa', bandwidth='hsheather', max_iter=1000, p_tol=1e-06)
            Y_pred[q] = R[q].predict(X_test)
            if summary is True:
                print(R[q].summary())
        if plot is True:
            plt.figure(figsize=(12, 6))
            for q in quantile:
                if q != 0.5:
                    plt.plot(X_test, Y_pred[q], linestyle='dotted', color='blue')
                else:
                    plt.plot(X_test, Y_pred[q], color='blue')

            plt.scatter(X_train, Y_train, color='red')
            plt.scatter(X_test, Y_test, color='black')
        return R, Y_pred
