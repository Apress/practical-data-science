
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
########################################### 
Base=getwd()
FileDir= paste0(Base,'/03-Hillman/01-Retrieve/01-EDS/01-R')
FileName=paste0(Base,'/03-Hillman/00-RawData/GB_Postcodes_Shops.csv') 
GB_Postcodes_Shops <- read_csv(FileName, 
                             col_types = cols(
                               id = col_integer(), 
                               latitude = col_double(), 
                               longitude = col_double(), 
                               postcode = col_character()
                             ), 
                             na = "empty")
###########################################
FileNameOut=paste0(FileDir,'/Retrieve_GB_Postcodes_Shops.csv')
fwrite(GB_Postcodes_Shops, FileNameOut)
###########################################
View(GB_Postcodes_Shops)
###########################################
GB_Five_Shops=GB_Postcodes_Shops[1:5,]
###########################################
library(XML)
###########################################
xml <- xmlTree()
xml$addTag("document", close=FALSE)
for (i in 1:nrow(GB_Five_Shops)) {
  xml$addTag("row", close=FALSE)
  for (j in 1:length(names(GB_Five_Shops))) {
    xml$addTag(names(GB_Five_Shops)[j], GB_Five_Shops[i, j])
  }
  xml$closeTag()
}
xml$closeTag()
GB_Postcodes_Shops_XML=saveXML(xml)
###########################################
FileNameXML=paste0(FileDir,'/Retrieve_GB_Postcodes_Shops.xml')
write(GB_Postcodes_Shops_XML, FileNameXML)
###########################################
xmlFile<-xmlTreeParse(FileNameXML)
class(xmlFile)
xmlTop = xmlRoot(xmlFile)
xmlText<- xmlSApply(xmlTop, function(x) xmlSApply(x, xmlValue))
GB_Postcodes_Shops_XML_A <- data.frame(t(xmlText),row.names=NULL)
###########################################
View(GB_Postcodes_Shops_XML_A)