```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```


```python
ted=pd.read_csv('C:/Users/20171/Desktop/python/2430e04f-4488-4432-ad6c-4c3571f49bd2/ted_main.csv')
ted.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>comments</th>
      <th>description</th>
      <th>duration</th>
      <th>event</th>
      <th>film_date</th>
      <th>languages</th>
      <th>main_speaker</th>
      <th>name</th>
      <th>num_speaker</th>
      <th>published_date</th>
      <th>ratings</th>
      <th>related_talks</th>
      <th>speaker_occupation</th>
      <th>tags</th>
      <th>title</th>
      <th>url</th>
      <th>views</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4553</td>
      <td>Sir Ken Robinson makes an entertaining and pro...</td>
      <td>1164</td>
      <td>TED2006</td>
      <td>1140825600</td>
      <td>60</td>
      <td>Ken Robinson</td>
      <td>Ken Robinson: Do schools kill creativity?</td>
      <td>1</td>
      <td>1151367060</td>
      <td>[{'id': 7, 'name': 'Funny', 'count': 19645}, {...</td>
      <td>[{'id': 865, 'hero': 'https://pe.tedcdn.com/im...</td>
      <td>Author/educator</td>
      <td>['children', 'creativity', 'culture', 'dance',...</td>
      <td>Do schools kill creativity?</td>
      <td>https://www.ted.com/talks/ken_robinson_says_sc...</td>
      <td>47227110</td>
    </tr>
    <tr>
      <th>1</th>
      <td>265</td>
      <td>With the same humor and humanity he exuded in ...</td>
      <td>977</td>
      <td>TED2006</td>
      <td>1140825600</td>
      <td>43</td>
      <td>Al Gore</td>
      <td>Al Gore: Averting the climate crisis</td>
      <td>1</td>
      <td>1151367060</td>
      <td>[{'id': 7, 'name': 'Funny', 'count': 544}, {'i...</td>
      <td>[{'id': 243, 'hero': 'https://pe.tedcdn.com/im...</td>
      <td>Climate advocate</td>
      <td>['alternative energy', 'cars', 'climate change...</td>
      <td>Averting the climate crisis</td>
      <td>https://www.ted.com/talks/al_gore_on_averting_...</td>
      <td>3200520</td>
    </tr>
    <tr>
      <th>2</th>
      <td>124</td>
      <td>New York Times columnist David Pogue takes aim...</td>
      <td>1286</td>
      <td>TED2006</td>
      <td>1140739200</td>
      <td>26</td>
      <td>David Pogue</td>
      <td>David Pogue: Simplicity sells</td>
      <td>1</td>
      <td>1151367060</td>
      <td>[{'id': 7, 'name': 'Funny', 'count': 964}, {'i...</td>
      <td>[{'id': 1725, 'hero': 'https://pe.tedcdn.com/i...</td>
      <td>Technology columnist</td>
      <td>['computers', 'entertainment', 'interface desi...</td>
      <td>Simplicity sells</td>
      <td>https://www.ted.com/talks/david_pogue_says_sim...</td>
      <td>1636292</td>
    </tr>
    <tr>
      <th>3</th>
      <td>200</td>
      <td>In an emotionally charged talk, MacArthur-winn...</td>
      <td>1116</td>
      <td>TED2006</td>
      <td>1140912000</td>
      <td>35</td>
      <td>Majora Carter</td>
      <td>Majora Carter: Greening the ghetto</td>
      <td>1</td>
      <td>1151367060</td>
      <td>[{'id': 3, 'name': 'Courageous', 'count': 760}...</td>
      <td>[{'id': 1041, 'hero': 'https://pe.tedcdn.com/i...</td>
      <td>Activist for environmental justice</td>
      <td>['MacArthur grant', 'activism', 'business', 'c...</td>
      <td>Greening the ghetto</td>
      <td>https://www.ted.com/talks/majora_carter_s_tale...</td>
      <td>1697550</td>
    </tr>
    <tr>
      <th>4</th>
      <td>593</td>
      <td>You've never seen data presented like this. Wi...</td>
      <td>1190</td>
      <td>TED2006</td>
      <td>1140566400</td>
      <td>48</td>
      <td>Hans Rosling</td>
      <td>Hans Rosling: The best stats you've ever seen</td>
      <td>1</td>
      <td>1151440680</td>
      <td>[{'id': 9, 'name': 'Ingenious', 'count': 3202}...</td>
      <td>[{'id': 2056, 'hero': 'https://pe.tedcdn.com/i...</td>
      <td>Global health expert; data visionary</td>
      <td>['Africa', 'Asia', 'Google', 'demo', 'economic...</td>
      <td>The best stats you've ever seen</td>
      <td>https://www.ted.com/talks/hans_rosling_shows_t...</td>
      <td>12005869</td>
    </tr>
  </tbody>
</table>
</div>




```python
#调整特征顺序
ted = ted[['name', 'title', 'description', 'main_speaker', 'speaker_occupation', 'num_speaker', 'duration', 'event', 'film_date', 'published_date', 'comments', 'tags', 'languages', 'ratings', 'related_talks', 'url', 'views']]
import datetime
#将日期转换成可读形式
ted['film_date'] = ted['film_date'].apply(lambda x: datetime.datetime.fromtimestamp(int(x)).strftime('%d-%m-%Y'))
ted['published_date'] = ted['published_date'].apply(lambda x: datetime.datetime.fromtimestamp(int(x)).strftime('%d-%m-%Y'))
ted.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>title</th>
      <th>description</th>
      <th>main_speaker</th>
      <th>speaker_occupation</th>
      <th>num_speaker</th>
      <th>duration</th>
      <th>event</th>
      <th>film_date</th>
      <th>published_date</th>
      <th>comments</th>
      <th>tags</th>
      <th>languages</th>
      <th>ratings</th>
      <th>related_talks</th>
      <th>url</th>
      <th>views</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Ken Robinson: Do schools kill creativity?</td>
      <td>Do schools kill creativity?</td>
      <td>Sir Ken Robinson makes an entertaining and pro...</td>
      <td>Ken Robinson</td>
      <td>Author/educator</td>
      <td>1</td>
      <td>1164</td>
      <td>TED2006</td>
      <td>25-02-2006</td>
      <td>27-06-2006</td>
      <td>4553</td>
      <td>['children', 'creativity', 'culture', 'dance',...</td>
      <td>60</td>
      <td>[{'id': 7, 'name': 'Funny', 'count': 19645}, {...</td>
      <td>[{'id': 865, 'hero': 'https://pe.tedcdn.com/im...</td>
      <td>https://www.ted.com/talks/ken_robinson_says_sc...</td>
      <td>47227110</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Al Gore: Averting the climate crisis</td>
      <td>Averting the climate crisis</td>
      <td>With the same humor and humanity he exuded in ...</td>
      <td>Al Gore</td>
      <td>Climate advocate</td>
      <td>1</td>
      <td>977</td>
      <td>TED2006</td>
      <td>25-02-2006</td>
      <td>27-06-2006</td>
      <td>265</td>
      <td>['alternative energy', 'cars', 'climate change...</td>
      <td>43</td>
      <td>[{'id': 7, 'name': 'Funny', 'count': 544}, {'i...</td>
      <td>[{'id': 243, 'hero': 'https://pe.tedcdn.com/im...</td>
      <td>https://www.ted.com/talks/al_gore_on_averting_...</td>
      <td>3200520</td>
    </tr>
    <tr>
      <th>2</th>
      <td>David Pogue: Simplicity sells</td>
      <td>Simplicity sells</td>
      <td>New York Times columnist David Pogue takes aim...</td>
      <td>David Pogue</td>
      <td>Technology columnist</td>
      <td>1</td>
      <td>1286</td>
      <td>TED2006</td>
      <td>24-02-2006</td>
      <td>27-06-2006</td>
      <td>124</td>
      <td>['computers', 'entertainment', 'interface desi...</td>
      <td>26</td>
      <td>[{'id': 7, 'name': 'Funny', 'count': 964}, {'i...</td>
      <td>[{'id': 1725, 'hero': 'https://pe.tedcdn.com/i...</td>
      <td>https://www.ted.com/talks/david_pogue_says_sim...</td>
      <td>1636292</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Majora Carter: Greening the ghetto</td>
      <td>Greening the ghetto</td>
      <td>In an emotionally charged talk, MacArthur-winn...</td>
      <td>Majora Carter</td>
      <td>Activist for environmental justice</td>
      <td>1</td>
      <td>1116</td>
      <td>TED2006</td>
      <td>26-02-2006</td>
      <td>27-06-2006</td>
      <td>200</td>
      <td>['MacArthur grant', 'activism', 'business', 'c...</td>
      <td>35</td>
      <td>[{'id': 3, 'name': 'Courageous', 'count': 760}...</td>
      <td>[{'id': 1041, 'hero': 'https://pe.tedcdn.com/i...</td>
      <td>https://www.ted.com/talks/majora_carter_s_tale...</td>
      <td>1697550</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Hans Rosling: The best stats you've ever seen</td>
      <td>The best stats you've ever seen</td>
      <td>You've never seen data presented like this. Wi...</td>
      <td>Hans Rosling</td>
      <td>Global health expert; data visionary</td>
      <td>1</td>
      <td>1190</td>
      <td>TED2006</td>
      <td>22-02-2006</td>
      <td>28-06-2006</td>
      <td>593</td>
      <td>['Africa', 'Asia', 'Google', 'demo', 'economic...</td>
      <td>48</td>
      <td>[{'id': 9, 'name': 'Ingenious', 'count': 3202}...</td>
      <td>[{'id': 2056, 'hero': 'https://pe.tedcdn.com/i...</td>
      <td>https://www.ted.com/talks/hans_rosling_shows_t...</td>
      <td>12005869</td>
    </tr>
  </tbody>
</table>
</div>




```python
#查询是否有缺省值
ted.isnull().any()
```




    name                  False
    title                 False
    description           False
    main_speaker          False
    speaker_occupation     True
    num_speaker           False
    duration              False
    event                 False
    film_date             False
    published_date        False
    comments              False
    tags                  False
    languages             False
    ratings               False
    related_talks         False
    url                   False
    views                 False
    dtype: bool




```python
ted[ted['speaker_occupation'].isnull()]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>title</th>
      <th>description</th>
      <th>main_speaker</th>
      <th>speaker_occupation</th>
      <th>num_speaker</th>
      <th>duration</th>
      <th>event</th>
      <th>film_date</th>
      <th>published_date</th>
      <th>comments</th>
      <th>tags</th>
      <th>languages</th>
      <th>ratings</th>
      <th>related_talks</th>
      <th>url</th>
      <th>views</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1113</th>
      <td>Sonaar Luthra: Meet the Water Canary</td>
      <td>Meet the Water Canary</td>
      <td>After a crisis, how can we tell if water is sa...</td>
      <td>Sonaar Luthra</td>
      <td>NaN</td>
      <td>1</td>
      <td>217</td>
      <td>TEDGlobal 2011</td>
      <td>14-07-2011</td>
      <td>17-01-2012</td>
      <td>145</td>
      <td>['TED Fellows', 'design', 'global development'...</td>
      <td>38</td>
      <td>[{'id': 10, 'name': 'Inspiring', 'count': 73},...</td>
      <td>[{'id': 523, 'hero': 'https://pe.tedcdn.com/im...</td>
      <td>https://www.ted.com/talks/sonaar_luthra_meet_t...</td>
      <td>353749</td>
    </tr>
    <tr>
      <th>1192</th>
      <td>Rick Falkvinge: I am a pirate</td>
      <td>I am a pirate</td>
      <td>The Pirate Party fights for transparency, anon...</td>
      <td>Rick Falkvinge</td>
      <td>NaN</td>
      <td>1</td>
      <td>1097</td>
      <td>TEDxObserver</td>
      <td>11-03-2012</td>
      <td>01-04-2012</td>
      <td>122</td>
      <td>['Internet', 'TEDx', 'global issues', 'politic...</td>
      <td>10</td>
      <td>[{'id': 8, 'name': 'Informative', 'count': 156...</td>
      <td>[{'id': 1329, 'hero': 'https://pe.tedcdn.com/i...</td>
      <td>https://www.ted.com/talks/rick_falkvinge_i_am_...</td>
      <td>181010</td>
    </tr>
    <tr>
      <th>1220</th>
      <td>Gary Kovacs: Tracking our online trackers</td>
      <td>Tracking our online trackers</td>
      <td>As you surf the Web, information is being coll...</td>
      <td>Gary Kovacs</td>
      <td>NaN</td>
      <td>1</td>
      <td>399</td>
      <td>TED2012</td>
      <td>29-02-2012</td>
      <td>03-05-2012</td>
      <td>257</td>
      <td>['Internet', 'advertising', 'business', 'priva...</td>
      <td>32</td>
      <td>[{'id': 23, 'name': 'Jaw-dropping', 'count': 9...</td>
      <td>[{'id': 1370, 'hero': 'https://pe.tedcdn.com/i...</td>
      <td>https://www.ted.com/talks/gary_kovacs_tracking...</td>
      <td>2098639</td>
    </tr>
    <tr>
      <th>1656</th>
      <td>Ryan Holladay: To hear this music you have to ...</td>
      <td>To hear this music you have to be there. Liter...</td>
      <td>In this lovely talk, TED Fellow Ryan Holladay ...</td>
      <td>Ryan Holladay</td>
      <td>NaN</td>
      <td>1</td>
      <td>389</td>
      <td>TED@BCG San Francisco</td>
      <td>30-10-2013</td>
      <td>11-01-2014</td>
      <td>140</td>
      <td>['TED Fellows', 'entertainment', 'music', 'tec...</td>
      <td>33</td>
      <td>[{'id': 1, 'name': 'Beautiful', 'count': 211},...</td>
      <td>[{'id': 1152, 'hero': 'https://pe.tedcdn.com/i...</td>
      <td>https://www.ted.com/talks/ryan_holladay_to_hea...</td>
      <td>1284510</td>
    </tr>
    <tr>
      <th>1911</th>
      <td>Brian Dettmer: Old books reborn as art</td>
      <td>Old books reborn as art</td>
      <td>What do you do with an outdated encyclopedia i...</td>
      <td>Brian Dettmer</td>
      <td>NaN</td>
      <td>1</td>
      <td>366</td>
      <td>TEDYouth 2014</td>
      <td>04-11-2014</td>
      <td>07-02-2015</td>
      <td>48</td>
      <td>['TEDYouth', 'art', 'books', 'creativity']</td>
      <td>34</td>
      <td>[{'id': 1, 'name': 'Beautiful', 'count': 361},...</td>
      <td>[{'id': 610, 'hero': 'https://pe.tedcdn.com/im...</td>
      <td>https://www.ted.com/talks/brian_dettmer_old_bo...</td>
      <td>1159937</td>
    </tr>
    <tr>
      <th>1949</th>
      <td>Boniface Mwangi: The day I stood up alone</td>
      <td>The day I stood up alone</td>
      <td>Photographer Boniface Mwangi wanted to protest...</td>
      <td>Boniface Mwangi</td>
      <td>NaN</td>
      <td>1</td>
      <td>440</td>
      <td>TEDGlobal 2014</td>
      <td>20-10-2014</td>
      <td>02-04-2015</td>
      <td>70</td>
      <td>['TED Fellows', 'activism', 'art', 'corruption...</td>
      <td>33</td>
      <td>[{'id': 3, 'name': 'Courageous', 'count': 614}...</td>
      <td>[{'id': 1757, 'hero': 'https://pe.tedcdn.com/i...</td>
      <td>https://www.ted.com/talks/boniface_mwangi_boni...</td>
      <td>1342431</td>
    </tr>
  </tbody>
</table>
</div>




```python
print("单人演讲占所有演讲的比例为{}%".format(round(sum(ted["num_speaker"] == 1)*100/len(ted), 1)))

print("时长小于18分钟的演讲数占所有演讲总数的{}%".format(round(sum(ted["duration"] <= 18*60)*100/len(ted), 1)))
```

    单人演讲占所有演讲的比例为97.7%
    时长小于18分钟的演讲数占所有演讲总数的79.1%
    


```python
#按浏览量排序
ted.sort_values(by='views',ascending=False)[:10]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>title</th>
      <th>description</th>
      <th>main_speaker</th>
      <th>speaker_occupation</th>
      <th>num_speaker</th>
      <th>duration</th>
      <th>event</th>
      <th>film_date</th>
      <th>published_date</th>
      <th>comments</th>
      <th>tags</th>
      <th>languages</th>
      <th>ratings</th>
      <th>related_talks</th>
      <th>url</th>
      <th>views</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Ken Robinson: Do schools kill creativity?</td>
      <td>Do schools kill creativity?</td>
      <td>Sir Ken Robinson makes an entertaining and pro...</td>
      <td>Ken Robinson</td>
      <td>Author/educator</td>
      <td>1</td>
      <td>1164</td>
      <td>TED2006</td>
      <td>25-02-2006</td>
      <td>27-06-2006</td>
      <td>4553</td>
      <td>['children', 'creativity', 'culture', 'dance',...</td>
      <td>60</td>
      <td>[{'id': 7, 'name': 'Funny', 'count': 19645}, {...</td>
      <td>[{'id': 865, 'hero': 'https://pe.tedcdn.com/im...</td>
      <td>https://www.ted.com/talks/ken_robinson_says_sc...</td>
      <td>47227110</td>
    </tr>
    <tr>
      <th>1346</th>
      <td>Amy Cuddy: Your body language may shape who yo...</td>
      <td>Your body language may shape who you are</td>
      <td>Body language affects how others see us, but i...</td>
      <td>Amy Cuddy</td>
      <td>Social psychologist</td>
      <td>1</td>
      <td>1262</td>
      <td>TEDGlobal 2012</td>
      <td>26-06-2012</td>
      <td>01-10-2012</td>
      <td>2290</td>
      <td>['body language', 'brain', 'business', 'psycho...</td>
      <td>51</td>
      <td>[{'id': 23, 'name': 'Jaw-dropping', 'count': 3...</td>
      <td>[{'id': 605, 'hero': 'https://pe.tedcdn.com/im...</td>
      <td>https://www.ted.com/talks/amy_cuddy_your_body_...</td>
      <td>43155405</td>
    </tr>
    <tr>
      <th>677</th>
      <td>Simon Sinek: How great leaders inspire action</td>
      <td>How great leaders inspire action</td>
      <td>Simon Sinek has a simple but powerful model fo...</td>
      <td>Simon Sinek</td>
      <td>Leadership expert</td>
      <td>1</td>
      <td>1084</td>
      <td>TEDxPuget Sound</td>
      <td>17-09-2009</td>
      <td>04-05-2010</td>
      <td>1930</td>
      <td>['TEDx', 'business', 'entrepreneur', 'leadersh...</td>
      <td>45</td>
      <td>[{'id': 21, 'name': 'Unconvincing', 'count': 9...</td>
      <td>[{'id': 814, 'hero': 'https://pe.tedcdn.com/im...</td>
      <td>https://www.ted.com/talks/simon_sinek_how_grea...</td>
      <td>34309432</td>
    </tr>
    <tr>
      <th>837</th>
      <td>Brené Brown: The power of vulnerability</td>
      <td>The power of vulnerability</td>
      <td>Brené Brown studies human connection -- our ab...</td>
      <td>Brené Brown</td>
      <td>Vulnerability researcher</td>
      <td>1</td>
      <td>1219</td>
      <td>TEDxHouston</td>
      <td>06-06-2010</td>
      <td>23-12-2010</td>
      <td>1927</td>
      <td>['TEDx', 'communication', 'culture', 'depressi...</td>
      <td>52</td>
      <td>[{'id': 10, 'name': 'Inspiring', 'count': 2144...</td>
      <td>[{'id': 1391, 'hero': 'https://pe.tedcdn.com/i...</td>
      <td>https://www.ted.com/talks/brene_brown_on_vulne...</td>
      <td>31168150</td>
    </tr>
    <tr>
      <th>452</th>
      <td>Mary Roach: 10 things you didn't know about or...</td>
      <td>10 things you didn't know about orgasm</td>
      <td>"Bonk" author Mary Roach delves into obscure s...</td>
      <td>Mary Roach</td>
      <td>Writer</td>
      <td>1</td>
      <td>1003</td>
      <td>TED2009</td>
      <td>06-02-2009</td>
      <td>20-05-2009</td>
      <td>354</td>
      <td>['books', 'culture', 'history', 'humor', 'scie...</td>
      <td>37</td>
      <td>[{'id': 23, 'name': 'Jaw-dropping', 'count': 3...</td>
      <td>[{'id': 16, 'hero': 'https://pe.tedcdn.com/ima...</td>
      <td>https://www.ted.com/talks/mary_roach_10_things...</td>
      <td>22270883</td>
    </tr>
    <tr>
      <th>1776</th>
      <td>Julian Treasure: How to speak so that people w...</td>
      <td>How to speak so that people want to listen</td>
      <td>Have you ever felt like you're talking, but no...</td>
      <td>Julian Treasure</td>
      <td>Sound consultant</td>
      <td>1</td>
      <td>598</td>
      <td>TEDGlobal 2013</td>
      <td>10-06-2013</td>
      <td>27-06-2014</td>
      <td>297</td>
      <td>['culture', 'sound', 'speech']</td>
      <td>45</td>
      <td>[{'id': 24, 'name': 'Persuasive', 'count': 267...</td>
      <td>[{'id': 1200, 'hero': 'https://pe.tedcdn.com/i...</td>
      <td>https://www.ted.com/talks/julian_treasure_how_...</td>
      <td>21594632</td>
    </tr>
    <tr>
      <th>201</th>
      <td>Jill Bolte Taylor: My stroke of insight</td>
      <td>My stroke of insight</td>
      <td>Jill Bolte Taylor got a research opportunity f...</td>
      <td>Jill Bolte Taylor</td>
      <td>Neuroanatomist</td>
      <td>1</td>
      <td>1099</td>
      <td>TED2008</td>
      <td>27-02-2008</td>
      <td>12-03-2008</td>
      <td>2877</td>
      <td>['biology', 'brain', 'consciousness', 'global ...</td>
      <td>49</td>
      <td>[{'id': 22, 'name': 'Fascinating', 'count': 14...</td>
      <td>[{'id': 184, 'hero': 'https://pe.tedcdn.com/im...</td>
      <td>https://www.ted.com/talks/jill_bolte_taylor_s_...</td>
      <td>21190883</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Tony Robbins: Why we do what we do</td>
      <td>Why we do what we do</td>
      <td>Tony Robbins discusses the "invisible forces" ...</td>
      <td>Tony Robbins</td>
      <td>Life coach; expert in leadership psychology</td>
      <td>1</td>
      <td>1305</td>
      <td>TED2006</td>
      <td>02-02-2006</td>
      <td>28-06-2006</td>
      <td>672</td>
      <td>['business', 'culture', 'entertainment', 'goal...</td>
      <td>36</td>
      <td>[{'id': 7, 'name': 'Funny', 'count': 1102}, {'...</td>
      <td>[{'id': 229, 'hero': 'https://pe.tedcdn.com/im...</td>
      <td>https://www.ted.com/talks/tony_robbins_asks_wh...</td>
      <td>20685401</td>
    </tr>
    <tr>
      <th>2114</th>
      <td>James Veitch: This is what happens when you re...</td>
      <td>This is what happens when you reply to spam email</td>
      <td>Suspicious emails: unclaimed insurance bonds, ...</td>
      <td>James Veitch</td>
      <td>Comedian and writer</td>
      <td>1</td>
      <td>588</td>
      <td>TEDGlobal&gt;Geneva</td>
      <td>08-12-2015</td>
      <td>09-01-2016</td>
      <td>150</td>
      <td>['comedy', 'communication', 'curiosity', 'humo...</td>
      <td>43</td>
      <td>[{'id': 7, 'name': 'Funny', 'count': 7731}, {'...</td>
      <td>[{'id': 2236, 'hero': 'https://pe.tedcdn.com/i...</td>
      <td>https://www.ted.com/talks/james_veitch_this_is...</td>
      <td>20475972</td>
    </tr>
    <tr>
      <th>1416</th>
      <td>Cameron Russell: Looks aren't everything. Beli...</td>
      <td>Looks aren't everything. Believe me, I'm a model.</td>
      <td>Cameron Russell admits she won “a genetic lott...</td>
      <td>Cameron Russell</td>
      <td>Model</td>
      <td>1</td>
      <td>577</td>
      <td>TEDxMidAtlantic</td>
      <td>27-10-2012</td>
      <td>17-01-2013</td>
      <td>846</td>
      <td>['TEDx', 'beauty', 'culture', 'fashion', 'phot...</td>
      <td>43</td>
      <td>[{'id': 11, 'name': 'Longwinded', 'count': 92}...</td>
      <td>[{'id': 1438, 'hero': 'https://pe.tedcdn.com/i...</td>
      <td>https://www.ted.com/talks/cameron_russell_look...</td>
      <td>19787465</td>
    </tr>
  </tbody>
</table>
</div>




```python
print("浏览量小于4 million的演讲视频数占总数的{}%".format(round(sum(ted["views"] <= 4000000)*100/len(ted), 1))) 
```

    浏览量小于4 million的演讲视频数占总数的93.5%
    


```python
#按评论量排序
ted.sort_values(by='comments',ascending=False)[:10]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>title</th>
      <th>description</th>
      <th>main_speaker</th>
      <th>speaker_occupation</th>
      <th>num_speaker</th>
      <th>duration</th>
      <th>event</th>
      <th>film_date</th>
      <th>published_date</th>
      <th>comments</th>
      <th>tags</th>
      <th>languages</th>
      <th>ratings</th>
      <th>related_talks</th>
      <th>url</th>
      <th>views</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>96</th>
      <td>Richard Dawkins: Militant atheism</td>
      <td>Militant atheism</td>
      <td>Richard Dawkins urges all atheists to openly s...</td>
      <td>Richard Dawkins</td>
      <td>Evolutionary biologist</td>
      <td>1</td>
      <td>1750</td>
      <td>TED2002</td>
      <td>02-02-2002</td>
      <td>16-04-2007</td>
      <td>6404</td>
      <td>['God', 'atheism', 'culture', 'religion', 'sci...</td>
      <td>42</td>
      <td>[{'id': 3, 'name': 'Courageous', 'count': 3236...</td>
      <td>[{'id': 86, 'hero': 'https://pe.tedcdn.com/ima...</td>
      <td>https://www.ted.com/talks/richard_dawkins_on_m...</td>
      <td>4374792</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Ken Robinson: Do schools kill creativity?</td>
      <td>Do schools kill creativity?</td>
      <td>Sir Ken Robinson makes an entertaining and pro...</td>
      <td>Ken Robinson</td>
      <td>Author/educator</td>
      <td>1</td>
      <td>1164</td>
      <td>TED2006</td>
      <td>25-02-2006</td>
      <td>27-06-2006</td>
      <td>4553</td>
      <td>['children', 'creativity', 'culture', 'dance',...</td>
      <td>60</td>
      <td>[{'id': 7, 'name': 'Funny', 'count': 19645}, {...</td>
      <td>[{'id': 865, 'hero': 'https://pe.tedcdn.com/im...</td>
      <td>https://www.ted.com/talks/ken_robinson_says_sc...</td>
      <td>47227110</td>
    </tr>
    <tr>
      <th>644</th>
      <td>Sam Harris: Science can answer moral questions</td>
      <td>Science can answer moral questions</td>
      <td>Questions of good and evil, right and wrong ar...</td>
      <td>Sam Harris</td>
      <td>Neuroscientist, philosopher</td>
      <td>1</td>
      <td>1386</td>
      <td>TED2010</td>
      <td>11-02-2010</td>
      <td>22-03-2010</td>
      <td>3356</td>
      <td>['culture', 'evolutionary psychology', 'global...</td>
      <td>39</td>
      <td>[{'id': 8, 'name': 'Informative', 'count': 923...</td>
      <td>[{'id': 666, 'hero': 'https://pe.tedcdn.com/im...</td>
      <td>https://www.ted.com/talks/sam_harris_science_c...</td>
      <td>3433437</td>
    </tr>
    <tr>
      <th>201</th>
      <td>Jill Bolte Taylor: My stroke of insight</td>
      <td>My stroke of insight</td>
      <td>Jill Bolte Taylor got a research opportunity f...</td>
      <td>Jill Bolte Taylor</td>
      <td>Neuroanatomist</td>
      <td>1</td>
      <td>1099</td>
      <td>TED2008</td>
      <td>27-02-2008</td>
      <td>12-03-2008</td>
      <td>2877</td>
      <td>['biology', 'brain', 'consciousness', 'global ...</td>
      <td>49</td>
      <td>[{'id': 22, 'name': 'Fascinating', 'count': 14...</td>
      <td>[{'id': 184, 'hero': 'https://pe.tedcdn.com/im...</td>
      <td>https://www.ted.com/talks/jill_bolte_taylor_s_...</td>
      <td>21190883</td>
    </tr>
    <tr>
      <th>1787</th>
      <td>David Chalmers: How do you explain consciousness?</td>
      <td>How do you explain consciousness?</td>
      <td>Our consciousness is a fundamental aspect of o...</td>
      <td>David Chalmers</td>
      <td>Philosopher</td>
      <td>1</td>
      <td>1117</td>
      <td>TED2014</td>
      <td>18-03-2014</td>
      <td>14-07-2014</td>
      <td>2673</td>
      <td>['brain', 'consciousness', 'neuroscience', 'ph...</td>
      <td>33</td>
      <td>[{'id': 25, 'name': 'OK', 'count': 280}, {'id'...</td>
      <td>[{'id': 1308, 'hero': 'https://pe.tedcdn.com/i...</td>
      <td>https://www.ted.com/talks/david_chalmers_how_d...</td>
      <td>2162764</td>
    </tr>
    <tr>
      <th>954</th>
      <td>Janet Echelman: Taking imagination seriously</td>
      <td>Taking imagination seriously</td>
      <td>Janet Echelman found her true voice as an arti...</td>
      <td>Janet Echelman</td>
      <td>Artist</td>
      <td>1</td>
      <td>566</td>
      <td>TED2011</td>
      <td>03-03-2011</td>
      <td>08-06-2011</td>
      <td>2492</td>
      <td>['art', 'cities', 'culture', 'data', 'design',...</td>
      <td>35</td>
      <td>[{'id': 23, 'name': 'Jaw-dropping', 'count': 3...</td>
      <td>[{'id': 453, 'hero': 'https://pe.tedcdn.com/im...</td>
      <td>https://www.ted.com/talks/janet_echelman\n</td>
      <td>1832930</td>
    </tr>
    <tr>
      <th>840</th>
      <td>Lesley Hazleton: On reading the Koran</td>
      <td>On reading the Koran</td>
      <td>Lesley Hazleton sat down one day to read the K...</td>
      <td>Lesley Hazleton</td>
      <td>Writer, psychologist</td>
      <td>1</td>
      <td>573</td>
      <td>TEDxRainier</td>
      <td>10-10-2010</td>
      <td>04-01-2011</td>
      <td>2374</td>
      <td>['TEDx', 'culture', 'global issues', 'journali...</td>
      <td>35</td>
      <td>[{'id': 3, 'name': 'Courageous', 'count': 488}...</td>
      <td>[{'id': 1772, 'hero': 'https://pe.tedcdn.com/i...</td>
      <td>https://www.ted.com/talks/lesley_hazelton_on_r...</td>
      <td>1847256</td>
    </tr>
    <tr>
      <th>1346</th>
      <td>Amy Cuddy: Your body language may shape who yo...</td>
      <td>Your body language may shape who you are</td>
      <td>Body language affects how others see us, but i...</td>
      <td>Amy Cuddy</td>
      <td>Social psychologist</td>
      <td>1</td>
      <td>1262</td>
      <td>TEDGlobal 2012</td>
      <td>26-06-2012</td>
      <td>01-10-2012</td>
      <td>2290</td>
      <td>['body language', 'brain', 'business', 'psycho...</td>
      <td>51</td>
      <td>[{'id': 23, 'name': 'Jaw-dropping', 'count': 3...</td>
      <td>[{'id': 605, 'hero': 'https://pe.tedcdn.com/im...</td>
      <td>https://www.ted.com/talks/amy_cuddy_your_body_...</td>
      <td>43155405</td>
    </tr>
    <tr>
      <th>661</th>
      <td>Michael Specter: The danger of science denial</td>
      <td>The danger of science denial</td>
      <td>Vaccine-autism claims, "Frankenfood" bans, the...</td>
      <td>Michael Specter</td>
      <td>Writer</td>
      <td>1</td>
      <td>1141</td>
      <td>TED2010</td>
      <td>11-02-2010</td>
      <td>12-04-2010</td>
      <td>2272</td>
      <td>['global issues', 'medicine', 'religion', 'sci...</td>
      <td>31</td>
      <td>[{'id': 3, 'name': 'Courageous', 'count': 702}...</td>
      <td>[{'id': 801, 'hero': 'https://pe.tedcdn.com/im...</td>
      <td>https://www.ted.com/talks/michael_specter_the_...</td>
      <td>1838628</td>
    </tr>
    <tr>
      <th>677</th>
      <td>Simon Sinek: How great leaders inspire action</td>
      <td>How great leaders inspire action</td>
      <td>Simon Sinek has a simple but powerful model fo...</td>
      <td>Simon Sinek</td>
      <td>Leadership expert</td>
      <td>1</td>
      <td>1084</td>
      <td>TEDxPuget Sound</td>
      <td>17-09-2009</td>
      <td>04-05-2010</td>
      <td>1930</td>
      <td>['TEDx', 'business', 'entrepreneur', 'leadersh...</td>
      <td>45</td>
      <td>[{'id': 21, 'name': 'Unconvincing', 'count': 9...</td>
      <td>[{'id': 814, 'hero': 'https://pe.tedcdn.com/im...</td>
      <td>https://www.ted.com/talks/simon_sinek_how_grea...</td>
      <td>34309432</td>
    </tr>
  </tbody>
</table>
</div>




```python
print("评论量小于500条：{}%".format(round(sum(ted["comments"] <= 500)*100/len(ted), 1)))
```

    评论量小于500条：93.3%
    


```python
#浏览量与评论量的相关性
ted.plot(kind="scatter", x="views", y="comments", alpha=0.1)
```




    <AxesSubplot:xlabel='views', ylabel='comments'>




    
![png](output_10_1.png)
    



```python
ted[['views', 'comments']].corr()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>views</th>
      <th>comments</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>views</th>
      <td>1.000000</td>
      <td>0.530939</td>
    </tr>
    <tr>
      <th>comments</th>
      <td>0.530939</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
day_order = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
#按月统计
ted['month'] = ted['film_date'].apply(lambda x: month_order[int(x.split('-')[1]) - 1])
month_df = ted['month'].value_counts()
month_df=month_df.reindex(index=month_order)
month_df
```




    Jan     33
    Feb    601
    Mar    397
    Apr    173
    May    123
    Jun    270
    Jul    253
    Aug     30
    Sep    107
    Oct    208
    Nov    232
    Dec    123
    Name: month, dtype: int64




```python
month_df.plot.bar(rot=0)
```




    <AxesSubplot:>




    
![png](output_13_1.png)
    



```python
#按日统计
def getday(x):
    day,month,year=(int(i) for i in x.split('-'))    
    answer=datetime.date(year, month, day).weekday()
    return day_order[answer]
ted['day']=ted['film_date'].apply(getday)
day_df=ted['day'].value_counts()
day_df=day_df.reindex(index=day_order)
day_df
```




    Mon    306
    Tue    327
    Wed    533
    Thu    552
    Fri    384
    Sat    338
    Sun    110
    Name: day, dtype: int64




```python
day_df.plot.bar(rot=0)
```




    <AxesSubplot:>




    
![png](output_15_1.png)
    



```python
#按年统计
ted['year']=ted['film_date'].apply(lambda x: int(x.split('-')[2]))
year_df=ted['year'].value_counts()
year_df=year_df.sort_index()
year_df
```




    1972      1
    1983      1
    1984      1
    1990      1
    1991      1
    1994      1
    1998      6
    2001      5
    2002     27
    2003     33
    2004     33
    2005     66
    2006     50
    2007    114
    2008     84
    2009    232
    2010    267
    2011    270
    2012    267
    2013    270
    2014    237
    2015    239
    2016    246
    2017     98
    Name: year, dtype: int64




```python
year_df.plot()
```




    <AxesSubplot:>




    
![png](output_17_1.png)
    



```python
#按年和月统计
year_month_df=ted.groupby(['year','month']).size().unstack().fillna(0)
year_month_df=year_month_df.reindex(columns=month_order)
year_month_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>month</th>
      <th>Jan</th>
      <th>Feb</th>
      <th>Mar</th>
      <th>Apr</th>
      <th>May</th>
      <th>Jun</th>
      <th>Jul</th>
      <th>Aug</th>
      <th>Sep</th>
      <th>Oct</th>
      <th>Nov</th>
      <th>Dec</th>
    </tr>
    <tr>
      <th>year</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1972</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1983</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1984</th>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1990</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1991</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1994</th>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1998</th>
      <td>0.0</td>
      <td>6.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2001</th>
      <td>0.0</td>
      <td>4.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2002</th>
      <td>0.0</td>
      <td>24.0</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2003</th>
      <td>0.0</td>
      <td>31.0</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2004</th>
      <td>0.0</td>
      <td>30.0</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2005</th>
      <td>0.0</td>
      <td>37.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>25.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2006</th>
      <td>0.0</td>
      <td>44.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2007</th>
      <td>2.0</td>
      <td>6.0</td>
      <td>62.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>27.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>14.0</td>
    </tr>
    <tr>
      <th>2008</th>
      <td>1.0</td>
      <td>47.0</td>
      <td>10.0</td>
      <td>0.0</td>
      <td>8.0</td>
      <td>2.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>2009</th>
      <td>0.0</td>
      <td>83.0</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>6.0</td>
      <td>65.0</td>
      <td>1.0</td>
      <td>7.0</td>
      <td>21.0</td>
      <td>40.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2010</th>
      <td>3.0</td>
      <td>70.0</td>
      <td>4.0</td>
      <td>27.0</td>
      <td>6.0</td>
      <td>11.0</td>
      <td>59.0</td>
      <td>2.0</td>
      <td>7.0</td>
      <td>19.0</td>
      <td>18.0</td>
      <td>41.0</td>
    </tr>
    <tr>
      <th>2011</th>
      <td>6.0</td>
      <td>2.0</td>
      <td>76.0</td>
      <td>10.0</td>
      <td>17.0</td>
      <td>5.0</td>
      <td>70.0</td>
      <td>2.0</td>
      <td>9.0</td>
      <td>12.0</td>
      <td>46.0</td>
      <td>15.0</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>2.0</td>
      <td>42.0</td>
      <td>38.0</td>
      <td>33.0</td>
      <td>18.0</td>
      <td>82.0</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>9.0</td>
      <td>12.0</td>
      <td>15.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>7.0</td>
      <td>75.0</td>
      <td>13.0</td>
      <td>15.0</td>
      <td>15.0</td>
      <td>70.0</td>
      <td>7.0</td>
      <td>5.0</td>
      <td>14.0</td>
      <td>28.0</td>
      <td>12.0</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>3.0</td>
      <td>4.0</td>
      <td>90.0</td>
      <td>5.0</td>
      <td>4.0</td>
      <td>12.0</td>
      <td>9.0</td>
      <td>4.0</td>
      <td>20.0</td>
      <td>57.0</td>
      <td>23.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>2.0</td>
      <td>1.0</td>
      <td>78.0</td>
      <td>3.0</td>
      <td>35.0</td>
      <td>14.0</td>
      <td>1.0</td>
      <td>10.0</td>
      <td>20.0</td>
      <td>18.0</td>
      <td>46.0</td>
      <td>11.0</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>4.0</td>
      <td>83.0</td>
      <td>3.0</td>
      <td>11.0</td>
      <td>16.0</td>
      <td>39.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>15.0</td>
      <td>38.0</td>
      <td>29.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>3.0</td>
      <td>10.0</td>
      <td>8.0</td>
      <td>68.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>4.0</td>
      <td>4.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
import seaborn as sns
sns.heatmap(year_month_df)
```




    <AxesSubplot:xlabel='month', ylabel='year'>




    
![png](output_19_1.png)
    



```python
#演讲者出场次数
speaker_df = ted.groupby('main_speaker').count().reset_index()[['main_speaker', 'comments']]
speaker_df.columns = ['主要演讲者', '演讲次数']
speaker_df = speaker_df.sort_values('演讲次数', ascending=False)
speaker_df.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>主要演讲者</th>
      <th>演讲次数</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>770</th>
      <td>Hans Rosling</td>
      <td>9</td>
    </tr>
    <tr>
      <th>1066</th>
      <td>Juan Enriquez</td>
      <td>7</td>
    </tr>
    <tr>
      <th>1693</th>
      <td>Rives</td>
      <td>6</td>
    </tr>
    <tr>
      <th>1278</th>
      <td>Marco Tempest</td>
      <td>6</td>
    </tr>
    <tr>
      <th>397</th>
      <td>Clay Shirky</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1487</th>
      <td>Nicholas Negroponte</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1075</th>
      <td>Julian Treasure</td>
      <td>5</td>
    </tr>
    <tr>
      <th>424</th>
      <td>Dan Ariely</td>
      <td>5</td>
    </tr>
    <tr>
      <th>850</th>
      <td>Jacqueline Novogratz</td>
      <td>5</td>
    </tr>
    <tr>
      <th>248</th>
      <td>Bill Gates</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
#演讲者职业出场次数
occupation_df = ted.groupby('speaker_occupation').count().reset_index()[['speaker_occupation', 'comments']]
occupation_df.columns = ['演讲者职业', '演讲次数']
occupation_df = occupation_df.sort_values('演讲次数', ascending = False)
occupation_df.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>演讲者职业</th>
      <th>演讲次数</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1426</th>
      <td>Writer</td>
      <td>45</td>
    </tr>
    <tr>
      <th>83</th>
      <td>Artist</td>
      <td>34</td>
    </tr>
    <tr>
      <th>413</th>
      <td>Designer</td>
      <td>34</td>
    </tr>
    <tr>
      <th>753</th>
      <td>Journalist</td>
      <td>33</td>
    </tr>
    <tr>
      <th>515</th>
      <td>Entrepreneur</td>
      <td>31</td>
    </tr>
    <tr>
      <th>71</th>
      <td>Architect</td>
      <td>30</td>
    </tr>
    <tr>
      <th>733</th>
      <td>Inventor</td>
      <td>27</td>
    </tr>
    <tr>
      <th>1131</th>
      <td>Psychologist</td>
      <td>26</td>
    </tr>
    <tr>
      <th>1011</th>
      <td>Photographer</td>
      <td>25</td>
    </tr>
    <tr>
      <th>567</th>
      <td>Filmmaker</td>
      <td>21</td>
    </tr>
  </tbody>
</table>
</div>




```python
#不同职业的平均浏览量
occupation_views_df=pd.Series(round(ted[ted['speaker_occupation']==x]['views'].mean(),1) for x in list(occupation_df['演讲者职业'][:10]))
occupation_views_df.index=list(occupation_df['演讲者职业'][:10])
occupation_views_df
```




    Writer          2967762.3
    Artist          1036726.6
    Designer        1273358.4
    Journalist      1450326.8
    Entrepreneur    1992387.8
    Architect       1251638.5
    Inventor        1161128.2
    Psychologist    3494284.5
    Photographer    1130300.4
    Filmmaker       1529156.6
    dtype: float64




```python
occupation_views_df.plot.bar()
```




    <AxesSubplot:>




    
![png](output_23_1.png)
    



```python
#每场的演讲人数
ted['num_speaker'].value_counts()
```




    1    2492
    2      49
    3       5
    4       3
    5       1
    Name: num_speaker, dtype: int64




```python
#TED活动演讲次数
event_df = ted.groupby('event').count().reset_index()[['event', 'comments']]
event_df.columns = ['TED活动', '演讲次数']
event_df = event_df.sort_values('演讲次数', ascending = False)
event_df.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>TED活动</th>
      <th>演讲次数</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>64</th>
      <td>TED2014</td>
      <td>84</td>
    </tr>
    <tr>
      <th>59</th>
      <td>TED2009</td>
      <td>83</td>
    </tr>
    <tr>
      <th>63</th>
      <td>TED2013</td>
      <td>77</td>
    </tr>
    <tr>
      <th>66</th>
      <td>TED2016</td>
      <td>77</td>
    </tr>
    <tr>
      <th>65</th>
      <td>TED2015</td>
      <td>75</td>
    </tr>
    <tr>
      <th>99</th>
      <td>TEDGlobal 2012</td>
      <td>70</td>
    </tr>
    <tr>
      <th>61</th>
      <td>TED2011</td>
      <td>70</td>
    </tr>
    <tr>
      <th>60</th>
      <td>TED2010</td>
      <td>68</td>
    </tr>
    <tr>
      <th>98</th>
      <td>TEDGlobal 2011</td>
      <td>68</td>
    </tr>
    <tr>
      <th>57</th>
      <td>TED2007</td>
      <td>68</td>
    </tr>
  </tbody>
</table>
</div>




```python
#浏览量与语言的相关性
ted.plot(kind="scatter", x="views", y="languages", alpha=0.1)
```




    <AxesSubplot:xlabel='views', ylabel='languages'>




    
![png](output_26_1.png)
    



```python
ted[['views', 'languages']].corr()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>views</th>
      <th>languages</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>views</th>
      <td>1.000000</td>
      <td>0.377623</td>
    </tr>
    <tr>
      <th>languages</th>
      <td>0.377623</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
import ast
ted['tags'] = ted['tags'].apply(lambda x: ast.literal_eval(x))
ted['tags'].head()
```




    0    [children, creativity, culture, dance, educati...
    1    [alternative energy, cars, climate change, cul...
    2    [computers, entertainment, interface design, m...
    3    [MacArthur grant, activism, business, cities, ...
    4    [Africa, Asia, Google, demo, economics, global...
    Name: tags, dtype: object




```python
s = ted.apply(lambda x: pd.Series(x['tags']),axis=1).stack().reset_index(level=1, drop=True)
s.name = 'theme'
s.head()
```




    0      children
    0    creativity
    0       culture
    0         dance
    0     education
    Name: theme, dtype: object




```python
theme_df = ted.drop('tags', axis = 1).join(s)
theme_df.head(2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>title</th>
      <th>description</th>
      <th>main_speaker</th>
      <th>speaker_occupation</th>
      <th>num_speaker</th>
      <th>duration</th>
      <th>event</th>
      <th>film_date</th>
      <th>published_date</th>
      <th>comments</th>
      <th>languages</th>
      <th>ratings</th>
      <th>related_talks</th>
      <th>url</th>
      <th>views</th>
      <th>month</th>
      <th>day</th>
      <th>year</th>
      <th>theme</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Ken Robinson: Do schools kill creativity?</td>
      <td>Do schools kill creativity?</td>
      <td>Sir Ken Robinson makes an entertaining and pro...</td>
      <td>Ken Robinson</td>
      <td>Author/educator</td>
      <td>1</td>
      <td>1164</td>
      <td>TED2006</td>
      <td>25-02-2006</td>
      <td>27-06-2006</td>
      <td>4553</td>
      <td>60</td>
      <td>[{'id': 7, 'name': 'Funny', 'count': 19645}, {...</td>
      <td>[{'id': 865, 'hero': 'https://pe.tedcdn.com/im...</td>
      <td>https://www.ted.com/talks/ken_robinson_says_sc...</td>
      <td>47227110</td>
      <td>Feb</td>
      <td>Sat</td>
      <td>2006</td>
      <td>children</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Ken Robinson: Do schools kill creativity?</td>
      <td>Do schools kill creativity?</td>
      <td>Sir Ken Robinson makes an entertaining and pro...</td>
      <td>Ken Robinson</td>
      <td>Author/educator</td>
      <td>1</td>
      <td>1164</td>
      <td>TED2006</td>
      <td>25-02-2006</td>
      <td>27-06-2006</td>
      <td>4553</td>
      <td>60</td>
      <td>[{'id': 7, 'name': 'Funny', 'count': 19645}, {...</td>
      <td>[{'id': 865, 'hero': 'https://pe.tedcdn.com/im...</td>
      <td>https://www.ted.com/talks/ken_robinson_says_sc...</td>
      <td>47227110</td>
      <td>Feb</td>
      <td>Sat</td>
      <td>2006</td>
      <td>creativity</td>
    </tr>
  </tbody>
</table>
</div>




```python
#按标签统计
theme_df['theme'].value_counts().sort_values(ascending=False)[:10]
```




    technology       727
    science          567
    global issues    501
    culture          486
    TEDx             450
    design           418
    business         348
    entertainment    299
    health           236
    innovation       229
    Name: theme, dtype: int64




```python
ted['ratings'] = ted['ratings'].apply(lambda x: ast.literal_eval(x))
ted.iloc[1]['ratings']
```




    [{'id': 7, 'name': 'Funny', 'count': 544},
     {'id': 3, 'name': 'Courageous', 'count': 139},
     {'id': 2, 'name': 'Confusing', 'count': 62},
     {'id': 1, 'name': 'Beautiful', 'count': 58},
     {'id': 21, 'name': 'Unconvincing', 'count': 258},
     {'id': 11, 'name': 'Longwinded', 'count': 113},
     {'id': 8, 'name': 'Informative', 'count': 443},
     {'id': 10, 'name': 'Inspiring', 'count': 413},
     {'id': 22, 'name': 'Fascinating', 'count': 132},
     {'id': 9, 'name': 'Ingenious', 'count': 56},
     {'id': 24, 'name': 'Persuasive', 'count': 268},
     {'id': 23, 'name': 'Jaw-dropping', 'count': 116},
     {'id': 26, 'name': 'Obnoxious', 'count': 131},
     {'id': 25, 'name': 'OK', 'count': 203}]




```python
rating_words = []

for i in range(len(ted)):
    l = ted.iloc[i]['ratings']
    for d in l:
        if d['name'] not in rating_words:
            rating_words.append(d['name'])

rating_words
```




    ['Funny',
     'Beautiful',
     'Ingenious',
     'Courageous',
     'Longwinded',
     'Confusing',
     'Informative',
     'Fascinating',
     'Unconvincing',
     'Persuasive',
     'Jaw-dropping',
     'OK',
     'Obnoxious',
     'Inspiring']




```python
def funny(x):
    for i in range(len(x)):
        if x[i]['name']=='Funny':
            return x[i]['count']
ted['funny'] = ted['ratings'].apply(funny)
ted.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>title</th>
      <th>description</th>
      <th>main_speaker</th>
      <th>speaker_occupation</th>
      <th>num_speaker</th>
      <th>duration</th>
      <th>event</th>
      <th>film_date</th>
      <th>published_date</th>
      <th>...</th>
      <th>tags</th>
      <th>languages</th>
      <th>ratings</th>
      <th>related_talks</th>
      <th>url</th>
      <th>views</th>
      <th>month</th>
      <th>day</th>
      <th>year</th>
      <th>funny</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Ken Robinson: Do schools kill creativity?</td>
      <td>Do schools kill creativity?</td>
      <td>Sir Ken Robinson makes an entertaining and pro...</td>
      <td>Ken Robinson</td>
      <td>Author/educator</td>
      <td>1</td>
      <td>1164</td>
      <td>TED2006</td>
      <td>25-02-2006</td>
      <td>27-06-2006</td>
      <td>...</td>
      <td>[children, creativity, culture, dance, educati...</td>
      <td>60</td>
      <td>[{'id': 7, 'name': 'Funny', 'count': 19645}, {...</td>
      <td>[{'id': 865, 'hero': 'https://pe.tedcdn.com/im...</td>
      <td>https://www.ted.com/talks/ken_robinson_says_sc...</td>
      <td>47227110</td>
      <td>Feb</td>
      <td>Sat</td>
      <td>2006</td>
      <td>19645</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Al Gore: Averting the climate crisis</td>
      <td>Averting the climate crisis</td>
      <td>With the same humor and humanity he exuded in ...</td>
      <td>Al Gore</td>
      <td>Climate advocate</td>
      <td>1</td>
      <td>977</td>
      <td>TED2006</td>
      <td>25-02-2006</td>
      <td>27-06-2006</td>
      <td>...</td>
      <td>[alternative energy, cars, climate change, cul...</td>
      <td>43</td>
      <td>[{'id': 7, 'name': 'Funny', 'count': 544}, {'i...</td>
      <td>[{'id': 243, 'hero': 'https://pe.tedcdn.com/im...</td>
      <td>https://www.ted.com/talks/al_gore_on_averting_...</td>
      <td>3200520</td>
      <td>Feb</td>
      <td>Sat</td>
      <td>2006</td>
      <td>544</td>
    </tr>
    <tr>
      <th>2</th>
      <td>David Pogue: Simplicity sells</td>
      <td>Simplicity sells</td>
      <td>New York Times columnist David Pogue takes aim...</td>
      <td>David Pogue</td>
      <td>Technology columnist</td>
      <td>1</td>
      <td>1286</td>
      <td>TED2006</td>
      <td>24-02-2006</td>
      <td>27-06-2006</td>
      <td>...</td>
      <td>[computers, entertainment, interface design, m...</td>
      <td>26</td>
      <td>[{'id': 7, 'name': 'Funny', 'count': 964}, {'i...</td>
      <td>[{'id': 1725, 'hero': 'https://pe.tedcdn.com/i...</td>
      <td>https://www.ted.com/talks/david_pogue_says_sim...</td>
      <td>1636292</td>
      <td>Feb</td>
      <td>Fri</td>
      <td>2006</td>
      <td>964</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Majora Carter: Greening the ghetto</td>
      <td>Greening the ghetto</td>
      <td>In an emotionally charged talk, MacArthur-winn...</td>
      <td>Majora Carter</td>
      <td>Activist for environmental justice</td>
      <td>1</td>
      <td>1116</td>
      <td>TED2006</td>
      <td>26-02-2006</td>
      <td>27-06-2006</td>
      <td>...</td>
      <td>[MacArthur grant, activism, business, cities, ...</td>
      <td>35</td>
      <td>[{'id': 3, 'name': 'Courageous', 'count': 760}...</td>
      <td>[{'id': 1041, 'hero': 'https://pe.tedcdn.com/i...</td>
      <td>https://www.ted.com/talks/majora_carter_s_tale...</td>
      <td>1697550</td>
      <td>Feb</td>
      <td>Sun</td>
      <td>2006</td>
      <td>59</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Hans Rosling: The best stats you've ever seen</td>
      <td>The best stats you've ever seen</td>
      <td>You've never seen data presented like this. Wi...</td>
      <td>Hans Rosling</td>
      <td>Global health expert; data visionary</td>
      <td>1</td>
      <td>1190</td>
      <td>TED2006</td>
      <td>22-02-2006</td>
      <td>28-06-2006</td>
      <td>...</td>
      <td>[Africa, Asia, Google, demo, economics, global...</td>
      <td>48</td>
      <td>[{'id': 9, 'name': 'Ingenious', 'count': 3202}...</td>
      <td>[{'id': 2056, 'hero': 'https://pe.tedcdn.com/i...</td>
      <td>https://www.ted.com/talks/hans_rosling_shows_t...</td>
      <td>12005869</td>
      <td>Feb</td>
      <td>Wed</td>
      <td>2006</td>
      <td>1390</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 21 columns</p>
</div>




```python
#按'Funny'评价统计
ted[['title', 'main_speaker', 'views', 'published_date', 'funny']].sort_values('funny', ascending = False)[:10]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>main_speaker</th>
      <th>views</th>
      <th>published_date</th>
      <th>funny</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Do schools kill creativity?</td>
      <td>Ken Robinson</td>
      <td>47227110</td>
      <td>27-06-2006</td>
      <td>19645</td>
    </tr>
    <tr>
      <th>2114</th>
      <td>This is what happens when you reply to spam email</td>
      <td>James Veitch</td>
      <td>20475972</td>
      <td>09-01-2016</td>
      <td>7731</td>
    </tr>
    <tr>
      <th>2161</th>
      <td>Inside the mind of a master procrastinator</td>
      <td>Tim Urban</td>
      <td>14745406</td>
      <td>16-03-2016</td>
      <td>7445</td>
    </tr>
    <tr>
      <th>1129</th>
      <td>The happy secret to better work</td>
      <td>Shawn Achor</td>
      <td>16209727</td>
      <td>02-02-2012</td>
      <td>7315</td>
    </tr>
    <tr>
      <th>675</th>
      <td>Lies, damned lies and statistics (about TEDTalks)</td>
      <td>Sebastian Wernicke</td>
      <td>2212944</td>
      <td>30-04-2010</td>
      <td>5552</td>
    </tr>
    <tr>
      <th>837</th>
      <td>The power of vulnerability</td>
      <td>Brené Brown</td>
      <td>31168150</td>
      <td>23-12-2010</td>
      <td>5225</td>
    </tr>
    <tr>
      <th>452</th>
      <td>10 things you didn't know about orgasm</td>
      <td>Mary Roach</td>
      <td>22270883</td>
      <td>20-05-2009</td>
      <td>4166</td>
    </tr>
    <tr>
      <th>685</th>
      <td>It's time for "The Talk"</td>
      <td>Julia Sweeney</td>
      <td>3362099</td>
      <td>14-05-2010</td>
      <td>4025</td>
    </tr>
    <tr>
      <th>747</th>
      <td>Did you hear the one about the Iranian-American?</td>
      <td>Maz Jobrani</td>
      <td>4646183</td>
      <td>19-08-2010</td>
      <td>4013</td>
    </tr>
    <tr>
      <th>692</th>
      <td>Bring on the learning revolution!</td>
      <td>Ken Robinson</td>
      <td>7266316</td>
      <td>24-05-2010</td>
      <td>3000</td>
    </tr>
  </tbody>
</table>
</div>




```python
#浏览量与有趣程度的相关性
ted.plot(kind="scatter", x="views", y="funny", alpha=0.1)
```




    <AxesSubplot:xlabel='views', ylabel='funny'>




    
![png](output_36_1.png)
    



```python
ted[['views', 'funny']].corr()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>views</th>
      <th>funny</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>views</th>
      <td>1.000000</td>
      <td>0.594588</td>
    </tr>
    <tr>
      <th>funny</th>
      <td>0.594588</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
#演讲时长
ted['duration'] = ted['duration']/60
ted['duration'].describe()
```




    count    2550.000000
    mean       13.775170
    std         6.233486
    min         2.250000
    25%         9.616667
    50%        14.133333
    75%        17.445833
    max        87.600000
    Name: duration, dtype: float64




```python

```
