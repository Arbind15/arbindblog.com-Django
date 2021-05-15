import requests, lxml
from bs4 import BeautifulSoup as bs
import geoip2.database
import ipinfo,random



def Corona_Update():
    try:
        main_lnk='https://www.worldometers.info/coronavirus/'
        lnk='https://www.worldometers.info/coronavirus/country/nepal/'
        tittle='Corona Update-Nepal'
        health_source=requests.get('https://www.worldometers.info/coronavirus/country/nepal/').text
        s_code=bs(health_source,'lxml')
        Source='worldometers.info'
        bdy=s_code.find('body')
        src_img='https://www.worldometers.info/img/worldometers-logo.gif'
        covid=bdy.find_all('div',class_='maincounter-number')
        dateandtime=bdy.find('div',class_='content-inner')
        dateandtime=dateandtime.find('div',style='font-size:13px; color:#999; text-align:center').text
        # print(dateandtime)
        num=[]
        for div in covid:
            spn=div.span
            num.append(spn.text)
        body_content=["Total Cases: "+str(num[0]),
                      "Total Recovered: " + str(num[2]),"Total Deaths: " + str(num[1])]
        # print(body_content)
        covid_list=[[tittle,src_img,dateandtime,body_content,lnk,Source,main_lnk,False]]
        return covid_list
    except:
        covid_list=[]
        return covid_list

def bbc_nepali():
    try:
        main_lnk = 'https://www.bbc.com/nepali'
        src_img='https://www.liveonlineradio.net/wp-content/uploads/2011/06/bbc-nepali-1-100x47.jpg'
        main_source = requests.get(main_lnk).text
        s_code = bs(main_source, 'lxml')
        Source = 'BBC NEWS | नेपाली'
        bdy = s_code.find('body')
        divs=bdy.find_all('div',class_='TextGridItem-sc-1lkbq5i-0 jJWtYv')
        main_lst=[]
        for div in divs[:10]:
            tittle=div.h3.a.text
            lnk=div.h3.a['href']
            lnk='https://www.bbc.com'+lnk
            body_content=[div.p.text]
            dateandtime=div.time['datetime']
            content=[tittle,src_img,dateandtime,body_content,lnk,Source,main_lnk,False]
            main_lst.append(content)
        # print(main_lst)
        return main_lst
    except:
        main_lst=[]
        return main_lst


def weather(ip):
    # cities=geoip2.database.Reader('GeoLite2-City.mmdb')
    # city=cities.city('103.104.28.149')
    # print(city)

    access_token = '16149689d259f0'
    ip_address = '103.104.28.149'
    ip_address = ip
    # try:
    #     handler = ipinfo.getHandler(access_token)
    #     details = handler.getDetails(ip_address)
    #     # print(details.all)
    #     city=details.city
    #     main_lnk=f"https://api.openweathermap.org/data/2.5/weather?q={str(city).lower()}&appid=0d9d6dc28fe68a58cab37d77696e62ea&units=metric"
    #     # print(main_lnk)
    #     main_data=requests.get(main_lnk).json()
    #     weather=main_data['weather']
    #     # print(main_data)
    #     # print(weather[0]['description'])
    #     avg_temp=main_data['main']['temp']
    #     humidity=main_data['main']['humidity']
    #     summary=weather[0]['description']
    #     wheather_info=[
    #         f'Avg. temp.: {avg_temp} ',
    #         f'Humidity: {humidity}',
    #         f'Weather: {summary}',
    #         f'Location: {city}',
    #         f'IP: {ip}',
    #     ]
    #     # print(wheather_info)
    #     return wheather_info
    # except:
    #     wheather_info='None'
    #     return wheather_info


    try:
        handler = ipinfo.getHandler(access_token)
        details = handler.getDetails(ip_address)
        # print(details.all)
        city = details.city
        # print(str(city))
        main_lnk = f"https://api.openweathermap.org/data/2.5/weather?q={str(city).lower()}&appid=0d9d6dc28fe68a58cab37d77696e62ea&units=metric"
        # print(main_lnk)
        main_data=requests.get(main_lnk).json()
        try:
            weather = main_data['weather']
            # print(main_data)
            # print(weather[0]['description'])
            avg_temp=main_data['main']['temp']
            humidity=main_data['main']['humidity']
            summary=weather[0]['description']
            wheather_info=[
                f'Avg. temp.: {avg_temp} ',
                f'Humidity: {humidity}',
                f'Weather: {summary}',
                f'Location: {city}',
                # f'IP: {ip}',
            ]
            # print(wheather_info)
            return wheather_info
        except:
            city = details.country_name
            # print(city)
            main_lnk = f"https://api.openweathermap.org/data/2.5/weather?q={str(city).lower()}&appid=0d9d6dc28fe68a58cab37d77696e62ea&units=metric"
            # print(main_lnk)
            main_data = requests.get(main_lnk).json()
            weather = main_data['weather']
            # print(main_data)
            # print(weather[0]['description'])
            avg_temp = main_data['main']['temp']
            humidity = main_data['main']['humidity']
            summary = weather[0]['description']
            wheather_info = [
                f'Avg. temp.: {avg_temp} ',
                f'Humidity: {humidity}',
                f'Weather: {summary}',
                f'Location: {city}',
                # f'IP: {ip}',
            ]
            # print(wheather_info)
            return wheather_info
    except:
        wheather_info = 'None'
        return wheather_info



# weather('103.1.28.149')

def neb():
    try:
        main_lnk = 'http://www.neb.gov.np/notices'
        main_source = requests.get(main_lnk).text
        s_code = bs(main_source, 'lxml')
        Source = 'neb.gov.np'
        src_img='http://www.neb.gov.np/application/resources/hseb_front/images/favicon.png'
        divs = s_code.find_all('div',class_='row col-xs-12')
        # print(divs)
        main_lst=[]
        for div in divs[:3]:
            content=div.a.h4.text
            dateandtime=div.h5.text
            # print(dateandtime)
            # print(content)
            sub_lnk=div.a['href']
            main_source = requests.get(sub_lnk).text
            s_code = bs(main_source, 'lxml')
            sub_div = s_code.find('div', class_='col-md-12 noticeDetails')
            lnk=sub_div.a['href']
            content=['नेपाल राष्ट्रिय परीक्षा बोर्ड',src_img,dateandtime,[content],lnk,Source,main_lnk,False]
            main_lst.append(content)
        # print(main_lst)
        return main_lst
    except:
        main_lst=[]
        return main_lst
# neb()

def health():
    try:
        main_lnk = 'https://www.mohp.gov.np/en/news/news'
        main_source = requests.get(main_lnk).text
        s_code = bs(main_source, 'lxml')
        Source = 'mohp.gov.np'
        src_img='https://www.mohp.gov.np/templates/urbanus/favicon.ico'
        divs1 = s_code.find_all('tr',class_='odd')
        divs2 = s_code.find_all('h1', class_='entry-title')
        # print(divs.a.text)
        main_lst = []
        for div1, div2 in zip(divs1[:3],divs2[:3]):
            content=div2.a.text
            dateandtime=div1.find('td',class_='at_created_date').text
            lnk=div1.a['href']
            lnk=str(lnk).replace(" ",'%20')
            content = ['स्वास्थ्य तथा जनसंख्या मन्त्रालय', src_img, dateandtime, [content], lnk, Source, main_lnk, False]
            main_lst.append(content)
        return main_lst
    except:
        main_lst=[]
        return main_lst

# print(health())
def ScrapAll():
    l1=Corona_Update()
    l2=bbc_nepali()
    l3=neb()
    l4=health()
    mn_lst=[]
    for lst in l1:
        mn_lst.append(lst)
    for lst in l2:
        mn_lst.append(lst)
    for lst in l3:
        mn_lst.append(lst)
    for lst in l4:
        mn_lst.append(lst)

    random.shuffle(mn_lst)
    return mn_lst