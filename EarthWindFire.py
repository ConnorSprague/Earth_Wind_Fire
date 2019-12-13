# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 14:22:07 2019

@author: fo628e
"""

import requests
from datetime import date

class date_formatter:
    today = date.today()

    def __init__(self):
        self.day_number = self.today.strftime("%d") #string, 22
        self.month = self.today.strftime("%B") #November
        self.basic_day = self.today.strftime("%B %d") #November 22
        self.shorthand_ordinal = 'empty'
        self.longhand_ordinal = 'empty'
        self.num_to_text = 'empty'
        

    def num2words(self):
        num = int(self.day_number)
        under_20 = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine',
                    'Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
        tens = ['Twenty','Thirty']
    
        if num < 20:
            self.num_to_text = under_20[num]
        else:
            self.num_to_text = tens[(int)(num/10)-2] + ('' if num%10==0 else ' ' + under_20[num%10])
            
        return(self.month+' '+self.num_to_text)
            
    def shorthand_date_ordinals(self):
        #date must be string
        #returns format; 22nd
        num = self.day_number
        last_digit = num[-1]
        
        if last_digit=='1':
            self.shorthand_ordinal = num+'st'
        elif last_digit=='2':
            self.shorthand_ordinal = num+'nd'
        elif last_digit=='3':
            self.shorthand_ordinal = num+'rd'
        else:
            self.shorthand_ordinal = num+'th'
            
        return(self.month+' '+self.shorthand_ordinal)
        
    def longhand_date_ordinals(self):
        #returns format: Twenty Second
        num = self.day_number
#        hold = self.num_to_text.split(' ')
#        if num 
#        non_zeroes = ['','first','second','third','fourth','fifth','sixth','seventh','eighth','ninth']
#        power = str(hold[0])
#        last_digit = num[-1]
#        if int(num) % 10 != 0:
#            self.longhand_ordinal = self.month+' '+power
        cheaters_translation = ['','first','second','third','fourth','fifth','sixth','seventh','eighth','ninth',
                       'tenth','eleventh','twelfth','thirteenth','fourteenth','fifteenth','sixteenth','seventeenth',
                       'eighteenth','nineteenth','twentieth','twenty-first','twenty-second','twenty-third','twenty-fourth',
                       'twenty-fifth','twenty-sixth','twenty-seventh','twenty-eighth','twenty-nineth','thirtieth', 'thirty-first']
        self.longhand_ordinal = self.month+' '+cheaters_translation[int(num)]
        return(self.longhand_ordinal)
    

    
    

class musixmatch:
    def __init__(self, dates):
        self.dates = dates
        
    def build_request(self):
        #format input dates into string
        return()
        
    def request_released_today(self):
        date_request = build_request(self.dates)
        api_string = ''
        return()
        
    def request_about_today(self):
        date_request = build_request(self.dates)
        api_string = ''
        return()
        
        


#API KEY

#API inputs
#q for query
#Most popular Songs about today   http://api.musixmatch.com/ws/1.1/track.search?q={my dates}&s_track_rating=desc
#Most popular songs songs released today http://api.musixmatch.com/ws/1.1/track.search?f_track_release_group_first_release_date_min={YYYYMMDD}&f_track_release_group_first_release_date_max={YYYYMMDD}&s_track_rating=desc

def main():
    my_date = date_formatter()

    today_date_array = [my_date.basic_day, my_date.num2words(),
                        my_date.shorthand_date_ordinals(),
                        my_date.longhand_date_ordinals()]
    request_string = ''
    for i in today_date_array:
        print(i)
        request_string = request_string + i + ','
    request_string = request_string[:-1]


main()