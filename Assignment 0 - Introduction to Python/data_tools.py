"""Processing data tools for mp0.
"""
import re
import numpy as np


def title_cleanup(data):
    """Remove all characters expect a-z, A-Z and spaces from the title,
       then convert all characters to lower case.

    Args:
        data(dict): Key: article_id(int),
                    Value: [title(str), positivity_score(float)](list)
    """
    pass


def most_frequent_words(data):
    """Find the more frequeny words (including all ties), returned in a list.

    Args:
        data(dict): Key: article_id(int),
                    Value: [title(str), positivity_score(float)](list)
    Returns:
        max_words(list): List of strings containing the most frequent words.
    """
    max_words = []
    return max_words


def most_positive_titles(data):
    """Computes the most positive titles.
    Args:
        data(dict): Key: article_id(int),
                    Value: [title(str), positivity_score(float)](list)
    Returns:
        titles(list): List of strings containing the most positive titles,
                      include all ties.
    """
    titles = []
    return titles


def most_negative_titles(data):
    """Computes the most negative titles.
    Args:
        data(dict): Key: article_id(int),
                    Value: [title(str), positivity_score(float)](list)
     Returns:
        titles(list): List of strings containing the most negative titles,
                      include all ties.
    """
    titles = []
    return titles


def compute_word_positivity(data):
    """Computes average word positivity.
    Args:
        data(dict): Key: article_id(int),
                    Value: [title(str), positivity_score(float)](list)
    Returns:
        word_dict(dict): Key: word(str), value: word_index(int)
        word_avg(numpy.ndarray): numpy array where element
                                 #word_dict[word] is the
                                 average word positivity for word.
    """
    word_dict = {}
    word_avg = None
    word_avg = word_score / word_count
    return word_dict, word_avg


def most_postivie_words(word_dict, word_avg):
    """Computes the most positive words.
    Args:
        word_dict(dict): output from compute_word_positivity.
        word_avg(numpy.ndarray): output from compute_word_positivity.
    Returns:
        words(list):
    """
    words = []
    return words


def most_negative_words(word_dict, word_avg):
    """Computes the most negative words.
    Args:
        word_dict(dict): output from compute_word_positivity.
        word_avg(numpy.ndarray): output from compute_word_positivity.
    Returns:
        words(list):
    """
    words = []
    return words
