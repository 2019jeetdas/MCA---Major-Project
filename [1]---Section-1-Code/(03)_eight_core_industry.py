# -*- coding: utf-8 -*-
#-----(03) data analysis of eight core industry -----

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

df = pd.read_csv ('C:/Users/Jeet Das/Desktop/Major Project - Indian Economy/Project ( Section 1-Indian Economy)/Section-1_Data_sheet/(03)_eight_core_industry.csv',encoding="cp1252")

print("\n------- output data :-----------\n")
print(" Data analysis of eight core industry :")
print("\n-----------------------------------\n")

dfD_2005 = df.iloc[0:9]
dfD_2006 = df.iloc[9:21]
dfD_2007 = df.iloc[21:33]
dfD_2008 = df.iloc[33:45]
dfD_2009 = df.iloc[45:57]
dfD_2010 = df.iloc[57:69]
dfD_2011 = df.iloc[69:81]
dfD_2012 = df.iloc[81:93]
dfD_2013 = df.iloc[93:105]
dfD_2014 = df.iloc[105:117]
dfD_2015 = df.iloc[117:129]
dfD_2016 = df.iloc[129:139]

df_year=(2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016)
avg_year_2005 = sum(dfD_2005['Overall Growth rate'])/9
avg_year_2006 = sum(dfD_2006['Overall Growth rate'])/12
avg_year_2007 = sum(dfD_2007['Overall Growth rate'])/12
avg_year_2008 = sum(dfD_2008['Overall Growth rate'])/12
avg_year_2009 = sum(dfD_2009['Overall Growth rate'])/12
avg_year_2010 = sum(dfD_2010['Overall Growth rate'])/12
avg_year_2011 = sum(dfD_2011['Overall Growth rate'])/12
avg_year_2012 = sum(dfD_2012['Overall Growth rate'])/12
avg_year_2013 = sum(dfD_2013['Overall Growth rate'])/12
avg_year_2014 = sum(dfD_2014['Overall Growth rate'])/12
avg_year_2015 = sum(dfD_2015['Overall Growth rate'])/12
avg_year_2016 = sum(dfD_2016['Overall Growth rate'])/10
    
df_avg_data =(avg_year_2005,avg_year_2006,avg_year_2007,avg_year_2008,
              avg_year_2009,avg_year_2010,avg_year_2011,avg_year_2012,
              avg_year_2013,avg_year_2014,avg_year_2015,avg_year_2016)
    

# Question – A : get row and column numbers 

def dimensions():
    print('---------------------------------------------')
    print("Dimension of the data frame = ",df.shape)
    print('---------------------------------------------')

# Question – B : print column names :

def column_names():
    print('------------------------\n Column names as follows :')
    print('------------------------\n')
    count = 1
    for col in df.columns: 
        print(count,"-->",col)
        count = count+1
    print("\n-----------------------------\n")


# Question – C : print available months year wise (2005 to 2016) :

def available_months():
    
    dfD_2005 = df.iloc[0:9]
    print(dfD_2005['Months/Years'])

    dfD_2006 = df.iloc[9:21]
    print(dfD_2006['Months/Years'])

    dfD_2007 = df.iloc[21:33]
    print(dfD_2007['Months/Years'])

    dfD_2008 = df.iloc[33:45]
    print(dfD_2008['Months/Years'])

    dfD_2009 = df.iloc[45:57]
    print(dfD_2009['Months/Years'])
    
    dfD_2010 = df.iloc[57:69]
    print(dfD_2010['Months/Years'])

    dfD_2011 = df.iloc[69:81]
    print(dfD_2011['Months/Years'])

    dfD_2012 = df.iloc[81:93]
    print(dfD_2012['Months/Years'])

    dfD_2013 = df.iloc[93:105]
    print(dfD_2013['Months/Years'])

    dfD_2014 = df.iloc[105:117]
    print(dfD_2014['Months/Years'])

    dfD_2015 = df.iloc[117:129]
    print(dfD_2015['Months/Years'])

    dfD_2016 = df.iloc[129:139]
    print(dfD_2016['Months/Years'])

# Question - D : data analysis year wise

# [D_2005] year - 2005

def year_2005():
    print("\n---------------------------------------------")
    print(dfD_2005[['Months/Years','Growth of Coal (%)']])
    print("---------------------------------------------")
    print(dfD_2005[['Months/Years','Growth of Crude Oil (%)']])
    print("---------------------------------------------")
    print(dfD_2005[['Months/Years','Growth of Natural Gas (%)']])
    print("---------------------------------------------")
    print(dfD_2005[['Months/Years','Growth of Petroleum Refinery Products (%)']])
    print("---------------------------------------------")
    print(dfD_2005[['Months/Years','Growth of Fertilizers (%)']])
    print("---------------------------------------------")
    print(dfD_2005[['Months/Years','Growth of Steel (%)']])
    print("---------------------------------------------")
    print(dfD_2005[['Months/Years','Growth of Cement (%)']])
    print("---------------------------------------------")
    print(dfD_2005[['Months/Years','Growth of Electricity (%)']])
    print("---------------------------------------------")
    
    plt.title('Question - D_2005 : Year 2005')
    plt.xlabel("month --- >")
    plt.ylabel("growth --- >")
    
    plt.plot(dfD_2005['Growth of Coal (%)'],
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="[1]coal")

    plt.plot(dfD_2005['Growth of Crude Oil (%)'],
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="[2]crude oil")

    plt.plot(dfD_2005['Growth of Natural Gas (%)'],
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="[3]natural gas")
            
    plt.plot(dfD_2005['Growth of Petroleum Refinery Products (%)'],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[4]Petroleum Refinery Products")
            
    plt.plot(dfD_2005['Growth of Fertilizers (%)'],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[5]Fertilizers")
            
    plt.plot(dfD_2005['Growth of Steel (%)'],
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[6]Steel")

    plt.plot(dfD_2005['Growth of Cement (%)'],
            marker='X',
            markersize=10,
            linestyle='dashed',
            label="[7]Cement")

    plt.plot(dfD_2005['Growth of Electricity (%)'],
            marker="o",
            markersize=10,
            linestyle='dashed',
            label="[8]Electricity")

    plt.legend()
    plt.show()

# [D_2006] year - 2006

def year_2006():
    print("\n---------------------------------------------")
    print(dfD_2006[['Months/Years','Growth of Coal (%)']])
    print("---------------------------------------------")
    print(dfD_2006[['Months/Years','Growth of Crude Oil (%)']])
    print("---------------------------------------------")
    print(dfD_2006[['Months/Years','Growth of Natural Gas (%)']])
    print("---------------------------------------------")
    print(dfD_2006[['Months/Years','Growth of Petroleum Refinery Products (%)']])
    print("---------------------------------------------")
    print(dfD_2006[['Months/Years','Growth of Fertilizers (%)']])
    print("---------------------------------------------")
    print(dfD_2006[['Months/Years','Growth of Steel (%)']])
    print("---------------------------------------------")
    print(dfD_2006[['Months/Years','Growth of Cement (%)']])
    print("---------------------------------------------")
    print(dfD_2006[['Months/Years','Growth of Electricity (%)']])
    print("---------------------------------------------")
    
    plt.title('Question - D_2006 : Year 2006')
    plt.xlabel("month --- >")
    plt.ylabel("growth --- >")
    
    plt.plot(dfD_2006['Growth of Coal (%)'],
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="[1]coal")

    plt.plot(dfD_2006['Growth of Crude Oil (%)'],
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="[2]crude oil")

    plt.plot(dfD_2006['Growth of Natural Gas (%)'],
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="[3]natural gas")
            
    plt.plot(dfD_2006['Growth of Petroleum Refinery Products (%)'],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[4]Petroleum Refinery Products")
            
    plt.plot(dfD_2006['Growth of Fertilizers (%)'],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[5]Fertilizers")
            
    plt.plot(dfD_2006['Growth of Steel (%)'],
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[6]Steel")

    plt.plot(dfD_2006['Growth of Cement (%)'],
            marker='X',
            markersize=10,
            linestyle='dashed',
            label="[7]Cement")

    plt.plot(dfD_2006['Growth of Electricity (%)'],
            marker="o",
            markersize=10,
            linestyle='dashed',
            label="[8]Electricity")

    plt.legend()
    plt.show()

# [D_2007] year - 2007

def year_2007():
    print("\n---------------------------------------------")
    print(dfD_2007[['Months/Years','Growth of Coal (%)']])
    print("---------------------------------------------")
    print(dfD_2007[['Months/Years','Growth of Crude Oil (%)']])
    print("---------------------------------------------")
    print(dfD_2007[['Months/Years','Growth of Natural Gas (%)']])
    print("---------------------------------------------")
    print(dfD_2007[['Months/Years','Growth of Petroleum Refinery Products (%)']])
    print("---------------------------------------------")
    print(dfD_2007[['Months/Years','Growth of Fertilizers (%)']])
    print("---------------------------------------------")
    print(dfD_2007[['Months/Years','Growth of Steel (%)']])
    print("---------------------------------------------")
    print(dfD_2007[['Months/Years','Growth of Cement (%)']])
    print("---------------------------------------------")
    print(dfD_2007[['Months/Years','Growth of Electricity (%)']])
    print("---------------------------------------------")
    plt.title('Question - D_2007 : Year 2007')
    plt.xlabel("month --- >")
    plt.ylabel("growth --- >")
    
    plt.plot(dfD_2007['Growth of Coal (%)'],
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="[1]coal")

    plt.plot(dfD_2007['Growth of Crude Oil (%)'],
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="[2]crude oil")

    plt.plot(dfD_2007['Growth of Natural Gas (%)'],
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="[3]natural gas")
            
    plt.plot(dfD_2007['Growth of Petroleum Refinery Products (%)'],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[4]Petroleum Refinery Products")
            
    plt.plot(dfD_2007['Growth of Fertilizers (%)'],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[5]Fertilizers")
            
    plt.plot(dfD_2007['Growth of Steel (%)'],
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[6]Steel")

    plt.plot(dfD_2007['Growth of Cement (%)'],
            marker='X',
            markersize=10,
            linestyle='dashed',
            label="[7]Cement")

    plt.plot(dfD_2007['Growth of Electricity (%)'],
            marker="o",
            markersize=10,
            linestyle='dashed',
            label="[8]Electricity")

    plt.legend()
    plt.show()


# [D_2008] year - 2008

def year_2008():
    print("\n---------------------------------------------")
    print(dfD_2008[['Months/Years','Growth of Coal (%)']])
    print("---------------------------------------------")
    print(dfD_2008[['Months/Years','Growth of Crude Oil (%)']])
    print("---------------------------------------------")
    print(dfD_2008[['Months/Years','Growth of Natural Gas (%)']])
    print("---------------------------------------------")
    print(dfD_2008[['Months/Years','Growth of Petroleum Refinery Products (%)']])
    print("---------------------------------------------")
    print(dfD_2008[['Months/Years','Growth of Fertilizers (%)']])
    print("---------------------------------------------")
    print(dfD_2008[['Months/Years','Growth of Steel (%)']])
    print("---------------------------------------------")
    print(dfD_2008[['Months/Years','Growth of Cement (%)']])
    print("---------------------------------------------")
    print(dfD_2008[['Months/Years','Growth of Electricity (%)']])
    print("---------------------------------------------")
    plt.title('Question - D_2008 : Year 2008')
    plt.xlabel("month --- >")
    plt.ylabel("growth --- >")
    
    plt.plot(dfD_2008['Growth of Coal (%)'],
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="[1]coal")

    plt.plot(dfD_2008['Growth of Crude Oil (%)'],
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="[2]crude oil")

    plt.plot(dfD_2008['Growth of Natural Gas (%)'],
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="[3]natural gas")
            
    plt.plot(dfD_2008['Growth of Petroleum Refinery Products (%)'],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[4]Petroleum Refinery Products")
            
    plt.plot(dfD_2008['Growth of Fertilizers (%)'],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[5]Fertilizers")
            
    plt.plot(dfD_2008['Growth of Steel (%)'],
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[6]Steel")

    plt.plot(dfD_2008['Growth of Cement (%)'],
            marker='X',
            markersize=10,
            linestyle='dashed',
            label="[7]Cement")

    plt.plot(dfD_2008['Growth of Electricity (%)'],
            marker="o",
            markersize=10,
            linestyle='dashed',
            label="[8]Electricity")

    plt.legend()
    plt.show()

# [D_2009] year - 2009

def year_2009():
    print("\n---------------------------------------------")
    print(dfD_2009[['Months/Years','Growth of Coal (%)']])
    print("---------------------------------------------")
    print(dfD_2009[['Months/Years','Growth of Crude Oil (%)']])
    print("---------------------------------------------")
    print(dfD_2009[['Months/Years','Growth of Natural Gas (%)']])
    print("---------------------------------------------")
    print(dfD_2009[['Months/Years','Growth of Petroleum Refinery Products (%)']])
    print("---------------------------------------------")
    print(dfD_2009[['Months/Years','Growth of Fertilizers (%)']])
    print("---------------------------------------------")
    print(dfD_2009[['Months/Years','Growth of Steel (%)']])
    print("---------------------------------------------")
    print(dfD_2009[['Months/Years','Growth of Cement (%)']])
    print("---------------------------------------------")
    print(dfD_2009[['Months/Years','Growth of Electricity (%)']])
    print("---------------------------------------------")
    plt.title('Question - D_2009 : Year 2009')
    plt.xlabel("month --- >")
    plt.ylabel("growth --- >")
    
    plt.plot(dfD_2009['Growth of Coal (%)'],
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="[1]coal")

    plt.plot(dfD_2009['Growth of Crude Oil (%)'],
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="[2]crude oil")

    plt.plot(dfD_2009['Growth of Natural Gas (%)'],
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="[3]natural gas")
            
    plt.plot(dfD_2009['Growth of Petroleum Refinery Products (%)'],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[4]Petroleum Refinery Products")
            
    plt.plot(dfD_2009['Growth of Fertilizers (%)'],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[5]Fertilizers")
            
    plt.plot(dfD_2009['Growth of Steel (%)'],
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[6]Steel")

    plt.plot(dfD_2009['Growth of Cement (%)'],
            marker='X',
            markersize=10,
            linestyle='dashed',
            label="[7]Cement")

    plt.plot(dfD_2009['Growth of Electricity (%)'],
            marker="o",
            markersize=10,
            linestyle='dashed',
            label="[8]Electricity")

    plt.legend()
    plt.show()

# [D_2010] year - 2010

def year_2010():
    print("\n---------------------------------------------")
    print(dfD_2010[['Months/Years','Growth of Coal (%)']])
    print("---------------------------------------------")
    print(dfD_2010[['Months/Years','Growth of Crude Oil (%)']])
    print("---------------------------------------------")
    print(dfD_2010[['Months/Years','Growth of Natural Gas (%)']])
    print("---------------------------------------------")
    print(dfD_2010[['Months/Years','Growth of Petroleum Refinery Products (%)']])
    print("---------------------------------------------")
    print(dfD_2010[['Months/Years','Growth of Fertilizers (%)']])
    print("---------------------------------------------")
    print(dfD_2010[['Months/Years','Growth of Steel (%)']])
    print("---------------------------------------------")
    print(dfD_2010[['Months/Years','Growth of Cement (%)']])
    print("---------------------------------------------")
    print(dfD_2010[['Months/Years','Growth of Electricity (%)']])
    print("---------------------------------------------")
    plt.title('Question - D_2010 : Year 2010')
    plt.xlabel("month --- >")
    plt.ylabel("growth --- >")
    
    plt.plot(dfD_2010['Growth of Coal (%)'],
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="[1]coal")

    plt.plot(dfD_2010['Growth of Crude Oil (%)'],
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="[2]crude oil")

    plt.plot(dfD_2010['Growth of Natural Gas (%)'],
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="[3]natural gas")
            
    plt.plot(dfD_2010['Growth of Petroleum Refinery Products (%)'],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[4]Petroleum Refinery Products")
            
    plt.plot(dfD_2010['Growth of Fertilizers (%)'],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[5]Fertilizers")
            
    plt.plot(dfD_2010['Growth of Steel (%)'],
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[6]Steel")

    plt.plot(dfD_2010['Growth of Cement (%)'],
            marker='X',
            markersize=10,
            linestyle='dashed',
            label="[7]Cement")

    plt.plot(dfD_2010['Growth of Electricity (%)'],
            marker="o",
            markersize=10,
            linestyle='dashed',
            label="[8]Electricity")

    plt.legend()
    plt.show()

# [D_2011] year - 2011

def year_2011():
    print("\n---------------------------------------------")
    print(dfD_2011[['Months/Years','Growth of Coal (%)']])
    print("---------------------------------------------")
    print(dfD_2011[['Months/Years','Growth of Crude Oil (%)']])
    print("---------------------------------------------")
    print(dfD_2011[['Months/Years','Growth of Natural Gas (%)']])
    print("---------------------------------------------")
    print(dfD_2011[['Months/Years','Growth of Petroleum Refinery Products (%)']])
    print("---------------------------------------------")
    print(dfD_2011[['Months/Years','Growth of Fertilizers (%)']])
    print("---------------------------------------------")
    print(dfD_2011[['Months/Years','Growth of Steel (%)']])
    print("---------------------------------------------")
    print(dfD_2011[['Months/Years','Growth of Cement (%)']])
    print("---------------------------------------------")
    print(dfD_2011[['Months/Years','Growth of Electricity (%)']])
    print("---------------------------------------------")
    plt.title('Question - D_2011 : Year 2011')
    plt.xlabel("month --- >")
    plt.ylabel("growth --- >")
    
    plt.plot(dfD_2011['Growth of Coal (%)'],
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="[1]coal")

    plt.plot(dfD_2011['Growth of Crude Oil (%)'],
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="[2]crude oil")

    plt.plot(dfD_2011['Growth of Natural Gas (%)'],
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="[3]natural gas")
            
    plt.plot(dfD_2011['Growth of Petroleum Refinery Products (%)'],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[4]Petroleum Refinery Products")
            
    plt.plot(dfD_2011['Growth of Fertilizers (%)'],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[5]Fertilizers")
            
    plt.plot(dfD_2011['Growth of Steel (%)'],
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[6]Steel")

    plt.plot(dfD_2011['Growth of Cement (%)'],
            marker='X',
            markersize=10,
            linestyle='dashed',
            label="[7]Cement")

    plt.plot(dfD_2011['Growth of Electricity (%)'],
            marker="o",
            markersize=10,
            linestyle='dashed',
            label="[8]Electricity")

    plt.legend()
    plt.show()

# [D_2012] year - 2012

def year_2012():
    print("\n---------------------------------------------")
    print(dfD_2012[['Months/Years','Growth of Coal (%)']])
    print("---------------------------------------------")
    print(dfD_2012[['Months/Years','Growth of Crude Oil (%)']])
    print("---------------------------------------------")
    print(dfD_2012[['Months/Years','Growth of Natural Gas (%)']])
    print("---------------------------------------------")
    print(dfD_2012[['Months/Years','Growth of Petroleum Refinery Products (%)']])
    print("---------------------------------------------")
    print(dfD_2012[['Months/Years','Growth of Fertilizers (%)']])
    print("---------------------------------------------")
    print(dfD_2012[['Months/Years','Growth of Steel (%)']])
    print("---------------------------------------------")
    print(dfD_2012[['Months/Years','Growth of Cement (%)']])
    print("---------------------------------------------")
    print(dfD_2012[['Months/Years','Growth of Electricity (%)']])
    print("---------------------------------------------")
    plt.title('Question - D_2012 : Year 2012')
    plt.xlabel("month --- >")
    plt.ylabel("growth --- >")
    
    plt.plot(dfD_2012['Growth of Coal (%)'],
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="[1]coal")

    plt.plot(dfD_2012['Growth of Crude Oil (%)'],
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="[2]crude oil")

    plt.plot(dfD_2012['Growth of Natural Gas (%)'],
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="[3]natural gas")
            
    plt.plot(dfD_2012['Growth of Petroleum Refinery Products (%)'],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[4]Petroleum Refinery Products")
            
    plt.plot(dfD_2012['Growth of Fertilizers (%)'],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[5]Fertilizers")
            
    plt.plot(dfD_2012['Growth of Steel (%)'],
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[6]Steel")

    plt.plot(dfD_2012['Growth of Cement (%)'],
            marker='X',
            markersize=10,
            linestyle='dashed',
            label="[7]Cement")

    plt.plot(dfD_2012['Growth of Electricity (%)'],
            marker="o",
            markersize=10,
            linestyle='dashed',
            label="[8]Electricity")

    plt.legend()
    plt.show()

# [D_2013] year - 2013

def year_2013():
    print("\n---------------------------------------------")
    print(dfD_2013[['Months/Years','Growth of Coal (%)']])
    print("---------------------------------------------")
    print(dfD_2013[['Months/Years','Growth of Crude Oil (%)']])
    print("---------------------------------------------")
    print(dfD_2013[['Months/Years','Growth of Natural Gas (%)']])
    print("---------------------------------------------")
    print(dfD_2013[['Months/Years','Growth of Petroleum Refinery Products (%)']])
    print("---------------------------------------------")
    print(dfD_2013[['Months/Years','Growth of Fertilizers (%)']])
    print("---------------------------------------------")
    print(dfD_2013[['Months/Years','Growth of Steel (%)']])
    print("---------------------------------------------")
    print(dfD_2013[['Months/Years','Growth of Cement (%)']])
    print("---------------------------------------------")
    print(dfD_2013[['Months/Years','Growth of Electricity (%)']])
    print("---------------------------------------------")
    plt.title('Question - D_2013 : Year 2013')
    plt.xlabel("month --- >")
    plt.ylabel("growth --- >")
    
    plt.plot(dfD_2013['Growth of Coal (%)'],
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="[1]coal")

    plt.plot(dfD_2013['Growth of Crude Oil (%)'],
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="[2]crude oil")

    plt.plot(dfD_2013['Growth of Natural Gas (%)'],
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="[3]natural gas")
            
    plt.plot(dfD_2013['Growth of Petroleum Refinery Products (%)'],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[4]Petroleum Refinery Products")
            
    plt.plot(dfD_2013['Growth of Fertilizers (%)'],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[5]Fertilizers")
            
    plt.plot(dfD_2013['Growth of Steel (%)'],
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[6]Steel")

    plt.plot(dfD_2013['Growth of Cement (%)'],
            marker='X',
            markersize=10,
            linestyle='dashed',
            label="[7]Cement")

    plt.plot(dfD_2013['Growth of Electricity (%)'],
            marker="o",
            markersize=10,
            linestyle='dashed',
            label="[8]Electricity")

    plt.legend()
    plt.show()

# [D_2014] year - 2014

def year_2014():
    print("\n---------------------------------------------")
    print(dfD_2014[['Months/Years','Growth of Coal (%)']])
    print("---------------------------------------------")
    print(dfD_2014[['Months/Years','Growth of Crude Oil (%)']])
    print("---------------------------------------------")
    print(dfD_2014[['Months/Years','Growth of Natural Gas (%)']])
    print("---------------------------------------------")
    print(dfD_2014[['Months/Years','Growth of Petroleum Refinery Products (%)']])
    print("---------------------------------------------")
    print(dfD_2014[['Months/Years','Growth of Fertilizers (%)']])
    print("---------------------------------------------")
    print(dfD_2014[['Months/Years','Growth of Steel (%)']])
    print("---------------------------------------------")
    print(dfD_2014[['Months/Years','Growth of Cement (%)']])
    print("---------------------------------------------")
    print(dfD_2014[['Months/Years','Growth of Electricity (%)']])
    print("---------------------------------------------")
    plt.title('Question - D_2014 : Year 2014')
    plt.xlabel("month --- >")
    plt.ylabel("growth --- >")
    
    plt.plot(dfD_2014['Growth of Coal (%)'],
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="[1]coal")

    plt.plot(dfD_2014['Growth of Crude Oil (%)'],
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="[2]crude oil")

    plt.plot(dfD_2014['Growth of Natural Gas (%)'],
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="[3]natural gas")
            
    plt.plot(dfD_2014['Growth of Petroleum Refinery Products (%)'],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[4]Petroleum Refinery Products")
            
    plt.plot(dfD_2014['Growth of Fertilizers (%)'],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[5]Fertilizers")
            
    plt.plot(dfD_2014['Growth of Steel (%)'],
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[6]Steel")

    plt.plot(dfD_2014['Growth of Cement (%)'],
            marker='X',
            markersize=10,
            linestyle='dashed',
            label="[7]Cement")

    plt.plot(dfD_2014['Growth of Electricity (%)'],
            marker="o",
            markersize=10,
            linestyle='dashed',
            label="[8]Electricity")

    plt.legend()
    plt.show()

# [D_2015] year - 2015

def year_2015():
    print("\n---------------------------------------------")
    print(dfD_2015[['Months/Years','Growth of Coal (%)']])
    print("---------------------------------------------")
    print(dfD_2015[['Months/Years','Growth of Crude Oil (%)']])
    print("---------------------------------------------")
    print(dfD_2015[['Months/Years','Growth of Natural Gas (%)']])
    print("---------------------------------------------")
    print(dfD_2015[['Months/Years','Growth of Petroleum Refinery Products (%)']])
    print("---------------------------------------------")
    print(dfD_2015[['Months/Years','Growth of Fertilizers (%)']])
    print("---------------------------------------------")
    print(dfD_2015[['Months/Years','Growth of Steel (%)']])
    print("---------------------------------------------")
    print(dfD_2015[['Months/Years','Growth of Cement (%)']])
    print("---------------------------------------------")
    print(dfD_2015[['Months/Years','Growth of Electricity (%)']])
    print("---------------------------------------------")
    plt.title('Question - D_2015 : Year 2015')
    plt.xlabel("month --- >")
    plt.ylabel("growth --- >")
    
    plt.plot(dfD_2015['Growth of Coal (%)'],
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="[1]coal")

    plt.plot(dfD_2015['Growth of Crude Oil (%)'],
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="[2]crude oil")

    plt.plot(dfD_2015['Growth of Natural Gas (%)'],
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="[3]natural gas")
            
    plt.plot(dfD_2015['Growth of Petroleum Refinery Products (%)'],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[4]Petroleum Refinery Products")
            
    plt.plot(dfD_2015['Growth of Fertilizers (%)'],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[5]Fertilizers")
            
    plt.plot(dfD_2015['Growth of Steel (%)'],
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[6]Steel")

    plt.plot(dfD_2015['Growth of Cement (%)'],
            marker='X',
            markersize=10,
            linestyle='dashed',
            label="[7]Cement")

    plt.plot(dfD_2015['Growth of Electricity (%)'],
            marker="o",
            markersize=10,
            linestyle='dashed',
            label="[8]Electricity")

    plt.legend()
    plt.show()


# [D_2016] year - 2016

def year_2016():
    print("\n---------------------------------------------")
    print(dfD_2016[['Months/Years','Growth of Coal (%)']])
    print("---------------------------------------------")
    print(dfD_2016[['Months/Years','Growth of Crude Oil (%)']])
    print("---------------------------------------------")
    print(dfD_2016[['Months/Years','Growth of Natural Gas (%)']])
    print("---------------------------------------------")
    print(dfD_2016[['Months/Years','Growth of Petroleum Refinery Products (%)']])
    print("---------------------------------------------")
    print(dfD_2016[['Months/Years','Growth of Fertilizers (%)']])
    print("---------------------------------------------")
    print(dfD_2016[['Months/Years','Growth of Steel (%)']])
    print("---------------------------------------------")
    print(dfD_2016[['Months/Years','Growth of Cement (%)']])
    print("---------------------------------------------")
    print(dfD_2016[['Months/Years','Growth of Electricity (%)']])
    print("---------------------------------------------")
    plt.title('Question - D_2016 : Year 2016')
    plt.xlabel("month --- >")
    plt.ylabel("growth --- >")
    
    plt.plot(dfD_2016['Growth of Coal (%)'],
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="[1]coal")

    plt.plot(dfD_2016['Growth of Crude Oil (%)'],
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="[2]crude oil")

    plt.plot(dfD_2016['Growth of Natural Gas (%)'],
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="[3]natural gas")
            
    plt.plot(dfD_2016['Growth of Petroleum Refinery Products (%)'],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[4]Petroleum Refinery Products")
            
    plt.plot(dfD_2016['Growth of Fertilizers (%)'],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[5]Fertilizers")
            
    plt.plot(dfD_2016['Growth of Steel (%)'],
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[6]Steel")

    plt.plot(dfD_2016['Growth of Cement (%)'],
            marker='X',
            markersize=10,
            linestyle='dashed',
            label="[7]Cement")

    plt.plot(dfD_2016['Growth of Electricity (%)'],
            marker="o",
            markersize=10,
            linestyle='dashed',
            label="[8]Electricity")

    plt.legend()
    plt.show()

# Question - F : data analysis 2005-06(Apr-Mar) to 2016-17(Apr-Mar)

def data_2005_06_2016_17():
    
    dfF = df.iloc[139:]
    print("\n---------------------------------------------")
    print(dfF[['Months/Years','Growth of Coal (%)']])
    print("---------------------------------------------")
    print(dfF[['Months/Years','Growth of Crude Oil (%)']])
    print("---------------------------------------------")
    print(dfF[['Months/Years','Growth of Natural Gas (%)']])
    print("---------------------------------------------")
    print(dfF[['Months/Years','Growth of Petroleum Refinery Products (%)']])
    print("---------------------------------------------")
    print(dfF[['Months/Years','Growth of Fertilizers (%)']])
    print("---------------------------------------------")
    print(dfF[['Months/Years','Growth of Steel (%)']])
    print("---------------------------------------------")
    print(dfF[['Months/Years','Growth of Cement (%)']])
    print("---------------------------------------------")
    print(dfF[['Months/Years','Growth of Electricity (%)']])
    print("---------------------------------------------")

    plt.title('Question - F : Data Analysis 2005-06(Apr-Mar) to 2016-17(Apr-Mar)')

    plt.plot(dfF['Growth of Coal (%)'],label="[1]coal")
    plt.plot(dfF['Growth of Crude Oil (%)'],label="[2]crude oil")
    plt.plot(dfF['Growth of Natural Gas (%)'],label="[3]natural gas")
    plt.plot(dfF['Growth of Petroleum Refinery Products (%)'],label="[4]Petroleum Refinery Products")
    plt.plot(dfF['Growth of Fertilizers (%)'],label="[5]Fertilizers")
    plt.plot(dfF['Growth of Steel (%)'],label="[6]Steel")
    plt.plot(dfF['Growth of Cement (%)'],label="[7]Cement")
    plt.plot(dfF['Growth of Electricity (%)'],label="[8]Electricity")

    plt.legend()
    plt.show()

   
#---- Production prediction model -----

def estimate_coef1(x, y): 
	
	n = np.size(x)  # size of data set
	mean_x = np.mean(x) 
	mean_y = np.mean(y) 
	xy  = np.sum(y*x) - n*(mean_y)*(mean_x) 
	xx  = np.sum(x*x) - n*(mean_x)*(mean_x)  
	b_1 = xy / xx 
	b_0 = (mean_y) - b_1*(mean_x)
	return(b_0,b_1) 

def prediction_2025(x,y,b,bm,a): 
    
    # Create perdiction upto 2025
    # Using Equation : y = b_0 + (b_1 * x)
   
    
    avg_year_2017 = bm + (a * 2017)
    avg_year_2018 = bm + (a * 2018)
    avg_year_2019 = bm + (a * 2019)
    avg_year_2020 = bm + (a * 2020)
    avg_year_2021 = bm + (a * 2021)
    avg_year_2022 = bm + (a * 2022)
    avg_year_2023 = bm + (a * 2023)
    avg_year_2024 = bm + (a * 2024)
    avg_year_2025 = bm + (a * 2025)
    
    avg_year_2005_2023 =(avg_year_2016,
                            avg_year_2017,avg_year_2018,avg_year_2019,
                            avg_year_2020,avg_year_2021,avg_year_2022,
                            avg_year_2023,avg_year_2024,avg_year_2025 )
                                  
    df_year1 = (2016,2017,int(2018),2019,2020,
                2021,2022,2023,2024,2025)
    
    # plot regression line
          
    plt.plot(df_year,df_avg_data, color = "m",marker = "o",label="Actual Growth")  
    y_pred = b[0] + b[1]*x 
    plt.plot(x,y_pred, color = "g",label="Regression line") 
    plt.xlabel('year -- >') 
    plt.ylabel('growth --->')                                  
    
    # plot prediction line
    
    plt.title("Prediction for industry growth from 2011 to 2025 ")
    plt.plot(df_year1,avg_year_2005_2023,linestyle="dashed",label="Predicted Growth")
    plt.legend()
    plt.show()
    
    mean_y = np.mean(y)
    
    growth_2017 = (((avg_year_2017)-(mean_y))/(mean_y))*100
    growth_2018 = (((avg_year_2018)-(mean_y))/(mean_y))*100
    growth_2019 = (((avg_year_2019)-(mean_y))/(mean_y))*100
    growth_2020 = (((avg_year_2020)-(mean_y))/(mean_y))*100
    growth_2021 = (((avg_year_2021)-(mean_y))/(mean_y))*100
    growth_2022 = (((avg_year_2022)-(mean_y))/(mean_y))*100
    growth_2023 = (((avg_year_2023)-(mean_y))/(mean_y))*100
    growth_2024 = (((avg_year_2024)-(mean_y))/(mean_y))*100
    growth_2025 = (((avg_year_2025)-(mean_y))/(mean_y))*100
    
    print("\n----------------------------------------------------------")
    print("growth according to prediction model")
    print("--------------------------------------------------------\n")
    print("growth in 2017 = ",growth_2017,"%")
    print("growth in 2018 = ",growth_2018,"%")
    print("growth in 2019 = ",growth_2019,"%")
    print("growth in 2020 = ",growth_2020,"%")
    print("growth in 2021 = ",growth_2021,"%")
    print("growth in 2022 = ",growth_2022,"%")
    print("growth in 2023 = ",growth_2023,"%")
    print("growth in 2024 = ",growth_2024,"%")
    print("growth in 2025 = ",growth_2025,"%")
    print("--------------------------------------------------------\n")


def industry_main():
    ch = 1
    while (ch == 1):
        print("-----------------------------------------")
        print("\tMain menu (Core Industry  Data Aanlysis) :")
        print("-----------------------------------------\n")
        print("[1] Print dimension of the data file")
        print("[2] Print column names of the data file")
        print("[3] print available months year wise (2005 to 2016)")
        print("[4] Print and plot year 2005")
        print("[5] Print and plot year 2006")
        print("[6] Print and plot year 2007")
        print("[7] Print and plot year 2008")
        print("[8] Print and plot year 2009")
        print("[9] Print and plot year 2010")
        print("[10] Print and plot year 2011")
        print("[11] Print and plot year 2012")
        print("[12] Print and plot year 2013")
        print("[13] Print and plot year 2014")
        print("[14] Print and plot year 2015")
        print("[15] Print and plot year 2016")
        print("[16] Print & Plot Data 2005-06(Apr-Mar) to 2016-17(Apr-Oct)")
        print("[17] Overall growth 2005 to 2016")
        print("---------------------------------------")

        op = input("enter your option : ")
        op1 = int(op,10)

        if op1 == 1:
            dimensions()
            
        elif op1 == 2: 
            column_names()
         
        elif op1 == 3:
            available_months()
            
        elif op1 == 4:
            year_2005()
            break
        
        elif op1 == 5:
            year_2006()
            break
        
        elif op1 == 6:
            year_2007()
            break
        
        elif op1 == 7:
            year_2008()
            break
        
        elif op1 == 8:
            year_2009()
            break
        
        elif op1 == 9:
            year_2010()
            break
        
        elif op1 == 10:
            year_2011()
            break
        
        elif op1 == 11:
            year_2012()
            break
        
        elif op1 == 12:
            year_2013()
            break
        
        elif op1 == 13:
            year_2014()
            break
        
        elif op1 == 14:
            year_2015()
            break
        
        elif op1 == 15:
            year_2016()
            break
                                                                                                                                                               
        elif op1 == 16:
            data_2005_06_2016_17()
            break
             
        elif op1 == 17:
            x = np.array(df_year)
            y = np.array(df_avg_data) 
            b = estimate_coef1(x, y)
            print("\n----------------------")
            print("Estimated coefficients for area:\n----------------------\n") 
            print("b_0 = {}\nb_1 = {}".format(b[0], b[1])) 
            print("----------------------\n")    
            prediction_2025(x,y,b,b[0],b[1])
            break 
                
        else:
            print("wrong input !!")

        #------- exit process design -------- 
    
        ch1 = input("enter:\n[0] for exit\n[1] for continue : ")
        ch =int(ch1,10)

if __name__ == "__main__": 
          industry_main()
