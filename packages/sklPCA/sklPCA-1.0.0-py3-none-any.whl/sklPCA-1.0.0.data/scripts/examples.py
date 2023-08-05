"""
    Supervised Kernel-based Longitudinal PCA (skl-PCA) examples script.
    Copyright (C) 2018  Mindstrong Health, Inc.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


# ########################################## Imports and Definitions ###################################################

from itertools import product
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from sklPCA import functions as sklPCA


def uniform(mu, sigma, shape):
    return np.random.uniform(mu - np.sqrt(3) * sigma, mu + np.sqrt(3) * sigma, shape)


def normal(mu, sigma, shape):
    return np.random.normal(mu, sigma, shape)


def RBF(x, mu, sigma):
    return np.exp(-np.sum((x-mu) ** 2) / 2 / sigma / sigma)


def LF(x, mu, sigma):
    return np.sum(x-mu)


# ############################################ Plot Sample Dataset #####################################################

m, ni = 200, 200
X, Y = sklPCA.simulate_data(normal, normal, RBF, m, ni, sigma_b=5, sigma_w=5, sigma_e=0, R=1, D=1)
colors = sklPCA.make_colors(m, 0, .65, pale=.3, light=.7, opacity=1)
for i in range(m):
    indices = range(ni * i, ni * (i + 1))
    plt.plot(X[indices], Y[indices], ".", c=colors[i])
    plt.xlabel("$\widetilde{X}_{ij}$")
    plt.ylabel("$\widetilde{Y}_{ij}$")
plt.show()


# ########################################### Reduce Predictors Only ####################################################

m, ni = 10, 10
X, Y = sklPCA.simulate_data(uniform, uniform, LF, m, ni, sigma_b=1, sigma_w=1, sigma_e=.01, R=2, D=1000)
features, target, nonrandom_feature_order, random_feature_order = sklPCA.format(X, Y, m, ni)
reduced = sklPCA.reduce(features, target, model_type="mixed",
                 kernel_predictors="linear", kernel_sigma_predictors=1,
                 kernel_target="linear", kernel_sigma_target=1,
                 n_eigenvectors=2)
print(reduced)


# ##################################### Reduce Predictors And Train Model #############################################

m, ni = 10, 10
X, Y = sklPCA.simulate_data(uniform, uniform, LF, m, ni, sigma_b=1, sigma_w=1, sigma_e=.01, R=2, D=1000)
features, target, nonrandom_feature_order, random_feature_order = sklPCA.format(X, Y, m, ni)

# for demonstration, only one train-test split is used
folds = sklPCA.within_subject_folds(features.index.values, n_folds=5, shuffled=True)
train_IDs, test_IDs = folds[0]

# fit the model
reduction_objects, models, fits = sklPCA.reduce_fit(features.iloc[train_IDs], target.iloc[train_IDs],
                                            model_type="mixed",
                                            kernel_predictors="linear", kernel_sigma_predictors=1,
                                            kernel_target="linear", kernel_sigma_target=1,
                                            n_eigenvectors=2)

# make predictions
predictions = sklPCA.reduce_predict(features.iloc[test_IDs], reduction_objects, models,
                            kernel_test="linear", kernel_sigma_test=1, n_eigenvectors=2)

# print pearson correlation and p-value
correlation = stats.pearsonr(predictions.values.flatten(), target.iloc[test_IDs].values)
print(correlation)


# ########################################### Comparison Simulation ####################################################

# parameters
reps, m, ni, sigma_b, sigma_e = 10, 50, 50, 1, 0.00001
sigma_ratios = (1/10, 1)
distribution_sets = ((uniform, uniform, LF, "linear"), (normal, normal, RBF, "radial"))
model_types = ("iid", "mixed")
Rs = (1, 5)
Ds = (10, 1000)

# compute correlations
correlations = []
for distribution_set, sigma_ratio, R, D, rep in product(distribution_sets, sigma_ratios, Rs, Ds, range(reps)):
    X, Y = sklPCA.simulate_data(*distribution_set[:-1], m, ni, sigma_b, sigma_ratio * sigma_b, sigma_e, R=R, D=D)
    features, target, nonrandom_feature_order, random_feature_order = sklPCA.format(X, Y, m, ni)
    for model_type in model_types:
        correlation, prediction = sklPCA.calculate_CV_correlation(
            features, target, model_type, n_folds=5, shuffled=True, n_eigenvectors=R,
            kernel_predictors=distribution_set[-1], kernel_sigma_predictors=1,
            kernel_target=distribution_set[-1], kernel_sigma_target=1)
        print("correlation: " + str(correlation[0]) + ", model_type: " + str(model_type))
        correlations.append([distribution_set[-1], sigma_ratio, R, D, str(model_type), correlation[0]])

# format and print results
column_names = ["distribution_set", "sigma_ratio", "R", "D", "model_type", "correlation"]
correlations_pd = pd.DataFrame(correlations, columns=column_names)
correlations_summary = correlations_pd.\
    groupby(column_names[:-1]).\
    agg({"correlation": ["mean", "std"]}).\
    reset_index()

print(correlations_summary)

