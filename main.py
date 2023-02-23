from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd
import time
from pytz import timezone
from datetime import datetime
import re
import smtplib
#from keep_alive import keep_alive


chrome_options = Options()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)
#direct it to the homepage
email_address="bartheart1717@gmail.com"
email_password="bemnet1712"

#keep_alive()
def ukraine():
    while True:
        central = timezone('US/Central')
        datetime_central=datetime.now(central)
        hours=datetime_central.strftime("%H")
        mins=datetime_central.strftime("%M")
        print(datetime_central)
        if hours=='02' and mins=='25':
            central = timezone('US/Central')
            datetime_central=datetime.now(central)
            print(datetime_central)
            
            
            years=datetime_central.strftime("%Y")
            months=datetime_central.strftime("%m")
            days=datetime_central.strftime("%d")
            hours=datetime_central.strftime("%H")
            mins=datetime_central.strftime("%M")
            
            #driver.get(todays_url)
            print(years)
            print(months)
            print(days)
            print(hours)
            print(mins)
            
            #todays_url=''
            driver.get('https://www.ohchr.org/en/search?query=Ukraine%3A+civilian+casualty+update')
            
            #find the first news article and click on it
            article1=driver.find_element(By.XPATH,'//article[@role="article"]//a')
            article1.click()
            
            news_block=driver.find_element(By.XPATH,'//div[@class="node-news__body"]').text
            dates=re.findall(r'(\d+ \w+ \d+) \(local time\)',news_block)
            
            try:
                published_dates=re.findall(r'Date: (\d+ \w+ \d+)',news_block)
            except:
                published_dates=[]
            
            casaulties=re.findall(r'([0-9]+[0-9,]+||[0-9]) casualties',news_block)
            deaths=re.findall(r'([0-9]+[0-9,]+) killed',news_block)
            injured=re.findall(r'([0-9]+[0-9,]+||[0-9]) injured',news_block)
            men=re.findall(r'([0-9]+[0-9,]+) men',news_block)
            women=re.findall(r'([0-9]+[0-9,]+) women',news_block)
            boys=re.findall(r'([0-9]+[0-9,]+||[0-9]) boys',news_block)
            girls=re.findall(r'([0-9]+[0-9,]+||[0-9]) girls',news_block)
            adults=re.findall(r'([0-9]+[0-9,]+||[0-9]) adults',news_block)
            childrens=re.findall(r'([0-9]+[0-9,]+||[0-9]) children',news_block)
            
            
            df =pd.DataFrame({'date':[''],
                            'publised_date':[''],
                            'total_death':[''],
                            'total_death_men':[''],
                            'total_death_women':[''],
                            'total_death_girls':[''],
                            'total_death_boys':[''],
                            'total_death_children':[''],
                            'total_death_adults':[''],
                            'total_injured':[''],
                            'total_injured_men':[''],
                            'total_injured_women':[''],
                            'total_injured_girls':[''],
                            'total_injured_boys':[''],
                            'total_injured_children':[''],
                            'total_injured_adults':[''],
                            'casualties_cptl':[''],
                            'death_cptl':[''],
                            'injured_cptl':[''],
                            'casaulties_gov_ctrl':[''],
                            'death_gov_ctrl':[''],
                            'injured_gov_ctrl':[''],
                            'casaulties_republic':[''],
                            'death_republic':[''],
                            'injured_republic':[''],
                            'casaulties_other_area':[''],
                            'death_other_area':[''],
                            'injured_other_area':['']
                            })
            
            
            date=dates[0]
            try:
                published_date=published_dates[0]
            except:
                published_date='NAN'
            
            total_death=deaths[0]
            total_death_men=men[0]
            total_death_women=women[0]
            total_death_girls=girls[0]
            total_death_boys=boys[0]
            total_death_children=childrens[0]
            total_death_adults=adults[0]
            
            total_injured=injured[1]
            total_injured_men=men[1]
            total_injured_women=women[1]
            total_injured_girls=girls[1]
            total_injured_boys=boys[1]
            total_injured_children=childrens[1]
            total_injured_adults=adults[1]
            
            casualties_cptl=casaulties[1]
            death_cptl=deaths[2]
            injured_cptl=injured[2]
            
            casaulties_gov_ctrl=casaulties[2]
            death_gov_ctrl=deaths[3]
            injured_gov_ctrl=injured[3]
            
            casaulties_republic=casaulties[3]
            death_republic=deaths[4]
            injured_republic=injured[4]
            
            casaulties_other_area=casaulties[5]
            death_other_area=deaths[5]
            injured_other_area=injured[5]
            
            df = df.append({  'date':date,
                            'published_date':published_date,
                            'total_death':total_death,
                            'total_death_men':total_death_men,
                            'total_death_women':total_death_women,
                            'total_death_girls':total_death_girls,
                            'total_death_boys':total_death_boys,
                            'total_death_children':total_death_children,
                            'total_death_adults':total_death_adults,
                            'total_injured':total_injured,
                            'total_injured_men':total_injured_men,
                            'total_injured_women':total_injured_women,
                            'total_injured_girls':total_injured_girls,
                            'total_injured_boys':total_injured_boys,
                            'total_injured_children':total_injured_children,
                            'total_injured_adults':total_injured_adults,
                            'casualties_cptl':casualties_cptl,
                            'death_cptl':death_cptl,
                            'injured_cptl':injured_cptl,
                            'casaulties_gov_ctrl':casaulties_gov_ctrl,
                            'death_gov_ctrl':death_gov_ctrl,
                            'injured_gov_ctrl':injured_gov_ctrl,
                            'casaulties_republic':casaulties_republic,
                            'death_republic':death_republic,
                            'injured_republic':injured_republic,
                            'casaulties_other_area':casaulties_other_area,
                            'death_other_area':death_other_area,
                            'injured_other_area':injured_other_area},ignore_index=True)
            
            
            
            with smtplib.SMTP('smtp.gmail.com',587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()
                
                smtp.login(email_address,email_password)
                
                subject="Date:"+str(date)
                body="Total number of deaths:"+str(total_death)
                
                msg=f'Subject:{subject}\n\n{body}'
                
                smtp.sendmail(email_address,email_address,msg)
                print('Email is sent')
            time.sleep(50)
        

            

        time.sleep(10)
    return(df) 

ukraine()
        