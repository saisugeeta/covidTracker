# -*- coding: utf-8 -11*-
"""
Spyder Editor

This is a temporary script file.
"""

# Librariies Import
import requests
import pandas as pd
import numpy as np
from flask import Flask,request,jsonify,render_template
from bs4 import BeautifulSoup
from flask_apscheduler import APScheduler
scheduler=APScheduler()# For Scheduling Every 1 second
def web_scraping():
        URl="https://www.grainmart.in/news/covid-19-coronavirus-india-state-and-district-wise-tally/"
        html_page=requests.get(URl).text
        #print(html_page)
        soup=BeautifulSoup(html_page,'lxml')
        #print(soup)
        table_data=soup.find("section",id="covid-19-table")
        get_table_data=table_data.find_all("div",{"class":"skgm-states"})
        #print(table_data)
        map_values={}
        only_states={}
        for i in range(len(get_table_data)):
            key=get_table_data[i].find_all("span",{"class":"show-district"})[0].text
            map_values[key]={}
            map_values[key]["Cases"]=get_table_data[i].find("div",{"class":"td-sc"}).text
            map_values[key]["Cured"]=get_table_data[i].find("div",{"class":"td-sr"}).text
            map_values[key]["Active"]=get_table_data[i].find("div",{"class":"td-sa"}).text
            map_values[key]["Deaths"]=get_table_data[i].find("div",{"class":"td-sd"}).text
            map_values[key]["Districts"]={}
            only_states[key]={}
        
            only_states[key]["Cases"]=get_table_data[i].find("div",{"class":"td-sc"}).text
            only_states[key]["Cured"]=get_table_data[i].find("div",{"class":"td-sr"}).text
            only_states[key]["Active"]=get_table_data[i].find("div",{"class":"td-sa"}).text
            only_states[key]["Deaths"]=get_table_data[i].find("div",{"class":"td-sd"}).text
            
            get_district_table=get_table_data[i].find_all("div",{"class":"skgm-tr"})
            for j in range(len(get_district_table)):
                city_key=get_district_table[j].find("div",{"class":"skgm-td"}).text
                
                if city_key.strip()!=key.strip():
                    
                    
                    map_values[key]["Districts"][city_key]={}
                    map_values[key]["Districts"][city_key]["Cases"]=get_district_table[j].find("div",{"class":"td-dc"}).text
                    map_values[key]["Districts"][city_key]["Cured"]=get_district_table[j].find("div",{"class":"td-dr"}).text
                    map_values[key]["Districts"][city_key]["Active"]=get_district_table[j].find("div",{"class":"td-da"}).text
                    map_values[key]["Districts"][city_key]["Deaths"]=get_district_table[j].find("div",{"class":"td-dd"}).text
        return map_values    
                #print("jjkhdsgjftjdfkydfgky")
         
    
    

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])

def dashboard():
    return render_template("home.html",dataframe=map_values)

if __name__=="__main__":
    map_values=web_scraping()
    scheduler.add_job(id='Scheduled task',func=web_scraping,trigger='interval',seconds=60)
    scheduler.start()

    app.run(debug=True)# -*- coding: utf-8 -*-

