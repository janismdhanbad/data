from urllib2 import urlopen

from bs4 import BeautifulSoup
import pandas as pd
import re

import numpy as np

class scrape:


    def internshala(self,link):
        link = str(link)
        html = urlopen(link)
        html_soup = BeautifulSoup(html, 'html.parser')
        total = len(html_soup.findAll('div',attrs={"class":"container-fluid individual_internship"}))
        internships_and_jobs1 = pd.DataFrame(np.arange(1000),columns=["Nature_of_job"])
        internships_and_jobs1["name_of_company"] = np.nan
        internships_and_jobs1["start_date"] = np.nan
        internships_and_jobs1["duration"] = np.nan
        internships_and_jobs1["stipened"] = np.nan
        internships_and_jobs1["posted_on"] = np.nan
        internships_and_jobs1["apply_by"] = np.nan
        internships_and_jobs1["brief_description"] = np.nan
        internships_and_jobs1["Nature_of_job"] = np.nan
        internships_and_jobs1["city"] = np.nan  
        
        for i in np.arange(total):
            try :
                name_of_company = str(html_soup.findAll('div',attrs={"class":"container-fluid individual_internship"})[i].findAll('div',attrs={"class":"individual_internship_header"})[0].findAll('div',attrs={"class":"table-cell"})[0].findAll('h4')[1].findAll('a')[0].contents[0])
                internships_and_jobs1.name_of_company.iloc[i] = name_of_company
        
            except IndexError :
                internships_and_jobs1.name_of_company.iloc[i] = "no_value"
            try:    
                nature_of_job = str(html_soup.findAll('div',attrs={"class":"container-fluid individual_internship"})[i].findAll('div',attrs={"class":"individual_internship_header"})[0].findAll('div',attrs={"class":"table-cell"})[0].findAll('h4')[0].get('title'))
                internships_and_jobs1.Nature_of_job.iloc[i] = nature_of_job
            except IndexError:
                internships_and_jobs1.Nature_of_job.iloc[i] = "no_value"
            try:
                brief_description = str(html_soup.findAll('div',attrs={"class":"container-fluid individual_internship"})[i].findAll('div',attrs={"class":"individual_internship_header"})[0].findAll('div',attrs={"class":"table-cell"})[1].findAll('div',attrs={"class":"internship_logo"})[0].findAll('img')[0].get('alt'))
                internships_and_jobs1.brief_description.iloc[i] = brief_description
            except IndexError:
                internships_and_jobs1.brief_description.iloc[i] = "no_value"
            try:
                city = str(html_soup.findAll('div',attrs={"class":"container-fluid individual_internship"})[i].findAll('div',attrs={"class":"individual_internship_details"})[0].findAll('a')[0].contents[0])
                internships_and_jobs1.city.iloc[i] = city
            except IndexError:
                internships_and_jobs1.city.iloc[i] ="no_value"
            try:
                when_to_start = str(html_soup.findAll('div',attrs={"class":"container-fluid individual_internship"})[i].findAll('div',attrs={"class":"individual_internship_details"})[0].findAll('td')[0].findAll('div',attrs={"id":"start-date-first"})[0].contents[0])
                when_to_start = re.sub('\r\n','',when_to_start)
                when_to_start = re.sub(' ','',when_to_start)
                internships_and_jobs1.start_date.iloc[i] = when_to_start
            except IndexError:
                internships_and_jobs1.start_date.iloc[i] = "no_value"
            try:
                stipend = str(html_soup.findAll('div',attrs={"class":"container-fluid individual_internship"})[i].findAll('div',attrs={"class":"individual_internship_details"})[0].findAll('td')[2].contents[2])
                stipend = re.sub(' ','',stipend)        
                internships_and_jobs1.stipened.iloc[i] = stipend
            except IndexError:
                internships_and_jobs1.stipened.iloc[i] = "no_value"
            try:
                apply_by = str(html_soup.findAll('div',attrs={"class":"container-fluid individual_internship"})[i].findAll('div',attrs={"class":"individual_internship_details"})[0].findAll('td')[4].contents[0])
                apply_by = re.sub('\r\n','',apply_by)
                apply_by = re.sub(' ','',apply_by)
                internships_and_jobs1.apply_by.iloc[i] = apply_by
            except IndexError:
                internships_and_jobs1.apply_by.iloc[i] = "no_value"
            try:
                posted_on = str(html_soup.findAll('div',attrs={"class":"container-fluid individual_internship"})[i].findAll('div',attrs={"class":"individual_internship_details"})[0].findAll('td')[3].contents[0])
                posted_on = re.sub(' ','',posted_on)
                posted_on = re.sub('\r\n','',posted_on)
                internships_and_jobs1.posted_on.iloc[i] = posted_on
            except IndexError:
                internships_and_jobs1.posted_on.iloc[i] = "no_value"
            try:    
                duration = str(html_soup.findAll('div',attrs={"class":"container-fluid individual_internship"})[i].findAll('div',attrs={"class":"individual_internship_details"})[0].findAll('td')[1].contents[0])
                duration = re.sub('\r\n','',duration)
                duration =re.sub(' ','',duration)        
                internships_and_jobs1.duration.iloc[i] = duration
            except IndexError:    
                internships_and_jobs1.duration.iloc[i] = "no_value"
    
        internships_and_jobs1.iloc[0:total,:].to_csv("internship.csv",index = False)


