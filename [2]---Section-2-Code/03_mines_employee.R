# (module - 3):employment in mines

# (1) Import and read the total data set ( CSV file) :
  
mines_data<-read.csv("C:/Users/Jeet Das/Desktop/Major Project - Indian Economy/Project ( Section 2-Employment Growth)/Section-2_Data_Sheet/(3)_mines_emloyment.csv");
View(mines_data)
  
  
# (2.1) Print the states and union territories from the data set :
    
state <- mines_data[,c(1,2)];
print(state);

# (2.2) Print all available column names in the main data set: 
      
sl_no. <- c(1:100)
all_column <- colnames(mines_data)
all_column.data <- data.frame(sl_no.,all_column)
print(all_column.data)

# (3) Total employment growth ( state wise ) from 2008 to 2014.
# NB : Here "sl.no" indicates state serial number
    
sl.no <- c(1:34)
all_year <- mines_data[,c(94:100)]
all_year.data <- data.frame(sl.no,all_year)
state <-  mines_data[,c(2)]
state.data <- data.frame(sl.no,state)
print(all_year.data)
    

all_year[is.na(all_year)] <- 0
all_year.data <- data.frame(sl.no,all_year)
print(all_year.data);
    
print(state.data)

total_2008_2014<- rowSums(all_year)
state <-  mines_data[,c(2)]
state.data <- data.frame(sl.no,state,total_2008_2014)
print(state.data)

# (4) Total employment growth (sector wise) from 2008 to 2014 :
#	(4.1) Coal sector :
      
coal <- mines_data[,c(3:9)]
print(coal)

coal[is.na(coal)] <- 0
print(coal)
   
total_2008_2014<- rowSums(coal)
state <-  mines_data[,c(2)]
state.data <- data.frame(sl.no,state,total_2008_2014)
print(state.data)


plot(sl.no,total_2008_2014,type = "o",xlab = "state serial no. ---->", ylab = "no. of employee ---->",
     main ="Coal : Total employee (state wise) from 2008-2014");
    
# (4.2) Copper sector :
      
copper <- mines_data[,c(10:16)]
print(copper)
    
copper[is.na(copper)] <- 0
print(copper)

total_2008_2014<- rowSums(copper)
state <-  mines_data[,c(2)]
state.data <- data.frame(sl.no,state,total_2008_2014)
print(state.data)

plot(sl.no,total_2008_2014,type = "o",xlab = "state serial no. ---->", ylab = "no. of employee ---->",main ="Copper : Total employee (state wise) from 2008-2014");
    
    
#	(4.3) Chromite sector :
 
chromite <- mines_data[,c(17:23)]
print(chromite)
    
chromite[is.na(chromite)] <- 0
print(chromite)
    
total_2008_2014<- rowSums(chromite)
state <-  mines_data[,c(2)]
state.data <- data.frame(sl.no,state,total_2008_2014)
print(state.data)
    
plot(sl.no,total_2008_2014,type = "o",xlab = "state serial no. ---->", ylab = "no. of employee ---->",
     main ="Chromite : Total employee (state wise) from 2008-2014");
    
#	(4.4) Diamond sector:
      
diamond <- mines_data[,c(24:30)]
print(diamond)
    
diamond[is.na(diamond)] <- 0
print(diamond)
    
total_2008_2014<- rowSums(diamond)
state <-  mines_data[,c(2)]
state.data <- data.frame(sl.no,state,total_2008_2014)
print(state.data)
    
plot(sl.no,total_2008_2014,type = "o",xlab = "state serial no. ---->",ylab = "no. of employee ---->",
      main ="Diamond : Total employee (state wise) from 2008-2014");
    
#???	(4.5) Gold sector :
      
gold <- mines_data[,c(31:37)]
print(gold)
    
gold[is.na(gold)] <- 0
print(gold)
   
total_2008_2014<- rowSums(gold)
state <-  mines_data[,c(2)]
state.data <- data.frame(sl.no,state,total_2008_2014)
print(state.data)
   
plot(sl.no,total_2008_2014,type = "o",xlab = "state serial no. ---->", ylab = "no. of employee ---->",
     main ="Gold : Total employee (state wise) from 2008-2014");
    
#???	(4.6) Gypsum sector :
      
gypsum <- mines_data[,c(38:44)]
print(gypsum)
    
gypsum[is.na(gypsum)] <- 0
print(gypsum)
    
total_2008_2014<- rowSums(gypsum)
state <-  mines_data[,c(2)]
state.data <- data.frame(sl.no,state,total_2008_2014)
print(state.data)
    
plot(sl.no,total_2008_2014,type = "o",xlab = "state serial no. ---->", ylab = "no. of employee ---->",
     main ="Gypsum : Total employee (state wise) from 2008-2014");
    
#	(4.7) Iron ore sector :
      
iron_ore <- mines_data[,c(45:51)]
view(iron_ore)

iron_ore[is.na(iron_ore)] <- 0
view(iron_ore)

total_2008_2014<- rowSums(iron_ore)
state <-  mines_data[,c(2)]
state.data <- data.frame(sl.no,state,total_2008_2014)
print(state.data)
    
plot(sl.no,total_2008_2014,type = "o",xlab = "state serial no. ---->", ylab = "no. of employee ---->",
           main ="Iron ore : Total employee (state wise) from 2008-2014");
    
#	(4.8) Limestone sector :

limestone <- mines_data[,c(52:58)]
view(limestone)

limestone[is.na(limestone)] <- 0
view(limestone)
total_2008_2014<- rowSums(limestone)
state <-  mines_data[,c(2)]
state.data <- data.frame(sl.no,state,total_2008_2014)
print(state.data)
    
plot(sl.no,total_2008_2014,type = "o",xlab = "state serial no. ---->", ylab = "no. of employee ---->",
     main ="Limestone : Total employee (state wise) from 2008-2014");
    
# (4.9) Magnetite sector :
      
magnetite <- mines_data[,c(59:65)]
view(magnetite)

magnetite[is.na(magnetite)] <- 0
view(magnetite)
total_2008_2014<- rowSums(magnetite)
state <-  mines_data[,c(2)]
state.data <- data.frame(sl.no,state,total_2008_2014)
print(state.data)
    
plot(sl.no,total_2008_2014,type = "o",xlab = "state serial no. ---->", ylab = "no. of employee ---->",
     main ="Magnetite : Total employee (state wise) from 2008-2014");
    
#	(4.10) Manganese sector :
      
manganese <- mines_data[,c(66:72)]
view(manganese)
    
manganese[is.na(manganese)] <- 0
view(manganese)
total_2008_2014<- rowSums(manganese)
state <-  mines_data[,c(2)]
state.data <- data.frame(sl.no,state,total_2008_2014)
print(state.data)
    
plot(sl.no,total_2008_2014,type = "o",xlab = "state serial no. ---->", ylab = "no. of employee ---->",
     main ="Manganese : Total employee (state wise) from 2008-2014");
    
    
# (4.11) Mica sector:
      
mica <- mines_data[,c(73:79)]
print(mica)
    
mica[is.na(mica)] <- 0
print(mica)
   
total_2008_2014<- rowSums(mica)
state <-  mines_data[,c(2)]
state.data <- data.frame(sl.no,state,total_2008_2014)
print(state.data)
    
plot(sl.no,total_2008_2014,type = "o",xlab = "state serial no. ---->", ylab = "no. of employee ---->",
     main ="Mica : Total employee (state wise) from 2008-2014");


#	(4.12) Stone sector:
      
stone <- mines_data[,c(80:86)]
print(stone)

stone[is.na(stone)] <- 0
print(stone)
   
total_2008_2014<- rowSums(stone)
state <-  mines_data[,c(2)]
state.data <- data.frame(sl.no,state,total_2008_2014)
print(state.data)
    
plot(sl.no,total_2008_2014,type = "o",xlab = "state serial no. ---->", ylab = "no. of employee ---->",
     main ="Stone : Total employee (state wise) from 2008-2014");


#	(4.13) Other minerals sector :
      
other_minerals <- mines_data[,c(87:93)]
view(other_minerals)
    
other_minerals[is.na(other_minerals)] <- 0
print(other_minerals)
total_2008_2014<- rowSums(other_minerals)
state <-  mines_data[,c(2)]
state.data <- data.frame(sl.no,state,total_2008_2014)
print(state.data)
   
    
plot(sl.no,total_2008_2014,type = "o",xlab = "state serial no. ---->", ylab = "no. of employee ---->",
     main ="Other Minerals : Total employee (state wise) from 2008-2014")
    