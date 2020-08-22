import datetime
 
class DateLine():
    def __init__(self):
        self.mon=[31,28,31,30,31,30,31,31,30,31,30,31]
        self.top=['Mo','Tu','We','Th','Fr','Sa','Su']
     
    def isleap(self,year):
        try:
           datetime.date(year,2,29)
           return True
        except ValueError: return False   
 
    def __str__(self):
        today=datetime.date.today()
        firstday=datetime.date(today.year,today.month,1)
        header=msg=""
        for i in range(firstday.weekday()):
            temp=self.top.pop(0)
            self.top.append(temp)
        if(self.isleap(today.year)):
              self.mon[1]=29
        days=self.mon[today.month-1]
        for i in 4*self.top+self.top[0:(days-28)]:
            header +=i + " "
        for i in range(1,days+1):
            msg += "%02d" %i + " "
        return header+" \n" +msg


class TimeInWords():

    def __init__(self):
        self.words=["one", "two", "three", "four", "five", "six", "seven", "eight","nine", 
        "ten", "eleven", "twelve", "thirteen", "fourteen", "quarter", "sixteen",
        "seventeen", "eighteen", "nineteen", "twenty", "twenty one", 
        "twenty two", "twenty three", "twenty four", "twenty five", 
        "twenty six", "twenty seven", "twenty eight", "twenty nine", "half"]

    def __str__(self):
        dd=datetime.datetime.now()
        hrs = dd.hour
        mins = dd.minute
        header="It's "
        msg=""
        if (hrs >12):
            hrs=hrs-12
        if (mins == 0):
            hr = self.words[hrs-1]
            msg=header + hr + " o'clock."
        elif (mins < 31):      
            hr = self.words[hrs-1]
            mn = self.words[mins-1]
            msg = header + mn + " minutes past " + hr + "."
        else:
            hr = self.words[hrs]
            mn =self.words[(60 - mins-1)]
            msg = header + mn + " minutes to " + hr + "."
        return msg

