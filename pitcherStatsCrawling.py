import requests
import pymysql
import json
from bs4 import BeautifulSoup

player_season = int(input("which season? : "))
salary_average=[]
name=[]
position=[]
def crawler():
    url = "https://www.usatoday.com/sports/mlb/salaries/"
    html = requests.get(url)
    soup= BeautifulSoup(html.text,'html.parser')
    result1=soup.find_all('td', class_='salary_average')
    result2=soup.find_all('td', class_='position')
    result3=soup.find_all('div', class_='sp-details-open')
    for i in result1:
        salary_average.append(i.text.strip().replace("$","").replace(",",""))
    for i in result2:
        position.append(i.text.strip())
    for i in result3[5:]:
        name.append(i.text.strip())

crawler()

user_db = pymysql.connect(user='root',password='*****',host='127.0.0.1',db='user',charset='utf8')
for idx,val in enumerate(position):
    if val == 'SP':
        try:
            # print(salary_average[idx],position[idx],name[idx].split(" ")[1])
            url = "http://lookup-service-prod.mlb.com/json/named.search_player_all.bam?sport_code='mlb'&active_sw='Y'&name_part='" + name[idx].split()[1] + "%25'"
            r = requests.get(url=url)
            json_data = r.json()
            player_id = json_data['search_player_all']['queryResults']['row']['player_id']
            player_name = json_data['search_player_all']['queryResults']['row']['name_display_first_last']
            player_birthdate= json_data['search_player_all']['queryResults']['row']['birth_date']
            player_team= json_data['search_player_all']['queryResults']['row']['team_full']

            url2 = " http://lookup-service-prod.mlb.com/json/named.proj_pecota_pitching.bam?season='"+ str(player_season) +"'&player_id='" + player_id + "'"
            r2 = requests.get(url=url2)
            json_data2 = r2.json()
            era = (json_data2['proj_pecota_pitching']['queryResults']['row']['era'])
            sql="INSERT INTO MLB(player_id,player_name,player_era,player_salary_average,player_birthdate,player_team,player_season)VALUES(%s,'%s',%s,%s,'%s','%s',%s);" % (player_id, name[idx], era, salary_average[idx],player_birthdate,player_team,player_season)
            cursor = user_db.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql)
            user_db.commit()
        except:
            print("no data")


