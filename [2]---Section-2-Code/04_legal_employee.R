# (module - 4): employment in legal sectors

#(4A-1)  Reading and print file:
  
data <- read.csv("C:/Users/Jeet Das/Desktop/Major Project - Indian Economy/Project ( Section 2-Employment Growth)/Section-2_Data_Sheet/(4.1)_legal.csv")
view(data) 
  
#(4A-2) print column names :
    
sl <- c(1:13)
column <- colnames(data)
data1 <- data.frame(sl,column)
print(data1)

# (4A-3) print row names :
      
sl2 <- c(1:27)
rows1 <- rownames(data)
data2 <- data.frame(sl2,data[,c(1,2)])
print(data2)
    
# (4A - 4) Plot  :  Year(2008-2016) vs . Total Employee :
      
t1 <- "Processing from total table : "
print(t1)

table_1 <- data.frame(data[c(3,6,9,12,15,18,21,24,27),c(1,2,3)])
print(table_1)

x <- c(2008:2016)
y <- table_1[,3]
plot(x,y,type = "o",xlab = "year ---->", ylab = "no.---->",     
           main = "Total employee in Legal Affairs(2008-2016)");
    
    
# (4A - 5) Plot  :  Year(2008-2016) vs . Total SC :
      
t1 <- "Processing from total table : "
print(t1)

table_2 <- data.frame(data[c(3,6,9,12,15,18,21,24,27),c(1,2,4)])
print(table_2)
    
x <- c(2008:2016)
y <- table_1[,3]
plot(x,y,type = "o",xlab = "year ---->", ylab = "no.---->",     
           main = "Total SC in Legal Affairs(2008-2016)");
    
# (4A - 6) Plot  :  Year(2008-2016) vs . Total ST :
      
t1 <- "Processing from total table : "
print(t1)

table_3 <- data.frame(data[c(3,6,9,12,15,18,21,24,27),c(1,2,6)])
print(table_3)
   
x <- c(2008:2016)
y <- table_3[,3]
y[is.na(y)] <- 0;
plot(x,y,type = "o",xlab = "year ---->", ylab = "no.---->",     
           main = "Total ST in Legal Affairs(2008-2016)");
    

# (4A - 7) Plot  :  Year(2008-2016) vs . OBC :
      
t1 <- "Processing from total table : "
print(t1)

table_4 <- data.frame(data[c(3,6,9,12,15,18,21,24,27),c(1,2,8)])
print(table_4)

x <- c(2008:2016)
y <- table_4[,3]
y[is.na(y)] <- 0;
plot(x,y,type = "o",xlab = "year ---->", ylab = "no.---->",
     main = "Total Other backward in Legal Affairs(2008-2016)");

# (4A - 8) Plot  :  Year(2008-2016) vs . EX.Serviceman :
      
t1 <- "Processing from total table : "
print(t1)

table_5 <- data.frame(data[c(3,6,9,12,15,18,21,24,27),c(1,2,10)])
print(table_5)
   
x <- c(2008:2016)
y <- table_4[,3]
y[is.na(y)] <- 0;
plot(x,y,type = "o",xlab = "year ---->", ylab = "no.---->",
     main = "Total ex-serviceman in Legal Affairs(2008-2016)");
    
    
# (4A - 9) Plot  :  Year(2008-2016) vs . Total Physically Handicapped :
      
t1 <- "Processing from total table : "
print(t1)

table_6 <- data.frame(data[c(3,6,9,12,15,18,21,24,27),c(1,2,12)])
print(table_6)
    
x <- c(2008:2016)
y <- table_6[,3]
y[is.na(y)] <- 0;
plot(x,y,type = "o",xlab = "year ---->", ylab = "no.---->",
     main = "Total Physically Handicapped in Legal Affairs(2008-2016)");
    
# (4A - 10) Plot  :  Year(2008-2016) vs . Complete data :
      
year <- table_1[,1]
TOTAL_EMP. <- table_1[,3]
SC <- table_2[,3]
ST <- table_3[,3]
OBC <- table_4[,3]
EX.SERVICEMAN <- table_5[,3]
PH<- table_6[,3]
total <-data.frame(year,TOTAL_EMP.,SC,ST,OBC,EX.SERVICEMAN,PH)
print(total)

SC[is.na(SC)] <- 0
ST[is.na(ST)] <- 0
OBC[is.na(OBC)] <- 0
EX.SERVICEMAN[is.na(EX.SERVICEMAN)] <- 0
PH[is.na(PH)] <- 0
total1 <-data.frame(SC,ST,OBC,EX.SERVICEMAN,PH)
print(total1)

total_emp <- colSums(total1)
print(total_emp)

barplot(total_emp,main="Compare all employee")
    
    
# (4A - 11) Plot  :  Year(2008-2016) vs . Complete data(% wise) :

year <- data[,c(1)]
GR <- data[,c(2)]
SC <- data[,c(5)]
ST <- data[,c(7)]
OBC <- data[,c(9)]
EX.SERVICEMAN <- data[,c(11)]
PH <- data[,c(13)]
data_percentage <- data.frame(year,GR,SC,ST,OBC,EX.SERVICEMAN,PH)
View(data_percentage)
    
# (4B)  Representation of female employees in Department of Legal Affairs from 1st January, 2013 
#       to 1st January, 2014 (Admin IV)
    
# (4B-1) Reading and writing files :

data1 <- read.csv("C:/Users/Jeet Das/Desktop/Major Project - Indian Economy/Project ( Section 2-Employment Growth)/Section-2_Data_Sheet/(4.2)_legal_female.csv")
view(data1)

# (4B-2) Print column names :

sl1 <- c(1:6)
column <- colnames(data1)
data11 <- data.frame(sl1,column)
print(data11)

# (4B-3) Print row names :

sl2 <- c(1:10)
rows1 <- rownames(data1)
data12 <- data.frame(sl2,data1[,c(1,2)])
print(data12)

# (4B-4) 2014_details :

GROUP1 <- data1[,2]
TOTAL_EMP_Legal <- data1[,3]
TOTAL_FEMALE_EMP_Legal<- data1[,4]
TOTAL_OTHER <- data1[,5]
TOTAL_OTHER_FEMALE <- data1[,6]
table11<- data.frame(TOTAL_EMP_Legal,TOTAL_FEMALE_EMP_Legal,TOTAL_OTHER,TOTAL_OTHER_FEMALE)
table1 <-data.frame(GROUP1,TOTAL_EMP_Legal,TOTAL_FEMALE_EMP_Legal,TOTAL_OTHER,TOTAL_OTHER_FEMALE)
print(table1)

table_2014 <- table1[(1:5),]
table_2014_1 <- table11[(1:5),]
print(table_2014)

column_sum_1 <- colSums(table_2014_1)
print(column_sum_1)

barplot(column_sum_1,main="2014 data1 Set")


# (4B-5) 2013 details :

GROUP1 <- data1[,2]
TOTAL_EMP_Legal <- data1[,3]
TOTAL_FEMALE_EMP_Legal<- data1[,4]
TOTAL_OTHER <- data1[,5]
TOTAL_OTHER_FEMALE <- data1[,6]
table11<- data.frame(TOTAL_EMP_Legal,TOTAL_FEMALE_EMP_Legal,TOTAL_OTHER,TOTAL_OTHER_FEMALE)
table1 <- data.frame(GROUP1,TOTAL_EMP_Legal,TOTAL_FEMALE_EMP_Legal,TOTAL_OTHER,TOTAL_OTHER_FEMALE)
print(table1)

table_2013 <- table1[(1:5),]
table_2013_1 <- table11[(1:5),]
print(table_2013)

column_sum_1 <- colSums(table_2013_1)
print(column_sum_1)

barplot(column_sum_1,main="2013 data1 Set")
