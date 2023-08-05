import re
import time

currnet_year = str (time.localtime (time.time ()) [0])
mons = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
monf = ['january','february','march','april','may','june','july','august','september','october','november','december']

monalpha = "(?P<month>%s)\.?" % "|".join (monf + mons)
mondigit = '(?P<month>0?[1-9]|1[0-2])'
fmondigit = '(?P<month>0[1-9]|1[0-2])'
day = '(?P<day>0?[1-9]|[12][0-9]|3[01])(?:st|nd|rd|th)?(?:\sday)?(?:\sof)?'
fday = '(?P<day>0[1-9]|[12][0-9]|3[01])(?:st|nd|rd|th)?'
year4 = '(?P<year>20[01234][0-9])'
year2 = '(?P<year>[1234][0-9])'
delima = '([-\s,]+)'
delims = '([-./]+)'
digit_nofollow = '(?![0-9])'
digit_nolead = '(?<![0-9])'
date_formats = ('mdy', 'ymd', 'dmy')

MDY = (
    '[:monalpha:][:delima:][:day:][:delima:][:year4:][:dnf:]',
    '[:monalpha:][:delima:][:day:][:delima:][:year2:][:dnf:]',
    '[:dnl:][:mondigit:][:delims:][:day:][:delims:][:year4:][:dnf:]',
    '[:dnl:][:mondigit:][:delims:][:day:][:delims:][:year2:][:dnf:]',
    '[:monalpha:][:delima:][:day:][:dnf:]',
    '[:dnl:][:fmondigit:][:fday:][:year4:][:dnf:]',
    '[:dnl:][:fmondigit:][:fday:][:year2:][:dnf:]',
)

DMY = (    
    '[:dnl:][:day:][:delima:][:monalpha:][:delima:][:year4:][:dnf:]',
    '[:dnl:][:day:][:delima:][:monalpha:][:delima:][:year2:][:dnf:]',
    '[:dnl:][:day:][:delims:][:mondigit:][:delims:][:year4:][:dnf:]',
    '[:dnl:][:day:][:delims:][:mondigit:][:delims:][:year2:][:dnf:]',
    '[:dnl:][:day:][:delima:][:monalpha:]',    
    '[:dnl:][:fday:][:fmondigit:][:year4:][:dnf:]',
    '[:dnl:][:fday:][:fmondigit:][:year2:][:dnf:]',
)

YMD = (    
    '[:dnl:][:year4:][:delima:][:monalpha:][:delima:][:day:][:dnf:]',
    '[:dnl:][:year2:][:delima:][:monalpha:][:delima:][:day:][:dnf:]',
    '[:dnl:][:year4:][:delims:][:mondigit:][:delims:][:day:][:dnf:]',
    '[:dnl:][:year2:][:delims:][:mondigit:][:delims:][:day:][:dnf:]',    
    '[:dnl:][:year4:][:fmondigit:][:fday:][:dnf:]',
    '[:dnl:][:year2:][:fmondigit:][:fday:][:dnf:]',
)

FORMATS = {}
for fmt, group in (('mdy', MDY), ('dmy', DMY), ('ymd', YMD)):
    ngroup = []
    for each in group:
        each = each.replace ('[:monalpha:]', monalpha)
        each = each.replace ('[:mondigit:]', mondigit)
        each = each.replace ('[:fmondigit:]', fmondigit)
        each = each.replace ('[:delims:]', delims)
        each = each.replace ('[:delima:]', delima)
        each = each.replace ('[:day:]', day)
        each = each.replace ('[:fday:]',fday)
        each = each.replace ('[:year4:]', year4)
        each = each.replace ('[:year2:]', year2)
        each = each.replace ('[:dnf:]', digit_nofollow)
        each = each.replace ('[:dnl:]', digit_nolead)        
        ngroup.append (each)
    FORMATS [fmt] = ngroup

RXS = []
for dateformat in date_formats:
    for b in FORMATS [dateformat]:            
        exp = "(%s)" % (b)
        RXS.append (re.compile (exp, re.S))
        
#-------------------------------------------------------------
def normtext (content):
    rt = content.lower()
    rt = re.sub ('</?.*?>',' ',rt)        
    rt = rt.replace('\n',' ')
    rt = rt.replace('\r',' ')
    rt = rt.replace('\t',' ')
    rt = re.sub ('[ ]{2,}',' ', rt)    
    return rt

#-------------------------------------------------------------
def replace (content, token = '<date>'):
    content = normtext (content)
    for rx in RXS:
       content = rx.sub (token, content)            
    return content.strip ()   


if __name__ == "__main__":    
    print (parse_date ("""
<p>Two Rivers School District
Notice of invitation for bid (IFB)
The Two Rivers District will be accepting bids for the foodservice dept. for the 2017-18 school year, including grocery's, milk and juice, bread, and supply's. Bid packets may be picked up at the Superintendent's office during the week of June 5th-23rd. 
All bids must be received by Thursday, July 6th at 10:00am. Bids should be in a sealed envelope and will be opened Friday July 7th at 9:00 am. The Two Rivers School District follows all rules pertaining to Debarment and Suspension and will use small, minority, and women's businesses whenever possible. For further questions please call: Becky Fowler, Food Service Director at 479-272-3113.
74157186f 
    """, "mdy")
    )
    
    #print (parse_date ("jun 1, 17", "mdy", 0))
    #print (parse_date ("Closes 05/30/2017 05:00 PM CT Solicitation No 750.5-17-01 Title Off-Highway Vehicle (OHV) Use Map for the Little Missouri National Grasslands Issuing Agency Parks & Recreation, Department of", "mdy", 1))
    
    print (parse_date ('June 18, 2018 at 2 pm', "mdy", 0))
    print (parse_date ('RFQ packets must be returned by 12 p.m. on Wednesday, May 1, 2019.', "mdy", 1))
    