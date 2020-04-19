<h1 align="center">Covid Companion Website - Testing Section</h1>

<h2 align="center"><a href="https://github.com/LouieOHagan/Covid-Companion-Website/blob/master/README.md"><img src="https://i.ibb.co/Qm1yCFH/learn-more-button.png"></a><img src="https://i.ibb.co/r3pzZnS/logo.png"><a href="https://covid-companion.herokuapp.com/"><img src="https://i.ibb.co/cgF4snj/live-website-button.png"></a></h2>

##### Note: TESTING.MD is a connected to [README.md](https://github.com/LouieOHagan/Covid-Companion-Website/blob/master/README.md) but a seperate file has been created to keep README and reasonable length and to maintain cleanliness

## Testing

### Testing User Stories from User Experience (UX) Section

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