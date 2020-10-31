# Azure notes
**ssh -i C:\Users\vreez\scrap3_key.pem azureuser@13.92.155.233**

# INSTALL

**sudo apt update**

## change directory etc...
**git clone https://github.com/vreezy/ingress_scraper.git**

**sudo apt install python-pip**

**pip install -r requirements.txt**

## copy and paste example ini and add cookie settings (bottom of readme -< getCOOKIE>)
**nano default.ini**

**python scrape_portal.py -s**

## webservice
**pip install Flask**

**python webserver.py**

# TEST
**http://13.92.155.233:5000/test/**

# FINAL
**http://13.92.155.233:5000/zone1/**


---
# getCOOKIE
original API by https://github.com/lc4t/ingress-api
since it was last modified in 2017, since URL of intel map has changed so installing ingressAPI via pip will install version that have old url. 


**Attention: Remember scrapping too often and big areas can cause account's ban. Don't use your private accounts.**

In order to make API work you need cookies from ingress's intel site. 
1. Log into you ingress account here https://intel.ingress.com/intel
2. Press F12 and go into Network tab , then press F5(refresh) to refresh browser and to reload all info in newtowrk tab then select intel in left coulumn and Headers in right, you should see *cookie* in **Request Headers**


![csrftoken-same-cookie](https://i.imgur.com/hyJ0ftT.jpg)




3. copy everything after **cookie:** and paste in Cookie section of default.ini
