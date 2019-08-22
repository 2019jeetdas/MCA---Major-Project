# -*- coding: utf-8 -*-
# International Monetary Fund, World Economic Outlook Database, April 2019
# Data Source : https://www.imf.org

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import random

df = pd.read_table("C:/Users/Jeet Das/Desktop/Major Project - Indian Economy/Project ( Section 1-Indian Economy)/Section-1_Data_sheet/indian_GDP.xls",encoding="cp1252")

# converting excel file to csv file 

df.to_csv("C:/Users/Jeet Das/Desktop/Major Project - Indian Economy/Project ( Section 1-Indian Economy)/Section-1_Data_sheet/indian_GDP.csv", encoding='utf-8',index=False)

df1 = df.iloc[0,6:45]
df1 = pd.to_numeric(df1,errors = 'coerce')

df2 = df.iloc[0,44:50]
df2 = pd.to_numeric(df2,errors = 'coerce')
        
year1=(1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,
        1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,
        2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,
        2011,2012,2013,2014,2015,2016,2017,2018,2019)
        
df21 =(6.006,3.476,7.289,3.821,5.254,4.777,3.965,9.628,5.947,5.534,
        1.057,5.48, 4.750,6.659,7.575,7.550,4.050,6.184,8.463,3.975,4.944,
        3.907,7.944,7.849,9.285,9.264,9.801,3.891,8.480,10.260,6.638,5.456,
        6.386,7.410,7.996,8.170,7.168,7.053,7.257) 
# Question – 1 : get row and column numbers 

def data_shape():
    print('\n-------------------------')
    print("Dimension of the data frame = ",df.shape)

# Question – 2 : print column names :

def available_columns():
    print('------------------------\n Column names as follows :')
    print('------------------------\n')
    count = 1
    for col in df.columns: 
        print(count,"-->",col)
        count = count+1
   
# Question - 3 : Indian GDP growth from 1981 to 2019 

def gdp_growth_2019():                    
    y_pos2 = np.arange(len(year1))
    plt.barh(y_pos2,df1,align='center', alpha=0.5)
    plt.yticks(y_pos2,year1)
    plt.xlabel('GDP growth(in %) --->')
    plt.title('[C] Indian GDP growth from 1981 to 2019 (39 years) according to IMF data')
    plt.show()

def estimate_coef(x, y): 
    n = np.size(x)  # size of data set
    mean_x = np.mean(x) 
    mean_y = np.mean(y) 
    xy  = np.sum(y*x) - n*(mean_y)*(mean_x) 
    xx  = np.sum(x*x) - n*(mean_x)*(mean_x)  
    b_1 = xy / xx 
    b_0 = (mean_y) - b_1*(mean_x)
    return(b_0,b_1) 

def gdp_prediction_2025(x,y,b,bm,a): 
    
    # Create perdiction upto 2023
    # Using Equation : y = b_0 + (b_1 * x)
   
    df_2019 = bm + (a * 2019)
    df_2020 = bm + (a * 2020)
    df_2021 = bm + (a * 2021)
    df_2022 = bm + (a * 2022)
    df_2023 = bm + (a * 2023)
    df_2024 = bm + (a * 2024)
    df_2025 = bm + (a * 2025)
    
    df_prediction_upto_2025 =(df_2019,
                              df_2020,df_2021,df_2022,
                              df_2023,df_2024,df_2025 )
                   
    year11=(2019,2020,2021,2022,2023,2024,2025)  
    # plot regression line
          
    plt.plot(x, y, color = "m",marker = "o",label="Actual")  
    y_pred = b[0] + b[1]*x 
    plt.plot(x, y_pred, color = "g",label="Regression line") 
    plt.xlabel('year -- >') 
    plt.ylabel('gdp growth(%) --->')                                  
    
    # plot prediction line
    
    plt.title("GDP prediction from 2020 to 2025 ")
    plt.plot(year11,df_prediction_upto_2025,linestyle="dashed",label="Prediction")
    plt.plot(df2,marker='*',markersize=10,label="Predicted by IMF")
    plt.legend()
    plt.show()
    
    mean_y=np.mean(y)
    
    growth_2019 = (((df_2019)-(mean_y))/(mean_y))*100
    growth_2020 = (((df_2020)-(mean_y))/(mean_y))*100
    growth_2021 = (((df_2021)-(mean_y))/(mean_y))*100
    growth_2022 = (((df_2022)-(mean_y))/(mean_y))*100
    growth_2023 = (((df_2023)-(mean_y))/(mean_y))*100
    growth_2024 = (((df_2024)-(mean_y))/(mean_y))*100
    growth_2025 = (((df_2025)-(mean_y))/(mean_y))*100
    
    print("\n----------------------------------------------------------")
    print("   Predicted Data")
    print("--------------------------------------------------------\n")
    print("GDP growth in 2019 = ",df_2019)
    print("GDP growth in 2020 = ",df_2020)
    print("GDP growth in 2021 = ",df_2021)
    print("GDP growth in 2022 = ",df_2022)
    print("GDP growth in 2023 = ",df_2023)
    print("GDP growth in 2024 = ",df_2024)
    print("GDP growth in 2025 = ",df_2025)
    print("--------------------------------------------------------\n")
    print("   Predicted by IMF ")
    print("--------------------------------------------------------\n")
    print(df2)
    print("\n----------------------------------------------------------")
    print("   Predicted Data(in % )according to mean data")
    print("--------------------------------------------------------\n")
    print("GDP growth in 2019 = ",growth_2019,"%")
    print("GDP growth in 2020 = ",growth_2020,"%")
    print("GDP growth in 2021 = ",growth_2021,"%")
    print("GDP growth in 2022 = ",growth_2022,"%")
    print("GDP growth in 2023 = ",growth_2023,"%")
    print("GDP growth in 2024 = ",growth_2024,"%")
    print("GDP growth in 2025 = ",growth_2025,"%")
    print("--------------------------------------------------------\n")
    
def main_menu():
    print("-----------------------------------------")
    print("    Main menu :")
    print("-----------------------------------------")
    print("[1] Dimension of the availabe data")
    print("[2] Available columns for the data set")
    print("[3] Plot GDP growth upto 2019")
    print("[4] Prediction model upto 2025")
    print("-----------------------------------------")  
    
    
def gdp_main():
    ch = 1
    while (ch == 1):
        main_menu()        
        op = input("enter your option : ")
        op1 = int(op,10)
        
        if op1 == 1:
            data_shape()
        
        elif op1 == 2:    
            available_columns()
            
        elif op1 == 3:
            gdp_growth_2019()
            break
        
        elif op1 == 4:
            x = np.array(year1)
            y = np.array(df21) 
            b = estimate_coef(x,y)
            print("\n----------------------")
            print("Estimated coefficients for area:\n----------------------\n") 
            print("b_0 = {}\nb_1 = {}".format(b[0], b[1])) 
            print("----------------------\n")    
            gdp_prediction_2025(x,y,b,b[0],b[1])
            break
        
        else:
            print("wrong input !!")
        
        #------- exit process design --------   
        
        print("--------------------------------------------") 
        ch1 = input("enter:\n[0] for exit\n[1] for continue : ")
        ch =int(ch1,10)
        print("--------------------------------------------")
                
if __name__ == "__main__": 
	gdp_main()    