#(module - 02): employment in indian railways:

# (01)Read and print the main file:

data1 <- read.csv("C:/Users/Jeet Das/Desktop/Major Project - Indian Economy/
                  Project ( Section 2-Employment Growth)/Section-2_Data_Sheet/(2)_railway_employee.csv");
View(data1);


# Print column names (contain zone names ) :-
  
column <- colnames(data1);
print(column);

# (2) Central Railway employee details :

col1  <- 1;
col2  <- 2;
grand_total <- data1[,c(col1,col2)];
year<- data1[,c(col1)];
total2 <- data1[,c(col2)];
print(grand_total);

library(ggplot2);
x <- c(1:15);
plot(x,total2,type = "o",xlab = "year ---->", ylab = "no. of employee---->",
     main ="Central Railway (2000-01) to (2014-15)");

year.data <- data.frame(x,year);
print(year.data);

# (3) Eastern Railway employee details:

col1  <- 1;
col3  <- 3;
grand_total <- data1[,c(col1,col3)];
year<- data1[,c(col1)];
total3 <- data1[,c(col3)];
print(grand_total);

library(ggplot2);
x <- c(1:15);
plot(x,total3,type = "o",xlab = "year ---->", ylab = "no. of employee---->",
     main ="Eastern Railway (2000-01) to (2014-15)");

year.data <- data.frame(x,year);
print(year.data);

# (4)Eastern central Railway employee details:
  
col1  <- 1;
col4  <- 4;
grand_total <- data1[,c(col1,col4)];
year<- data1[,c(col1)];
total4 <- data1[,c(col4)];
print(grand_total);

library(ggplot2);
x <- c(1:15);
plot(x,total4,type = "o",xlab = "year ---->", ylab = "no. of employee---->",
     main ="Eastern central Railway (2000-01) to (2014-15)");

year.data <- data.frame(x,year);
print(year.data);

# (5) Eastern coast Railway employee details:
  
col1  <- 1;
col5  <- 5;
grand_total <- data1[,c(col1,col5)];
year<- data1[,c(col1)];
total5 <- data1[,c(col5)];
print(grand_total);

library(ggplot2);
x <- c(1:15);
plot(x,total5,type = "o",xlab = "year ---->", ylab = "no. of employee---->",
     main ="Eastern cost Railway (2000-01) to (2014-15)");

year.data <- data.frame(x,year);
print(year.data);


# (6) Eastern coast Railway employee details :
  
col1  <- 1;
col6  <- 6;
grand_total <- data1[,c(col1,col6)];
year<- data1[,c(col1)];
total6 <- data1[,c(col6)];
print(grand_total);

library(ggplot2);
x <- c(1:15);
plot(x,total6,type = "o",xlab = "year ---->", ylab = "no. of employee---->",
     main ="Metro Railway Kolkata (2000-01) to (2014-15)");

year.data <- data.frame(x,year);
print(year.data);

# (7) Northern Railway employee details :
  
col1  <- 1;
col7  <- 7;
grand_total <- data1[,c(col1,col7)];
year<- data1[,c(col1)];
total7 <- data1[,c(col7)];
print(grand_total);

library(ggplot2);
x <- c(1:15);
plot(x,total7,type = "o",xlab = "year ---->", ylab = "no. of employee---->",
     main ="Northern Railway (2000-01) to (2014-15)");

year.data <- data.frame(x,year);
print(year.data);

# (8) North central Railway employee details :
  
col1  <- 1;
col8  <- 8;
grand_total <- data1[,c(col1,col8)];
year<- data1[,c(col1)];
total8 <- data1[,c(col8)];
print(grand_total);

library(ggplot2);
x <- c(1:15);
plot(x,total8,type = "o",xlab = "year ---->", ylab = "no. of employee---->",
     main ="North cenral Railway (2000-01) to (2014-15)");

year.data <- data.frame(x,year);
print(year.data);

# (9) North Eastern Railway employee details :
  
col1  <- 1;
col9  <- 9;
grand_total <- data1[,c(col1,col9)];
year<- data1[,c(col1)];
total9 <- data1[,c(col9)];
print(grand_total);

library(ggplot2);
x <- c(1:15);
plot(x,total9,type = "o",xlab = "year ---->", ylab = "no. of employee---->",
     main ="North Eastern Railway (2000-01) to (2014-15)");

year.data <- data.frame(x,year);
print(year.data);


# (10) Northeast Frontier Railway employee details:
  
col1  <- 1;
col10  <- 10;
grand_total <- data1[,c(col1,col10)];
year<- data1[,c(col1)];
total10 <- data1[,c(col10)];
print(grand_total);

library(ggplot2);
x <- c(1:15);
plot(x,total10,type = "o",xlab = "year ---->", ylab = "no. of employee---->",
     main ="Northeast Frointier Railway (2000-01) to (2014-15)");

year.data <- data.frame(x,year);
print(year.data);

# (11) North Western Railway employee details :
  
col1  <- 1;
col11  <- 11;
grand_total <- data1[,c(col1,col11)];
year<- data1[,c(col1)];
total11 <- data1[,c(col11)];
print(grand_total);

library(ggplot2);
x <- c(1:15);
plot(x,total11,type = "o",xlab = "year ---->", ylab = "no. of employee---->",
     main ="North Western Railway (2000-01) to (2014-15)");

year.data <- data.frame(x,year);
print(year.data);


# (12) Southern Railway employee details :
  
col1  <- 1;
col12  <- 12;
grand_total <- data1[,c(col1,col12)];
year<- data1[,c(col1)];
total12 <- data1[,c(col12)];
print(grand_total);

library(ggplot2);
x <- c(1:15);
plot(x,total12,type = "o",xlab = "year ---->", ylab = "no. of employee---->",
     main ="Southern Railway (2000-01) to (2014-15)");

year.data <- data.frame(x,year);
print(year.data);

# (13) South Central Railway employee details :
  
col1  <- 1;
col13  <- 13;
grand_total <- data1[,c(col1,col13)];
year<- data1[,c(col1)];
total13 <- data1[,c(col13)];
print(grand_total);

library(ggplot2);
x <- c(1:15);
plot(x,total13,type = "o",xlab = "year ---->", ylab = "no. of employee---->",
     main ="South central Railway (2000-01) to (2014-15)");

year.data <- data.frame(x,year);
print(year.data);


# (14) South Eastern Railway employee details :
  
col1  <- 1;
col14  <- 14;
grand_total <- data1[,c(col1,col14)];
year<- data1[,c(col1)];
total14 <- data1[,c(col14)];
print(grand_total);

library(ggplot2);
x <- c(1:15);
plot(x,total14,type = "o",xlab = "year ---->", ylab = "no. of employee---->",
     main ="South eastern Railway (2000-01) to (2014-15)");

year.data <- data.frame(x,year);
print(year.data);


# (15) Southeast Central Railway employee details :
  
col1  <- 1;
col15  <- 15;
grand_total <- data1[,c(col1,col15)];
year<- data1[,c(col1)];
total15 <- data1[,c(col15)];
print(grand_total);

library(ggplot2);
x <- c(1:15);
plot(x,total15,type = "o",xlab = "year ---->", ylab = "no. of employee---->",
     main ="Southeast central Railway (2000-01) to (2014-15)");

year.data <- data.frame(x,year);
print(year.data);


# (16) South western Railway employee details :
  
col1  <- 1;
col16  <- 16;
grand_total <- data1[,c(col1,col16)];
year<- data1[,c(col1)];
total16 <- data1[,c(col16)];
print(grand_total);

library(ggplot2);
x <- c(1:15);
plot(x,total16,type = "o",xlab = "year ---->", ylab = "no. of employee---->",main ="South western Railway (2000-01) to (2014-15)");

year.data <- data.frame(x,year);
print(year.data);


# (17) Western Railway employee details :
  
col1  <- 1;
col17  <- 17;
grand_total <- data1[,c(col1,col17)];
year<- data1[,c(col1)];
total17 <- data1[,c(col17)];
print(grand_total);

library(ggplot2);
x <- c(1:15);
plot(x,total17,type = "o",xlab = "year ---->", ylab = "no. of employee---->",
     main ="Western Railway (2000-01) to (2014-15)");

year.data <- data.frame(x,year);
print(year.data);


# (18) West central Railway employee details :
  
col1  <- 1;
col18  <- 18;
grand_total <- data1[,c(col1,col18)];
year<- data1[,c(col1)];
total18 <- data1[,c(col18)];
print(grand_total);

library(ggplot2);
x <- c(1:15);
plot(x,total18,type = "o",xlab = "year ---->", ylab = "no. of employee---->",main ="West central Railway (2000-01) to (2014-15)");

year.data <- data.frame(x,year);
print(year.data);


# (19) Railway production unit employee details :
  
col1  <- 1;
col19  <- 19;
grand_total <- data1[,c(col1,col19)];
year<- data1[,c(col1)];
total19 <- data1[,c(col19)];
print(grand_total);

library(ggplot2);
x <- c(1:15);
plot(x,total19,type = "o",xlab = "year ---->", ylab = "no. of employee---->",
     main ="Railway Production unit (2000-01) to (2014-15)");

year.data <- data.frame(x,year);
print(year.data);

# (20) Railway board metropolitan transport projects employee details : 
  
col1  <- 1;
col20  <- 20;
grand_total <- data1[,c(col1,col20)];
year<- data1[,c(col1)];
total20 <- data1[,c(col20)];
print(grand_total);

library(ggplot2);
x <- c(1:15);
plot(x,total20,type = "o",xlab = "year ---->", ylab = "no. of employee---->",
     main ="Railway board metropolitan transport projects (2000-01) to (2014-15)");

year.data <- data.frame(x,year);
print(year.data);


# (21) Plot the total employee details year wise :
  
col1  <- 1;
col21 <- 21;
grand_total <- data1[,c(col1,col21)];
year<- data1[,c(col1)];
total <- data1[,c(col21)];
print(grand_total);

library(ggplot2);
x <- c(1:15);
plot(x,total,type = "o",xlab = "year ---->", ylab = "no. of employee---->",
     main ="Total employee yearwise (2000-01) to (2014-15)");

year.data <- data.frame(x,year);
print(year.data);


# (22) Plot the total employee details zone wise :

total2[is.na(total2)] <- 0;
sum2 <- sum(total2);
print(sum2);

total3[is.na(total3)] <- 0;
sum3 <- sum(total3);
print(sum3);

total4[is.na(total4)] <- 0;
sum4 <- sum(total4);
print(sum4);

total5[is.na(total5)] <- 0;
sum5 <- sum(total5);
print(sum5);

total6[is.na(total6)] <- 0;
sum6 <- sum(total6);
print(sum6);

total7[is.na(total7)] <- 0;
sum7 <- sum(total7);
print(sum7);

total8[is.na(total8)] <- 0;
sum8 <- sum(total8);
print(sum8);

total9[is.na(total9)] <- 0;
sum9 <- sum(total9);
print(sum9);

total10[is.na(total10)] <- 0;
sum10 <- sum(total10);
print(sum10);

total11[is.na(total11)] <- 0;
sum11 <- sum(total11);
print(sum11);

total12[is.na(total12)] <- 0;
sum12 <- sum(total12);
print(sum12);

total13[is.na(total13)] <- 0;
sum13 <- sum(total13);
print(sum13);

total14[is.na(total14)] <- 0;
sum14 <- sum(total14);
print(sum14);

total15[is.na(total15)] <- 0;
sum15 <- sum(total15);
print(sum15);

total16[is.na(total16)] <- 0;
sum16 <- sum(total16);
print(sum16);

total17[is.na(total17)] <- 0;
sum17 <- sum(total17);
print(sum17);

total18[is.na(total18)] <- 0;
sum18 <- sum(total18);
print(sum18);

total19[is.na(total19)] <- 0;
sum19 <- sum(total19);
print(sum19);

total20[is.na(total20)] <- 0;
sum20 <- sum(total20);
print(sum20);

zone <- c('Central','Eastern','East central','East coast','Kolkata Metro',
          'Northern','north central','north eastern','northesat frontier',
          'north western','southern','south central','south eastern',
          'southeast central','south western','western','west central',
          'production unit','transport project');

zonewise_sum <- c(sum2,sum3,sum4,sum5,sum6,sum7,sum8,sum9,sum10,sum11,sum12,sum13,sum14,sum15,sum16,sum17,sum18,sum19,sum20);
print(zonewise_sum);

zonewise_sum.data <- data.frame(zone,zonewise_sum);
print(zonewise_sum.data);

library(ggplot2);
x1 <- c(1:19); #-- represents zone list
plot(x1,zonewise_sum,type = "o",xlab = "zone ---->", ylab = "no. of employee---->",
    main ="Total employee zonewise");

  