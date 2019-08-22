# module -1:Bank employment data analysis

data_set <- read.csv("C:/Users/Jeet Das/Desktop/Major Project - Indian Economy/Project ( Section 2-Employment Growth)/Section-2_Data_Sheet/(1)_bank_employee.csv");

col1 <- 1;
col2 <- 2;
col3 <- 3;
col4 <- 4;
col5 <- 5;
col6 <- 6;
col7 <- 7;
col8 <- 8;
col9 <- 9;
col10 <-10;

count_banks = data_set[,c(col1, col2, col3,col6,col8)];

#(a)Indian scheduled bank employee details(2001-2016):

x = data_set[,c(col1)];
sum1=data_set[,c(col4)];

#(b)Foreign scheduled bank details(2001-2016):

x = data_set[,c(col1)];
sum2=data_set[,c(col5)];

#(c)Non-scheduled bank employment detail:

x = data_set[,c(col1)];
sum3=data_set[,c(col7)];
sum3[is.na(sum3)] <- 0;

#(d)Regional rural bank employment bank details(2001-2016) :

x = data_set[,c(col1)];
sum4 = data_set[,c(col9)];
sum4[is.na(sum4)] <- 0;

#(e) RBI bank employment details(2001-2016):

x = data_set[,c(col1)];
sum5=data_set[,c(col10)];
sum5[is.na(sum5)] <- 0;

#--------------------------------------

sum1 = count_banks[,c(col2)];
sum111 <- sum(sum1);	

sum2 = count_banks[,c(col3)];
sum222 <- sum(sum2);

sum3 = data_set[,c(col6)];
sum333 <- sum(sum3, NA, na.rm = TRUE);

sum4 = data_set[,c(col8)];
sum444 <- sum(sum4, NA, na.rm = TRUE);
#-------------------------------------
sum11 <- sum(sum1);
sum22 <- sum(sum2);
sum33 <- sum(sum3);
sum44 <- sum(sum4);
sum55 <- sum(sum5);
#----------------------------------

main_menu <- function()
{
  print("-------------------------------------------------")
  print("     Main Menu")
  print("-------------------------------------------------")
  print("[1] Print available columns in the data set ")
  print("[2] plot growth of no. of banks from 2001 to 2016 ")
  print("[3] Print and plot total banks in India")
  print("[4] plot employment growth")
  print("[5] Print and plot total employment")
  print("[6] print total no. of banks with employment data")
  print("-------------------------------------------------")
}

#(01) Print the columns of the data set :
 
column_names <- function()
 {
  column1 <- colnames(data_set);
  print(column1)
 }

#(02) Print the no. of scheduled (Indian and foreign ), non-scheduled , regional rural banks in 2001-2016 :

bank_growth <- function()
{
  x = data_set[,c(col1)];
  
  #(2a)Indian scheduled bank details (2001-2016 )
  
  sum1 = data_set[,c(col2)];
  
  #(2b)Foreign scheduled bank details(2001-2016):
    
  sum2 = data_set[,c(col3)];
  
  #(2c)Non-scheduled bank details(2001-2016):
      
  sum3 = data_set[,c(col6)];
  sum3[is.na(sum3)] <- 0;
  
 
  #(2d)Regional rural bank details(2001-2016): 
          
  sum4 = data_set[,c(col8)];
  sum4[is.na(sum4)] <- 0;
  
  # plot the bank growth

  par(mfrow=c(2,2))
  
  plot(x,sum1,type = "o",xlab = "year ---->", ylab = "no.---->", 
       main = "Indian Scheduled no. of bank growth(2001-2016)");

  plot(x,sum2,type = "o",xlab = "year ---->", ylab = "no.---->",     
       main = "foreign Scheduled no. of bank growth(2001-2016)");

  plot(x,sum3,type = "o",xlab = "year ---->", ylab = "no.---->",     
       main = "Non-Scheduled no. of bank growth(2001-2016)");

  plot(x,sum4,type = "o",xlab = "year ---->", ylab = "no.---->",
       main = "Regional rural no. of bank growth (2001-2016)");
}

# (03) Count total no. of scheduled(Indian),scheduled(foreign), 
#         Non-scheduled and regional rural banks in india :

total_banks <- function()
{
  mdf1 = data_set[,c(col2, col3, col6,col8)];
  x <- colnames(mdf1)
  
  y <- c(sum111,sum222,sum333,sum444);
  print(y);
            
  bank.data <- data.frame(x,y);
  print(bank.data);
  
  par(mfrow=c(1,1))
  barplot(y,xlab="Bank types---->",ylab="no.--->",main="Bank Details");
} 

#(04) Print and plot Employment growth(2001-2016)  :
            
employee <- function()
{
  
  # plotting of employment in all banks from 2001 to 2016
  
  par(mfrow=c(2,2))
  
  plot(x,sum1,type = "o",xlab = "year ---->", ylab = "emp. no.---->",  
       main = "Indian Scheduled bank employment growth(2001-2016)");
  
  plot(x,sum2,type = "o",xlab = "year ---->", ylab = "emp. no.---->",  
       main = "foreign Scheduled bank employment growth(2001-2016)");
  
  plot(x,sum4,type = "o",xlab = "year ---->", ylab = "emp. no.---->",  
       main = "Regional rural bank employment growth(2001-2016)");
  
  plot(x,sum5,type = "o",xlab = "year ---->", ylab = "emp. no.---->",  
     main = "RBI employment growth(2001-2016)");
  }  
            
#(5)total employment data            

total_employee <- function()
{
  x <- c("indian","foreign","non-scheduled","regional","RBI");
  y <- c(sum11,sum22,sum33,sum44,sum55);
  emp.data <- data.frame(x,y);
  print(emp.data);
  
  barplot(y,names.arg=x,xlab="bank type -->",ylab="emp. no.--->", main="Employee Details");
}

#(6) final list of bank type,total banks,total employee            

final_list <- function()
{
 bank <-c(sum111,sum222,sum333,sum444,"NA");
 type <- c("indian","foreign","non-scheduled","regional","RBI");
 emp  <- c(sum11,sum22,sum33,sum44,sum55);
 total.data <- data.frame(type,bank,emp);
 print(total.data)
}           
            
bank_main <- function()
{
  ch = 1 
  while(ch != 0)
  {
    main_menu()
    
    op <- readline("Enter your choice :")
    op <- as.integer(op) 
    print("-------------------------------------------------")
    
    if(op == 1)
     {
      column_names()  
     }
    else if(op == 2)
    {
      bank_growth()
    }
    else if(op == 3)
    {
      total_banks()
    }
    else if(op == 4)
    {
      employee()
    }
    else if(op == 5)
    {
      total_employee()
    }
    else if(op == 6)
    {
      final_list()
    }
    else
    {
      print("Wrong input !! Try again ...")
    }
    print("------------------------------------------------------")
    ch <- readline("[0] for Exit || Any KEY to Continue : ")
  } 
}

