# Aljild-Walshier
## Background
Aljild-Walshier in arabic means skin & hair, and was formed from taking traditional hair & skin treatment recipes passed down through generations and offer natural product treaments to all that are rooted in history. They would like to have a professional looking website that exhibits their modern approach whilst focusing on their hand blended formulas.

As the company is only starting a digital offering they require a website with a level of automation that would suit their needs. They would need and automated way for customers to make order and be able to keep track of activity on their accounts.

The aim is to build a website where users may be able to make and amend orders but where unregistered users also have an option to purchase. It would also require a facility for the site administrator to be able to quickly and easily amend and update product and departmental listings.

## User Experience
### User & Site Owner Goals
* Please see the project and issue planning tracker using Github's project planning function and can be found [HERE](https://github.com/moshabbir-dotcom/Project-Portfolio-5/projects/1) or a screenshot of completion [HERE](media/User_Stories_Complete.png)

## Wireframe
* The basic wireframe design was put together with the client with a few preference as to how the site was visualised and on discussion it was possible to identify a few points to work towards with an element of flexibility around visuals to be reviewed at the end of every sprint. 

### Desktop
[Desktop]()

### Mobile
[Mobile]()



The points pulled from the wireframes were:
* Minimalist design with attention towards the interactive parts of the pages.
* Homepage to have a "hero" image with text & button overlay.
* The menu and logo would fit convention standards with a "burger" menu for smaller screen sizes.
* Quick link options for search as part of a dropdown menu.

* With these defined it was a matter of using bootstrap to customise the visuals of the site although using a bootstrap template would also have been an option. These were looked at with the client in order to understand what "look" the site owners were after. Pages from allauth were then customised to fit the requirements of the client with regards to visual aesthetic of the trest of the site both in HTML design and CSS styling.

* The design that fit the clients'preferences were:

**NAME** [Bootstrap1]()

**NAME** [Bootstrap2]()

## Design
* The colour scheme was chosen by the site owner from a colour pallette hosted on a website called Coloors available on [Coloors](https://coolors.co/). The website has mutiple complimenting colour palettes which can be selected as a base selection of colours or mixed and matched as required. On submission this will continue to be a working project and will be cloned into a new respository for continuing work.

### Fonts
* The fonts as per the template are "Akshar" & "sans-serif" as the backup font. Fonts would remain relatively consistent in the event the site is viewed on different devices with the font sans-serif being available on all devices.
### Colours
* The font was chosen by the site owner due to its clean contrast between colour combinations which were simple & warm conveying the relaxing enviroment of the clinic itself. It will allow for the official trademarked branding to be added at a later date as well as copyrighted photographs whilst remaining aesthitically pleasing. This was tested as part of the template selection process however for this project stock images have been used to not infringe on copyright.<!-- finsih-->

The contrast checking on the website showed 7 failed colour contrast pairs although this was an automated check and the checking site states <em>"Automatic programs such as this cannot analyze text embedded in images and may misdiagnose or ignore certain critical issues. We recommend that you combine contrast testing results from this website with a manual test performed by a trained accessibility expert."</em> With this in mind it is important to note that all issues raised were related to text within images so a recommendation would be to perform an accessibility analysis by a trained professional to ensure and prove digital compliance before the JA Therapies site is hosted in the public domain. [Bureau of Internet Accessibility](https://www.boia.org/)
<!-- finsih-->
However slightly adjusting the colour contrast by amending the css stylesheet allowed the test to pass:
* Before: [FAIL](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/1c98200a9541fa5c0546035cc394269ee2562be2/media/images/ContrastFail.png)<!-- finsih-->

* After: [PASS](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/1c98200a9541fa5c0546035cc394269ee2562be2/media/images/ContrastPass.png)<!-- finsih-->

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

## Features
### Navigation
* The navigation bar was designed as a collapsible menu from heading on larger screen sizes above mobile to allow for ease of navigation with cluttering the simplicity of the aesthetics.
* As per the clients request the menu was a "burger" menu on smaller devices and a concious decision was made by the client to not utilise a collapsible menu on the site to not have the site seem overly "busy".<!-- finsih-->

## Rendering on different screen sizes
### Home
* [HomeMobile]()<!-- finsih-->

### About
* [TestemonialMobile]()<!-- finsih-->

### Treatments & Prices
* [TherapiesMobile]()<!-- finsih-->

### Contact
* <!-- finsih-->

### Booking
* <!-- finsih-->

## Code validation & Testing
### Testing
* <!-- finsih-->

### HTML <!-- finsih-->
* All HTML pages were tested via URL input and passed validation before submission. Links to validation evidence is below.
* [Home](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/5e60e111a5041675f93b33352599d8254d0fefc0/media/images/HomePASShtml.png)
* [About]
* [Prices]
* [Booking]
* [Contact]
* [Login]
* [Logout]
* [Signup]
### CSS <!-- finsih-->
* The bulk of the CSS was from the bootstrap template provided by the CI walkthrough however this was customised in order to fulfill marking criteria and adhere to the colour scheme selected and passed validation which is evidenced [HERE].
### JavaScript<!-- finsih-->
* 
### Python <!-- finsih-->
* All Python code was tested through a PEP8 validator and passed even though the pylint module in some occasions reported errors. The evidence of validation is below:
* [Admin.py](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/39853abb1ee53aea7edad976d9eb1e1274e60a7f/media/images/Admin.png)
* [Forms.py](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/39853abb1ee53aea7edad976d9eb1e1274e60a7f/media/images/Forms.png)
* [Models.py](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/39853abb1ee53aea7edad976d9eb1e1274e60a7f/media/images/Models.png)
* [Settings.py](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/39853abb1ee53aea7edad976d9eb1e1274e60a7f/media/images/Settings.png)
* [Tests.py](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/39853abb1ee53aea7edad976d9eb1e1274e60a7f/media/images/Tests.png)
* [Urls.py](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/39853abb1ee53aea7edad976d9eb1e1274e60a7f/media/images/Urls.png)
* [Views.py](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/39853abb1ee53aea7edad976d9eb1e1274e60a7f/media/images/Views.png)

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

### Credits
* <!-- finsih-->