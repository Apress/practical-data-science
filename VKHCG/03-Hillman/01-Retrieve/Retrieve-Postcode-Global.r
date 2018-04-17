 #!/usr/bin/Rscript
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
FileNameInput=paste0(Base,'/03-Hillman/00-RawData/All_Countries.txt') 
library(readr)
All_Countries <- read_delim(FileNameInput, "\t", col_names = FALSE, 
col_types = cols(
X12 = col_skip(), 
X6 = col_skip(), 
X7 = col_skip(), 
X8 = col_skip(), 
X9 = col_skip()), 
na = "null", trim_ws = TRUE)
FileNameOutput=paste0(Base,'/03-Hillman/01-Retrieve/01-EDS/01-R/Retrieve_All_Countries.csv') 
write.csv(All_Countries, file = FileNameOutput)