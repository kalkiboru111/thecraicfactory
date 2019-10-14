[![Build Status](https://travis-ci.org/kalkiboru111/thecraicfactory.svg?branch=master)](https://travis-ci.org/kalkiboru111/thecraicfactory)

# The Craic Factory

The point of this site is to pun. That is to say, the point of this site is to make puns about how "craic" (the Irish slang term for raillery, banter, persiflage) sounds like "crack" (...the drug). Yes, that's it. Yes, it's stupid. That's the point. 

To try to construe this site in a more flattering light, we could say it's a social media platform providing curated content to members. The curation function is achieved through member voting, and the attribution of certain quantities of "craic" to posts. This attribuation happens when a member chooses to purchase craic for another member to reward them for a good post. In other words, Craic is a nominal reward for saying something funny. It is somewhat analagous to Reddit Gold on reddit.com, except that Reddit Gold grants the recipient access to premium features - here no one really gains from the purchase of the craic (in that way, it's quite similar to crack).

## UX

The UX of this site is designed for compulsive users ("craic addicts"). I therefore have the content on the home page hugging the left margin, which provides the most natural and frictionless line of site for users who are quickly scrolling through the content. I call this the "craic pipe". Consistent with convention, the prime real estate is given to the primary heading, "The Craic Factory" which resets the home page to the most recent posts that users have uploaded. 

Everything relevant to a post is displayed within the post. The purhcase of craic is meant to be fricionless - it's a pointless reward; the users already have "no reason to buy it", so the goal is to avoid providing the user with "a reason to not buy it". The purchase therefore happens with a large bright button from within the post, with the name of the user for whom the craic is being bought embedded in the button. 

The purchase button directs the user right to the prodcuts page, containing a veritable smorgasbord of amusing product names, "8-ball", "the mother load" - realistically, the user is only likely going to buy a dime bag, but providing this range of products with high prices inflates the value of the dime bag. It's similar to how a watch salesman might cajole you into trying on a Rolex, and then make you feel like you out maneuvered him when you leave wearing a less expensive watch that you never wanted in the first place. The products purchased are then displayed next to the post. The publisher of the post thereby gets their nominal kudos for their witty pun/repartee. The posts also show the amount of views and votes, which serve essentially the same purpose as the craic, except the craic is a most potent signal of quality content because it has been paid for.The text areas and image areas for posts are gratnted the majority of the real estate, because they are the primary points of interest on the site. 

In terms of user stories:
- As a "lurker" or passive user type, I want to only peruse the content, but not post any myself. To achieve this goal, I merely have to log in and scroll through the posts. 
- As an active user, I can use the "New Post" button in the nav bar to add content and photos. 

Note: I did not create a wireframe here, because the application does not vary between web and mobile, and, in any event, is optimally simplified such that a wireframe is not going to add anything of value. 

## Features

The project has a number of features, some of which have already been touched on above.

 
### Existing Features
- The Craic Pipe - allows users to get their fix of craic, by having a stream of content that is "weighted" based upon votes, views and craic. 
- The Vote Button - allows users to vote on posts which they like, by clicking on the thumbs up button next to the post. Each user can only vote only once, which means that votes are a felicitous representation of what the Craic Factor Community prefers. 
- The View Count - allows user to assess how many other user have seen a post, and thereby determine whether its perceived value relative to the amount of votes and craic that it has.
- The Craic Count - displays the quantity of craic that has been purchased for a particular post. 
- The Buy Craic Button - enables users who wish to purchase craic to do so in a relatively seemless fashion, by clicking on the button which redirects to the products page. 
- The Cart - enables users to track the quantity of craic products they are using by signifying the number of products the user has added to their cart as a number next to the cart. It then persists that quantity, while allowing the user to continue to browse the application. This ensures continuity of use and that users don't get distracted from the application or or simply quit the application once they have made a single purchase. 
- The New Form - feature enables user to submit new posts, with images, tags and other fields, by simply clicking on the next form button. The text field then provides users with the area to enter their titillating tale of craic. 
- The Search Bar - a user who wants to search through posts for a particular type of craic can do so by simply entering their search query into the search bar. Consistent with this application's emphasis on content, the search bar features in the same place in the nav bar on every paage in the application. It thereby enables a user to search for whatever craic strikes his fancy, no matter where he may be in the application at that particular moment. 

### Features Left to Implement
- I am considering adding an algorithm that sorts the posts in terms either votes, views, the quantity of craic that has been purchased for a particular post, or some cobination of these criteria. However, I feel ranking in this fashion is not really consistent with the organic nature of this application. Also, it's unlikely to be necessary to provide this degree of order to the content unless and until this app has a large amount of users. 
- I may provide users with an add videos feature.  
- I have deliberately left a significant amount of white space to the right side of the Craic Pipe - this is real estate for advertisers (no advertisements for the sale of illicit substances will be accepted).
- The Friends Tag - will enable users to tag other users whom they feel will find the post particularly interesting. 
- The Topic Tag - enables users to tag posts with particular categories by simply entering the name of the category into the tag field. This enables the user to categorize their craic into genres of sub-craic, and search through these sub-genres accordingly. 

## Technologies Used

In terms of the languages, frameworks, libraries used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
- **HTML**, **CSS**, **Javascript** and **Python**
  - Base languages used to create website
- [Django](https://www.djangoproject.com/)
    - The python framework **Django** was used to develop views, models and templates.
- [Bootstrap](http://getbootstrap.com/)
    - **Bootstrap** is used to render a responsive layout
- [Whitenoise](https://warehouse.python.org/project/whitenoise/)
    - Static files are served in production with Whitenoise 
- [Stripe](https://stripe.com)
    - The online payment processing system **Stripe** is used to handle purchases of Craic.
- [AWS S3](https://aws.amazon.com/s3/)
    - **AWS S3** cloud storage is used to store static and media files for the application.
- [Heroku](https://www.heroku.com/)
    - The Cloud Application Platform **Heroku** hosts the Craic Factory application.
- [Heroku-Postres](https://www.heroku.com/postgres)
    - During development mode, models were migrated to the default SQLite databse provided by Django. In production mode, data is stored in a postgreSQL database using **Heroku-Postres**. 
    

## Testing

In terms of testing, I conducted both manual and automated testing.

### Automated

I used Chrome Developer tools to inspect the application's code, checking that all elements and styles were loading as intended, and that all file paths were functioning correctly. I also used the following services to verify the correct syntax for HTML and CSS: 
[HTML Validator W3](https://validator.w3.org)<br>
[W3 CSS Validator](https://jigsaw.w3.org/css-validator/)<br>

The automated testing was carried out by Travis CI, by inputting the relevant link into the markdown formatted ReadME file. The logs within Travis were then closely inspected to determine if the tests were passing or failing. Initial tests failed, and this required me to remove a number of files from the requirements.txt file which had been automatically installed by Amazon C9. AFter this, there were some more failed tests due to certain libraries not being up to do date, e.g., the pillow library was not initially up to date, and this required me to uninstall and reinstall the approach version. Furthermore, the travis integration itself did not initially function because Travis is picky with respect to which version of Python is cited in the .travis.yaml file - so this required some modificationt to ensure that the correct version of python was mentioned and that the correct commeand for install was provided ("pip3 install -r requirements.txt"). 

A great deal of time was spent attempting to get images uploading to the S3 Bucket. For some reason (and even with the input of a number of tutors, I was not able to determine exactly what the problem was), the S3 Bucket was not receiving media files that were uploaded from within the application. Eventually, after setting up a new S3 Bucket, with new users, groups, ACLs, permissions, and CORs configurations, and adjusting all of the settings in the settings.py and env.py files, we were able to get the bucket functioning (this took well over a week to get this functioning, and it's still not entirely clear what was wrong). 

Travis CI pre-deployment tests were carried out using the Travis Continuous Integration service. At time of deployment, integration tests were passing. However, it's worth noting that there were some issues with the Travis testing being incapable of connecting to the Postgres database on Heroku, and was attemptting to create a test database for testing purposes. It then asked to confirm this action by typing "yes" into the Travis log, but the log didn't accept text input and so I was unable to confirm. I consulted with some tutors on Slack and was informed that I should include an if-else statement that redirects to an sqlite database - however, this was already included in the settings, so it's still a bit of a mystery as to why this wasn't funcionting .

### Manual Testing:

In terms of manual testing, the following scenarios were tested:

1. Login:
    1. Verify that the login button appears in the appointed place ion the nav bar, and only for users whom are not logged in
    2. Click on the login link in the nav bar
    3. Try to submit the empty form and verify that an error message about the required fields appears
    4. Try to submit the form with an invalid email address and verify that a relevant error message appears
    5. Try to submit the form with an invalid password and verify that the relevant error message appears
    6. Try to submit the form with an invalid username and verify that the relevant error message appears
    7. Try to submit the form with all inputs valid, verify that a success message appears, and verify that you are redirected to the home page
2. Register:
    1. Verify that the register button appears in the appointed place in the nav bar, and only for users whom are not logged in
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with an email address for an existing user and verify that the relevant error message appears "A user with that username already exists"
    5. Try to submit the form with all inputs valid and verify that a success message appears.
    6. Try to login wtih the new user and verify by logging in with the new user credentials.  
3. Reset Password:
    1. Verify that the reset password button appears in the appointed place below the login fields
    2. Try to reset the password by clicking on this link and verify that the correct form appears with the requisite fiels for resetting the password
    3. Try to submit the form with all inputs valid and verify that a success message appears.
    4. Verify that the reset process works by logging back in with the new password
4. Craic Pipe:
    1. Go to the "Craic Factory" home page
    2. Try to scroll through the posts. Verify that posts are displaying wtih correct fields, that images are loading
    3. Click "Read More" and verify that you are redirected to another page with the post detail.
    4. Click "Return to Craic Pipe" and verify that you are redirected back to the Craic Pipe 
    5. Try to submit the form with an invalid email address and verify that a relevant error message appears
    6. Try to submit the form with all inputs valid and verify that a success message appears.
5. New Post:
    1. Go to the Craic Pipe, verify that the new post button appears in the appointed place in the nav bar, and verify that it does not appear for users that are not logged in
    2. Try to add a new post by clicking on the new post button and verify that you are redirected to the appropriate form with the relevant fields
    3. Try to submit a new post by filling out all the fields, including uploading an image, and verify that the user is redirected to the craic pipe and that the post appears correctly wtih all fields populated
    4. Try to submit the empty form and verify that an error message about the required fields appears
    5. Try to submit the form with all inputs valid and verify that a success message appears.
6. Search Bar:
    1. Go to the Craic Pipe, verify that the search bar appears in the appointed place in the nav bar, and verify that it does not appear for users that are not logged in
    2. Conduct spot checks to determine that the search field is correctly returning posts based on the content of the search query
7. Add Products to Cart:
    1. Go to the Craic Pipe, verify that the cart appears in the appointed place in the nav bar, and verify that it does not appear for users that are not logged in
    2. Verify that the "Purchase [Username] Craic" appears in the appointed place in each post
    3. Try to add some Craic to the cart by clicking on the button, and verify that the button redirects to the products page
    4. Try to add some products to the cart by inputting some quantities, clicking add, verifing that the user is redirected to the Craic Pipe and that the same quantity of products appears next to the Cart icon in the nav bar
8. Cart Functionality & Checkout:
    1. Try to purchase the products in the cart by clicking on the cart icon and verify that the user is redirected to the cart page with the correct products and the checkout button
    2. Try to purchase the products by clicking on the checkout button and verify that you are redirected to a payment form
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with invalid fields and verify that the relevant error messages appear
    4. Try to submit the form with all inputs valid and verify that a success message appears, and consult the Stripe dashboard to confirm that the payment was in fact successful. 
9. Logout:
    1. Go to the Craic Pipe, verify that the log out appears in the appointed place in the nav bar, and verify that it does not appear for users that are not logged in
    2. Try to log out by clickign the log out button and verify that the user is logged out and redirected to the login page of the application

I also conducted UX testing across a range of devices, browsers, and screen sizes. The application is designed to look the same on every device. Browser compatibility was tested on the following browsers: -Mozilla Firefox
-Google Chrome

Device compatibility was testing on the following devices, using the Chrome inspect functionality: 
- GalaxyS5
- Pixel
- Pixel 2XL
- IPhone 5/SE
- IPhone 6/7/8
- IPhone 6/7/8 Plus
- IPhone X
- IPad
- IPad Pro

## Deployment

In terms of development, I created the application using the AWS Cloud9 IDE. This was a problematic IDE to use at the best of times, as there were a number of instances when technical issues interfered with the development process. The application was tested in a development environment with Django's debug mode (in settings: Debug=True). This enables the display of error pages, with detailed traceback, including metadata about the environment, such as all the currently defined Django settings (from settings.py). 

In terms of preparation for deployment, I removed all hard-coded environment variables. These were placed in the env.py for development and entered into Heroku's Config Vars for production (further detailed below). I ensured the requirements.txt was up-to-date with all the latest packages installed recorded therein (updating this file using the "pip3 freeze > requirements.txt" command). A Procfile was included as required by Heroku in order to run the application. I pushed all static files to S3 Bucket using the "python3 manage.py collectstatic" files. I incrementally pushed all code GitHub ready for deployment via Heroku's GitHub function.

This application is deployed to Heroku here:https://thecraicfactory.herokuapp.com/accounts/login/?next=/. Config variables were stored in an environment file during development. Heroku settings were updated with the relevant config variables upon deployment. The following variables were used: 
1. AWS_ACCESS_KEY_ID
2. AWS_SECRET_ACCESS_KEY
3. DATABASE-URL
4. DISABLE_COLLECTSTATIC
5. SECRET_KEY
6. STRIPLE_PUBLISHABLE
7. STRIPE_SECRET

The SECRET_KEY used in development is different from that used in production. Debug settings were only used in the development environment, and not the production environment, to ensure that sensitive data was not inadvertently published. In lieu of the ephemeral storage system of Heroku, I opted for media file hosting with AWS (which led to some of the aforementioned problems wtih the S3 Buckets). 
COLLECTSTATIC was used to gather local static files and bring them to the database. This was disabled during the deploy to Heroku by setting the DISABLE_COLLECTSTATIC to 1. 

I included an if-else statement in settings which used the PostgreSQL database, but reverted to dbsqlite if the latter was unavailable. I initialized the PostgreSQL database and pushed the migrations and used dj_database_url module thus enablign me to refer to the url directly in my settings.py (via the variable in my env file).

To deploy the code locally, undertake the following steps: 

## On Github

Manually download the code base and then upload to your preferred IDE. Install requirements.txt using the "pip3 install -r requirements.txt" command. Changed the following settings:
- ADD ALLOWED HOST
- Amend the config variables as necessary.

Run the application using the "python3 manage.py runserver $IP:$PORT" command. 
Please note step 4 may be different depending on the operating system you are running, please refer to the documentation for more details on running the Django server on different OS's

## Via the Terminal

Clone the repo from GitHub and innstall the requirements.txt "using pip3 install -r requirements.txt". Update the settings, as above. Run the application using the "python3 manage.py runserver $IP:$PORT" command. 

## Acknowledgments
[Fontawesome](https://www.fontawesome.com)<br> 
[Favicon](https://gauger.io/fonticon/)<br> 
[Fonts](https://fonts.google.com/)

## Credits
I would like to thank Michael, Xavier and Haley for their assistance in handling a number of techincal issues that arose during development. 

I relied on Corey Schafer's tutorial regarding Django Signals and profile images, availabl here:  https://www.youtube.com/watch?v=FdVuKt_iuSI
