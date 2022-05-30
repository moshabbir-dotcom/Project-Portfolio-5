# Aljild-Walshier

## Table of contents
### [Background](#background)
### [User_Experience](#user-experience)
### [Wireframe_&_Database_schema](#wireframe--database-schema---finish)
### [Design](#design)
### [Technologies](#technologies)
### [Features](#features)
### [Code_validation_&_Testing](#code-validation--testing)
### [Deployment](#deployment--setting-up-postgres-db)
### [Acknowledgements](#acknowledgements-1)


## Background
Aljild-Walshier in arabic means skin & hair, and was formed from taking traditional hair & skin treatment recipes passed down through generations and offer natural product treaments to all that are rooted in history. They would like to have a professional looking website that exhibits their modern approach whilst focusing on their hand blended formulas.

As the company is only starting a digital offering they require a website with a level of automation that would suit their needs. They would need and automated way for customers to make order and be able to keep track of activity on their accounts.

The aim is to build a website where users may be able to make and amend orders but where unregistered users also have an option to purchase. It would also require a facility for the site administrator to be able to quickly and easily amend and update product and departmental listings.

[Back To Top](#aljild-walshier)
## User Experience
### User Stories
* As a user I can view a list of items so that some can be selected for purchase.
* As a user I can view individual item specifics so that details of the item can be obtained before purchase.
* As a user I can view running total of spending so that make an informed purchase within budget.
* As a user I can sort items so that view items by price and/or department.
* As a user I can sort departments so that items relevant only to that department are displayed.
* As a user I can search items so that find a specific item within the catalogue with ease.
* As a user I can view search results so that the results of my search are accurate.
* As a user I can search related departments so that similar items within departments can be displayed.
* As a user I can select quantity of items so that an incorrect amount are not purchased.
* As a user I can view basket so that I can be sure of what I am purchasing.
* As a user I can amend basket so that I can change my order before payment if I require.
* As a user I can make payment so that I am able to purchase easily.
* As a user I can view order confirmation so that verify my purchase has been successful.
* As a user I can receive email confirmation so that I can have a record of my purchase.
* As a user I can ensure payment security on checkout so that I am comfortable providing payment details.
* As a user I can register account so that I can have a personal account to view my activity.
* As a user I can signin/signout so that access my personal account.
* As a user I can have a personal profile so that I can view my order history, confirmations, save payment information, blogs and comments.
* As a user I can receive email confirmation on registering so that I am aware my registration was completed successfully.
* As a user I can reset password so that I can recover site access.
* As a user I can add blog so that I can publish an article for others to see.
* As a user I can edit blog so that make amendments to what I have published on the site.
* As a user I can view blogs so that I can see what others have published on the site.
* As a user I can delete blogs so that I can remove blogs I have already published.
* As a user I can comment on blogs so that I can publish a response to what others have published.

### Site Owner Goals
* As a site owner I can add items to product list so that I can grow the website listings.
* As a site owner I can update items so that I can amend items listed on the site.
* As a site owner I can delete items so that website item listing remains accurate.
* As a site owner I can obtain users emails addresses with opting in to aid in email marketing activity.

* The project was transferred from a manual kanban tracker to a digital format using Github's project planning function and can be found [HERE](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/User_Stories_Progess.png) or a screenshot of completion [HERE](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/User_Stories_Complete.png)

[Back To Top](#aljild-walshier)
## Wireframe & Database schema
* Database schema describing models and relation to one another is [HERE](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/database_schema/Database_Schema_PP5.pdf)

The points pulled from the wireframes were:
* Minimalist design with attention towards the interactive parts of the pages.
* Social media links to be on home page only to not clutter other pages.
* Homepage to have a "hero" image with text & button overlay.
* The menu and logo would fit convention standards with a "burger" menu for smaller screen sizes.
* Quick link options for search as part of a dropdown menu.
* Blog page will have 3x3 grid as opposed to 4x4 grid for products.
* Tablet display will have mobile style "condensed" nav with 2x2 grids for both blogs and product views.
* Input and report pages to be offset left with related content on the right such as a Blogpost on the left and comments to the right & delivery information to the left.
* The basic wireframe designs were put together with a few preference as to how the site was visualised and it was possible to identify a few points to work towards with consistancy to be put into the base.html file an element of flexibility around visuals on other pages and some images are able to be accessed below. (As this piece of work is not a team effort, wireframes were handrawn with points to cover although in a team enviroment designs would have to be more specific to prevent different interpretation of design.)

### Desktop 1024px wireframes
* [Desktop_Home_&_Products](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/wireframes/Home_ProductsWF1024.jpg)
* [Desktop_Blog_&_Info](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/wireframes/Blog_InfoWF1024.jpg)

### Tablet 768px wireframes
* [Tablet_Home_&_Products](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/wireframes/Home_ProductsWF768.jpg)
* [Tablet_Blog_&_Info](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/wireframes/Blog_InfoWF768.jpg)

### Mobile 375px wireframes
* 375px was selected as minimimum screen size to cater for mobiles as that is the average entry screen size for smartphones.
* [Mobile](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/wireframes/MobileWF_All.jpg)

[Back To Top](#aljild-walshier)
## Design
### Colours
* The colour scheme was chosen by the site owner from a colour pallette hosted on a website called Coloors available on [Coloors](https://coolors.co/). The website has mutiple complimenting colour palettes which can be selected as a base selection of colours or mixed and matched as required. On submission this will continue to be a working project and will be cloned into a new respository for continuing work. The selected colour scheme can be seen [HERE] (https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/coloors.png) where 4 of the 5 hero colours were utilised in addition to the bootstrap default colours for banners to maintain the minimalist look of the site.
* The contrast checking on the [a11y](https://color.a11y.com/Contrast/) website showed NO contrast issues although this was an automated check and the checking site states <em>"Automatic programs such as this cannot analyze text embedded in images and may misdiagnose or ignore certain critical issues. We recommend that you combine contrast testing results from this website with a manual test performed by a trained accessibility expert."</em> With this in mind it is important to note that in the event any issues were found and raised it would be a recommendation to have an accessibility analysis performed by a trained professional to ensure and prove digital compliance before the ecommerce site would hosted in the public domain. [Bureau of Internet Accessibility](https://www.boia.org/) Evidence of the contrats check is [HERE](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/Contrast_Check.png).
### Fonts
* The fonts as per the template are "Akshar" & "sans-serif" as the backup font. Fonts would remain relatively consistent in the event the site is viewed on different devices with the font sans-serif being available on all devices.

[Back To Top](#aljild-walshier)
## Technologies
### Languages
* [HTML](https://www.w3schools.com/html/)
* [CSS](https://www.w3schools.com/css/)
* [JavaScript](https://www.w3schools.com/js/)
* [Python](https://www.python.org/)

### Tools & Frameworks
* [GitHub](https://github.com/)
* [Gitpod](https://www.gitpod.io/)
* [Django](https://www.djangoproject.com/)
* [Heroku](https://www.heroku.com/home)
* [Postgres](https://www.postgresql.org/)
* [Google Fonts](https://fonts.google.com/)
* [W3C HTML Validation](https://validator.w3.org/)
* [H3C CSS Validation](https://jigsaw.w3.org/css-validator/validator.html.en)
* [http://pep8online.com/](http://pep8online.com/)
* [a11y](https://color.a11y.com/Contrast/)
* [TinyPNG](https://tinypng.com/)
* [AWS](https://aws.amazon.com/)
* [Stripe](https://stripe.com/gb)
* [ES6 Syntax Checker](https://www.piliapp.com/syntax-check/es6/)
* [W3C CSS Checker](https://jigsaw.w3.org/css-validator/)
* [W3C HTML Checker](https://validator.w3.org/)
* [WhiteNoise](http://whitenoise.evans.io/en/stable/)
* [Coloors](https://coolors.co/)

[Back To Top](#aljild-walshier)
## Features
### Navigation
* The navigation bar was designed as a collapsible menu from heading on larger screen sizes above mobile to allow for ease of navigation with cluttering the simplicity of the aesthetics.
* The menu was a combination of "burger" menu on smaller devices in additon to the heading icons to allow for ease of UX

### Rendering on different screen sizes
* Below are examples of varying screen sizes of the same pages for different devices.
#### Desktop 1024px
* [Desktop Home](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/Home1024px.png)
* [Desktop Blog](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/Blog1024.png)
* [Desktop Basket](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/Basket1024px.png)
* [Desktop Products](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/Products1024px.png)

#### Tablet 768px
* [Tablet Home](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/Home768px.png)
* [Tablet Blog](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/Blog768px.png)
* [Tablet Basket](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/Basket768px.png)
* [Tablet Products](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/Products768px.png)

#### Mobile 375px
* 375px was selected as minimimum screen size to cater for mobiles as that is the average entry screen size for smartphones.
* [Mobile Home](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/Home375px.png)
* [Mobile Blog](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/Blog375px.png)
* [Mobile Basket](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/Basket375px.png)
* [Mobile Products](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/Products375px.png)

[Back To Top](#aljild-walshier)
## Code validation & Testing
### Testing
* The website was tested for functionality on edge, firefox, chrome & safari browsers across Samsung S10+, S22 ultra, iPhone 11+, Macbook pro HP Pavilion & HP Spectre devices each running an operating system from macOS 12, windows 10 & 11, android and iOS 15.
* Automated testing was not used for this project although manual testing principles were followed in testing functionality aspects of the website and proof of such is evidenced through screengrabs of the UX interface notifactions shown below:
[TEST_ADD_COMMENT](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/Test_Add_Comment.png)
[TEST_ADD_POST](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/Test_Add_Post.png)
[TEST_ADD_PRODUCT](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/Test_Add_Product.png)
[TEST_AMEND+-_PRODUCT](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/Test_Amend%2B-_Product.png)
[TEST_AMENDBASKET_PRODUCT](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/Test_AmendBasket_Product.png)
[TEST_EDIT_PRODUCT](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/Test_Edit_Product.png)
[TEST_EDIT_POST](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/Test_Edit_Post.png)
[TEST_EDITED_POST](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/Test_Post_Edited.png)
[TEST_CLEAR_BASKET](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/Test_RemoveBasket_Product.png)
[TEST_SIGNIN](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/Test_SignIn.png)
[TEST_SORT_AZ](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/Test_Sort_AZ.png)
[TEST_SORT_DEPT_AZ](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/Test_Sort_Dept_AZ.png)
[TEST_SORT_PRICE](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/Test_Sort_Price.png)
[TEST_SORT_ZA](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/Test_Sort_ZA.png)
[TEST_UPDATE_PRODUCT](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/Test_Update_Product.png)
[TEST_UPDATE_USER](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/Test_Update_User.png)
[TEST_VIEW_ORDER_DETAIL](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/Test_View_Order_Detail.png)
[TEST_VIEW_ORDERS](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/Test_View_Orders.png)

### HTML
* All HTML pages were tested via URL input and passed validation before submission. Errors were displayed on the validation pages however these were due to the the jinja templating language used in python triggering error warnings in the HTML validator. The Gitpod terminal however had extensions installed to ensure the formatting was correct and this is evidenced [HERE]() with a creengrab of HTML pages open in the workspace with NO PROBLEMS highligted in the workspace. In addition to this there are also W3C screenshots of randomly selected HTML pages showing no issue.
* [HomeHTML](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/HomeHTML.png)
* [BlogHTML](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/BlogHTML.png)
* [ProductsHTML](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/ProductsHTML.png)

### CSS
* The bulk of the CSS was from the bootstrap template provided by the CI walkthrough however this was customised in order to fulfill marking criteria and adhere to the colour scheme selected and passed validation which is evidenced for each respective CSS style sheet below:
* [STYLE.CSS](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/Style_CSS.png)
* [CHECKOUT.CSS](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/Checkout_CSS.png)
* [BLOG.CSS](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/Blog_CSS.png)
* [PROFILE.CSS](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/Profile_CSS.png)
### JavaScript
* Javascript was taken from the CI walkthrough and modified in places and passed validation with evidence [HERE](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/JSValidation2.png) & [HERE](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/JSValidation3.png)
### Python
* All Python code was tested through an external PEP8 validator and passed even though the pylint module in some occasions reported errors. The evidence of PEP8 validation being adhered to on the files that showed these errors is below:
* [Product Views](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/ProductviewsPY.png)
* [Profile Views](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/ProfileviewsPY.png)
* [Home Views](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/HomeviewsPY.png)
* [Checkout Views](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/CheckoutviewsPY.png)
* [Blog Views](https://github.com/moshabbir-dotcom/Project-Portfolio-5/blob/main/docs/images/readme-images/BlogviewsPY.png)

### Bugs
* When attempting to add the "sort" functions in the products views it resulted in an error stating that the view could not return a sort by department. This was due to me filtering by using category name which I had registered in my product model causing confusion. To rectify this I changed the name of the field to "department" and adjusted the filtering code to also refer to department in order to maintain consistency in development.
* When adding the functionality for "add to basket"
* When completing the layout for the basket.html view I encountered and issue whereby I had an error being shown in debug view highligting the endblock stating thaty there was an endfor or endif block statement missing within the file. This was due not to being missing but they had been put into the wrong positions and when swapped the page loaded as required.
* When rendering the basket.html page an error was displayed stating that there was an error in the view_basket view resulting in an image file being unsubscriptable. This was rectified by adding an if/else statement withing the basket.html template to display an image if available or if not to default to the placeholder image.
* When creating the blogpost app I realised that I had not accounted for the relationship to the user models for which the profile app had not been created. Not quite a bug but more a learning for how to approach the app order in future.
* The exposed postgres URI was accidentally pushed to the repo, but that database was destroyed and a new one created.
* The above had to be done again as when creating a heroku app vis the CLI by default the wrong region was set so the app was then created on the Heroku dashboard and the connected vis the CLI for deployment subsequent pushes.
* After deploying to Heroku when running the port 8000 development there was an error stating "SECRET_KEY cannot be empty" so DEVELOPMENT was set back to true and the delployed secret key added back to settings until final deployment when new one was generated so any secret key in commit historys would be irrelevant and no longer valid.
* When setting the url for the newsletter subscription page there was an error generated where the url pattern defined was looking for a slug within the which was not relevant for this particular page, (as would have been the case for the CRUD functions within the blog app). This was fixed by setting the url pattern for blog/newsletter to BEFORE those requiring a slug and the page was then rendered without issue.

[Back To Top](#aljild-walshier)
## Deployment & setting up Postgres DB
* On the home screen click on create new app
* Enter project name & select region
* Under resources add database to the app resources by selecting Herku Postgres and adding it to env.py in the follwing steps
* Select settings and go to config vars and then reveal config vars
* Set the secret key and database url in heroku config vars and env.py and finalise the connection in settings to ensure sensitive data is not visible in the settings.py file
* Deploy to Heroku by selecting Github as the method and connecting via the prompt
* Click into the search box type project name and then connect
* Click deploy branch. (Before final deployment staticfiles were collected via CLI and debug set to "False" in settings.py file.)
* Once complete the view button will allow the app to be shown in a browser

The program is set to be deployed automatically manually after each push from gitpod since the heroku security breach. This ensures the website is running before a deployment with minor changes to it could potentially create an issue and this way allows for more control. It is done but logging in via the CLI and connecting to the relevant repo and pushing to github and heroku seperatley with <em>git push origin main</em> & <em>git push heroku main</em> respectively.

[Back To Top](#aljild-walshier)
## Acknowledgements
* Django tutorial videos from Codemy.com
* CI walkthrough videos.
* Bim Williams, Manny Silva & Adil Bashir for providing experiential learning from themselves as well as best practice.
* The CI walkthrough came with CSS and JS files which were adapted however bespoke code was also written and placed in relevant CSS files with additonal class names assigned to elements across the site.
* Business name and product names belong to S.Noor and used with permission.
* Lastly my new mentor Chris Quinn who measured me on the marking criteria and gave me specific next steps to keep to my personal timeframe.