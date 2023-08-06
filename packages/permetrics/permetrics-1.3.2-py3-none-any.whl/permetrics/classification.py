# !/usr/bin/env python
# Created by "Thieu" at 09:29, 23/09/2020 ----------%
#       Email: nguyenthieu2102@gmail.com            %
#       Github: https://github.com/thieu1995        %
# --------------------------------------------------%

from permetrics.evaluator import Evaluator
from permetrics.utils.data_util import *
from permetrics.utils.classifier_util import *
import numpy as np


class ClassificationMetric(Evaluator):
    """
    This is class contains all classification metrics (for both binary and multiple classification problem)

    Notes
    ~~~~~
    + Extension of: https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics
    """

    def __init__(self, y_true=None, y_pred=None, decimal=5, **kwargs):
        """
        Args:
            y_true (tuple, list, np.ndarray): The ground truth values
            y_pred (tuple, list, np.ndarray): The prediction values
            decimal (int): The number of fractional parts after the decimal point
            **kwargs ():
        """
        super().__init__(y_true, y_pred, decimal, **kwargs)
        if kwargs is None: kwargs = {}
        self.set_keyword_arguments(kwargs)
        self.binary = True
        self.representor = "number"     # "number" or "string"

    def get_processed_data(self, y_true=None, y_pred=None, decimal=None):
        """
        Args:
            y_true (tuple, list, np.ndarray): The ground truth values
            y_pred (tuple, list, np.ndarray): The prediction values
            clean (bool): Remove all rows contain 0 value in y_pred (some methods have denominator is y_pred)
            decimal (int, None): The number of fractional parts after the decimal point

        Returns:
            y_true_final: y_true used in evaluation process.
            y_pred_final: y_pred used in evaluation process
            one_dim: is y_true has 1 dimensions or not
            decimal: The number of fractional parts after the decimal point
        """
        decimal = self.decimal if decimal is None else decimal
        if (y_true is not None) and (y_pred is not None):
            y_true, y_pred = format_classification_data_type(y_true, y_pred)
            y_true, y_pred, binary, representor = format_classification_data(y_true, y_pred)
        else:
            if (self.y_true is not None) and (self.y_pred is not None):
                y_true, y_pred = format_classification_data_type(self.y_true, self.y_pred)
                y_true, y_pred, binary, representor = format_classification_data(y_true, y_pred)
            else:
                raise ValueError("y_true or y_pred is None. You need to pass y_true and y_pred to object creation or function called.")
        return y_true, y_pred, binary, representor, decimal

    def confusion_matrix(self, y_true=None, y_pred=None, labels=None, normalize=None):
        """
        Generate confusion matrix and useful information

        Args:
            y_true (tuple, list, np.ndarray): a list of integers or strings for known classes
            y_pred (tuple, list, np.ndarray): a list of integers or strings for y_pred classes
            labels (tuple, list, np.ndarray): List of labels to index the matrix. This may be used to reorder or select a subset of labels.
            normalize ('true', 'pred', 'all', None): Normalizes confusion matrix over the true (rows), predicted (columns) conditions or all the population.

        Returns:
            matrix (np.ndarray): a 2-dimensional list of pairwise counts
            imap (dict): a map between label and index of confusion matrix
            imap_count (dict): a map between label and number of true label in y_true
        """
        y_true, y_pred, binary, representor, decimal = self.get_processed_data(y_true, y_pred, decimal=None)
        matrix, imap, imap_count = confusion_matrix(y_true, y_pred, labels, normalize)
        return matrix, imap, imap_count

    def precision_score(self, y_true=None, y_pred=None, labels=None, average="macro", decimal=None):
        """
        Generate precision score for multiple classification problem

        Args:
            y_true (tuple, list, np.ndarray): a list of integers or strings for known classes
            y_pred (tuple, list, np.ndarray): a list of integers or strings for y_pred classes
            labels (tuple, list, np.ndarray): List of labels to index the matrix. This may be used to reorder or select a subset of labels.
            average (str, None): {'micro', 'macro', 'weighted'} or None, default="macro"
                If None, the scores for each class are returned. Otherwise, this determines the type of averaging performed on the data:

                ``'micro'``:
                    Calculate metrics globally by considering each element of the label indicator matrix as a label.
                ``'macro'``:
                    Calculate metrics for each label, and find their unweighted mean.  This does not take label imbalance into account.
                ``'weighted'``:
                    Calculate metrics for each label, and find their average, weighted by support (the number of true instances for each label).

            decimal (int): The number of fractional parts after the decimal point

        Returns:
            precision (float, dict): the precision score
        """
        y_true, y_pred, binary, representor, decimal = self.get_processed_data(y_true, y_pred, decimal)
        matrix, imap, imap_count = confusion_matrix(y_true, y_pred, labels, normalize=None)
        metrics = calculate_single_label_metric(matrix, imap, imap_count)

        list_precision = np.array([item["precision"] for item in metrics.values()])
        list_weights = np.array([item["n_true"] for item in metrics.values()])

        if average == "micro":
            tp_global = np.sum(np.diag(matrix))
            fp_global = fn_global = np.sum(matrix) - tp_global
            precision = np.round(tp_global / (tp_global + fp_global), decimal)
        elif average == "macro":
            precision = np.mean(list_precision)
        elif average == "weighted":
            precision = np.dot(list_weights, list_precision) / np.sum(list_weights)
        else:
            precision = dict([(label, np.round(item["precision"], decimal)) for label, item in metrics.items()])
        return precision if type(precision) == dict else np.round(precision, decimal)

    def negative_predictive_value(self, y_true=None, y_pred=None, labels=None, average="macro", decimal=None):
        """
        Generate negative predictive value for multiple classification problem

        Args:
            y_true (tuple, list, np.ndarray): a list of integers or strings for known classes
            y_pred (tuple, list, np.ndarray): a list of integers or strings for y_pred classes
            labels (tuple, list, np.ndarray): List of labels to index the matrix. This may be used to reorder or select a subset of labels.
            average (str, None): {'micro', 'macro', 'weighted'} or None, default="macro"
            decimal (int): The number of fractional parts after the decimal point

        Returns:
            npv (float, dict): the negative predictive value
        """
        y_true, y_pred, binary, representor, decimal = self.get_processed_data(y_true, y_pred, decimal)
        matrix, imap, imap_count = confusion_matrix(y_true, y_pred, labels, normalize=None)
        metrics = calculate_single_label_metric(matrix, imap, imap_count)

        list_npv = np.array([item["negative_predictive_value"] for item in metrics.values()])
        list_weights = np.array([item["n_true"] for item in metrics.values()])

        if average == "micro":
            tp_global = tn_global = np.sum(np.diag(matrix))
            fp_global = fn_global = np.sum(matrix) - tp_global
            npv = tn_global / (tn_global + fn_global)
        elif average == "macro":
            npv = np.mean(list_npv)
        elif average == "weighted":
            npv = np.dot(list_weights, list_npv) / np.sum(list_weights)
        else:
            npv = dict([(label, np.round(item["negative_predictive_value"], decimal)) for label, item in metrics.items()])
        return npv if type(npv) == dict else np.round(npv, decimal)

    def specificity_score(self, y_true=None, y_pred=None, labels=None, average="macro", decimal=None):
        """
        Generate specificity score for multiple classification problem

        Args:
            y_true (tuple, list, np.ndarray): a list of integers or strings for known classes
            y_pred (tuple, list, np.ndarray): a list of integers or strings for y_pred classes
            labels (tuple, list, np.ndarray): List of labels to index the matrix. This may be used to reorder or select a subset of labels.
            average (str, None): {'micro', 'macro', 'weighted'} or None, default="macro"
            decimal (int): The number of fractional parts after the decimal point

        Returns:
            ss (float, dict): the specificity score
        """
        y_true, y_pred, binary, representor, decimal = self.get_processed_data(y_true, y_pred, decimal)
        matrix, imap, imap_count = confusion_matrix(y_true, y_pred, labels, normalize=None)
        metrics = calculate_single_label_metric(matrix, imap, imap_count)

        list_ss = np.array([item["specificity"] for item in metrics.values()])
        list_weights = np.array([item["n_true"] for item in metrics.values()])

        if average == "micro":
            tp_global = tn_global = np.sum(np.diag(matrix))
            fp_global = fn_global = np.sum(matrix) - tp_global
            ss = tn_global / (tn_global + fp_global)
        elif average == "macro":
            ss = np.mean(list_ss)
        elif average == "weighted":
            ss = np.dot(list_weights, list_ss) / np.sum(list_weights)
        else:
            ss = dict([(label, np.round(item["specificity"], decimal)) for label, item in metrics.items()])
        return ss if type(ss) == dict else np.round(ss, decimal)

    def recall_score(self, y_true=None, y_pred=None, labels=None, average="macro", decimal=None):
        """
        Generate recall score for multiple classification problem

        Args:
            y_true (tuple, list, np.ndarray): a list of integers or strings for known classes
            y_pred (tuple, list, np.ndarray): a list of integers or strings for y_pred classes
            labels (tuple, list, np.ndarray): List of labels to index the matrix. This may be used to reorder or select a subset of labels.
            average (str, None): {'micro', 'macro', 'weighted'} or None, default="macro"
            decimal (int): The number of fractional parts after the decimal point

        Returns:
            recall (float, dict): the recall score
        """
        y_true, y_pred, binary, representor, decimal = self.get_processed_data(y_true, y_pred, decimal)
        matrix, imap, imap_count = confusion_matrix(y_true, y_pred, labels, normalize=None)
        metrics = calculate_single_label_metric(matrix, imap, imap_count)

        list_recall = np.array([item["recall"] for item in metrics.values()])
        list_weights = np.array([item["n_true"] for item in metrics.values()])

        if average == "micro":
            tp_global = np.sum(np.diag(matrix))
            fp_global = fn_global = np.sum(matrix) - tp_global
            recall = tp_global / (tp_global + fn_global)
        elif average == "macro":
            recall = np.mean(list_recall)
        elif average == "weighted":
            recall = np.dot(list_weights, list_recall) / np.sum(list_weights)
        else:
            recall = dict([(label, np.round(item["recall"], decimal)) for label, item in metrics.items()])
        return recall if type(recall) == dict else np.round(recall, decimal)

    def accuracy_score(self, y_true=None, y_pred=None, labels=None, average="macro", decimal=None):
        """
        Generate accuracy score for multiple classification problem

        Args:
            y_true (tuple, list, np.ndarray): a list of integers or strings for known classes
            y_pred (tuple, list, np.ndarray): a list of integers or strings for y_pred classes
            labels (tuple, list, np.ndarray): List of labels to index the matrix. This may be used to reorder or select a subset of labels.
            average (str, None): {'micro', 'macro', 'weighted'} or None, default="macro"
            decimal (int): The number of fractional parts after the decimal point

        Returns:
            accuracy (float, dict): the accuracy score
        """
        y_true, y_pred, binary, representor, decimal = self.get_processed_data(y_true, y_pred, decimal)
        matrix, imap, imap_count = confusion_matrix(y_true, y_pred, labels, normalize=None)
        metrics = calculate_single_label_metric(matrix, imap, imap_count)

        list_accuracy = np.array([item["accuracy"] for item in metrics.values()])
        list_weights = np.array([item["n_true"] for item in metrics.values()])
        list_tp = np.array([item['tp'] for item in metrics.values()])

        if average == "micro":
            accuracy = np.sum(list_tp) / np.sum(list_weights)
        elif average == "macro":
            accuracy = np.mean(list_accuracy)
        elif average == "weighted":
            accuracy = np.dot(list_weights, list_accuracy) / np.sum(list_weights)
        else:
            accuracy = dict([(label, np.round(item["precision"], decimal)) for label, item in metrics.items()])
        return accuracy if type(accuracy) == dict else np.round(accuracy, decimal)

    def f1_score(self, y_true=None, y_pred=None, labels=None, average="macro", decimal=None):
        """
        Generate f1 score for multiple classification problem

        Args:
            y_true (tuple, list, np.ndarray): a list of integers or strings for known classes
            y_pred (tuple, list, np.ndarray): a list of integers or strings for y_pred classes
            labels (tuple, list, np.ndarray): List of labels to index the matrix. This may be used to reorder or select a subset of labels.
            average (str, None): {'micro', 'macro', 'weighted'} or None, default="macro"
            decimal (int): The number of fractional parts after the decimal point

        Returns:
            f1 (float, dict): the f1 score
        """
        y_true, y_pred, binary, representor, decimal = self.get_processed_data(y_true, y_pred, decimal)
        matrix, imap, imap_count = confusion_matrix(y_true, y_pred, labels, normalize=None)
        metrics = calculate_single_label_metric(matrix, imap, imap_count)

        list_f1 = np.array([item["f1"] for item in metrics.values()])
        list_weights = np.array([item["n_true"] for item in metrics.values()])

        if average == "micro":
            tp_global = np.sum(np.diag(matrix))
            fp_global = fn_global = np.sum(matrix) - tp_global
            precision = np.round(tp_global / (tp_global + fp_global), decimal)
            recall = tp_global / (tp_global + fn_global)
            f1 = (2 * precision * recall) / (precision + recall)
        elif average == "macro":
            f1 = np.mean(list_f1)
        elif average == "weighted":
            f1 = np.dot(list_weights, list_f1) / np.sum(list_weights)
        else:
            f1 = dict([(label, item["f1"]) for label, item in metrics.items()])
        return f1 if type(f1) == dict else np.round(f1, decimal)

    def f2_score(self, y_true=None, y_pred=None, labels=None, average="macro", decimal=None):
        """
        Generate f2 score for multiple classification problem

        Args:
            y_true (tuple, list, np.ndarray): a list of integers or strings for known classes
            y_pred (tuple, list, np.ndarray): a list of integers or strings for y_pred classes
            labels (tuple, list, np.ndarray): List of labels to index the matrix. This may be used to reorder or select a subset of labels.
            average (str, None): {'micro', 'macro', 'weighted'} or None, default="macro"
            decimal (int): The number of fractional parts after the decimal point

        Returns:
            f2 (float, dict): the f2 score
        """
        y_true, y_pred, binary, representor, decimal = self.get_processed_data(y_true, y_pred, decimal)
        matrix, imap, imap_count = confusion_matrix(y_true, y_pred, labels, normalize=None)
        metrics = calculate_single_label_metric(matrix, imap, imap_count)

        list_f2 = np.array([item["f1"] for item in metrics.values()])
        list_weights = np.array([item["n_true"] for item in metrics.values()])

        if average == "micro":
            tp_global = np.sum(np.diag(matrix))
            fp_global = fn_global = np.sum(matrix) - tp_global
            precision = np.round(tp_global / (tp_global + fp_global), decimal)
            recall = tp_global / (tp_global + fn_global)
            f2 = (5 * precision * recall) / (4 * precision + recall)
        elif average == "macro":
            f2 = np.mean(list_f2)
        elif average == "weighted":
            f2 = np.dot(list_weights, list_f2) / np.sum(list_weights)
        else:
            f2 = dict([(label, item["f2"]) for label, item in metrics.items()])
        return f2 if type(f2) == dict else np.round(f2, decimal)

    def fbeta_score(self, y_true=None, y_pred=None, beta=1.0, labels=None, average="macro", decimal=None):
        """
        The beta parameter determines the weight of recall in the combined score.
        beta < 1 lends more weight to precision, while beta > 1 favors recall
        (beta -> 0 considers only precision, beta -> +inf only recall).

        Args:
            y_true (tuple, list, np.ndarray): a list of integers or strings for known classes
            y_pred (tuple, list, np.ndarray): a list of integers or strings for y_pred classes
            beta (float): the weight of recall in the combined score, default = 1.0
            labels (tuple, list, np.ndarray): List of labels to index the matrix. This may be used to reorder or select a subset of labels.
            average (str, None): {'micro', 'macro', 'weighted'} or None, default="macro"
            decimal (int): The number of fractional parts after the decimal point

        Returns:
            fbeta (float, dict): the fbeta score
        """
        y_true, y_pred, binary, representor, decimal = self.get_processed_data(y_true, y_pred, decimal)
        matrix, imap, imap_count = confusion_matrix(y_true, y_pred, labels, normalize=None)
        metrics = calculate_single_label_metric(matrix, imap, imap_count, beta=beta)

        list_fbeta = np.array([item["f1"] for item in metrics.values()])
        list_weights = np.array([item["n_true"] for item in metrics.values()])

        if average == "micro":
            tp_global = np.sum(np.diag(matrix))
            fp_global = fn_global = np.sum(matrix) - tp_global
            precision = np.round(tp_global / (tp_global + fp_global), decimal)
            recall = tp_global / (tp_global + fn_global)
            fbeta = ((1 + beta ** 2) * precision * recall) / (beta ** 2 * precision + recall)
        elif average == "macro":
            fbeta = np.mean(list_fbeta)
        elif average == "weighted":
            fbeta = np.dot(list_weights, list_fbeta) / np.sum(list_weights)
        else:
            fbeta = dict([(label, item["fbeta"]) for label, item in metrics.items()])
        return fbeta if type(fbeta) == dict else np.round(fbeta, decimal)

    def matthews_correlation_coefficient(self, y_true=None, y_pred=None, labels=None, average="macro", decimal=None):
        """
        Args:
            y_true (tuple, list, np.ndarray): a list of integers or strings for known classes
            y_pred (tuple, list, np.ndarray): a list of integers or strings for y_pred classes
            labels (tuple, list, np.ndarray): List of labels to index the matrix. This may be used to reorder or select a subset of labels.
            average (str, None): {'micro', 'macro', 'weighted'} or None, default="macro"
            decimal (int): The number of fractional parts after the decimal point

        Returns:
            mcc (float, dict): the Matthews correlation coefficient
        """
        y_true, y_pred, binary, representor, decimal = self.get_processed_data(y_true, y_pred, decimal)
        matrix, imap, imap_count = confusion_matrix(y_true, y_pred, labels, normalize=None)
        metrics = calculate_single_label_metric(matrix, imap, imap_count)

        list_mcc = np.array([item["mcc"] for item in metrics.values()])
        list_weights = np.array([item["n_true"] for item in metrics.values()])

        if average == "micro":
            tp = tn = np.sum(np.diag(matrix))
            fp = fn = np.sum(matrix) - tp
            mcc = (tp * tn - fp * fn) / np.sqrt(((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn)))
        elif average == "macro":
            mcc = np.mean(list_mcc)
        elif average == "weighted":
            mcc = np.dot(list_weights, list_mcc) / np.sum(list_weights)
        else:
            mcc = dict([(label, item["mcc"]) for label, item in metrics.items()])
        return mcc if type(mcc) == dict else np.round(mcc, decimal)

    def hamming_loss(self, y_true=None, y_pred=None, labels=None, average="macro", decimal=None):
        """
        Generate hamming loss for multiple classification problem

        Args:
            y_true (tuple, list, np.ndarray): a list of integers or strings for known classes
            y_pred (tuple, list, np.ndarray): a list of integers or strings for y_pred classes
            labels (tuple, list, np.ndarray): List of labels to index the matrix. This may be used to reorder or select a subset of labels.
            average (str, None): {'micro', 'macro', 'weighted'} or None, default="macro"
            decimal (int): The number of fractional parts after the decimal point

        Returns:
            hl (float, dict): the hamming loss
        """
        y_true, y_pred, binary, representor, decimal = self.get_processed_data(y_true, y_pred, decimal)
        matrix, imap, imap_count = confusion_matrix(y_true, y_pred, labels, normalize=None)
        metrics = calculate_single_label_metric(matrix, imap, imap_count)

        list_accuracy = np.array([item["accuracy"] for item in metrics.values()])
        list_weights = np.array([item["n_true"] for item in metrics.values()])
        list_tp = np.array([item['tp'] for item in metrics.values()])

        if average == "micro":
            hl = 1.0 - np.sum(list_tp) / np.sum(list_weights)
        elif average == "macro":
            hl = np.mean(list_accuracy)
        elif average == "weighted":
            hl = np.dot(list_weights, list_accuracy) / np.sum(list_weights)
        else:
            hl = dict([(label, np.round(item["hamming_loss"], decimal)) for label, item in metrics.items()])
        return hl if type(hl) == dict else np.round(hl, decimal)

    def lift_score(self, y_true=None, y_pred=None, labels=None, average="macro", decimal=None):
        """
        Generate lift score for multiple classification problem

        Args:
            y_true (tuple, list, np.ndarray): a list of integers or strings for known classes
            y_pred (tuple, list, np.ndarray): a list of integers or strings for y_pred classes
            labels (tuple, list, np.ndarray): List of labels to index the matrix. This may be used to reorder or select a subset of labels.
            average (str, None): {'micro', 'macro', 'weighted'} or None, default="macro"
            decimal (int): The number of fractional parts after the decimal point

        Returns:
            ls (float, dict): the lift score
        """
        y_true, y_pred, binary, representor, decimal = self.get_processed_data(y_true, y_pred, decimal)
        matrix, imap, imap_count = confusion_matrix(y_true, y_pred, labels, normalize=None)
        metrics = calculate_single_label_metric(matrix, imap, imap_count)

        list_ls = np.array([item["lift_score"] for item in metrics.values()])
        list_weights = np.array([item["n_true"] for item in metrics.values()])

        if average == "micro":
            tp = tn = np.sum(np.diag(matrix))
            fp = fn = np.sum(matrix) - tp
            ls = (tp/(tp + fp)) / ((tp + fn) / (tp + tn + fp + fn))
        elif average == "macro":
            ls = np.mean(list_ls)
        elif average == "weighted":
            ls = np.dot(list_weights, list_ls) / np.sum(list_weights)
        else:
            ls = dict([(label, np.round(item["lift_score"], decimal)) for label, item in metrics.items()])
        return ls if type(ls) == dict else np.round(ls, decimal)

    CM = cm = confusion_matrix
    PS = ps = precision_score
    NPV = npv = negative_predictive_value
    RS = rs = recall_score
    AS = accuracy_score
    F1S = f1s = f1_score
    F2S = f2s = f2_score
    FBS = fbs = fbeta_score
    SS = ss = specificity_score
    MCC = mcc = matthews_correlation_coefficient
    HL = hl = hamming_loss
    LS = ls = lift_score


