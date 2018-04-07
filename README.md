<h4>Project 3 Team 30.</h4>
<h4>Team: Vipra, Vilok, Vibhor, Ali, Hemang</h4>


We created a dashboard that analysis different data points in the Mozilla dataset. We have created 5 visualization showing and comparing the following data points: 
1. Highly ranked parameters in making purchase of a tech toy.
2. Percentage of tech savvy citizens.
3. Top and lowest countries in Fitness tracking devices
4. Relationship between security and Privacy
5. Relationship between the smartphone and smart TV users among the top five countries


<h4>Above and Beyond parts completed (Considering the viz numbers as given above): </h4>
* Uncertainty: Viz 2 uses percentages.
* Semantic Zoom: Viz 1 implements it.
* Missing Data: Viz 1, 2, 3 implement it.  
* Perceptually-Informed Design: Viz 1, 2, 3 implement it.
* Coordinated Views: Viz 5 implement it.
* Style: Viz 1 ,2,3,4,5 implement it.
We are using d3 framework for our visualizations.




<h4>Vilok: </h4>

I worked on the scatter plot visual. I mainly wanted to show some kind of relationship between two different variables so I figured it was best to go simple and use a scatter plot. I showed the relationship between people who ranked security as 1, 2, or 3 and between people who ranked privacy as 1, 2, or 3. All these numbers are in percents and came from the csv file Vibhor cleaned up. As you can see, when people rate security in the top 3, then they tend to also put privacy in there too. For the overall design, I kept it consistent with what everyone else did and also added an interactive feature where you can hover over each point to see which country it is and to see the actual numbers for security and privacy 


<h4>Hemang: </h4>

I worked on the Dashboard(linking all the visualizations together) and navigating back to the home page. I also took up tasks from above and beyond , the style part needed tweeks in the css and hardcoded styles used in different visualization. The design process i used to implement the dashboard is simple javascript. I created the links to all the visualization and linked them to the home page.


<h4>Vipra: </h4>

I worked on creating the visualization “Top countries based on Technical Comfortness criteria”. The visualization displays countries vs Percentage of citizens. It shows the top countries by percentage based on how the citizens of the country categorizes themselves.  I have put 3 different types of queries on top as options that you can use to modify and control the data that is used to construct it. I have included the third query - “Consider countries from where total number of responses were more than” because number of responses from many countries are really less like e.g. 50 and if 40 citizens out of 50 say that they are “tech savvy” the reason behind it might also be that it is a poor country and a very few have access to technology at all. But when we go about finding the percentage with these numbers, it will be around 80% which is misleading.
For this viz, I started with cleaning the data, counting the number of responses from each country and finding the percentages for each category. The code for it can be found in vipra/test.py. Then I started with making a simple bar graph with only “tech savvy” percentage. When I was able to construct this, then I went ahead adding the options/queries.


<h4>Ali Raza:</h4>

Information about visualizations: I created two pairs of visualization which are bar charts. The first bar chart shows the comparison between the no of smart trackers users in the top five countries in the world and the top five countries who are below the average of using the smart trackers. Whereas my second pair of visualization shows the difference between the no of users of the smartphones and the no of users of the smart TV based on the top five countries. Both the visualization is interactive with the tool tip and color changing when the bar is clicked. Whereas the second pair of the visualization also shows the coordinated views because the countries on the x-axis of the graph are same.
Design process: I analyzed the data and then created the rough visualization on the notebook for the two visualizations along with the Vibhor. We also cleaned the original data file and got the fields which were relevant to our visualizations. Then we decided that one visualization would be map and other would show some significant difference between the countries. So, we opted to make a bar charts that will show difference between the fitness trackers, smartphone and smart to users on the basis of top five countries in these lists. The design of the visualizations are perceptually informed since it provides the stakeholder to compare and view the difference at the same time.The reason I went towards the bar charts comparison is because I feel that almost all users know about these visualizations and can get the sense of the data out of it pretty easily.
 
Team role: My team role was to create at least one or more visualization from the data that can draw some meaningful comparison between the data attributes. 


<h4>Vibhor:</h4>
 
Information about the visualization: I created a visualization on the demographic map that shows the demographic distribution of high ranked parameters in purchasing of a tech toy. By moving mouse on each specific country, you can view the parameter percentage of that country. On the top of the map you can select the parameter, which tells which parameter is significance to each country in the world. You can also zoom in and out the map. Whereas by selecting any country it also shows its boundary.
 
Design process: I created a visual idea about mapping all the countries in the world on the map. Which shows about what factor matters most to the countries when they are purchasing a tech toy. I along with the Ali, designed different visualization of the paper and also helped him. I got the data of the map, then I cleaned the data between the JSON file and the csv file. Then matched and fixed the data between these two files. Also, I selected the top three files when selecting the choice about the data. My design is perceptual informed one because it conveys all the information about the different parameters to the stakeholder and letting them compare together..I selected this visualization because this provides the stakeholders with the total view of the world on the perspective of buying a tech toy. What matters to each country most based on the parameters to each country.
 
Team role:
My main responsibility in the team was to come with new visualization that can show something significant about the data to the stakeholder. So, I opted to make a demographic map of the world, which I completed in a meaningful and professional way. Whereas I also worked with the Ali in coming up with different ideas on how to visualize the data and also cleaning of the data.
 


<h4>How to run the project:</h4>
* After cloning the project from github, run the file index.html and use the links on the html page to navigate to various visualizations.
* We have also provided a back button to come back to the home page.


<hr/>
<h2>Project 3:</h2>
Due 4.6.2018 by 11:59pm through GitHub Classroom 
Projects may be submitted up to 3 days late, with a 10% penalty per day.

<h2>Overview: </h2>
Mozilla (the same company that created the Firefox web browser) recently conducted a survey on people's perceptions of privacy in our modern, highly connected world. The survey was aimed at understanding how comfortable people from all over the world are with various technology and how that comfort varies with things like device ownership or tech savvy. You can learn more about their data here: https://blog.mozilla.org/blog/2017/11/01/10-fascinating-things-we-learned-when-we-asked-the-world-how-connected-are-you/?utm_source=newsletter-mofo&utm_medium=email&utm_campaign=IOTsurveyresults&utm_content=callout&utm_term=4434975

The challenge is that, while they have a rich set of data, they don't have strong ways of exploring that data beyond basic spreadsheets and descriptive statistics. Your goal is to create a set of visualizations that allows them to engage with their data. The raw data is available at: https://drive.google.com/file/d/0B5UMbl9u1_wQc2l0ZTU0dTdoYnM/view

<h2>Minimum Requirements:</h2> 
Your project must:
<ul>
<li> Include a README.md file that outlines:
  <ul>
  <li>Information about your visualizations and what they show. Include information about interactions, preprocesses, and design as appropriate.</li>
  <li>Your design process (e.g., how did you go about designing, building, and refining your system? Why did you choose these representations?)</li>
  <li>Your team roles for each individual</li>
  <li>How to run your project</li></ul></li>
<li>Include at least three unique visualizations:
  <ul>
  <li>One visualization must include some element of geography</li>
  <li>One visualization must include categorical data</li>
  <li>Each visualization must be interactive</li>
  <li>Your set of three visualizations should support at least one meaningful comparison between related data attributes</li>
  <li>Your set of three visualizations should visualize at least five data attributes total</li></ul></li>
<li>Be able to work with any dataset of this format (e.g., the numbers are interchangable but the columns and document titles are fixed).</li>
</ul>

<h2>Above and Beyond:</h2> 
The above requirements are the minimum for a passing grade on this project. Some ideas to improve your project include:<ul>
<li>Uncertainty: Include sources of uncertainty in your representation, such as margins of error or variance in your computed data</li>
<li>Semantic Zoom: Allow yourself to zoom into different levels of hierarchically grouped data (e.g., data grouped by continent, device type, etc).</li>
<li>Missing Data: Not all rows have data for all columns. Design ways of handling missing data intelligently.</li>
<li>Perceptually-Informed Design: Integrate perceptual concepts into your visualization design and discuss how you've integrated those concepts in your readme.</li>
<li>Coordinated Views: Have two or more visualizations that interact with one another as you move through the data.</li>
<li>Style: Keep the style consistent across all your views, with an eye towards intelligently applying visual design.</li></ul>

<h2>Platforms:</h2> 
You can use any development platform you'd like so long as it is not proprietary (exception: MatLab as we have a University License). Your project readme should include step-by-step instructions on how to run your projects and it should run without me having to modify the code. You are welcome to use different platforms for each visualization.

Some platforms to look at include:
<ul>
<li>D3</li>
<li>R with ggplot</li>
<li>WebGL or Three.js</li>
<li>Processing or ProcessingJS</li>
<li>Google Maps API</li>
<li>Open Street Map API</li>
<li>Bokeh</li>
<li>Creatively engineered tangible/audio artifacts</li>
</ul>

If you would like to use a platform that will push you in creative ways but may not support all of the requirements of the project, please come talk to me. 

<h2>Submissions:</h2>
All submissions must be made through GitHub with a timestamp by 11:59pm on 4.6. Your submission files should include:
<ul>
<li>Your README</li>
<li>Your code and/or project</li>
</ul>
Note that each group only needs to submit one file. 

Each member of the team should also send Danielle & Jim a project post-mortem through email with the subject line "INFO 4602/5602: Project 3" documenting the following:
* What you worked on in the project
* What your teammates worked on in the project
* How you would rate your performance and why (out of 10 points)
* How you would rate each teammates' performance and why (out of 10 points)

These documents will be kept confidential and will factor into project grades. If you feel all of the team worked hard and performed well, please don't hesitate to tell me that (no curving is necessary on performance reviews :-))! Also, please keep in mind that different team members have different skillsets, roles, and experiences.

<h2>Grading: </h2>
The project will be scored out of 100 points total. Your project will be graded on four different criteria:
<ol>
<li> Creativity</li>
<li> Technical execution (how well does it meet the stakeholder's objectives?)</li>
<li> Design (both aesthetic and your visualization choices)</li>
<li> Project Post-Mortems</li>
</ol>
