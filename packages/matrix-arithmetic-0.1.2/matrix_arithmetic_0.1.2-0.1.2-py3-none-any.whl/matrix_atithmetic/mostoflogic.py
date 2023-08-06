#!/usr/bin/python
# -*- coding: utf-8 -*-

# ADDITION OF 1D MATRIXES

def checkDimention(m1):
    try:
        if type(m1[0]) is list:
            if type(m1[0][0]) is list:

                # 'greater than 2d arr'

                return 'must be 1 or 2 dimention list'
            else:

                # '2d array'

                return 2
        else:

            # "1d array"

            return 1
    except NameError:
        return NameError


# CHECKING IF INPUT IS ARRAY

def checkInput(m1):
    if type(m1) is not list:
        return TypeError('input must be a list')
    return True

def addFor1d(m1, m2):
    ans = []
    if len(m1) != len(m2):
        return 'must be of same length to add'
    for i in range(len(m1)):
        try:
            ans.append(m1[i] + m2[i])
        except:
            return TypeError('must be an int')
    return ans


# ADDITION OF 2D MATRIXES

def addFor2d(m1, m2):
    ans = []
    ans1 = []

    # if len(m1)==len(m2):

    for i in range(len(m1)):
        if len(m1[i]) == len(m2[i]) and len(m1) == len(m2):
            try:
                for j in range(len(m1[i])):
                    ans1.append(m1[i][j] + m2[i][j])
                ans.append(ans1)
                ans1 = []
            except:
                return TypeError('must be an int')
        else:
            return 'must be of same length to add'
    return ans


# SUBTRACTION OF 1D MATRIXES

def subFor1d(m1, m2):
    ans = []
    if len(m1) != len(m2):
        return 'must be of same length to add'
    for i in range(len(m1)):
        try:
            ans.append(m1[i] - m2[i])
        except:
            return TypeError('must be an int')
    return ans


# SUBTRACTION OF 2D MATRIXES

def subFor2d(m1, m2):
    ans = []
    ans1 = []

    # if len(m1)==len(m2):

    for i in range(len(m1)):
        if len(m1[i]) == len(m2[i]) and len(m1) == len(m2):
            try:
                for j in range(len(m1[i])):
                    ans1.append(m1[i][j] - m2[i][j])
                ans.append(ans1)
                ans1 = []
            except:
                return TypeError('must be an int')
        else:
            return 'must be of same length to add'
    return ans


# TRANSPOSE OF 1D MATRIXES

def transposed1d(m1):
    ans = []
    for i in range(len(m1)):
        ans.append([m1[i]])
    return ans


# TRANSPOSE OF 2D MATRIXES

def transposed2d(m1):
    ans = []
    ans1 = []
    try:
        for i in range(len(m1[0])):
            for j in range(len(m1)):
                ans1.append(m1[j][i])
            ans.append(ans1)
            ans1 = []
        return ans
    except:
        return 'un matched dimention'


# CHECKING ARRAY DIMENTION


