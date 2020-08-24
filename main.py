import curses
import time
import sys
import pymysql
import pandas
from pandas import Series
from pandas import Series, DataFrame


def intro_code():

    print("*"*77)
    print("*  "+"\t\t\t\t\t\tMLB Pitcher Stats Calculator"+"\t\t\t\t\t\t*")
    print("*"+"\t"*19+"*")
    print("*  "+"\t\t\t\t\t\t\tcode by Leo Cho"+"\t\t\t\t\t\t\t\t\t*")
    print("*"+"\t"*19+"*")
    print("*  "+"To calculate salary in designated Team with given ERA, press '1'"+"\t\t\t*")
    print("*  "+"To print Players with similar performances with given ERA, press '2'"+"\t\t*")
    print("*  "+"To determine the predicted ranking with given ERA, press '3'"+"\t\t\t\t*")
    print("*  "+"To quit, press '0'"+"\t\t\t\t\t\t\t\t\t\t\t\t\t\t*")
    print("*"+"\t"*19+"*")
    print("*"*77)

def prog_code():

    a=int(input("Type Here : "))
    if a==1:
        team_name = input("type team name : ")

        new_era = float(input("type new era : "))

        conn = pymysql.connect(host='localhost', user='root', password='*****',
                               db='user', charset='utf8')

        curs = conn.cursor()

        sql = 'SELECT * FROM user.MLB  WHERE player_team = "%s";' % (team_name)

        curs.execute(sql)
        nv = [1, 'random', new_era, 1, 1, 'random', 1]
        rows = curs.fetchall()
        rows_list = list(rows)
        rows_list.append(nv)
        rows_list.sort(key=lambda element: element[2])

        era_list = []
        count = 0
        for i in rows_list:
            era_list.append(i[2])

        salary_list = []
        for i in rows_list:
            salary_list.append(i[3])

        df = DataFrame({'player_era': era_list, 'player_salary': salary_list}, columns=['player_era', 'player_salary'])
        df['rank_by_min'] = df['player_era'].rank(method='min', ascending=True)

        count = 0
        for i in df['player_era']:
            if i == new_era:
                break
            else:
                count = count + 1

        x = []
        x.append(sum(df['player_salary'].iloc[count - 1:count + 1]))
        print("$" + str(x[0] / 2))

        conn.close()
        prog_code()
    elif a==2:
        new_era = float(input("type new era : "))
        minus_era = new_era - 0.5
        plus_era = new_era + 0.5
        conn = pymysql.connect(host='localhost', user='root', password='*****',
                               db='user', charset='utf8')

        curs = conn.cursor()

        sql = 'SELECT * FROM user.MLB  WHERE player_era<%s and player_era>%s;' % (plus_era, minus_era)

        curs.execute(sql)

        rows = curs.fetchall()
        rows_list = list(rows)
        rows_list.sort(key=lambda element: element[3], reverse=True)

        for i in rows_list:
            print("%-20s  $%s" % (i[1], i[3]))
        prog_code()

    elif a==3:
        new_era = float(input("type new era : "))

        conn = pymysql.connect(host='localhost', user='root', password='*****',
                               db='user', charset='utf8')

        curs = conn.cursor()

        sql = 'SELECT * FROM user.MLB'

        curs.execute(sql)
        nv = [1, 'random', new_era, 1, 1, 'random', 1]
        rows = curs.fetchall()
        rows_list = list(rows)
        rows_list.append(nv)
        rows_list.sort(key=lambda element: element[2])

        era_list = []
        count = 0
        for i in rows_list:
            era_list.append(i[2])

        era_list_removed = list(filter(lambda a: a != 0.0, era_list))
        final = era_list_removed.index(new_era)
        array = Series(era_list_removed)
        ranks = array.rank(method='dense')
        print('your ranking is %dth' % (ranks[final]))
        prog_code()
    elif a==0:
        exit()
    else:
        print("redirected to start page due to wrong input")
        intro_code()
        prog_code()

intro_code()
prog_code()