###########################################
rm(list=ls()) #will remove ALL objects 
###########################################
library("data.table")
library("readr")
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
FileName=paste0(Base,'/04-Clark/00-RawData/Euro_ExchangeRates.csv') 
Euro_EchangeRates <- read_csv(FileName, 
                              col_types = cols(
                                Date = col_date(format = "%d/%m/%Y"),
                                .default = col_character()
                              ), locale = locale(encoding = "ASCII", asciify = TRUE)
)
###########################################
### Get the list of headings
###########################################
CA=as.vector(names(Euro_EchangeRates))
###########################################
### Remove Date from the vector to get Exchange Codes
###########################################
C=CA [! CA %in% "Date"]
###########################################
### Create a default table structure
###########################################
Echange=data.table(Date="1900-01-01",Code="Code",Rate=0,Base="Base")
###########################################
### Add the data for Exchange Code Euro pairs
###########################################
for (R in C) {
  EchangeRates=data.table(subset(Euro_EchangeRates[c('Date',R)],
                    is.na(Euro_EchangeRates[R])==FALSE),R,Base="EUR")
  colnames(EchangeRates)[colnames(EchangeRates)==R] <- "Rate"
  colnames(EchangeRates)[colnames(EchangeRates)=="R"] <- "Code"
  if(nrow(Echange)==1) Echange=EchangeRates
  if(nrow(Echange)>1) Echange=data.table(rbind(Echange,EchangeRates))
}
###########################################
Echange2=Echange
###########################################
colnames(Echange)[colnames(Echange)=="Rate"] <- "RateIn"
colnames(Echange)[colnames(Echange)=="Code"] <- "CodeIn"
colnames(Echange2)[colnames(Echange2)=="Rate"] <- "RateOut"
colnames(Echange2)[colnames(Echange2)=="Code"] <- "CodeOut"
EchangeRate=merge(Echange, Echange2, by=c("Base","Date"), all=TRUE, 
                  sort=FALSE,allow.cartesian=TRUE)
EchangeRates <- data.table(EchangeRate,
                 Rate=with(
                   EchangeRate, 
                   round((as.numeric(RateOut) / as.numeric(RateIn)),9)
                 ))
###########################################
### Remove work columns
###########################################
EchangeRates$Base <-NULL
EchangeRates$RateIn <-NULL
EchangeRates$RateOut  <-NULL
###########################################
### Make entries unique
###########################################
EchangeRate=unique(EchangeRates)
###########################################
### Sort the results
###########################################
setorderv(EchangeRate, c('Date','CodeIn','CodeOut'),
          order= c(-1L,1L,1L), na.last=FALSE)
###########################################
### Write Results
###########################################
FileNameOut=paste0(FileDir,'/Retrieve_Euro_EchangeRates.csv')
fwrite(EchangeRate, FileNameOut)
###########################################
### View Results
###########################################
View(EchangeRate) 
###########################################