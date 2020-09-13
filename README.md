# What Should I Wear

## Introduction and Inspiration

Have you ever been planning to go outside, when you are suddenly stumped by what to wear? Ever had to peek outside to assess the temperature in order to decide what to wear? **_Well, look no more, for the solution is here!_** What Should I Wear is a website made by Krishnan Shankar, Michael Spence, Sammy Dods, and Hamza Khan that determines what clothing you should be wearing. Sometimes it will tell you to wear a T-Shirt, Shorts, maybe a Jacket? It will even tell you when to carry an _umbrella_! It all depends on your location's current weather.

## How it works

What Should I Wear does many things to ensure you are comfortable going outside, without needing to reconsider. First, What Should You Wear will ask for your location, in order to get the current weather for your location. To perform this task, it will use [WeatherAPI](https://weatherapi.com) to retreive the weather.  
After retreiving the weather for your location, What Should I Wear will use a _special algorithm_ to determine the ideal clothing to wear at that moment. It will also display some weather stats, such as temperature, feels like temperature, precipitation, gust, humidity, and so much more!

## How we built it

For the backend of our project, we used Python's [Flask](https://flask.palletsprojects.com/) framework, a lightweight framework that allows you to host websites while integrating it with Python code. We also used [Glitch](https://glitch.com), a Google Docs-like IDE for collaborative coding, to host our website. We used [WeatherAPI](https://weatherapi.com) to get weather data for locations, and we used the Python requests module to use get requests for accessing the APIs. We also used python-dotenv, json, and os to get our code working.

## Challenges we ran into

Some challenges we had during development were accessing the location of users. At the start, we tried using a Flask extension to try and get the location data, but we could never get it to work. Then, we moved to the javascript approach, by trying to send a post request to send the location data from the frontend to the backend. Finally, after looking up tons of documentation and posts on [Stack Overflow](https://stackoverflow.com), we finally got the location system to work.

Another major challenge we ran into was trying to use a Weather API. We started off with using [weather.gov](https://weather.gov), but we faced many problems, data was jumbled and often inaccurate, and it would just crash when given certain locations. After doing our best to figure it out, we scrapped the approach and moved on to [WeatherAPI](https://weatherapi.com). This was way easier to use, gave more accurate data, and solved all our problems.

## Accomplishments that we're proud of

The first major accomplishment we are proud of is getting the location detection to work. As we kept spending hours and hours on trying to solve this, we realized why popular weather services like [weather.gov](https://weather.gov) ask you to enter your location instead of detecting it. However, we were determined to figure it out, and after a lot of hard work, we finally did it.

Another major accomplishment we are proud of is getting Flask to work with [Glitch](https://glitch.com). We have all known that Glitch is a way to host your personal website for free, but we thought that it only worked with Node.js. However, we wanted to learn something new like Flask, so that we can expand our knowledge and learn something new. We started by trying to use Git, Github, VSCode LiveShare, and so much more, but they were so hard to use when you need to collaborate with your teammates. Finally, we figured out how to run a Flask app in [Glitch](https://glitch.com), and we continued coding, way faster than usual.

## What we learned

For most of us in the group it was our first hackathon. It was a little daunting but we were all excited for it. We learned a lot about the proccesses behind full stack development, including API calls, backend scripts, frontend development, how the two interact and so much more. There was a lot of stuff to learn, but we challanged ourselves and never looked back!

## Our Roles

### Krishnan Shankar

I worked on almost all of the backend for this project, including the Flask setup, API calls, location management, and our _special algorithm_ to determine what to wear. I also set up the project on Glitch, so that we can all collaborate together. Finally, I added some jinja2 code to the HTML in order to display Python data in HTML.

### Michael Spence

I worked on the design and look of the project. I suggested ideas for improvements to the UI, in order to start conversations to improve the UI of the project and make the project look more appealing to the average user. I also used CSS to style the website, to make sure it looked good in all weather conditions.

### Sammy Dods

I worked on a lot of the front end of the project. I oversaw the design of layout, which was sketched out over [AWW App](https://awwapp.com/), an online whiteboard. We decided that a 3 div layout would be able to clearly present relevant information, and give a pleasant minimal appeal. I built the foundation of the website in HTML, and then worked with Michael on styling it in CSS. 

### Hamza Khan

I worked on helping with both the backend and frontend. I researched APIs, modules, and other resources to help Krishnan with the backend, making sure the resources are compatible and work in every country/area. I also worked with Michael and Sammy to format the website, adding CSS to make it look better.

## What's next for What Should I Wear

Next for What Should I Wear is a plan to customize preferences for each user. After the user comes back home, our website will ask them how they felt, like did they feel too cold, too hot, and by how much. By adding an optional login, we can connect to a database to store the temperatures when the user decides to use a sweater instead of a long sleeve shirt. This will allow What Should I Wear to be different for every person, since no two people are alike. 
We could also turn this into a mobile app/widget for ease of access for the user to the app. 
**Thank You Judges for your time, and we hope you like our project!**
