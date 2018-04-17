###########################################
rm(list=ls()) #will remove ALL objects
###########################################
library(readr)
library(data.table)
library(tibble) 
###########################################
if (Sys.info()['sysname'] == "Windows") 
	{
		BaseSet = "C:/VKHCG"
		setwd(BaseSet)
	} else {
		BaseSet = paste0("/home/" , Sys.info()['user'] , "/VKHCG")
		setwd(BaseSet)
	}
########################################### 
Base=getwd()
FileDir= paste0(Base,'/04-Clark/01-Retrieve/01-EDS/01-R')
FileName=paste0(Base,'/04-Clark/00-RawData/Profit_And_Loss.csv') 
########################################### 
Profit_And_Loss <- read_csv(FileName,
                    col_types = cols(
                      Amount = col_double(), 
                      ProductClass1 = col_character(), 
                      ProductClass2 = col_character(), 
                      ProductClass3 = col_character(), 
                      QTR = col_character(), 
                      QTY = col_double(), 
                      TypeOfEntry = col_character()
                    ), na = "empty") 
###########################################
### Sort the results
###########################################
keyList=c('QTR','TypeOfEntry','ProductClass1','ProductClass2','ProductClass3')
setorderv(Profit_And_Loss, keyList, order= c(-1L,1L,1L,1L,1L), na.last=FALSE)
###########################################
FileNameOut=paste0(FileDir,'/Retrieve_Profit_And_Loss.csv')
fwrite(Profit_And_Loss, FileNameOut)
###########################################
View(Profit_And_Loss)
###########################################
