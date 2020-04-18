<h1 align="center">Covid Companion Responsive Website Project</h1>

<h2 align="center"><a href="https://github.com/LouieOHagan/Covid-Companion-Website#user-experience-ux"><img src="https://i.ibb.co/Qm1yCFH/learn-more-button.png"></a><img src="https://i.ibb.co/r3pzZnS/logo.png"><a href="https://covid-companion.herokuapp.com/"><img src="https://i.ibb.co/cgF4snj/live-website-button.png"></a></h2>

This is a website for a volunteer organisation called "Covid Companion". Covid Companion was set up to provide help for both old people and people who are classed as vulnerable during the current Covid-19 (Coronavirus) pandemic.
Their goal is to connect the old and vulnerable with people who are willing to volunteer their time to retrieve essential goods such as food and medication. This goal is achieved by providing a
navigable website that is very simplistic and that ensures all user actions that result in an error are given sufficient feedback in order to correct the mistake. This is a vital part of the website
in order to make the users experience as enjoyable and easy as possible while also ensuring the website is friendly to all types of users, specifically elderly people who may not be as "tech-savy".

Once registered, volunteer users will be given access to the "Give Help" page where they can see all the posts that have been created by people reaching out looking for help. They will be able to filter by county to find
people in their county that are in need of help and then open their post to see what the person is in need of. All posts have a status field which can be updated by volunteers. By default, posts will be assigned the "Available" status
once created, inside of the posts users can change the status to "In Progress" when they take on the role of retrieving the post creators things & "Complete" once they have delivered the items to the person in need.

Once registered, vulnerable users can navigable to the "Get Help" page where users can create posts. When creating a post, half of the form is automatically filled in for you, the information is 
retrieved from the users profile however these values can be changed like any other input field in case that the user is filling out a form on behalf of a family member or friend who does not have 
access to a computer. Users also have the option to provide the volunteer with a list of items that they require or can click the "Is this a Click and Collect Order ?" checkbox and provide the order 
number that they were given from the shop when they completed their click and collect order on their website.

Project preview/showcase

## User Experience (UX)

- ### User stories

- ### Design

* ### Wireframes
    
## Features

### Current Pages & Features

### To Do List
#### MUST DO
- ~~Get button on accordion and test on iphone~~ - **Implemented 18/04/20**
	- ~~If it works then style accordion properly~~
	- ~~look in to fix where one accordion is open all others close~~
	- ~~Add mailto: & tel: around contact info~~
- ~~Form validation~~ - **Implemented 15/04/20**
	- ~~checking if email exists already on register~~
	- ~~check that passwords match on register~~
	- ~~check if email exists on login aswell as password~~
    - ~~Setup Flash error responses~~
- ~~Add autofill values on forms from session information~~ - **Implemented 15/04/20**
- ~~Get content and styling for 404 pages, 500 pages, access denied pages and not your post pages~~ - **Implemented 18/04/20**
- Hero image for home page
- Content for home page
- ~~Add content and styling for dashboard~~ - **Implemented 17/04/20**
- ~~Create edit profile page~~ - **Implemented 16/04/20**
- Complete README.md
- ~~Fix site wide console error of id not being detected caused by eventlistenerID in main.js.~~ - **Implemented 15/04/20**
- ~~Fix border radius bug that appears on iphones with all input field border radius visible.~~ - **Implemented 15/04/20**
- Add more commenting on all code
	- Specifically the app.py file

#### PRIORITY
- Auto login when user creates account rather than redirecting to login page
- Add create account button on login form
- Fix bug on Edge & explorer with label width stretching across whole screen.
- For email in footer, instead of doing basic herf, toggle modal that gives option to copy email to clipboard OR mailto:

#### IF HAVE TIME
- Redo navbar with active class method from stackoverflow - use Refact in git commit
- Rewrite JS for hiding and showing order number with jQuery to fade in and out.
- Helpers pulsing, add with display absolute or relative and only show on larger screen devices.
- Make sign up form button not clickable until user confirms they are over 18
- Filter by county section
- Create update password page where they need to put in old password, new password and confirm new password.
- Setup so that all information doesnt dissapear if login or signup is unnsuccessful, only passwords dissappear.

###### Last Updated: 14:02pm GMT - 18/04/20 

### Features Left to Implement
##### These are features that have not been added at the time of development due to various reasons such as time limitations.

## Technologies Used

### Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://www.python.org/)

### Frameworks, Libraries & Programs Used
1. [Flask:](https://flask.palletsprojects.com/en/1.1.x/)
    - Flask was the primary framework used to handle all routes and provide all tools, libraries, and technologies required for the project.
1. [Flask-PyMongo:](https://flask-pymongo.readthedocs.io/en/latest/)
    - Flask-PyMongo was used to bridge Flask and PyMongo & to allow me to work with MongoDB from Python.
1. [PassLib:](https://passlib.readthedocs.io/en/stable/)
    - PassLib was used to hash passwords prior to entering the data in to the Database.
1. [MongoDB Atlas:](https://www.mongodb.com/cloud/atlas)
    - MongoDB Atlas was the cloud (non-relational) databse used to store all data being created on the website such as users and posts.
1. [Heroku:](https://www.heroku.com/home)
    - Heroku was used deploy the website.
1. [Bootstrap 4.4.1:](https://getbootstrap.com/docs/4.4/getting-started/introduction/) 
    - Bootstrap was used primarily for the grid system however the Bootstrap accordion & bootstrap classes for styling were also used throughout the project.
1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Titillium Web' font into the style.css file which is used on all pages throughout the project.
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used to add icons throughout the project for aesthetic and UX purposes.
1. [jQuery:](https://jquery.com/)
    - jQuery was used by Bootstrap specifically for the functionality of the accordion on the Give Help page.
1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [Gitpod:](https://www.gitpod.io/)
    - Gitpod was the primary IDE used throughout the entirety of the project. 
1. [GitHub:](https://github.com/)
    - GitHub is used to store the project code after being pushed from Git.
    - The GitHub repository is also linked to Heroku which is automatically deployed when a new commit is pushed.
1. [Photoshop:](https://www.adobe.com/ie/products/photoshop.html)
    - Photoshop was used to create the logo, the image used in the footer, images in the README and to edit background photos to maintain consistency in style (Black and white image with a 9px gaussian blur filter)  
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the [wireframes](https://github.com/LouieOHagan/Covid-Companion-Website#wireframes) during the design process. 
1. [Screen to GIF](https://www.screentogif.com/)
    - Screen to GIF was used to record the screen to create GIF's to demonstrate a specific task in video for the README.md file.
1. [HTML Formatter](https://htmlformatter.com/)
    - HTML Formatter was used to beautify code to keep the code neat and easy to read. It was utilised as Beautify Cmd (Shift + Alt + F) in GitPod distorted the code in GitHub.


## Testing

### Testing User Stories from User Experience (UX) Section

### Further Testing

### Known Bugs

## Deployment

## Credits

### Code

### Content

### Media

### Acknowledgements
