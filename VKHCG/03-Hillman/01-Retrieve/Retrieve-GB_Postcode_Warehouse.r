
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
rm(list=ls()) #will remove ALL objects
###########################################
library(readr)
library(data.table)
library(jsonlite)
########################################### 
Base=getwd()
FileDir= paste0(Base,'/03-Hillman/01-Retrieve/01-EDS/01-R')
FileName=paste0(Base,'/03-Hillman/00-RawData/GB_Postcode_Warehouse.csv') 
GB_Postcode_Warehouse <- read_csv(FileName, 
                             col_types = cols(
                               id = col_integer(), 
                               latitude = col_double(), 
                               longitude = col_double(), 
                               postcode = col_character()
                             ), 
                             na = "empty")
###########################################
FileNameOut=paste0(FileDir,'/Retrieve_GB_Postcode_Warehouse.csv')
fwrite(GB_Postcode_Warehouse, FileNameOut)
###########################################
GB_Postcode_Warehouse_JSON_A=toJSON(GB_Postcode_Warehouse, pretty=TRUE)
###########################################
FileNameJSONA=paste0(FileDir,'/Retrieve_GB_Postcode_Warehouse_A.json')
write(GB_Postcode_Warehouse_JSON_A, FileNameJSONA)
###########################################
GB_Postcode_Warehouse_JSON_B=toJSON(GB_Postcode_Warehouse, pretty=FALSE)
###########################################
FileNameJSONB=paste0(FileDir,'/Retrieve_GB_Postcode_Warehouse_B.json')
write(GB_Postcode_Warehouse_JSON_B, FileNameJSONB)
###########################################
View(GB_Postcode_Warehouse)
###########################################
GB_Postcode_Warehouse_A=json_data <- fromJSON(paste(readLines(FileNameJSONA), collapse=""))
###########################################
View(GB_Postcode_Warehouse_A)
###########################################
GB_Postcode_Warehouse_B=json_data <- fromJSON(paste(readLines(FileNameJSONB), collapse=""))
###########################################
View(GB_Postcode_Warehouse_B)
###########################################