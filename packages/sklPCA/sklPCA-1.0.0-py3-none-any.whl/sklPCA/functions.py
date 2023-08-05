"""
    Supervised Kernel-based Longitudinal PCA (skl-PCA) core and support functions.
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

from collections import Counter
import numpy as np
import scipy
from scipy import stats
import pandas as pd
import sklearn
from sklearn import linear_model
from sklearn.model_selection import KFold


# ######################################################################################################################
# ################################################ Distributions #######################################################
# ######################################################################################################################


def uniform(mu, sigma, shape):
    return np.random.uniform(mu - np.sqrt(3) * sigma, mu + np.sqrt(3) * sigma, shape)


def normal(mu, sigma, shape):
    return np.random.normal(mu, sigma, shape)


def RBF(x, mu, sigma):
    return np.exp(-np.sum((x-mu) ** 2) / 2 / sigma / sigma)


def LF(x, mu, sigma):
    return np.sum(x-mu)


# ######################################################################################################################
# ############################################# Kernel Computation #####################################################
# ######################################################################################################################


def compute_kernel(W_test, W_train, kernel_type, kernel_sigma):
    a = np.diagonal(np.dot(W_test, W_test.T))
    b = np.diagonal(np.dot(W_train, W_train.T))
    A = np.matlib.repmat(a.reshape(len(a), 1), 1, len(b))
    B = np.matlib.repmat(b, len(a), 1)
    arg = abs(A + B - 2 * np.dot(W_test, W_train.T))
    if kernel_type == 'linear':
        kernel = np.dot(W_test, W_train.T)
    elif kernel_type == 'radial':
        kernel = np.exp(-arg / kernel_sigma)
    elif kernel_type == 'laplace':
        kernel = np.exp(-np.sqrt(arg) / kernel_sigma)
    elif kernel_type == 'exponential':
        kernel = np.exp(-(np.dot(W_test, W_train.T)) / kernel_sigma)
    elif kernel_type == 'polynomial':
        kernel = np.power((1 + np.dot(W_test, W_train.T)), kernel_sigma)
    elif kernel_type == 'power':
        kernel = - np.power(arg, kernel_sigma)
    elif kernel_type == 'log':
        kernel = - np.log(1.0 + np.power(arg, kernel_sigma))
    return kernel


def center_feature_matrix(features, calculate_center, mu_vector, sd_vector):
    if calculate_center:
        if features.ndim == 1:
            features = features.reshape(len(features), 1)
        mu_vector = np.mean(features, axis=0)
        sd_vector = np.empty([0])

    n_row, n_col = features.shape
    Z = features - np.matlib.repmat(mu_vector, n_row, 1)
    for j in range(n_col):
        sd_vector = np.append(sd_vector, np.std(Z[:, j], ddof=1, dtype=np.float64))
        if sd_vector[j] == float(0) or np.isnan(sd_vector[j]):
            sd_vector[j] = 1
        Z[:, j] = Z[:, j] / sd_vector[j]

    return Z, mu_vector, sd_vector


def mean_kernel_per_subject(kernel, row_labels, column_labels):
    urs = list(np.unique(row_labels, return_index=True)[1]) + [len(row_labels)]
    ucs = list(np.unique(column_labels, return_index=True)[1]) + [len(column_labels)]
    reduced_kernel = np.array([[np.mean(kernel[urs[i]:urs[i + 1], ucs[j]:ucs[j + 1]])
                                for j in range(len(ucs) - 1)] for i in range(len(urs) - 1)])
    return reduced_kernel


# ######################################################################################################################
# ######################################### Generalized Eigenvector Calculation ########################################
# ######################################################################################################################


def generate_training_model(predictors, kernel_predictors, kernel_sigma_predictors, target, kernel_target,
                            kernel_sigma_target, row_labels, column_labels, reduce_by_mean, regularization):
    centered_predictors, _, _ = center_feature_matrix(predictors, True, None, None)
    centered_target, _, _ = center_feature_matrix(target, True, None, None)

    kernelResult = compute_kernel(centered_predictors, centered_predictors, kernel_predictors, kernel_sigma_predictors)
    K_centerer = sklearn.preprocessing.KernelCenterer()
    K_centerer = K_centerer.fit(kernelResult)
    centered_K = K_centerer.transform(kernelResult)
    Lambda = regularization * max(np.diag(centered_K))
    centered_K = (centered_K + Lambda * np.eye(centered_K.shape[0]))
    L = compute_kernel(centered_target, centered_target, kernel_target, kernel_sigma_target)
    if reduce_by_mean:
        centered_K = mean_kernel_per_subject(centered_K, row_labels, column_labels)
        L = mean_kernel_per_subject(L, row_labels, column_labels)
        reduced_labels = np.unique(row_labels)
    else:
        reduced_labels = row_labels
    Q = np.dot(centered_K, np.dot(L, centered_K))
    D, V = scipy.linalg.eigh(Q, centered_K)
    D[np.isinf(D)] = 0
    oidx = sorted(range(len(D)), key=lambda i: -abs(D[i].real))
    D, V = D[oidx], V[:, oidx].real
    return centered_K, V, K_centerer, centered_target, reduced_labels


def generate_test_model(predictors, test_predictors, kernel_predictors, kernel_sigma_predictors, kernel_centering_object,
                        row_labels, column_labels, reduce_by_mean=False):
    centered_predictors, mu_vector, sd_vector = center_feature_matrix(predictors, True, None, None)
    centered_test_predictors, _, _ = center_feature_matrix(test_predictors, False, mu_vector, sd_vector)
    kernel_result = compute_kernel(centered_test_predictors, centered_predictors, kernel_predictors, kernel_sigma_predictors)
    centered_kernel_result = kernel_centering_object.transform(kernel_result)
    if reduce_by_mean:
        centered_kernel_result = mean_kernel_per_subject(centered_kernel_result, row_labels, column_labels)
        reduced_labels = np.unique(row_labels)
    else:
        reduced_labels = row_labels
    return centered_kernel_result, reduced_labels


# ######################################################################################################################
# ############################################ Predictor Reduction #####################################################
# ######################################################################################################################


def reduce_training_predictors(predictors, target, component_type, labels, kernel_predictors, kernel_sigma_predictors, kernel_target, kernel_sigma_target, n_eigenvectors, regularization):
    reduce_by_mean = component_type == "Fixed"
    K, V, kernel_centering_object, centered_target, reduced_labels = generate_training_model(predictors, kernel_predictors, kernel_sigma_predictors, target, kernel_target, kernel_sigma_target, labels, labels, reduce_by_mean, regularization)
    reduced_predictors = pd.DataFrame(np.dot(K, V[:, :n_eigenvectors]), index=reduced_labels)
    reduced_predictors.columns = [component_type + "_" + str(i) for i in range(reduced_predictors.shape[1])]
    reduced_predictors.index.name = "Subject"
    ksPCA_object = {"original_predictors": predictors, "reduced_predictors": reduced_predictors, "V": V, "kernel_centering_object": kernel_centering_object, "labels": labels}
    return ksPCA_object


def reduce_test_predictors(test_predictors, component_type, labels, ksPCA_object, kernel_test, kernel_sigma_test, n_eigenvectors):
    reduce_by_mean = component_type == "Fixed"
    predictors, V, kernel_centering_object, training_labels = [ksPCA_object[i] for i in ["original_predictors", "V", "kernel_centering_object", "labels"]]
    K_test, reduced_test_labels = generate_test_model(predictors, test_predictors, kernel_test, kernel_sigma_test, kernel_centering_object, labels, training_labels, reduce_by_mean)
    reduced_predictors_test = pd.DataFrame(np.dot(K_test, V[:, range(n_eigenvectors)]), index=reduced_test_labels)
    reduced_predictors_test.columns = [component_type + "_Test_" + str(i) for i in range(reduced_predictors_test.shape[1])]
    reduced_predictors_test.index.name = "Subject"
    return reduced_predictors_test


def reduce(features, target, model_type, kernel_predictors, kernel_sigma_predictors, kernel_target, kernel_sigma_target, n_eigenvectors, regularization=0.01):
    labels = features.index.values
    target = pd.DataFrame(center_feature_matrix(np.array(target), True, None, None)[0], index=target.index.values, columns=["value"])
    target.index.name = "Subject"
    subjects = np.unique(labels)
    reduced_predictors = {}

    if model_type == "iid":
        reduced_predictors["iid"] = reduce_training_predictors(features.values, target.values, "IID", labels,
            kernel_predictors, kernel_sigma_predictors, kernel_target, kernel_sigma_target, n_eigenvectors, regularization)
    else:
        reduced_predictors["fixed"] = reduce_training_predictors(features.values, target.values, "Fixed", labels,
            kernel_predictors, kernel_sigma_predictors, kernel_target, kernel_sigma_target, n_eigenvectors, regularization)

    if model_type == "mixed":
        reduced_predictors["random"] = {}
        for subject in subjects:
            subject_indices = features.index == subject
            try:
                selected_subject_features = features.loc[subject_indices]
                subject_target = target.loc[subject_indices]
                reduced_predictors["random"][subject] = reduce_training_predictors(
                    selected_subject_features.values, subject_target.values, "Random", selected_subject_features.index,
                    kernel_predictors, kernel_sigma_predictors, kernel_target, kernel_sigma_target,
                    min(n_eigenvectors, selected_subject_features.values.shape[0]), regularization)["reduced_predictors"]
            except:
                print("Random component covariate reduction failed for Subject %s." % subject)

    return reduced_predictors


# ######################################################################################################################
# ########################################## Model Fitting and Prediction ##############################################
# ######################################################################################################################


def reduce_fit(features, target, model_type, kernel_predictors, kernel_sigma_predictors, kernel_target, kernel_sigma_target, n_eigenvectors, regularization=0.01):
    labels = features.index.values
    target = pd.DataFrame(center_feature_matrix(np.array(target), True, None, None)[0], index=target.index.values, columns=["value"])
    target.index.name = "Subject"
    subjects = np.unique(labels)
    ksPCA_objects, regression_models, training_fits = {}, {}, {}

    if model_type == "iid":
        ksPCA_objects["iid"] = reduce_training_predictors(features.values, target.values, "IID", labels,
            kernel_predictors, kernel_sigma_predictors, kernel_target, kernel_sigma_target, n_eigenvectors, regularization)
        regression_models["iid"] = linear_model.LinearRegression().fit(ksPCA_objects["iid"]["reduced_predictors"], target)
        nonrandom_fits = training_fits["iid"] = pd.DataFrame(regression_models["iid"].predict(ksPCA_objects["iid"]["reduced_predictors"]), index=labels)

    else:
        fixed_target = target.groupby("Subject").mean()
        ksPCA_objects["fixed"] = reduce_training_predictors(features.values, target.values, "Fixed", labels, kernel_predictors, kernel_sigma_predictors, kernel_target, kernel_sigma_target, n_eigenvectors, regularization)
        regression_models["fixed"] = linear_model.LinearRegression().fit(ksPCA_objects["fixed"]["reduced_predictors"], fixed_target)
        nonrandom_fits = training_fits["fixed"] = features[[]].join(pd.DataFrame(regression_models["fixed"].predict(ksPCA_objects["fixed"]["reduced_predictors"]), index=ksPCA_objects["fixed"]["reduced_predictors"].index))

    nonrandom_residuals = pd.DataFrame(pd.DataFrame(target.values - nonrandom_fits.values, index=target.index))
    nonrandom_fits.columns, nonrandom_fits.index.name = ["Fit"], "Subject"

    if model_type == "mixed":
        ksPCA_objects["random"], regression_models["random"], training_fits["random"] = {}, {}, {}
        for subject in subjects:
            subject_indices = features.index == subject
            try:
                selected_subject_features = features.loc[subject_indices]
                subject_residuals = nonrandom_residuals.loc[subject_indices]
                ksPCA_objects["random"][subject] = reduce_training_predictors(
                    selected_subject_features.values, subject_residuals.values, "Random", selected_subject_features.index,
                    kernel_predictors, kernel_sigma_predictors, kernel_target, kernel_sigma_target,
                    min(n_eigenvectors, selected_subject_features.values.shape[0]), regularization)
                subject_reduced_predictors = ksPCA_objects["random"][subject]["reduced_predictors"]
                subject_model = linear_model.LinearRegression().fit(subject_reduced_predictors, subject_residuals)
                regression_models["random"][subject] = subject_model
                training_fits["random"][subject] = subject_model.predict(subject_reduced_predictors).reshape((subject_reduced_predictors.shape[0], 1))
            except:
                print("Mixed Model failed for Subject %s." % subject)

    return ksPCA_objects, regression_models, training_fits


def reduce_predict(features, ksPCA_objects, models, kernel_test, kernel_sigma_test, n_eigenvectors):

    labels = features.index.values
    subjects = np.unique(labels)

    if "iid" in models:
        iid_reduced_predictors = reduce_test_predictors(features.values, "IID", labels, ksPCA_objects["iid"], kernel_test, kernel_sigma_test, n_eigenvectors)
        predictions = pd.DataFrame(models["iid"].predict(iid_reduced_predictors), index=labels)
        predictions.index.name = "Subject"

    else:
        fixed_reduced_predictors = reduce_test_predictors(features.values, "Fixed", features.index, ksPCA_objects["fixed"], kernel_test, kernel_sigma_test, n_eigenvectors)
        predictions = features[[]].join(pd.DataFrame(models["fixed"].predict(fixed_reduced_predictors), index=fixed_reduced_predictors.index))
    predictions.columns = ["Prediction"]

    if "random" in models:
        random_predictions = predictions.copy(deep=True).abs() * 0
        for subject in subjects:
            if subject in models["random"]:
                try:
                    selected_subject_features = features.loc[features.index == subject]
                    subject_reduced_predictors = reduce_test_predictors(selected_subject_features.values, "Random", selected_subject_features.index.values, ksPCA_objects["random"][subject], kernel_test, kernel_sigma_test, n_eigenvectors)
                    random_predictions.loc[random_predictions.index == subject] = models["random"][subject].predict(subject_reduced_predictors).reshape((subject_reduced_predictors.shape[0], 1))
                except:
                    print("Mixed Model failed for Subject %s" % subject)
        predictions = predictions + random_predictions

    return predictions


# #######################################################################################################################
# ################################################ Cross Validation ####################################################
# ######################################################################################################################

def within_subject_folds(labels, n_folds, shuffled=False):
    data, excluded = [], []
    nis = list(Counter(labels).values())
    starting_indices = np.concatenate([[0], np.cumsum(nis[:-1])])
    for k in range(len(nis)):
        try:
            zeroed_folds_subject_k = list(KFold(n_folds).split(range(nis[k])))
            if shuffled:
                shuffle = np.random.choice(range(nis[k]), nis[k], replace=False)
                zeroed_folds_subject_k = [(shuffle[fold[0]], shuffle[fold[1]]) for fold in zeroed_folds_subject_k]
            data.append([[i + starting_indices[k] for i in j] for j in zeroed_folds_subject_k])
        except ValueError:
            excluded.append(k)
            pass

    folds = [[np.concatenate([k[i][j] for k in data]) for j in range(2)] for i in range(n_folds)]
    print("Subjects discarded: " + str(excluded))

    return folds


def calculate_CV_correlation(features, target, model_type, n_folds=5, shuffled=True, n_eigenvectors=2,
                             kernel_predictors="linear", kernel_sigma_predictors=1,
                             kernel_target="linear", kernel_sigma_target=1):

    test_predictions = pd.DataFrame({"Prediction": np.empty(target.shape) * np.nan}, index=target.index)
    for train_IDs, test_IDs in within_subject_folds(features.index.values, n_folds, shuffled):
        reduction_objects, models, fits = reduce_fit(features.iloc[train_IDs], target.iloc[train_IDs], model_type, kernel_predictors, kernel_sigma_predictors, kernel_target, kernel_sigma_target, n_eigenvectors)
        test_predictions.iloc[test_IDs] = reduce_predict(features.iloc[test_IDs], reduction_objects, models, kernel_predictors, kernel_sigma_predictors, n_eigenvectors)
    correlation = stats.pearsonr(test_predictions.values.flatten(), target)

    return correlation, test_predictions


# ######################################################################################################################
# ########################################### Simulation and Formatting ################################################
# ######################################################################################################################


def simulate_data(f_mu, f_X, f_Y, m, ni, sigma_b, sigma_w, sigma_e, R, D):
    mu = f_mu(0, sigma_b, (m, R))
    X_tilde = np.vstack([np.hstack([f_X(mu[i, r], sigma_w, (ni, 1)) for r in range(R)]) for i in range(m)])
    P = np.random.normal(0, 1, (R, D))
    X = X_tilde.dot(P)
    Y_tilde = np.hstack([
        np.array([f_Y(X_tilde[i * ni + j, :], mu[i], sigma_w) for j in range(ni)]) -
        np.repeat(f_Y(mu[i], np.zeros(R), sigma_b), ni)
        for i in range(m)]).reshape((m * ni, 1))
    Y = Y_tilde + np.random.normal(0, sigma_e, Y_tilde.shape)
    return X, Y


def simulate_data_lattice(m, ni, sigma_b, sigma_w, sigma_e, D, shuffle=True):
    n = m * ni
    X_tilde = np.array([sigma_b * (i/m - 1/2) + sigma_w * (j/ni - 1/2) for i in range(m) for j in range(ni)]).reshape((n, 1))
    Y_tilde = np.array([sigma_b * (1/2 - i/m) + sigma_w * (j/ni - 1/2) for i in range(m) for j in range(ni)]).reshape((n, 1))
    P = np.random.normal(0, 1, (1, D))
    X = X_tilde.dot(P)
    Y = Y_tilde + np.random.normal(0, sigma_e, Y_tilde.shape)
    if shuffle:
        shuffled_order = np.concatenate([np.random.choice(ni, ni, replace=False) + ni * i for i in range(m)])
        X_tilde, X, Y = X_tilde[shuffled_order], X[shuffled_order], Y[shuffled_order]
    return X, Y


def format(X, Y, m, ni):
    features = X
    target = Y.flatten()
    subject_labels = ["Subject_" + str(i).zfill(int(np.log10(m - 1)) + 1) for i in range(m)]
    labels = np.repeat(subject_labels, ni)
    features = pd.DataFrame(features)
    features.index = labels
    feature_labels = np.array(["Feature_" + str(i) for i in range(X.shape[1])])
    features.columns = feature_labels
    target = pd.Series(target, index=labels)
    features.index.name = "Subject"
    target.index.name = "Subject"
    nonrandom_feature_order = feature_labels
    random_feature_order = {subject: feature_labels for subject in subject_labels}

    return features, target, nonrandom_feature_order, random_feature_order


def make_colors(n=100, start=0, end=1, pale=.3, light=.7, opacity=1):
    t = np.linspace(start, end, n)
    t *= 6
    r = 1*(t<1) + (2-t)*(1<=t)*(t<2) + (t-4)*(4<=t)*(t<5) + 1*(5<=t)
    g = t*(t<1) + 1*(1<=t)*(t<3) + (4-t)*(3<=t)*(t<4)
    b = (t-2)*(2<=t)*(t<3) + 1*(3<=t)*(t<5) + (6-t)*(5<=t)*(t<6)
    o = np.repeat(opacity, n)
    output = np.array(list(zip(r, g, b, o))) * (1-pale) + pale * light
    return output