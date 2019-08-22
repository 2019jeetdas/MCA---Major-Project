# -*- coding: utf-8 -*-
# prediction for bank,railway,legal affairs

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df_bank = pd.read_csv ('C:/Users/Jeet Das/Desktop/Major Project - Indian Economy/Project ( Section 2-Employment Growth)/Section-2_Data_Sheet/(1)_bank_employee.csv',encoding="cp1252")
df_rail = pd.read_csv ('C:/Users/Jeet Das/Desktop/Major Project - Indian Economy/Project ( Section 2-Employment Growth)/Section-2_Data_Sheet/(2)_railway_employee.csv',encoding="cp1252")
df_legal= pd.read_csv ('C:/Users/Jeet Das/Desktop/Major Project - Indian Economy/Project ( Section 2-Employment Growth)/Section-2_Data_Sheet/(4.1)_legal.csv',encoding="cp1252")

# Bank employment data
bank_year = df_bank.iloc[:,0]
df11 = df_bank.iloc[:,[3,4,6,8,9]]
df21 = df11.sum(axis =1, skipna = True)

# Railways employment data
rail_year = [2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015]
df_rail_data=df_rail.iloc[:,[0,20]]
df_rail_1 = df_rail.iloc[:,20]

# legal affiars employment data
legal_all_year = df_legal.iloc[:,[0,2]]
legal_data = legal_all_year.iloc[[2,5,8,11,14,17,20,23,26],]
print(legal_data)
legal_year = [2008,2009,2010,2011,2012,2013,2014,2015,2016]
legal_data_1 = legal_data.iloc[:,1]


# Question – 1 : get row and column numbers 

def data_shape():
    
    print("Dimension of Bank data = ",df_bank.shape)
    print("Dimension of Railway data = ",df_rail.shape)
    print("Dimension of Legal Affiars data = ",df_legal.shape)

# Question – 2 : print column names :

def available_columns():
    
    print('------------------------\n Column names for banking sector :')
    print('------------------------\n')
    count = 1
    for col in df_bank.columns: 
        print(count,"-->",col)
        count = count+1
    print('\n------------------------\n Column names for railway sector :')
    print('------------------------\n')
    count = 1
    for col in df_rail.columns: 
        print(count,"-->",col)
        count = count+1
    
    print('\n------------------------\n Column names for Legal sector :')
    print('------------------------\n')
    count = 1
    for col in df_legal.columns: 
        print(count,"-->",col)
        count = count+1

def estimate_coef(x, y): 
    
    n = np.size(x)  # size of data set
    mean_x = np.mean(x) 
    mean_y = np.mean(y) 
    xy  = np.sum(y*x) - n*(mean_y)*(mean_x) 
    xx  = np.sum(x*x) - n*(mean_x)*(mean_x)  
    b_1 = xy / xx 
    b_0 = (mean_y) - b_1*(mean_x)
    return(b_0,b_1) 

def banking_prediction():
    
    print('\n---: Bank employment details :---\n')
    df_total_bank = pd.DataFrame(list(zip(bank_year,df21)),columns =['Year','No. of Employee'])
    print(df_total_bank) 

def bank_prediction_2025(x,y,b,bm,a): 
    
    # Create perdiction upto 2025
    # Using Equation : y = b_0 + (b_1 * x)
    
    df_2016 = bm + (a * 2016)
    df_2017 = bm + (a * 2017)
    df_2018 = bm + (a * 2018)   
    df_2019 = bm + (a * 2019)
    df_2020 = bm + (a * 2020)
    df_2021 = bm + (a * 2021)
    df_2022 = bm + (a * 2022)
    df_2023 = bm + (a * 2023)
    df_2024 = bm + (a * 2024)
    df_2025 = bm + (a * 2025)
    
    df_prediction_upto_2025 =(df_2016,
                              df_2017,df_2018,df_2019,
                              df_2020,df_2021,df_2022,
                              df_2023,df_2024,df_2025)
                   
    year11=(2016,2017,2018,2019,2020,2021,2022,2023,2024,2025)  
    
    # plot regression line
          
    plt.plot(x, y, color = "m",marker = "o",label="Actual")  
    y_pred = b[0] + b[1]*x 
    plt.plot(x, y_pred, color = "g",label="Regression line") 
    plt.xlabel('year -- >') 
    plt.ylabel('growth(%) --->')                                  
    
    # plot prediction line
    
    plt.title("Banking employment Prediction from 2017 to 2025 ")
    plt.plot(year11,df_prediction_upto_2025,linestyle="dashed",label="Prediction")
    plt.legend()
    plt.show()
    
    mean_y=np.mean(y)
    
    growth_2017 = (((df_2017)-(mean_y))/(mean_y))*100
    growth_2018 = (((df_2018)-(mean_y))/(mean_y))*100
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
    print("growth in 2017 = ",df_2017)
    print("growth in 2018 = ",df_2018)
    print("growth in 2019 = ",df_2019)
    print("growth in 2020 = ",df_2020)
    print("growth in 2021 = ",df_2021)
    print("growth in 2022 = ",df_2022)
    print("growth in 2023 = ",df_2023)
    print("growth in 2024 = ",df_2024)
    print("growth in 2025 = ",df_2025)
    print("\n----------------------------------------------------------")
    print("   Predicted Data(in % )according to mean data")
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

def railway_prediction():
    
    print('\n---: Railway employment details :---\n')
    df_total_rail = pd.DataFrame(list(zip(rail_year,df_rail_1)),columns =['Year','No. of Employee'])
    print(df_total_rail)    

def railway_prediction_2025(x,y,b,bm,a): 
    
    # Create perdiction upto 2025
    # Using Equation : y = b_0 + (b_1 * x)
    
    df_2015 = bm + (a * 2015)
    df_2016 = bm + (a * 2016)
    df_2017 = bm + (a * 2017)
    df_2018 = bm + (a * 2018)   
    df_2019 = bm + (a * 2019)
    df_2020 = bm + (a * 2020)
    df_2021 = bm + (a * 2021)
    df_2022 = bm + (a * 2022)
    df_2023 = bm + (a * 2023)
    df_2024 = bm + (a * 2024)
    df_2025 = bm + (a * 2025)
    
    df_prediction_upto_2025 =(df_2015,df_2016,
                              df_2017,df_2018,df_2019,
                              df_2020,df_2021,df_2022,
                              df_2023,df_2024,df_2025)
                   
    year11=(2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025)  
    
    # plot regression line
          
    plt.plot(x, y, color = "m",marker = "o",label="Actual")  
    y_pred = b[0] + b[1]*x 
    plt.plot(x, y_pred, color = "g",label="Regression line") 
    plt.xlabel('year -- >') 
    plt.ylabel('growth(%) --->')                                  
    
    # plot prediction line
    
    plt.title("Railway employment Prediction from 2016 to 2025 ")
    plt.plot(year11,df_prediction_upto_2025,linestyle="dashed",label="Prediction")
    plt.legend()
    plt.show()
    
    mean_y=np.mean(y)
    
    growth_2015 = (((df_2015)-(mean_y))/(mean_y))*100
    growth_2016 = (((df_2016)-(mean_y))/(mean_y))*100
    growth_2017 = (((df_2017)-(mean_y))/(mean_y))*100
    growth_2018 = (((df_2018)-(mean_y))/(mean_y))*100
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
    print("growth in 2015 = ",df_2015)
    print("growth in 2016 = ",df_2016)
    print("growth in 2017 = ",df_2017)
    print("growth in 2018 = ",df_2018)
    print("growth in 2019 = ",df_2019)
    print("growth in 2020 = ",df_2020)
    print("growth in 2021 = ",df_2021)
    print("growth in 2022 = ",df_2022)
    print("growth in 2023 = ",df_2023)
    print("growth in 2024 = ",df_2024)
    print("growth in 2025 = ",df_2025)
    print("\n----------------------------------------------------------")
    print("   Predicted Data(in % )according to mean data")
    print("--------------------------------------------------------\n")
    print("growth in 2015 = ",growth_2015,"%")
    print("growth in 2016 = ",growth_2016,"%")
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

#--------------- legal sector ------------
def legal_prediction():
    
    print('\n---: Employment details of Legal affiars  :---\n')
    print(legal_data)    

def legal_prediction_2025(x,y,b,bm,a): 
    
    # Create perdiction upto 2025
    # Using Equation : y = b_0 + (b_1 * x)
    
    df_2016 = bm + (a * 2016)
    df_2017 = bm + (a * 2017)
    df_2018 = bm + (a * 2018)   
    df_2019 = bm + (a * 2019)
    df_2020 = bm + (a * 2020)
    df_2021 = bm + (a * 2021)
    df_2022 = bm + (a * 2022)
    df_2023 = bm + (a * 2023)
    df_2024 = bm + (a * 2024)
    df_2025 = bm + (a * 2025)
    
    df_prediction_upto_2025 =(df_2016,
                              df_2017,df_2018,df_2019,
                              df_2020,df_2021,df_2022,
                              df_2023,df_2024,df_2025)
                   
    year11=(2016,2017,2018,2019,2020,2021,2022,2023,2024,2025)  
    
    # plot regression line
          
    plt.plot(x,y, color = "m",marker = "o",label="Actual")  
    y_pred = b[0] + b[1]*x 
    plt.plot(x,y_pred, color = "g",label="Regression line") 
    plt.xlabel('year -- >') 
    plt.ylabel('growth(%) --->')                                  
    
    # plot prediction line
    
    plt.title("Legal employment Prediction from 2017 to 2025 ")
    plt.plot(year11,df_prediction_upto_2025,linestyle="dashed",label="Prediction")
    plt.legend()
    plt.show()
    
    mean_y=np.mean(y)
    
    growth_2016 = (((df_2016)-(mean_y))/(mean_y))*100
    growth_2017 = (((df_2017)-(mean_y))/(mean_y))*100
    growth_2018 = (((df_2018)-(mean_y))/(mean_y))*100
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
    print("growth in 2016 = ",df_2016)
    print("growth in 2017 = ",df_2017)
    print("growth in 2018 = ",df_2018)
    print("growth in 2019 = ",df_2019)
    print("growth in 2020 = ",df_2020)
    print("growth in 2021 = ",df_2021)
    print("growth in 2022 = ",df_2022)
    print("growth in 2023 = ",df_2023)
    print("growth in 2024 = ",df_2024)
    print("growth in 2025 = ",df_2025)
    print("\n----------------------------------------------------------")
    print("   Predicted Data(in % )according to mean data")
    print("--------------------------------------------------------\n")
    print("growth in 2016 = ",growth_2016,"%")
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
                                                
def pie_chart():

    bank_pie = sum(df21.iloc[[7,8,9,10,11,12,13,14],])
    rail_pie = sum(df_rail_1)
    legal_pie = sum(legal_data_1.iloc[[0,1,2,3,4,5,6,7],])
    total = bank_pie + rail_pie + legal_pie
    print("total employment",total)
    print("\n\nBank employment percentage = ",((bank_pie/total)*100))
    print("Railway employment percentage = " , ((rail_pie/total)*100))
    print("Employment percentage in Legal affiars = ",((legal_pie/total)*100)) 
                                                                                                
                                                                                                                                                                                                                                                                                              
def main_menu():
    
    print("-----------------------------------------")
    print("    Main menu :")
    print("-----------------------------------------")
    print("[1] Dimension of the availabe data")
    print("[2] Available columns for the data set")
    print("[3] Prediction for employment in Banking sector")
    print("[4] Prediction for employment in Railway sector")
    print("[5] Prediction for employment in Legal affiars")
    print("[6] Comapre employment in Bank,Railway & Lergal affiars")
    print("-----------------------------------------")
    
def main_function():
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
            banking_prediction()
            x = np.array(bank_year)
            y = np.array(df21) 
            b = estimate_coef(x,y)
            print("\n----------------------")
            print("Estimated coefficients for area:\n----------------------\n") 
            print("b_0 = {}\nb_1 = {}".format(b[0], b[1])) 
            print("----------------------\n")    
            bank_prediction_2025(x,y,b,b[0],b[1])
            break    
        
        elif op1 == 4:
            railway_prediction()
            x = np.array(rail_year)
            y = np.array(df_rail_1) 
            b = estimate_coef(x,y)
            print("\n----------------------")
            print("Estimated coefficients for area:\n----------------------\n") 
            print("b_0 = {}\nb_1 = {}".format(b[0], b[1])) 
            print("----------------------\n")    
            railway_prediction_2025(x,y,b,b[0],b[1])
            break
            
        elif op1 == 5:
            legal_prediction()
            x = np.array(legal_year)
            y = np.array(legal_data_1) 
            b = estimate_coef(x,y)
            print("\n----------------------")
            print("Estimated coefficients for area:\n----------------------\n") 
            print("b_0 = {}\nb_1 = {}".format(b[0], b[1])) 
            print("----------------------\n")    
            legal_prediction_2025(x,y,b,b[0],b[1])
            break
        
        elif op1 == 6:                
             pie_chart()         
                                                                                          
        else:
            print("wrong input !")
             
        print("--------------------------------------------") 
        ch1 = input("enter:\n[0] for exit\n[1] for continue : ")
        ch =int(ch1,10)
        print("--------------------------------------------")
                
if __name__ == "__main__": 
    main_function()             
    