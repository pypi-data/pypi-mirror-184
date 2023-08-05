# Copyright (C) 2021- 2022 Cosmo Tech
# This document and all information contained herein is the exclusive property -
# including all intellectual property rights pertaining thereto - of Cosmo Tech.
# Any use, reproduction, translation, broadcasting, transmission, distribution,
# etc., to any person is prohibited unless it has been previously and
# specifically authorized by written means by Cosmo Tech.

import pandas
import scipy.stats
import inspect


def count(df):
    return {"count": df.count()}


def min(df):
    return {"min": df.min()}


def max(df):
    return {"max": df.max()}


def minmax(df):
    return {**min(df), **max(df)}


def mean(df):
    return {"mean": df.mean()}


def std(df):
    return {"std": df.std(ddof=1)}


def median(df):
    return {"median": df.median()}


def sem(df):
    return {"sem": df.sem(ddof=1)}


def confidence_intervals_of_the_mean(df, loc=None, scale=None):
    if loc is None:
        loc = mean(df)["mean"]
    if scale is None:
        scale = sem(df)["sem"]
    dfcount = count(df)['count']
    result = {}
    confidence_levels = [0.68, 0.95, 0.99]
    for confidence_level in confidence_levels:
        key = (
            "confidence interval of the mean at "
            + str(int(confidence_level * 100))
            + "%"
        )
        series = {}
        for column in df:
            # This construction deals with the new parameter name in scipy.stats.t.interval()
            # previously 'alpha', now 'confidence' (changed in scipy 1.9.0, July 2022)
            confkey = (
                'alpha'
                if 'alpha' in inspect.signature(scipy.stats.t.interval).parameters
                else 'confidence'
            )
            params = {
                confkey: confidence_level,
                'df': dfcount[column] - 1,
                'loc': loc[column],
                'scale': scale[column],
            }
            series[column] = scipy.stats.t.interval(**params)
        result[key] = pandas.Series(series)
    return result


def standard(df):
    mean_ = mean(df)
    sem_ = sem(df)
    count_ = count(df)
    intervals = {}
    for column in df:
        # This construction deals with the new parameter name in scipy.stats.t.interval()
        # previously 'alpha', now 'confidence' (changed in scipy 1.9.0, July 2022)
        confkey = (
            'alpha'
            if 'alpha' in inspect.signature(scipy.stats.t.interval).parameters
            else 'confidence'
        )
        params = {
            confkey: 0.95,
            'df': count_['count'][column] - 1,
            'loc': mean_["mean"][column],
            'scale': sem_["sem"][column],
        }
        intervals[column] = scipy.stats.t.interval(**params)
    return {
        **mean_,
        **std(df),
        **sem_,
        "confidence interval of the mean at 95%": pandas.Series(intervals),
    }


def skewness(df):
    return {"skewness": df.skew()}


def kurtosis(df):
    return {"kurtosis": df.kurtosis()}


def high_order(df):
    return {**skewness(df), **kurtosis(df)}


def mode(df):
    return {"mode": df.mode()}


def harmonic_mean(df):
    res = {}
    for column in df:
        res[column] = scipy.stats.hmean(df[column])
    return {"harmonic_mean": pandas.Series(res)}


def geometric_mean(df):
    res = {}
    for column in df:
        res[column] = scipy.stats.gmean(df[column])
    return {"geometric_mean": pandas.Series(res)}


def central(df):
    return {**mean(df), **geometric_mean(df), **harmonic_mean(df)}


def covariance(df):
    return {"covariance": df.cov()}


def correlation(df):
    return {"correlation": df.corr()}


def quantiles(df):
    q = [
        0.05,
        0.1,
        0.15,
        0.2,
        0.25,
        0.30,
        0.35,
        0.4,
        0.45,
        0.5,
        0.55,
        0.6,
        0.65,
        0.7,
        0.75,
        0.8,
        0.85,
        0.9,
        0.95,
    ]
    result = {}
    for percentage in q:
        key = "quantile " + str(int(percentage * 100)) + "%"
        result[key] = df.quantile(q=percentage)
    return result


def box_plot(df):
    q1 = df.quantile(q=0.25)
    q3 = df.quantile(q=0.75)
    return {**mean(df), **median(df), "Q1": q1, "Q3": q3, **min(df), **max(df)}
