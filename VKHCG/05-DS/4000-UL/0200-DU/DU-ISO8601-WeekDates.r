library("lubridate")
lastweek=paste0("-",12,"-",31)
x <- paste0(1900:2020, lastweek, sep = "")
y <- as.Date(x)
z <- y+1
WeekValue<-data.frame(date = y, weekdate = ISOweek(y), weeknum = week(y), date2 = z, weekdate2 = ISOweek(z))