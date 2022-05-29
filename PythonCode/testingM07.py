import datetime
import json
from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass
from datetime import timedelta
from datetime import datetime as dt


# -------------------------------------------
# Modify the holiday class to 
# 1. Only accept Datetime objects for date.
# 2. You may need to add additional functions
# 3. You may drop the init if you are using @dataclasses
# --------------------------------------------

#task in demo

class Holiday:
    
    DTF = '%Y-%m-%d'

      
    def __init__(self,name, date):
        #Your Code Here  
        self.name = name
        self.date = date 
    
    def __str__ (self):
        # String output
        # Holiday output when printed.
        return f'{self.name}, {self.date}'

halloween = Holiday('Halloween','2022-10-31')
print(halloween)

#def getHTML(url):
#    response = requests.get(url)
#    return response.text




#import requests
#response = requests.get("https://www.timeanddate.com/holidays/us/")
#print(response)

#html = 'https://www.timeanddate.com/holidays/us/'
#html_soup = BeautifulSoup(html, 'html.parser')
            #table = html_soup.find('table',attrs = {'id':'holidays-table'})    #one layer too high in html?
#table = html_soup.find('tbody')
            #print(table)       weird id attribute
#tablerow = table.find_all('tr')
#if 'hol_' not in tablerow:
#    for row in tablerow:
#        tabledate = row.find('th',attrs={'class':'nw'})    
#print(tabledate)

              
                
#print(type(Holiday))
#for row in table.find_all('tr'):
 #   cells = row.find_all('td')


#for row in table.find_all('body'):
 #   cells = row.find_all('tr')

#for holiday in table:
#    print(holiday)

#weekNum=2
#todaydate = datetime.datetime.today()           #today date 
#todayweeknum = datetime.datetime.today().isocalendar().week         #today weeknum
#weeks_apart = todayweeknum - weekNum    #current weeknum - user input

#print(weeks_apart)
#todaydate = datetime.datetime.today() +timedelta(day=1)
#print(todaydate)


#year=2022
#date = datetime.date(year, 1,1) + timedelta(weeks=weekNum)
#print(date)

#url = 'https://community-open-weather-map.p.rapidapi.com/forecast'       #past weather required parameters are lat,lon,dt
#url2 = 'https://community-open-weather-map.p.rapidapi.com/forecast/daily'
#headers = {           #given                                          
#            "X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com",
#            "X-RapidAPI-Key": "fd9874cbeemshfc4a6b08e010a22p13857fjsn0cd5b84b40b3"
#        }

#querystring = {"q":"san francisco,us"}   #given
#querystring = {"q":"san francisco,us","lat":"35","lon":"139","cnt":"10","units":"imperial"} 

#response = requests.get(urlforecast, headers=headers, params=querystring).json()
#response = requests.request("Get",url, headers=headers, params=querystring).json()
#data = response.json()
#print(type(responseDict))

#dates = []
#currentday = datetime.datetime.today()      #todays date
#dates.append(currentday)
#for i in range(1,7):                            #the previous 6 days
#    previousday = currentday+timedelta(days=i)
#    dates.append(previousday)

            #weather
#weather_list=[]
#time_stamp= '12:00:00'
#for i in range(5):
    #if time_stamp in response['list'][i]['dt_txt']: 
     #   weather = response['list'][i]['weather'][0]['description']
      #  weather_list.append(weather)
#    weather_list.append(data['list'][8*i]['weather'][0]['description'])     
#print(weather_list)



def filter_holidays_by_week(self,year, week_number):
        # Use a Lambda function to filter by week number and save this as holidays, use the filter on innerHolidays
        # Week number is part of the the Datetime object
        # Cast filter results as list       
        # return your holidays

    filter_year = list(filter(lambda x: x.date.year == year, self.innerHolidays))
    filter_week = list(filter(lambda x: x.date.isocalendar().week == week_number, filter_year))
    return filter_week





#def getWeather(self):
        # Convert weekNum to range between two days (2 digits 1-52)
        # Use Try / Except to catch problems
        # Query API for weather in that week range
        # Format weather information and return weather string.


        #date = datetime.date(2022, 1,1) + timedelta(weeks=weekNum)          #sunday of the weeknumber (the last day of the week)

#    url = 'https://community-open-weather-map.p.rapidapi.com/forecast'       #past weather required parameters are lat,lon,dt

#    headers = {           #given                                          
#            "X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com",
#            "X-RapidAPI-Key": "fd9874cbeemshfc4a6b08e010a22p13857fjsn0cd5b84b40b3"
#        }

#    querystring = {"q":"san francisco,us"}   #given


#    try:

            #weather
#        response = requests.request("GET", url, headers=headers, params=querystring)
#        info = response.json()

#        weather_List = []
#        for i in range(5):          #5 day forecast
#            weather_List.append(info['list'][8*i]['weather'][0]['description'])    

            #print(weatherList)
            

#        return weather_List

#    except:
#        print('There was an error accessing weather api')

def viewCurrentWeek(self):
    currentyr = datetime.datetime.today().isocalendar().year        
    currentweek = datetime.datetime.today().isocalendar().week
    fhlist = self.filter_holidays_by_week(currentyr,currentweek)

    dates = []
    currentday = datetime.datetime.today()      #todays date
    dates.append(currentday)
    for i in range(1,5):                            #the next 4 days
        previousday = currentday+timedelta(days=i)
        dates.append(previousday)


    question = input('Would you like to see this weeks weather [y/n]: ')
    if question == 'y':
        weather_List = self.getWeather()
        for i in range(0,len(dates)):
            print(f'{dates[i]}: {weather_List[i]}')


#viewCurrentWeek()





#url = "https://community-open-weather-map.p.rapidapi.com/forecast"
#querystring = {"q":"san francisco,us"}
#headers = {
#	        "X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com",
#	        "X-RapidAPI-Key": "032495499cmsh87a7f851860036ap143e00jsn16c55b0cdc5f"
 #       }
#response = requests.request("GET", url, headers=headers, params=querystring)
#info = response.json()

#weather_List = []
#for i in range(5):
#    weather_List.append(info['list'][8*i]['weather'][0]['description'])    #gives weather for the next 5 days
#print(weather_List)
       