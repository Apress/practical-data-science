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
FileDir= paste0(Base,'/01-Vermeulen/01-Retrieve/01-EDS/01-R')
dir.create(FileDir)
FileDirLog=paste0(FileDir,'/log')
dir.create(FileDirLog) 
FileDirRun=paste0(FileDirLog,'/Run0001')
dir.create(FileDirRun)
###########################################
StartTime=Sys.time()
###########################################
# Set up logging
###########################################
debugLog=paste0(FileDirRun,'/debug.Log')
infoLog=paste0(FileDirRun,'/info.Log')
errorLog=paste0(FileDirRun,'/error.Log')
###########################################
write(paste0('Start Debug Log File ',
             format(StartTime, "%Y/%d/%m %H:%M:%S")),
      file=debugLog,append = FALSE)
write(paste0('Start Information Log File ',
             format(StartTime, "%Y/%d/%m %H:%M:%S")),
      file=infoLog,append = FALSE)
write(paste0('Start Error Log File ',
             format(StartTime, "%Y/%d/%m %H:%M:%S")),
      file=errorLog,append = FALSE)
###########################################
UserName='Practical Data Scientist'
###########################################
write(paste0(UserName,' Load library: ', 'readr'),
      infoLog,append = TRUE)
library(readr) 
write(paste0(UserName,' Load library: ', 'data.table'),
      infoLog,append = TRUE)
library(data.table) 
write(paste0(UserName,' Load library: ', 'tibble'),
      infoLog,append = TRUE)
library(tibble) 
###########################################
FileName=paste0(Base,'/01-Vermeulen/00-RawData/IP_DATA_ALL.csv')
write(paste0(UserName,' Retrieve data file: ', FileName),
      file=infoLog,append = TRUE)
###########################################
IP_DATA_ALL <- read_csv(FileName, 
                        col_types = cols(
                          Country = col_character(),
                          ID = col_skip(), 
                          'First IP Number' = col_skip(), 
                          'Last IP Number' = col_skip(),
                          Latitude = col_double(), 
                          Longitude = col_double(),
                          'Place Name' = col_character(), 
                          'Post Code' = col_character()
                        ), na = "empty")
###########################################
IP_DATA_ALL_FIX=set_tidy_names(IP_DATA_ALL, syntactic = TRUE, quiet = TRUE) 
###########################################
IP_DATA_ALL_with_ID=rowid_to_column(IP_DATA_ALL_FIX, var = "RowID")
###########################################
FileNameOut=paste0(FileDir,'/Retrieve_IP_DATA.csv')
fwrite(IP_DATA_ALL_with_ID, FileNameOut)
write(paste0(UserName,' Stores Retrieve data file: ', FileNameOut),
      file=infoLog,append = TRUE)
###########################################
StopTime=Sys.time()
###########################################
write(paste0('Stop Debug Log File ',
             format(StopTime, "%Y/%d/%m %H:%M:%S")),
      file=debugLog,append = TRUE)
write(paste0('Stop Information Log File ',
             format(StopTime, "%Y/%d/%m %H:%M:%S")),
      file=infoLog,append = TRUE)
write(paste0('Stop Error Log File ',
             format(StopTime, "%Y/%d/%m %H:%M:%S")),
      file=errorLog,append = TRUE)
###########################################
View(IP_DATA_ALL_with_ID)
###########################################