Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus.

Most people infected with the COVID-19 virus will experience mild to moderate respiratory illness and recover without requiring special treatment. 

Older people, and those with underlying medical problems like cardiovascular disease, diabetes, chronic respiratory disease, and cancer are more likely to develop serious illness.

Current evidence suggests that COVID-19 spreads between people through direct, indirect (through contaminated objects or surfaces), or close contact with infected people via mouth and nose secretions.

The number of people affected by the virus is increasing with each passing day.

The dataset used in this project was the [CSSEGSISandData](https://github.com/CSSEGISandData/COVID-19)

This project aims at providing the case counts of confirmed, death and recovered cases for each country, via a horizontal bar graph and a world map and a line graph.


The project can be executed by:-
* Navigate into the **coronaDash** directory.
* Open the command prompt.
* Execute the following command - python manage.py runserver.
* Make sure you have Python 3.x and django package installed.

<br><br>
### The main page when rendered looks like this:-<br>
<img src="https://github.com/SUPREME-CODER/COVID-19-DASHBOARD/blob/master/Screen_Shots/Capture%201.PNG?raw=true" style="height:750px; weight:1000px;"></img>
<br><br><br>

### World Map
Hovering over the highlighted regions on the map gives the latest details of confirmed, death and recovered cases of the region
<br>
<img src="https://github.com/SUPREME-CODER/COVID-19-DASHBOARD/blob/master/Screen_Shots/Capture%202.png?raw=true" style="height:750px; weight:1000px;"></img>
<br><br><br>

### The Horizontal Graph
The horizontal bar graph shows the latest number of active cases in each country in a descending order.

The bars depict the number of active cases and the buttons on th eleft side denote the corresponding country.

The data is as latest as the one updated by the **CSSEGSIS** on thier git account.

Hovering over the bars of the horizontal bar graph displays the number of the active cases.

<br>
<img src="https://github.com/SUPREME-CODER/COVID-19-DASHBOARD/blob/master/Screen_Shots/Capture%203.png?raw=true" style="height:750px; weight:1000px;"></img>
<br><br><br>


### The Line Graph
On the left side of the bars are buttons. Pressing them shows the rise [number of] of active and death cases each day of that region from the beginning of this pandemic.

Rise in cases of the US.
<br>
<img src="https://github.com/SUPREME-CODER/COVID-19-DASHBOARD/blob/master/Screen_Shots/Capture%204.png?raw=true" style="height:750px; weight:1000px;"></img>
<br><br><br>

Rise in cases of India.
<br>
<img src="https://github.com/SUPREME-CODER/COVID-19-DASHBOARD/blob/master/Screen_Shots/Capture%205.png?raw=true" style="height:750px; weight:1000px;"></img>
<br><br><br>


### Future Modifications
Since only the numbers of cases cannot be considered as complete information about the pandemic.

Articles, newsletters also constitute an important part of the same.

My future plan is to add a article column on the right side of the page which will display the latest articles and trends on Covid-19 pandemic and also provide a link to the site / blog / article.
