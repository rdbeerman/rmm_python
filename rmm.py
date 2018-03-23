# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(username)s
"""
"""
Created on %(data)s
@title: Robins Magical Module
@description: Module with generally useful functions.
@author: RD Beerman
"""
import numpy as np
import matplotlib.pyplot as plt

"""
    Gaussian takes array and maxval to calculate array with gaussian function
    width is half std dev
"""
def gaussian(array,maxval,center,width): 
    arrayout = []
    for i in range(0,len(array)):
        value = array[i]
        val = maxval*np.exp((-((value-center)**2)/(2*width**2)))
        arrayout.append(val)
    return arrayout

"""
    Same aus gaussian but plots it with argument for label, color and linestyle
"""
def gaussianplot(array,maxval,center,width,label,color,linestyle): 
    arrayout = []
    for i in range(0,len(array)):
        value = array[i]
        val = maxval*np.exp((-((value-center)**2)/(2*width**2)))
        arrayout.append(val)
    plt.plot(array,arrayout,label=label,color=color,linestyle=linestyle)
    plt.legend()
    return

"""
    plot plots x and y automatically with labels
"""
def plot(x,y,label,markertype,markersize,ylabel,xlabel):
    plt.plot(x,y,label=label,marker=markertype,markersize=markersize)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.legend()
    plt.grid()
    return
""""
    Plots a polynomal with order with no extrapolation 
    (between 1st and last value) with arguments for linestyle, label and color
"""
def plotpolyfit(xarray,yarray,order,label,linestyle,color):
    trendlineparams = np.polyfit(xarray,yarray,order)                               #Find best fitting line parameters
    trendline = np.poly1d(trendlineparams)
    xtrend = np.linspace(xarray[0],xarray[len(xarray)-1])
    plt.plot(xtrend,trendline(xtrend),label=label,linestyle=linestyle,color=color)
    plt.legend()
    return
