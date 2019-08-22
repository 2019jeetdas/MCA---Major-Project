#Module 5 : Employment & Unemployment per 1000

#	(5.1) Employment Per 1000 Persons: Type wise till June 2012
#??? (5.2) Unemployment Per 1000 Persons: Type wise till June 2012

# Data source :
# (5.1) https://data.gov.in/resources/employment-1000-persons-type-wise-till-june-2012 
# (5.2) https://data.gov.in/resources/unemployment-1000-persons-type-wise-till-june-2012


#	(5.1 - 1)Reading and writing files :
  
data <- read.csv("C:/Users/Jeet Das/Desktop/Major Project - Indian Economy/Project ( Section 2-Employment Growth)/Section-2_Data_Sheet/(5.1)_employment_per_1000.csv")

# (5.1 - 2) Print column names :
  
sl1 <- c(1:11)
column <- colnames(data)
data1 <- data.frame(sl1,column)
print(data1)

# (5.1 - 3)Print row names :
  
sl2 <- c(1:27)
rows1 <- rownames(data)
data2 <- data.frame(sl2,data[,c(1,2,3)])
print(data2)


# (5.1 - 4a)Usual status(total) :
  
table1 <- data[1:9,]
print(table1)

table2 <- table1[c(1,4,7),]
print(table2)

par(mfrow=c(1,3))
x1 <- data[1,4:8]
x1[is.na(x1)]<-0
barplot(as.matrix(x1),main="Usual status(Total)-All")
 
x2 <- data[4,4:8]
x2[is.na(x2)]<-0
barplot(as.matrix(x2),main="Usual status(Total)-Rural")

x3 <- data[7,4:8]
x3[is.na(x3)]<-0
barplot(as.matrix(x3),main="Usual status(Total)-urban")



# (5.1 - 4b) Usual status(male):
  
table21 <- table1[c(2,5,8),]
print(table21)

par(mfrow=c(1,3))
x1 <- data[2,4:8]
x1[is.na(x1)]<-0
barplot(as.matrix(x1),main="Usual status(Male)-All")

x2 <- data[5,4:8]
x2[is.na(x2)]<-0
barplot(as.matrix(x2),main="Usual status(Male)-Rural")
 
x3 <- data[8,4:8]
x3[is.na(x3)]<-0
barplot(as.matrix(x3),main="Usual status(Male)-urban")


# (5.1-4c) Usual status(Female):
  
table211 <- table1[c(3,6,9),]
print(table211)

par(mfrow=c(1,3))

x1 <- data[3,4:8]
x1[is.na(x1)]<-0
barplot(as.matrix(x1),main="Usual status(Female)-All")
 
x2 <- data[6,4:8]
x2[is.na(x2)]<-0
barplot(as.matrix(x2),main="Usual status(female)-Rural")
 
x3 <- data[9,4:8]
x3[is.na(x3)]<-0
barplot(as.matrix(x3),main="Usual status(female)-urban")


# (5.1-5a) Usual status(principle activity)[total] :
  
table3 <- data[10:18,]
print(table3)

table4 <- table3[c(1,4,7),]
print(table4)

par(mfrow=c(1,3))
 
x1 <- data[10,4:8]
x1[is.na(x1)]<-0
barplot(as.matrix(x1),main="Usual status[Principle activity](Total)-All")
 
x2 <- data[13,4:8]
x2[is.na(x2)]<-0
barplot(as.matrix(x2),main="Usual status[principle activity](Total)-Rural")
 
x3 <- data[16,4:8]
x3[is.na(x3)]<-0
barplot(as.matrix(x3),main="Usual status[principle activity](Total)-urban")


# (5.1-5b) Usual status(principle activity)[male] :
  
table41 <- table3[c(2,5,8),]
print(table41)


par(mfrow=c(1,3))
 
x1 <- data[11,4:8]
x1[is.na(x1)]<-0
barplot(as.matrix(x1),main="Usual status[principle activity](Male)-All")
 
x2 <- data[14,4:8]
x2[is.na(x2)]<-0
barplot(as.matrix(x2),main="Usual status[principle activity](Male)-Rural")
 
x3 <- data[17,4:8]
x3[is.na(x3)]<-0
barplot(as.matrix(x3),main="Usual status[principle activity](Male)-urban")


# (5.1-5c) Usual status(principle activity)[female] :
  
table411 <- table3[c(3,6,9),]
print(table411)

par(mfrow=c(1,3))
 
x1 <- data[12,4:8]
x1[is.na(x1)]<-0
barplot(as.matrix(x1),main="Usual status[principle activity](Female)-All")
 
x2 <- data[15,4:8]
x2[is.na(x2)]<-0
barplot(as.matrix(x2),main="Usual status[principle activity](female)-Rural")
 
x3 <- data[18,4:8]
x3[is.na(x3)]<-0
barplot(as.matrix(x3),main="Usual status[principle activity](female)-urban")

# (5.1-6a) Usual status(subsidiary activity)[total]:
  
table5 <- data[19:27,]
print(table5)

par(mfrow=c(1,3))
 
x1 <- data[19,4:8]
x1[is.na(x1)]<-0
barplot(as.matrix(x1),main="Usual status[subsidiary activity](Total)-All")
 
x2 <- data[22,4:8]
x2[is.na(x2)]<-0
barplot(as.matrix(x2),main="Usual status[subsidiary activity](Total)-Rural")
 
x3 <- data[25,4:8]
x3[is.na(x3)]<-0
barplot(as.matrix(x3),main="Usual status[subsidiary activity](Total)-urban")


# (5.1-6b) Usual status(subsidiary activity)[male]:
  
table61 <- table5[c(2,5,8),]
print(table61)

par(mfrow=c(1,3))
 
x1 <- data[20,4:8]
x1[is.na(x1)]<-0
barplot(as.matrix(x1),main="Usual status[subsidiary activity](Male)-All")
 
x2 <- data[23,4:8]
x2[is.na(x2)]<-0
barplot(as.matrix(x2),main="Usual status[subsidiary activity](Male)-Rural")
 
x3 <- data[26,4:8]
x3[is.na(x3)]<-0
barplot(as.matrix(x3),main="Usual status[subsidiary activity](Male)-urban")

# (5.1-6c) Usual status(subsidiary activity)[female]:
  
table611 <- table5[c(3,6,9),]
print(table611)

par(mfrow=c(1,3))
 
x1 <- data[21,4:8]
x1[is.na(x1)]<-0
barplot(as.matrix(x1),main="Usual status[subsidiary activity](Female)-All")
 
x2 <- data[24,4:8]
x2[is.na(x2)]<-0
barplot(as.matrix(x2),main="Usual status[subsidiary activity](female)-Rural")
 
x3 <- data[27,4:8]
x3[is.na(x3)]<-0
barplot(as.matrix(x3),main="Usual status[subsidiary activity](female)-urban")


# (5.2) Unemployment Per 1000 Persons : Type wise till June 2012

#	(5.2-1)Reading_and_printing_file: ???
# (5.2-2)Print_column_names :	
# (5.2-3)print_row_names :	
# (5.2-4a)Usual Status-Rural :	
# (5.2-4b)Usual Status-Urban :	
# (5.2-5a)Usual Status(adjusted)-Rural :	
# (5.2-5b)Usual Status(adjusted)-Urban :	
# (5.2-6a)current weekly status-Rural :	
# (5.2-6b)Current weekly status-Urban :	
# (5.2-7a)Current Daily status-Rural :	
# (5.2-7b)Current Daily status-Urban :
  
  
  
# (5.2) Unemployment Per 1000 Persons:Type wise till June 2012

# (5.2-1)Reading_and_printing_file :
 
data <- read.csv("C:/Users/Jeet Das/Desktop/Major Project - Indian Economy/Project ( Section 2-Employment Growth)/Section-2_Data_Sheet/(5.2)_unemployment_per_1000.csv")
View(data)

# (5.2-2)Print_column_names :
   
sl1 <- c(1:9)
column <- colnames(data)
data1 <- data.frame(sl1,column)
print(data1)


# (5.2-3)print_row_names :
 
sl2 <- c(1:24)
rows_name <- data[,1]
data2 <- data.frame(sl2,rows_name)
print(data2)

# (5.2-4a)Usual Status-Rural :
   
u_s_rural <- data[1:3,]
view(u_s_rural)

par(mfrow=c(1,3))
 
x1 <- data[1,2:9]
x1[is.na(x1)]<-0
barplot(as.matrix(x1),main="usual status- Rural - Total")
 
x2 <- data[2,2:9]
x2[is.na(x2)]<-0
barplot(as.matrix(x2),main="usual status- Rural - Male")
 
x3 <- data[3,2:9]
x2[is.na(x3)]<-0
barplot(as.matrix(x3),main="usual status- Rural - Female")


# (5.2-4b)Usual Status-Urban :
   
u_s_urban <- data[4:6,]
print(u_s_urban)

par(mfrow=c(1,3))
 
x1 <- data[4,2:9]
x1[is.na(x1)]<-0
barplot(as.matrix(x1),main="usual status-urban - Total")
 
x2 <- data[5,2:9]
x2[is.na(x2)]<-0
barplot(as.matrix(x2),main="usual status -urban - Male")
 
x3 <- data[6,2:9]
x3[is.na(x3)]<-0
barplot(as.matrix(x3),main="usual status-urban - Female")


# (5.2-5a)Usual Status(adjusted)-Rural :
   
u_s_a_rural <- data[7:9,]
view(u_s_a_rural)

par(mfrow=c(1,3))
 
x1 <- data[7,2:9]
x1[is.na(x1)]<-0
barplot(as.matrix(x1),main="usual status(adjusted) - Rural - Total")

x2 <- data[8,2:9]
x2[is.na(x2)]<-0
barplot(as.matrix(x2),main="usual status(adjusted) - Rural - Male")
 
x3 <- data[9,2:9]
x3[is.na(x3)]<-0
barplot(as.matrix(x3),main="usual status(adjusted) - Rural - Female")


# (5.2-5b)Usual Status(adjusted)-Urban :
 
u_s_a_urban <- data[10:12,]
view(u_s_a_urban)

par(mfrow=c(1,3))
 
x1 <- data[10,2:9]
x1[is.na(x1)]<-0
barplot(as.matrix(x1),main="usual status(adjusted)-urban - Total")
 
x2 <- data[11,2:9]
x2[is.na(x2)]<-0
barplot(as.matrix(x2),main="usual status(adjusted)-urban - Male")
 
x3 <- data[12,2:9]
x3[is.na(x3)]<-0
barplot(as.matrix(x3),main="usual status(adjusted)-urban - Female")

# (5.2-6a)current weekly status-Rural :
 
c_w_s_rural <- data[13:15,]
print(c_w_s_rural)

par(mfrow=c(1,3))
 
x1 <- data[13,2:9]
x1[is.na(x1)]<-0
barplot(as.matrix(x1),main="Current Weekly Status - Rural - Total")
 
x2 <- data[14,2:9]
x2[is.na(x2)]<-0
barplot(as.matrix(x2),main="Current Weekly Status - Rural - Male")
 
x3 <- data[15,2:9]
x3[is.na(x3)]<-0
barplot(as.matrix(x3),main="Current Weekly Status - Rural - Female")

# (5.2-6b)Current weekly status-Urban :
 
c_w_s_urban <- data[16:18,]
print(c_w_s_urban)

par(mfrow=c(1,3))
 
x1 <- data[16,2:9]
x1[is.na(x1)]<-0
barplot(as.matrix(x1),main="Current Weekly Status - Urban - Total")

x2 <- data[17,2:9]
x2[is.na(x2)]<-0
barplot(as.matrix(x2),main="Current Weekly Status - urban - Male")
 
x3 <- data[18,2:9]
x2[is.na(x3)]<-0
barplot(as.matrix(x3),main="Current Weekly Status - urban - Female")

# (5.2-7a)Current Daily status-Rural :
 
c_d_s_rural <- data[19:21,]
print(c_d_s_rural)

par(mfrow=c(1,3))
 
x1 <- data[19,2:9]
x1[is.na(x1)]<-0
barplot(as.matrix(x1),main="Current Daily Status - Rural - Total")
 
x2 <- data[20,2:9]
x2[is.na(x2)]<-0
barplot(as.matrix(x2),main="Current Daily Status - Rural - Male")
 
x3 <- data[21,2:9]
x2[is.na(x3)]<-0
barplot(as.matrix(x3),main="Current Daily Status - Rural - Female")

# (5.2-7b)Current Daily status-Urban :
   
c_d_s_urban <- data[22:24,]
print(c_d_s_urban)

par(mfrow=c(1,3))
 
x1 <- data[22,2:9]
x1[is.na(x1)]<-0
barplot(as.matrix(x1),main="Current Daily Status - Urban - Total")
 
x2 <- data[23,2:9]
x2[is.na(x2)]<-0
barplot(as.matrix(x2),main="Current Daily Status - Urban - Male")
 
x3 <- data[24,2:9]
x3[is.na(x3)]<-0
barplot(as.matrix(x3),main="Current Daily Status - Urban - Female")
