
###########################################
rm(list=ls()) #will remove ALL objects
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
library(readr)
library(data.table)
library(tibble) 
########################################### 
Base=getwd()
FileDir= paste0(Base,'/03-Hillman/01-Retrieve/01-EDS/01-R')
FileName=paste0(Base,'/03-Hillman/00-RawData/GB_Postcode_Full.csv') 
GB_Postcode_Full <- read_csv(FileName, 
                             col_types = cols(
                               AreaName = col_character(), 
                               Country = col_character(), 
                               ID = col_integer(), 
                               PlaceName = col_character(), 
                               PostCode = col_character(), 
                               Region = col_character(), 
                               RegionCode = col_character()
                             ), 
                             na = "empty")
###########################################
FileNameOut=paste0(FileDir,'/Retrieve_GB_Postcode_Full.csv')
fwrite(GB_Postcode_Full, FileNameOut)
###########################################
View(GB_Postcode_Full)
###########################################