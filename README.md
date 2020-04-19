<h1 align="center">Covid Companion Responsive Website Project</h1>

<h2 align="center"><a href="https://github.com/LouieOHagan/Covid-Companion-Website#user-experience-ux"><img src="https://i.ibb.co/Qm1yCFH/learn-more-button.png"></a><img src="https://i.ibb.co/r3pzZnS/logo.png"><a href="https://covid-companion.herokuapp.com/"><img src="https://i.ibb.co/cgF4snj/live-website-button.png"></a></h2>

This is a website for a volunteer organisation called "Covid Companion". Covid Companion was set up to provide help for both old people and people who are classed as vulnerable during the current Covid-19 (Coronavirus) pandemic.
Their goal is to connect the old and vulnerable with people who are willing to volunteer their time to retrieve essential goods such as food and medication. This goal is achieved by providing a
navigable website that is very simplistic and that ensures all user actions that result in an error are given sufficient feedback in order to correct the mistake. This is a vital part of the website
in order to make the users experience as enjoyable and easy as possible while also ensuring the website is friendly to all types of users, specifically elderly people who may not be as "tech-savy".

Once registered, volunteer users will be given access to the "Give Help" page where they can see all the posts that have been created by people reaching out looking for help. They will be able to filter by county to find
people in their county that are in need of help and then open their post to see what the person is in need of. All posts have a status field which can be updated by volunteers. By default, posts will be assigned the "Available" status
once created, inside of the posts users can change the status to "In Progress" when they take on the role of retrieving the post creator's things & "Complete" once they have delivered the items to the person in need.

Once registered, vulnerable users can navigable to the "Get Help" page where users can create posts. When creating a post, half of the form is automatically filled in for you, the information is 
retrieved from the users profile however these values can be changed like any other input field in case that the user is filling out a form on behalf of a family member or friend who does not have 
access to a computer. Users also have the option to provide the volunteer with a list of items that they require or can click the "Is this a Click and Collect Order ?" checkbox and provide the order 
number that they were given from the shop when they completed their click and collect order on their website.

<h2 align="center"><img src="https://i.ibb.co/LQLmwY7/Final-Showcase.jpg"></h2>

## User Experience (UX)

- ### User stories
    - #### First Time User 
        1. As a First Time User, I want to be greeted with an easily navigable website which would require a simple and clean navigation bar.
        2. As a First Time User, I want to be given feedback on any mistakes/actions I make such as an error message.
        3. As a First Time User, I want to be able to create an account so that I can explore the options I have as a registered user. 
    - #### Vulnerable person 
        1. As a Vulnerable person, I want to be able to create a post to describe in detail what I am in need of.
        2. As a Vulnerable person, I want to be able to see the post I created to make sure it posted and to ensure that all the information is correct.
        3. As a Vulnerable person, I want to be able to edit a post that I created but accidentally made some typos on.
        4. As a Vulnerable person, I want to be able to delete a post after a volunteer has kindly done my shopping for me.
    - #### Volunteer 
        1. As a Volunteer, I want to be able to view posts that vulnerable people have created so that I can do my part by helping the people in need in my community.
        2. As a Volunteer, I want to be able to get in contact with the creator of the post to double check they don't need anything else while I'm out.
        3. As a Volunteer, I want to be able to communicate to the post creator and other volunteers that I am going to do the shop so that more than 1 person isn't getting things for the one person at the same time.
    - #### Returning user
        1. As a Returning user, I want to be able to edit the information on my profile in case I inputted something wrong during registration.
        2. As a Returning user, I want to be able to logout of my account for privacy and safety reasons.

- ### Design
    - #### Colour Scheme
        - The 2 main colours I chose for the project was #3c3c3c (a dark gray) & #feb62e (A mustard yellow/light orange) while also incorporating #f5f5f5 (an off-white) too as I felt
        that the constant use of a dark colour (#3c3c3c) on a vibrant mustard yellow (#feb62e) would be too much and instead the mustard yellow would be used to make certain features 
        "pop"/stick out and make them more visually powerful.
        - Originally I planned to go with black (#000) and a very bright yellow that is usually seen on Covid-19 warning signs such as [here](https://www.rehab.ie/images_upload/news-and-stories/blogs/COVID.jpg)
        however after considering the thoughts the user could generate after seeing such bright colours I reconsidered the colour scheme as the website is meant to be warm and welcoming. Many people 
        would consider bright yellow as a colour of warning and is usually used to grab the attention of a person, as a result I changed the colour scheme to a mustard yellow / bright orange
        (#feb62e) and also changed the black to a dark grey (#3c3c3c) to ensure the website felt warm and welcoming to the user so they are instantly attracted to the site and
        their mind is relaxed and feels secure to ensure the best user experience. The Psychological effects that colours can have was a big part of deciding what colours to go with.
            - [#3c3c3c](https://www.color-hex.com/color/3c3c3c) (Dark gray): "Black communicates absolute clarity, with no fine nuances. It communicates sophistication and uncompromising 
            excellence and it works particularly well with white. Black creates a perception of weight and seriousness."
            - [#feb62e](https://www.color-hex.com/color/feb62e) (Mustard Yellow/Light Orange): "Since it is a combination of red and yellow, orange is stimulating and the reaction to 
            it is a combination of the physical and the  emotional. It focuses our minds on issues of physical comfort - food, warmth, shelter etc. - and sensuality. It is a 'fun' colour."

    - #### Typography
        - The Titillium Web is the only font used throughout the whole website with Sans Serif as the backup font in case for any reason the font isn't being imported into the site correctly.
        I have found that finding the correct font can usually be quite a time consuming process however in this case I was looking for a font that offered many different font weights but also
        was very simplistic and easy to read without being too big and "in your face". As I have used the Titillium Web font in a previous project I was confident that this would be a good
        choice. The font was imported in to the style.css from Google Fonts who make it very easy to to import fonts and are a very reliable external source. The Titillium Web font offers 11 font 
        weight styles from "Extra Light" (200 weight) to "Black" (900 weight) however for this project only the 300, 400, 500 & 600 font weights were imported and utilised.

    - #### Imagery
        - During the design process, imagery was a massive factor because instead of having a background colour I planned to have an image in the background of all of the pages because I
        felt that it would too dark and boring to have a solid dark grey background. I decided on a style of image that would be consistent throughout the whole website which ended up being
            - The theme I planned to keep for all of the images was outdoor photos from around Dublin. I planned to edit all photos in photoshop to ensure all background images maintained the 
            same style which was a black and white image with a 9px gaussian blur filter. After testing the black and white image without the blur filter, there wasnt enough contrast and 
            the background image took too much of the attention of the primary purpose of the page.
        - As well as the background images, I decided to create an image for the footer that was a simplistic but powerful "swoosh" which matched the colour scheme of the website. I felt it
        would add a bit more personality and colour to the footer as the footer of a page is the end of the page and commonly isnt the most exciting part of a website.    

* ### Wireframes
    * Home Page Wireframe - [View](https://github.com/LouieOHagan/Covid-Companion-Website/blob/master/readMe-assets/wireframes/Home%20Page.png)   

    * Give Help Page Wireframe - [View](https://github.com/LouieOHagan/Covid-Companion-Website/blob/master/readMe-assets/wireframes/Give%20Help%20Page.png)

    * Get Help Page Wireframe - [View](https://github.com/LouieOHagan/Covid-Companion-Website/blob/master/readMe-assets/wireframes/Get%20Help%20Page.png)

    * Login Page Wireframe - [View](https://github.com/LouieOHagan/Covid-Companion-Website/blob/master/readMe-assets/wireframes/Sign%20In%20Page%20Page.png)

    * Sign Up Help Page Wireframe - [View](https://github.com/LouieOHagan/Covid-Companion-Website/blob/master/readMe-assets/wireframes/Sign%20Up%20Page.png)

    * User Dashboard Help Page Wireframe - [View](https://github.com/LouieOHagan/Covid-Companion-Website/blob/master/readMe-assets/wireframes/User%20Dashboard%20Page.png)

    * Edit Post Page Wireframe - [View](https://github.com/LouieOHagan/Covid-Companion-Website/blob/master/readMe-assets/wireframes/Edit%20Post%20Page.png)

    * Edit Profile Page Wireframe - [View](https://github.com/LouieOHagan/Covid-Companion-Website/blob/master/readMe-assets/wireframes/Edit%20Profile%20Page.png)

    * Error Pages Wireframe - [View](https://github.com/LouieOHagan/Covid-Companion-Website/blob/master/readMe-assets/wireframes/Error%20Page.png)

    * Click [Here](https://github.com/LouieOHagan/Covid-Companion-Website/blob/master/readMe-assets/wireframes/MS3%20Wireframes.pdf) for Document containing all Wireframes in .pdf format.
    
## Features

### Current Pages & Features

- Navigation bar
    - For larger screened devices the website has a "traditional" navigation bar that any user would expect to see when they load on to a website
    however once the screen width size reaches below 768px pixel I decided to take a different design route. "Traditionalally" I would go for a burger 
    icon however during my design process I came across "Thumb zone designing".  
    - "Hoober’s research shows that 49% of people hold their smartphones with one hand, relying on thumbs to do the heavy lifting. Clark took this even 
    further and determined that 75% of interactions are thumb-driven. With this understanding of hand placement, we can conclude that certain zones for 
    thumb movement apply to most smartphones. We’ll define them as easy-to-reach, hard-to-reach and in-between areas."
        - A diagram showing these places to reach can be found [here](https://cloud.netlifyusercontent.com/assets/344dbf88-fdf9-42bb-adb4-46f01eedd629/496f7bc0-4c6c-4159-b731-ec3adcf91105/thumb-zone-mapping-opt.png)
        - Further information on Thumb Zone design found [here](https://www.smashingmagazine.com/2016/09/the-thumb-zone-designing-for-mobile-users/)
    - The navigation bar down the bottom of your screen is simply a lot more convinient for the user and offers a better user experience. When looking on a computer it can
    be a little bit surprising as you expect to see a burger icon however after testing it on multiple smartphones I realised that you would hardly notice the different 
    as in our everyday lives we use Instagram, Facebook, Twitter, Youtube etc countless amounts of times, all of which use the same styled navigation bar in their mobile apps.
    
- Accordion 

- CRUD Functionality

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
- ~~Hero image for home page~~ - **Implemented 19/04/20**
- ~~Content for home page~~ - **Implemented 19/04/20**
- ~~Add content and styling for dashboard~~ - **Implemented 17/04/20**
- ~~Create edit profile page~~ - **Implemented 16/04/20**
- ~~Complete README.md~~ - **Implemented 16/04/20**
- ~~Fix site wide console error of id not being detected caused by eventlistenerID in main.js.~~ - **Implemented 15/04/20**
- ~~Fix border radius bug that appears on iphones with all input field border radius visible.~~ - **Implemented 15/04/20**
- Add more commenting on all code
	- Specifically the app.py file
- ~~Fix bug on Edge & explorer with label width stretching across whole screen.~~ - **Implemented 18/04/20**

#### IF HAVE TIME
- Auto login when user creates account rather than redirecting to login page
- Add create account button on login form
- For email in footer, instead of doing basic herf, toggle modal that gives option to copy email to clipboard OR mailto:
- Redo navbar with active class method from stackoverflow - use Refact in git commit
- Rewrite JS for hiding and showing order number with jQuery to fade in and out.
- Helpers pulsing, add with display absolute or relative and only show on larger screen devices.
- Make sign up form button not clickable until user confirms they are over 18
- Filter by county section
- Create update password page where they need to put in old password, new password and confirm new password.
- Setup so that all information doesnt dissapear if login or signup is unnsuccessful, only passwords dissappear.

###### Last Updated: 11:52am GMT - 19/04/20 

### Features Left to Implement
##### These are features that have not been added at the time of development due to various reasons such as time limitations.

- Login with google, facebook, twitter etc
- Verification system for volunteers so volunteers are all verified and not people that could possibly rob money, foods, medicines etc.
- Archive posts that are complete so thats posts arent deleted but also so they arent clogging up the main posts section waiting for the creator to delete it.
- Two Factor Authentication by sending email to user to confirm and then user is redirected to login page when they sign up until they confirm their email.
- Pagination on Give Help page
- Limit amount of characters users can input in to any text field input
	- For security reasons so millions of characters cant be pasted in
	- Also to be able to better plan for the responsiveness of displaying data 
		- Right now posts can be as long or short as possible so not much can be done when it comes to the responsive side other than make sure everything is well spaced apart
- Get rid of accordion and make another template page so users can just click in to a page and have the data presented neatly 
- Features in the "If have time" section of the To Do list.
- Remake home page with cleaner look and more content.
- Add more content to the Features section of README.md file.

## Database Schema
- The Database is made up of 3 collections in total, `counties`, `posts` & `users`
#### Counties Collection
- The counties collection has 32 documents overall, each one containing 2 keys, the autogenerated _id & county_name which contains the name of a county of Ireland.
- The decision to create the collection was to make it easy to store the county names and then loop thorugh them in a drop down while creating a posts. I originally planned
to also be able to filter by county on the Give Help page which would contain another drop down that looped through this collection however due to time limitations that function
was not complete.
```
    '_id': ObjectId('...'),
    'county_name': '...',
```
#### Posts Collection
- The posts collection houses all the posts that are created in the Get Help Page.
- There are 11 keys overall inc: the autogenerated _id key. When a post is created, it automatically is assigned the status of "Available"
and the post_creator retrieves the logged in users (session['user_id']) _id and is stored as a string. The values for the rest of the keys are
retrieved from the form that the user fills out when creating a post.
```
    '_id': ObjectId('...'),
    'title': '...',
    'description': '...',
    'order_number': '...',
    'county': '...',
    'address': '...',
    'name': '...',
    'email': '...',
    'phone_number': '...',
    'status': '...',
    'post_creator': '...'
```
#### Users Collection
- The users collection houses all the user profiles that are created when signing up and registering an account.
- There are 9 keys overall inc: the autogenerated _id key. The values for all of the keys are retrieved from the 
form that the user fills out when signing up and registering an account. When signing up, the user has to 
type the password twice however before any data is inserted in to the collection the passwords are checked to confirm
they are the same, the password is then hashed and inserted once.
```
    '_id': ObjectId('...'),
    'first_name': '...',
    'last_name': '...',
    'user_email': '...',
    'password': '...',
    'user_phone': '...',
    'user_address': '...',
    'user_type': '...',
    'is_over_18': '...'
```
- Database Schema Diagram can be found [Here](https://github.com/LouieOHagan/Covid-Companion-Website/blob/master/readMe-assets/database-scheme.PNG)

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

**Note:** All Testing Information can be located in seperate [TESTING.MD File](https://github.com/LouieOHagan/Covid-Companion-Website/blob/master/TESTING.md) due to length of content.

## Deployment

I took the following steps to deploy the project successfully to Heroku.
### Deploying by connecting Github to Heroku

1. Up to the top right of the screen I clicked the "New" Dropdown button and then clicked the dropdown and selected "Create new app".
2. I called the app "covid-companion" and set the region to "Europe".
3. Once my app was created, I chose my deployment method which was "Connect to GitHub".
4. After logging and authenticating my GitHub account, I typed the repository name in to the search bar in the "Connect to GitHub" section and searched for "Covid-Companion-Website".
5. When the repository appeared, I clicked the "Connect Button"
6. Once connected, I selected my master branch in the "Automatic deploys" section and clicked "Enable Automatic Deploys" button to ensure that every time I push to GitHub the app is rebuilt and is always up to date with the latest code.
7. Afterwards I went back to my Gitpod workspace and in my CLI I created a requirements.txt so Heroku knows what dependecies need to be installed for the application to run by running the following command. `pip3 freeze > requirements.txt`.
8. I then created a Procfile which Heroku also requires by running the following command. `echo web: python app.py > Procfile`.
9. I then went through the standard process of pushing these files to Github, which Heroku recognised and rebuilt the app.

Alternatively I could have connected my application through Heroku CLI
### Deploying using Heroku CLI

1. Up to the top right of the screen I would click the "New" Dropdown button and then click the dropdown and select "Create new app".
2. I would then call the app "covid-companion" and set the region to "Europe".
3. Once my app was created, I would chose my deployment method which would be "Use Heroku CLI".
4. Next I would go to my Gitpod workspace and in my CLI I would login in to Heroku using the following command. `heroku login -i`.
5. I would then go back to my Application dashboard and in the settings section I would take the "Heroku git URL" in "App Information".
6. Back in my Gitpod workspace, I would link my repository to Heroku using the following command. `git remote add heroku https://git.heroku.com/covid-companion.git`.
7. I would then create a requirements.txt so Heroku knows what dependecies need to be installed for the application to run by running the following command. `pip3 freeze > requirements.txt`.
8. I would then create a Procfile which Heroku also requires by running the following command. `echo web: python app.py > Procfile`.
9. Lastly, I would push my application to Heroku which I will have to do manually each time using the following command. `git push heroku -u master`.

### Setting Up Heroku Enviroment Variables

1. In the application dashboard, navigate up the top of the screen and click the "Settings" button in the navigation menu.
2. In the "Config Vars" section, click "Reveal Config Vars" which is where I added my enviroment variables.
3. I then set all the enviroment variables up by adding the variable name to the "KEY" field and the variable value to the "VALUE" field and clicking the "Add" button.
```
    IP = 0.0.0.0
    MONGO_DBNAME = '...'
    MONGO_URI = '...'
    PORT = 5000
    SECRET_KEY = '...'
```

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/LouieOHagan/Covid-Companion-Website)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type ```git clone```, and then paste the URL you copied in Step 3.
```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```
7. Press Enter. Your local clone will be created.
```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `Spoon-Knife`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```
Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Credits

### Code
- [Bootstrap4](https://getbootstrap.com/docs/4.4/getting-started/introduction/): Bootstrap Library used throughout the project mainly to make the site responsive using the Bootstrap Grid System, as well as utilizing Bootstraps accordion component and various bootstrap classes for styling.
- [Martin Wolf](https://www.youtube.com/watch?v=t9nQDdrPgZ0): for tutorial on how to animate the border-bottom of a link on hover that I used in the navbar of my project.
- [Florin Pop](https://codepen.io/FlorinPop17): for original inspiration and pieces of code for bottom mobile navigation bar. Both HTML & CSS modified and some parts rewritten to better fit use.
- Kevin Loughrey for help setting up basic account system & for check_logged_in wrapper function on line 21-28 of app.py
```
def check_logged_in(func):
    @wraps(func)
    def wrapped_function(*args, **kwargs):
        if 'logged-in' in session:
            return(func(*args, **kwargs))
        else:
            return render_template('403.html', title="Access Denied")
    return wrapped_function
```

### Content
- Psychological properties of colours text in the README.md was found [here](http://www.colour-affects.co.uk/psychological-properties-of-colours)
- Smashing Magazine for information on Thumb zone design was found [here](https://www.smashingmagazine.com/2016/09/the-thumb-zone-designing-for-mobile-users/)

### Media
- [Pixabay](https://pixabay.com/): All stock background images of Dublin were obtained from Pixabay.

### Acknowledgements
- My Mentor Adegbenga Adeye for continuous helpful feedback and ideas to improve both myself as a developer and my project.

- Kevin Loughrey and Xavier Astor for continuous assistance with technical issues and project feedback day in, day out 

- [Matt Rudge](https://github.com/lechien73): for project idea inspiration and continuous assistance with technical issues and project feedback.

- [sentdex](https://pythonprogramming.net/flash-flask-tutorial/): for information and a video tutorial on Flasks Flash function.