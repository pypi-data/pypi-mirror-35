#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2018 The MUSSLES developers
#
# This file is part of MUSSLES.
#
# MUSSLES is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# MUSSLES is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with MUSSLES.  If not, see <http://www.gnu.org/licenses/>.

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

from .utils import log


# Some settings
plt.style.use("fivethirtyeight")
COLORS = ["skyblue", "steelblue", "gray"]
ALPHAS = [1.0, 1.0, 0.45]


# Everything else!
def update_mean(m, X):
    N = len(X[0])
    n = []
    for i in range(len(m)):
        n.append([(m[i][0]*(N-1) + X[i][-1])/N])
    return np.array(n)

def update_cov(X, m, Ct, Sd, Id, eps):
    m1 = update_mean(m, X)
    t = len(X[0])-1
    part1 = ((t-1)/t)*Ct
    part2 = t*np.matmul(m, np.transpose(m))
    part3 = (t+1)*np.matmul(m1, np.transpose(m1))
    Xt = []
    Xt.append(X[:,-1])
    part4 = np.matmul(np.transpose(Xt), Xt)
    part5 = eps*Id
    cov = part1 + (Sd/t)*(part2 - part3 + part4 + part5)
    return (cov + np.transpose(cov))/2, m1

def random_move(current_state, X, Ct, t, t0, stepsize, data_meas, logpost, m, S_d, I_d):
    if (t <= t0):
        next_move = stats.multivariate_normal.rvs(current_state, stepsize)
        return next_move, logpost(next_move, data_meas), m, stepsize
    elif (t == t0 + 1):
        n = []
        for i in range(len(X)):
            n.append([np.mean(X[i])])
        cov = S_d*np.cov(X) + I_d*0.0001*S_d
        next_move = stats.multivariate_normal.rvs(current_state, cov)
        return next_move, logpost(next_move, data_meas), n, cov
    else:
        cov, m1 = update_cov(X, m, Ct, S_d, I_d, 0.0001)
        next_move = stats.multivariate_normal.rvs(current_state, cov)
        return next_move, logpost(next_move, data_meas), m1, cov
    
def adaptivemcmc(initial_state, n_iter, stepsize, data_meas, logpost, t0):
    d = len(initial_state)
    I_d = np.identity(d)
    S_d = (2.4)**2/d
    parameters = []
    current_state = initial_state
    current_value = logpost(initial_state, data_meas)
    for i in range(d):
        parameters.append([])
        parameters[i].append(initial_state[i])
    lpost = [current_value]    
    n_accept = 0
    S = 0
    np.seterr(over='ignore')
    cov = stepsize
    m = []
    for t in range(n_iter):
        S += 1
        nextMove, nextValue, m, cov = random_move(current_state, np.array(parameters), cov, t, t0, stepsize, data_meas, logpost,m, S_d, I_d)
        delta_obj = np.exp(nextValue - lpost[-1])
        if delta_obj > 1:
            n_accept += 1
            for i in range(d):
                parameters[i].append(nextMove[i])
            lpost.append(nextValue)
            current_state = nextMove
            current_value = nextValue
        else:
            p_accept = delta_obj
            accept = np.random.choice([True, False], p=[p_accept, 1-p_accept])
            if accept:
                n_accept += 1
                for i in range(d):
                    parameters[i].append(nextMove[i])
                lpost.append(nextValue)
                current_state = nextMove
                current_value = nextValue
            else:
                for i in range(d):
                    parameters[i].append(parameters[i][-1])
                lpost.append(lpost[-1])
    return (parameters, lpost, n_accept/S)

def runner(m, n_iter, data_meas, logpost, t=1000, stepsize=[10, 2, 0.01]):
    np.seterr(divide='ignore', invalid='ignore')
    loc_est = np.median(data_meas)
    scale_est = (np.percentile(data_meas, 75) - np.percentile(data_meas, 25))/2
    shape_est = 0
    gevfit = stats.genextreme.fit(data_meas, loc=loc_est, scale=scale_est)
    
    if logpost([gevfit[1], gevfit[2], gevfit[0]], data_meas) > -np.inf:
        loc_est, scale_est, shape_est = gevfit[1], gevfit[2], gevfit[0]
        
    elif logpost([loc_est, scale_est, -0.1], data_meas) > -np.inf:
        loc_est, scale_est, shape_est = loc_est, scale_est, -0.1
        
    elif logpost([loc_est, scale_est, 0.1], data_meas) > -np.inf:
        loc_est, scale_est, shape_est = loc_est, scale_est, 0.1
        
    else:
        loc_est, scale_est, shape_est = loc_est, scale_est, 0
        
    problems = []
    for i in range(m):
        ui = np.random.randint(low=loc_est, high=loc_est+100)
        si = np.random.randint(low=scale_est, high=scale_est+100)
        shapei = shape_est
        theta =[ui, si, shapei]
        problems.append(theta)
    ar, mcmc_chains, ls = [], [], []
    for i in range(m):
        parameters, l, r = adaptivemcmc(problems[i], n_iter, stepsize, data_meas, logpost, t)
        mcmc_chains.append(parameters)
        ar.append(r)
        ls.append(l)
    return mcmc_chains, ar, ls


# Auto-Correlation Function
def ACF(X, end=200):
    N = len(X)
    acf = []
    for a in range(0, end):
        acf.append(np.corrcoef(X[a:], X[: N - a])[0][1])

    lag = -1
    for i in range(len(acf)):
        if acf[i] <= 0.05:
            lag = i
            break
    if lag == -1:
        print(
            "Please increase the value of the end parameter for this function"
        )
    return lag, acf


def acf_result(mcmc_chains, output_dir, params, plot):
    lag_params, acf_params = [], []
    m, d = len(mcmc_chains), len(mcmc_chains[0])
    end = 100
    for i in range(d):
        lag_params.append([])
        acf_params.append([])
        for j in range(m):
            lag, acf = ACF(mcmc_chains[j][i], end)
            lag_params[i].append(lag)
            acf_params[i].append(acf)
    lags = [max(np.array(lag_params)[:, i]) for i in range(m)]

    if plot:
        fig, ax = plt.subplots(nrows=1, ncols=m, figsize=(25, 6))
        for i in range(m):
            for j in range(d):
                ax[i].scatter(
                    np.arange(0, end),
                    acf_params[j][i],
                    label=params[j],
                    color=COLORS[j % 3],
                )
                ax[i].fill_between(
                    x=np.arange(0, end),
                    y2=np.zeros_like(acf_params[j][i]),
                    y1=acf_params[j][i],
                    alpha=0.3,
                    facecolor="skyblue",
                )
            ax[i].plot(
                [lags[i], lags[i]],
                ax[i].get_ylim(),
                label="lag = {0}".format(lags[i]),
            )
            ax[i].set_xlabel("Lag")
            ax[i].set_ylabel("ACF")
            ax[i].set_title("Sequence {0}".format(i + 1))
            ax[i].legend(loc="best")
            ax[i].grid(alpha=0.5)
        fig.savefig(output_dir + "/plots/ac_function.png")
    return lags


# History plots
def history_plots(mcmc_chains, output_dir, params, true_params=None):
    m = len(mcmc_chains)
    fig, ax = plt.subplots(nrows=1, ncols=len(params), figsize=(16, 6))
    fig.suptitle("History Plots", fontsize=20)
    for i in range(len(params)):
        for j in range(m):
            ax[i].plot(
                mcmc_chains[j][i],
                label="Sequence {0}".format(j + 1),
                color=COLORS[j % 3],
                alpha=ALPHAS[j % 3],
            )
        if true_params is not None:
            ax[i].plot(
                ax[i].get_xbound(),
                [true_params[i], true_params[i]],
                color="black",
                linestyle="dashed",
                label=params[i] + " true value",
                linewidth=2.5,
            )
        ax[i].set_xlabel("Iteration", fontsize=16)
        ax[i].set_ylabel(params[i] + " Trace", fontsize=16)
        ax[i].legend(loc="best")
    fig.savefig(output_dir + "/plots/history_plots.png")


# Final Parameters Pool
def final_params_pool(mcmc_chains, output_dir, burnin, lags, params, plot):
    m, d, n = len(mcmc_chains), len(mcmc_chains[0]), len(mcmc_chains[0][0])
    params_pool, params_ana = [], [[] for i in range(d)]
    for i in range(m):
        for j in range(burnin, n, lags[i]):
            params_pool.append([])
            for k in range(d):
                params_ana[k].append(mcmc_chains[i][k][j])
                params_pool[-1].append(mcmc_chains[i][k][j])

    if plot:
        fig, ax = plt.subplots(nrows=1, ncols=d, figsize=(16, 6))
        for i in range(d):
            ax[i].hist(params_ana[i], color="steelblue")
            ax[i].set_xlabel(params[i])
            ax[i].set_ylabel("Frequency")
            ax[i].grid(alpha=0.5)
        fig.savefig(output_dir + "/plots/params_pool.png")
    return params_pool


# Max Log-Posterior Score
def max_ls_parameters(ls, mcmc_chains, logger, verbose):
    max_indices = []
    maxs = []
    for i in range(len(mcmc_chains)):
        max_indices.append(
            np.where(np.array(ls[i]) == np.array(ls[i]).max())[0][0]
        )
        maxs.append(np.array(ls[i]).max())
    seqi = np.where(np.array(maxs) == np.array(maxs).max())[0][0]
    iterj = max_indices[seqi]
    max_params = []
    d = len(mcmc_chains[0])
    for i in range(d):
        max_params.append(mcmc_chains[seqi][i][iterj])
    logger = log(
        logger,
        "The parameters with max log-posterior score are: " + str(max_params),
        verbose,
    )
    return max_params


# Diagnostic Plots
def diagnostic_plots(data_meas, max_params, params_analysis, output_dir, plot):
    RP = np.arange(1, 501, 1)
    RL = []
    RL_max = []
    percentile_95 = []
    percentile_5 = []
    percentile_995 = []
    percentile_05 = []
    for i in range(len(RP)):
        RL.append([])
        RL_max.append(
            stats.genextreme.ppf(
                q=(1 - 1 / RP[i]),
                c=max_params[2],
                loc=max_params[0],
                scale=max_params[1],
            )
        )
        for j in range(len(params_analysis)):
            RL[i].append(
                stats.genextreme.ppf(
                    q=(1 - 1 / RP[i]),
                    c=params_analysis[j][2],
                    loc=params_analysis[j][0],
                    scale=params_analysis[j][1],
                )
            )
    for i in range(len(RL)):
        percentile_95.append(np.percentile((RL[i]), 95))
        percentile_5.append(np.percentile((RL[i]), 5))
        percentile_995.append(np.percentile((RL[i]), 99.5))
        percentile_05.append(np.percentile((RL[i]), 0.5))

    empirical = [
        stats.genextreme.ppf(
            q=(i + 1) / (len(data_meas) + 1),
            c=max_params[2],
            loc=max_params[0],
            scale=max_params[1],
        )
        for i in range(len(data_meas))
    ]
    cdf = [
        stats.genextreme.cdf(
            x=np.sort(data_meas)[i],
            c=max_params[2],
            loc=max_params[0],
            scale=max_params[1],
        )
        for i in range(len(data_meas))
    ]
    x_range = np.arange(0, max(data_meas) + 1, 0.5)
    y_range = [
        stats.genextreme.pdf(
            x=xi, c=max_params[2], loc=max_params[0], scale=max_params[1]
        )
        for xi in x_range
    ]

    if plot:
        fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(18, 12))

        ax[0, 0].scatter(
            cdf,
            [(i + 1) / (len(data_meas) + 1) for i in range(len(data_meas))],
            color="black",
        )
        ax[0, 0].plot(
            np.arange(0, 1, 0.01), np.arange(0, 1, 0.01), color="steelblue"
        )
        ax[0, 0].set_title("Probability Plot", fontsize=14)
        ax[0, 0].set_xlabel("Model", fontsize=14)
        ax[0, 0].set_ylabel("Empirical", fontsize=14)
        ax[0, 0].annotate(
            "A", xy=(0.0, 1.03), xycoords="axes fraction", fontsize=30
        )

        ax[0, 1].scatter(empirical, np.sort(data_meas), color="black")
        ax[0, 1].plot(
            np.arange(0, max(empirical)),
            np.arange(0, max(empirical)),
            color="steelblue",
        )
        ax[0, 1].set_title("Quantile Plot", fontsize=14)
        ax[0, 1].set_xlabel("Model (in MM)", fontsize=14)
        ax[0, 1].set_ylabel("Empirical (in MM)", fontsize=14)
        ax[0, 1].annotate(
            "B", xy=(0.0, 1.03), xycoords="axes fraction", fontsize=30
        )

        ax[1, 0].plot(
            np.log10(RP),
            RL_max,
            color="r",
            label="max posterior score parameter sets",
        )
        ax[1, 0].scatter(
            np.log10(
                [
                    (len(data_meas) + 1) / (len(data_meas) + 1 - k)
                    for k in np.arange(1, len(data_meas) + 1, 1)
                ]
            ),
            np.sort(data_meas),
            label="actual sorted observations",
            color="black",
            marker="X",
        )
        ax[1, 0].fill_between(
            x=np.log10(RP),
            y1=percentile_95,
            y2=percentile_5,
            alpha=0.3,
            label="90% credible interval",
            facecolor="skyblue",
        )
        ax[1, 0].fill_between(
            x=np.log10(RP),
            y1=percentile_995,
            y2=percentile_05,
            alpha=0.27,
            label="99% credible interval",
            facecolor="skyblue",
        )
        ax[1, 0].legend(loc="upper left", fontsize=10)
        ax[1, 0].set_xticks(np.log10([1, 2, 5, 10, 20, 100, 200, 500]))
        ax[1, 0].set_xticklabels([1, 2, 5, 10, 20, 100, 200, 500])
        ax[1, 0].set_title("Return Level Plot", fontsize=14)
        ax[1, 0].set_xlabel("Return Period (in year)", fontsize=14)
        ax[1, 0].set_ylabel("Return Level (in MM)", fontsize=14)
        ax[1, 0].annotate(
            "C", xy=(0.0, 1.03), xycoords="axes fraction", fontsize=30
        )

        ax[1, 1].hist(
            data_meas,
            bins=np.linspace(min(data_meas), max(data_meas)),
            normed=True,
            edgecolor="black",
            label="Histogram for observations",
            color="white",
            alpha=0.4,
        )
        ax[1, 1].plot(x_range, y_range, label="Best Model", color="black")
        ax[1, 1].plot(
            data_meas,
            np.zeros_like(data_meas),
            "b+",
            ms=20,
            color="black",
            label="observations",
        )
        ax[1, 1].legend(loc="best", fontsize=10)
        ax[1, 1].set_yticklabels([])
        ax[1, 1].set_title("Density Plot", fontsize=14)
        ax[1, 1].set_xlabel("Annual Max Sea Level (in MM)", fontsize=14)
        ax[1, 1].set_ylabel("Density", fontsize=14)
        ax[1, 1].annotate(
            "D", xy=(0.0, 1.03), xycoords="axes fraction", fontsize=30
        )

        fig.savefig(output_dir + "/plots/diagnostic_plots.png")

    return percentile_05, percentile_5, percentile_95, percentile_995
