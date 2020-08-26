# MLB-pitcher-stats-calculator

### Description
이 프로그램은 mlb 야구를 즐겨보던 중 투수들의 정보를 빠르게 알고 싶어서 만들게 되었다. Mlb에는 무수히 많은 투수들이 있지만 그들의 실력을 한눈에 비교하는 것은 어렵다. 그리고 누가 어느정도 실력에 어느정도의 연봉을 받는지도 궁금할 수 있다. 따라서 이 프로그램은 era정보 하나만으로 투수의 연봉을 예측, 비슷한 순위의 투수 추출, 그리고 총 등수까지 알려주는 기능을 가지고 있다.
***

### Data source

+ [MLB Data Api]("https://appac.github.io/mlb-data-api-docs/")

+ [USA Today]("https://www.usatoday.com/sports/mlb/salaries/")
***

### Code flow
<div>
<img src=https://user-images.githubusercontent.com/70150687/91303293-c14e9800-e7e2-11ea-8584-39e7283e942f.jpg>
</div>

***

### Function
#### 1) 들어가고싶은 구단에서 ERA 넣었을때 연봉

    **input** : team, era

    **output** : salary estimation

    **algorithm** : accept input, create sql list with all the players in designated team. Append a list with faulty values but the ERA. Sort the list by ERA. Create two new lists, and append all the ERA values from the previous list into one of them using ‘for’. Append all the salary values into the other new list, for the faulty value will not be put into account. Create a dataframe using pandas, which allows us to acquire the preceding and succeeding values . Create new list and append the dataframe, which is the sum of the two salary values. Print product by dividing into two.

#### 2) era 입력하면 실력 비슷한 친구들 뽑아주기

    **input** : era=float(input())

    **output** : name of other players

    **algorithm** : era from database for (input+-0.5)

#### 3) ERA 입력하면 mlb에서 몇등인지 뽑아주기

    **input** : era=float(input())

    **output** : number

    **algorithm** : era from database+new era⇒ list and sort, print([index(new era)])
***
