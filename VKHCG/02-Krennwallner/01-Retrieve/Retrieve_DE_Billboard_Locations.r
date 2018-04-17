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
Base=getwd()
FileDir= paste0(Base,'/02-Krennwallner/01-Retrieve/01-EDS/01-R')
###########################################
library(readr)
library(data.table)
###########################################
FileName=paste0(Base,'/02-Krennwallner/00-RawData/DE_Billboard_Locations.csv')
###########################################
DE_Billboard_Locations <- read_csv(FileName,
                                   col_types = cols(
                                     Country = col_character(), 
                                     ID = col_integer(), 
                                     Latitude = col_double(), 
                                     Longitude = col_double(), 
                                     PlaceName = col_character()
                                   ), na = "empty")
###########################################
setnames(DE_Billboard_Locations,'PlaceName','Place.Name')
###########################################
setorder(DE_Billboard_Locations,Latitude,Longitude)
###########################################
FileNameOut=paste0(FileDir,'/Retrieve_DE_Billboard_Locations.csv')
fwrite(DE_Billboard_Locations, FileNameOut)
###########################################
View(DE_Billboard_Locations)
###########################################