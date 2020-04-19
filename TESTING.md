<h1 align="center">Covid Companion Website - Testing Section</h1>

<h2 align="center"><a href="https://github.com/LouieOHagan/Covid-Companion-Website/blob/master/README.md"><img src="https://i.ibb.co/Qm1yCFH/learn-more-button.png"></a><img src="https://i.ibb.co/r3pzZnS/logo.png"><a href="https://covid-companion.herokuapp.com/"><img src="https://i.ibb.co/cgF4snj/live-website-button.png"></a></h2>

##### Note: TESTING.MD is a connected to [README.md](https://github.com/LouieOHagan/Covid-Companion-Website/blob/master/README.md) but a seperate file has been created to keep README and reasonable length and to maintain cleanliness

## Testing

### Testing User Stories from User Experience (UX) Section

- #### First Time User Goals
    1. As a first time user, I want to be greeted with an easily navigable website which would require a simple and clean navigation bar.
        1. Upon successful loading of the website the user is greeted with the landing page.
        2. At the top of the screen the user can easily identify the navigation bar which has all the links well spaced for a clean look and making them easy to read.
    2. As a first time user, I want to be given feedback on any mistakes/actions I make such as an error message.
        1. If the user tries to access the "Give Help" or "Get Help" pages when not logged in they are given the 403 error page
        2. If the user enters the wrong URL that doesnt exist, they are given the 404 error page.
        3. Both of the above pages explain what has happened. whats gone wrong and offers a resoltion by either asking the user to login (403 error) or directing the user to the home page to get them back on track (404)
        4. If users are filling out a form and they have invalid information in the form they wont be able to continue and will get a small popup asking them to fill in a specific field or explaining there input is invalid.
        5. If a user is filling out a login or signup form and there is an error such as wrong password, email isnt on system when loggin in, email is already on system when signing up or passwords dont match when signing up the user will be given an error explaining what went wrong so they can correct it.
    3. As a first time user, I want to be able to create an account so that I can explore the options I have as a registered user.
        1. Upon successful loading of the website the user is greeted with the landing page.
        2. At the top of the screen the user can easily identify the navigation bar. To the far left a big yellow button grabs the users attention which takes them to the page to sign up.
        3. Pictures can be found [Here](https://github.com/LouieOHagan/Covid-Companion-Website/blob/master/readMe-assets/user-stories/sign-up.PNG)

- #### Vulnerable person Goals
    1. As a Vulnerable person, I want to be able to create a post to describe in detail what I am in need of.
        1. After logging in, from the dashboard the user can click the 'Get Help' button on their dashboard or in the navigation bar.
        2. The user is then directed to a page where half the form is automatically filled out with information from their account and they can fill out the remaining fields and adjust the autofilled ones if needed.
        3. Demonstration GIF can be found [Here](https://github.com/LouieOHagan/Covid-Companion-Website/blob/master/readMe-assets/user-stories/create%20post.gif)
    2. As a Vulnerable person, I want to be able to see the post I created to make sure it posted and to ensure that all the information is correct.
        1. After logging in, from the dashboard the user can click the 'Give Help' link in the navigation bar.
        2. Here they can see all posts that have been created which is where they will locate their post. 
        3. The user can open the post by clicking the card header and/or the button on the left handside of the card to view the information of their post.
        4. Demonstration GIF can be found [Here](https://github.com/LouieOHagan/Covid-Companion-Website/blob/master/readMe-assets/user-stories/read-post.gif)
    3. As a Vulnerable person, I want to be able to edit a post that I created but accidentally made some typos on.
        1. After logging in, from the dashboard the user can click the 'Give Help' link in the navigation bar.
        2. Here they can see all posts that have been created which is where they will locate their post. 
        3. The user can open the post by clicking the card header and/or the button on the left handside of the card to view the information of their post.
        4. If the user is the person who created the post, 2 buttons will be visible, "Edit" and "Delete".
        5. The user can click the edit button, make their changes and then click the "Update" button to update their post.
        6. Demonstration GIF can be found [Here](https://github.com/LouieOHagan/Covid-Companion-Website/blob/master/readMe-assets/user-stories/edit-post2.gif)
    4. As a Vulnerable person, I want to be able to delete a post after a volunteer has kindly done my shopping for me.
        1. After logging in, from the dashboard the user can click the 'Give Help' link in the navigation bar.
        2. Here they can see all posts that have been created which is where they will locate their post. 
        3. The user can open the post by clicking the card header and/or the button on the left handside of the card to view the information of their post.
        4. If the user is the person who created the post, 2 buttons will be visible, "Edit" and "Delete".
        5. The user can click the delete button and will be directed to a confirmation page to make sure they want to delete the post in case they clicked it by accident.
        6. Demonstration GIF can be found [Here](https://github.com/LouieOHagan/Covid-Companion-Website/blob/master/readMe-assets/user-stories/delete-post.gif)

- #### Vulnerable person Goals
    1. As a Volunteer, I want to be able to view posts that vulnerable people have created so that I can do my part by helping the people in need in my community.
        1. After logging in, from the dashboard the user can click the 'Give Help' link in the navigation bar.
        2. Here they can see all posts that have been created.
        3. Demonstration GIF can be found [Here](https://github.com/LouieOHagan/Covid-Companion-Website/blob/master/readMe-assets/user-stories/volunteer-read-post.gif)
    2. As a Volunteer, I want to be able to get in contact with the creator of the post to double check they don't need anything else while I'm out.
        1. After logging in, from the dashboard the user can click the 'Give Help' link in the navigation bar.
        2. Here they can see all posts that have been created.
        3. The user can open the post by clicking the card header and/or the button on the left handside of the card to view the information of the post which is where they will find the contact information.
        4. Demonstration GIF can be found [Here](https://github.com/LouieOHagan/Covid-Companion-Website/blob/master/readMe-assets/user-stories/volunteer-contact.gif)
    3. As a Volunteer, I want to be able to communicate to the post creator and other volunteers that I am going to do the shop to ensure more than 1 person isn't getting things for the one person at the same time.
        1. After logging in, from the dashboard the user can click the 'Give Help' link in the navigation bar.
        2. Here they can see all posts that have been created.
        3. The user can open the post by clicking the card header and/or the button on the left handside of the card to view the information of the post.
        4. The user will be able to see 3 buttons, "Available", "In Progress" & "Complete", one of these buttons will be disabled depending on what the status of the post is which can also be found in the post header.
        5. The user can click the button of the status they would like to change the post to.
        6. Demonstration GIF can be found [Here](https://github.com/LouieOHagan/Covid-Companion-Website/blob/master/readMe-assets/user-stories/volunteer-status.gif)

- #### Vulnerable person Goals
    1. As a Returning user, I want to be able to edit the information on my profile in case I inputted something wrong during registration.
        1. After logging in, from the dashboard the user can click the 'Edit Profile' button.
        2. The user will directed to the form where they can make adjustments to their profile information and can save it by clicking "Update"
        3. Demonstration GIF can be found [Here](https://github.com/LouieOHagan/Covid-Companion-Website/blob/master/readMe-assets/user-stories/edit-profile.gif)
    2. As a Returning user, I want to be able to logout of my account for privacy and safety reasons.
        1. After logging in, from the dashboard the user can click the 'Logout' link in the navigation bar.
        2. This will log the user out of their account and they will be redirected to the login page.
        3. Demonstration GIF can be found [Here](https://github.com/LouieOHagan/Covid-Companion-Website/blob/master/readMe-assets/user-stories/logout.gif)

### Further Testing
- The website was tested across a wide range of devices and browsers to ensure its fully responsive and compatible for all users.
    - Devices: The website was tested on Desktop, HP Envy Laptop, iPhone7, iPhone8 & iPhoneX. Chrome Developer tools was also used 
    throughout the entirety of development to test the screen sizes and compatability of 33 devices. 
    Full list of 33 devices can be found [Here](https://github.com/LouieOHagan/Covid-Companion-Website/blob/master/readMe-assets/device-list.png)
    - Browsers: The website was tested on Chrome, Microsoft Edge, Safari, Firefox and Internet Explorer.

- White space at bottom of screen below footer in iPad view (screen size of 768px in width).
    - After experiencing the issue in my previous project, I was aware the issue was with the bootstrap md class 
    only changing when it hit 767px where as my media query was pushing my footer up so that the phone navigation bar
    which became visible at this breakpoint wasnt overlapping the footer. As a result of this I had to create a seperate 
    media query with a max-width of 767px so that it was waiting until the screen size was 767px when the navbar switched 
    to push the footer up which fixed the bug in Ipad view.

- When a post was being updated, the `status` & `post_creator` keys and values were being removed from the updated post.
    - After looking through the MongoDB [Documentation](https://docs.mongodb.com/manual/reference/operator/update/set/) I discovered
    that the `update_one` method was updating the whole document by essentially clearing the document and updating it with the new keys & values.
    By using `$set:` in the format of `{ $set: { <field1>: <value1>, ... } }`, only the specified keys were being updated.

- Navbar active class not changing to the page that is active as the navbar is within the base.html page and unable to detect what page is currenty 
"active"
    - A fix was found for this issue in the [Flask Documentation](https://flask-navigation.readthedocs.io/en/latest/) & 
    on [Stack overflow](https://stackoverflow.com/questions/18600031/changing-the-active-class-of-a-link-with-the-twitter-bootstrap-css-in-python-fla) 
    by making the navigation bar dynamic using a for loop in the base.html. However, due to time limitations I  was unable to fix this issue so I 
    removed the active class and it has been added to the features to Implement in the future.

- Mobile navigation bar links and icons werent connected, when icon was hovered over the icon went orange but the link didnt and vice versa.
When the icon was clicked, the user wasnt being directed anywhere, it was only when the link was clicked.
    - This issue was fixed by putting the i element inside of the a tags and adjusted the styling in the style.css to have target them together.

- Error in Chrome developer tools console that stated "Cannot Read Property 'addeventlistener' of null".
    - After looking in to the issue I realized the issue was being caused because the main.js file was linked in the base.html meaning
    it was adding the eventlistener to all pages that base.html was being extended to. When the ID it was targetting couldnt be found,
    the console error was occuring.
    - I fixed the issue by removing the eventlistener and instead added an onclick attribute to the input element to call the function
    because that was the only place the function was being used in the project and only had to be called once.

- `__pycache__` folder was created and I pushed it to Github without knowing the contents of the cached file was the contents of the `env.py`
which contained all my enviroment variables.
    - To fix this issue I added the file to the `.gitignore` file and then used the `$ git rm --cached filename` command. This removed the file
    from my repository and it was no longer being pushed to github however the file was still easily accessible if someone reverted
    to an older commit that contained the file. As this was still a security risk I changed the passwords and keys inside of the `env.py` so that 
    if anyone did find the old file the contents would be useless. 

- Accordion functionality on Give Help page not working on Safari browser when tested on iPhone.
    - I am using the Bootstrap accordion which came with a button element that opened and closed the accordion,
    I removed that and put all the aria attributes in the accordion card-header div so the card could be clicked
    anywhere and it would open however safari was not recognising this.
    - I tried fixing the issue by giving the div a `type="button"` but that gave the whole card the safari button
    style and messed up the layout and `role="button"` proved ineffective so I decided to keep it the way it was but 
    also add a dropdown button with a type of button so that could be clicked on iphone and computer users could continue
    to click anywhere on the card-header div to open the accordion.

- Margin bottom for form labels stretches across the whole width of form on Firefox, Edge and Internet Explorer instead of 
just going across the length of the label + pushed out an extra 5px by padding.
    - After looking in to the issue [here](https://developer.mozilla.org/en-US/docs/Web/CSS/width#Browser_compatibility) 
    I found out that `width: fit-content` is still in experimental stages and is not compatible with Internet explorer. 
    I got it working on Firefox using `width: -moz-fit-content;` and `width: -webkit-fit-content;` is meant to work on Edge 
    however after testing it seemed that it didnt work.
    - I looked in to the issue further and found an alternative way of getting the bottom border the way I envision by using the
    css properties `display: table;`.

- When testing the website on an iPhone I noticed that even though I had the border set to none, the border-radius's were still there 
and were just floating there along.
    - After looking in to the issue I discovered that I had the css properties `border-radius:none` which was invalid. I fixed the issue by 
    setting the properties to `border-radius: 0px;`.

- When a user goes to the edit profile page and updates any information, the newest information is in the database however when they go back
to the dashboard their updated information isnt displayed. This is again confirmed when the user goes back to edit their profile, the old 
information is autofilled on the form ready to be edited again.
    - The information (specifically the users name which is in the page title & h1 element) in the dashboard and all other pages were being retrieved 
    through the session variables (`session['first_name']`)  which wasnt being updated when the information was updated. The changes were only reflected
    on page when the user logged out and logged back in which retrieved the newest information from the database.
    - I fixed this by removing all the session variables that were being created when a user logged in and only kept `session['logged-in']` & 
    `session['user_id']`. When I needed the information such as the first & last name about the user to display on the dashboard and any other pages
    the session variables were previosuly used, I using the find_one method to find the object using `session['user_id']` and then passed in the
    document through a variable to the page.

### Known Bugs