# POSTER PANDA
___
___

#### ![responsive image]()

At Poster Panda, we are passionate about interior decoration and design. We offer wide range of stylish high quality posters along with frames and have something to suit every wall. Express yourself by creating a personalized wall of posters! Inspire others and have fun!

### :panda_face: [Live demo]()


## Table of Contents
___



## UX
___
### Strategy 
* #### Project Goals
    * To create a fully-optimized responsive site for flawless user experience on all devices.
    * To create a platform that allows all users to purchase stylish and affordable posters and frames.
    * Convert website visitors into registered users to utilize the website to it's full potential. 


* #### Business Goals
    * Achieve sales growth by offering competitively priced, good value products and increase profit.
    * Drive traffic to the site by promoting it on various social media sites and collaborating with influencers.
    * Offer new and exclusive collections every month by collaborating with original photographers and artists.


* #### Target Audience
    * Mainly female audience (around 75% according to the market research data) aged 14-65 who have interest in:
        * Lifestyle, beauty and fashion 
        * Travel and tourism 
        * Art and Design
        * Home and Garden
    * Users looking to buy a trendy gift.


### User Stories

* #### As a **First-time / casual visitor** I want to be able to:
    * Navigate the site intuitively and easily access all available website features from different screen size devices.
    * See list of all the products offered on the site and use sorting and filters to narrow down the search for posters that I am interested in purchasing.
    * See the new collections and other featured favourites to be inspired and informed on latest trends.
    * Search products by name or description to quickly find the product that I need.
    * View individual product details on a separate page including price, image, description, product rating, reviews and available sizes.
    * Add the products that I like to the cart, select the quantity and view the total amount for the items in the cart to be able to see the costs before I decide to checkout. 
    * Easily sign-up for an account and create a profile for faster checkout in the future and keeping track of order details and history.

* #### As a **Registered / returning visitor** I want to be able to:
    * Easily login to view my profile and access my personal information and logout from my account to ensure personal data protection and security.
    * View all items in the cart as well as delivery charges and order total to be aware of the costs before I go through the checkout process.
    * Adjust the quantity of the products in the cart so I can make changes easily.
    * Remove items in the cart so I can purchase only the ones that I really want.
    * Add and save my personal information when checking out for the first time, so it can safely be stored in my account to ensure faster and hussle free checkout next time. 
    * Securely add my card details when checking out.
    * See an instant confirmation of the order on the site and receive an email confirming that the order has been placed successfully for proof of purchase and peace of mind.  
    * Easily view my current order details and previous orders history, all saved in one place - my account.
    * Leave reviews for the products to interract and provide feedback to the store, encourage them make product improvements if neccessary and offer valuable guidance to other shoppers and make it easier for them to decide. 
    * Edit and delete my reviews if I change my mind or if they are no longer relevant. 
    * Save items in my wishlist, to create a personilised collection of posters that I like and might consider purchasing in the future.  
    * Remove items that I am no longer interested in from my wishlist.

* #### As a **Store owner / Superuser** I want to be able to:
    * Add products to enable me to add new items to the store.
    * Edit and update products to enable me to update prices, descriptions, images and apply any discounts, if applicable.
    * Delete products, if they are no longer available, to keep the stocks up to date.


### Scope 
* To create user friendly and simple to use e-commerce website using HTML, CSS, JavaScript, Python and Django framework that includes following features:
    * Intuitive design: allow users to navigate the site intuitively, view products.
    * Authorisation: allow users to Register, Login and Logout.
    * Wishlist: allow users to add products to the wishlist and remove from it.
    * Reviews: allow users to leave product reviews on the website.
    * Simple checkout: allow users to checkut in a few simple steps. 
    * Secure payment: allow users to securely enter their payment details to complete the purchase. 
    * Superuser: allow admin user to add, edit delete products to keet the store up to date. 

### Structure
The database structure was created as a visual representation for logical understanding of the data. Detailed information can be found in the [Information Architecture]() section. 

- [x] **![Database Structure]()**


### Skeleton 
- [x] **[Desktop/Tablet and Mobile Wireframes](readme_docs/ms-4-all-wireframes)**

Wireframes were created using Balsamiq Wireframes at the planning stage of the project. 

Some changes were made to the original wireframes during development process, particularly, I decided that only the Home page will feature a footer and all the rest of the pages fit in one page for better user experience. Also, About, FAQs and Contact Us pages were not included in the project because of the time constraints.

### Surface

- [x] **Color Scheme**
* [Coolors](https://coolors.co/) was used to creat the color palette for this project.
* Deeper shade of turquoise was chosen as a background color for the banner to support the Summer Collection images on the Home page and for some of the buttons. It is planned to change this banner's and the buttons' color every time when a new collection is out, so it fully complements the scheme of the collection. 
* Light grey and black were used for the rest of the elements to keep it simple and less cluttered as products' images can be quite colourful. 

- [x] **Typography**
* Google Fonts *Noto Sans* used accross the site for a harmonious look and feel.

- [x] **Imagery**
* All supporting images for the website as well as products' images were carefully selected from [Unsplash](https://unsplash.com/) and [Pexels](https://www.pexels.com/). 


## Technologies Used
___
### Languages
* HTML5
* CSS3
* JavaScript
* Python

### Frameworks, Libraries and Tools
- [x] **Front-end**
* **[Bootstrap v4.6](https://getbootstrap.com/)** - a front-end open source toolkit, used to create a sleek, consistent, functional and responsive website.
The main components used: navbar, cards, footer, buttons, toasts etc.  
* **[jQuery](https://jquery.com/)** - required to ensure proper rendering of the Bootstrap components listed above.
* **[Google Fonts](https://fonts.google.com/)** for typography. 
* **[Font Awesome v5.15](https://fontawesome.com/)** for icons throughout the pages, on the navbar and social icons.
* **[Tinypng.com](https://tinypng.com/)** - to reduce size and compress the images used in this project.
* **[MiniWebTool](https://miniwebtool.com/django-secret-key-generator/)** - to generate Django Secret Key.
* **[Balsamiq](https://balsamiq.com/wireframes/desktop/)** - to generate project wireframes for better planning of the layout of the website.
* **[Markdown-toc](http://ecotrust-canada.github.io/markdown-toc)** - to generate the Table of contents.


- [x] **Back-end**
* **[Django](https://www.djangoproject.com/)** - free and open-source Python Framework for rapid development and clean design.
* **[Stripe](https://stripe.com/gb)** - for fast and easy to implement way of accepting online payments from customers.
* **[Pillow](https://pypi.org/project/Pillow/2.2.1/)** - Python Imaging Library (PIL), that supports opening, manipulating and saving images.
* **[Django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/)** - to render Django forms in a very elegant and DRY way.
* **[Gunicorn](https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/gunicorn/)** - an HTTP server for use with Django on Heroku.
* **[SQLite](https://www.sqlite.org/index.html)** - for economical, efficient, reliable and independent local data storage for the application.
* **[Pip3](https://packaging.python.org/key_projects/#pip)** - the most popular package installer for Python.
* **[PostgreSQL](https://www.postgresql.org/)** - powerful, reliable, open source object-relational database system.
* **[AWS S3](https://aws.amazon.com/s3/?c=s&sec=srv)** - an object storage service, used to store and protect project's images and static files.


- [x] **IDE and Deployment**
* **[Git](https://git-scm.com/)** - used to keep track of the changes made to the repository and for version control.
* **[Gitpod](https://www.gitpod.io/)** - I used CI full template as an IDE to develop, commit and push files to GitHub. 
* **[GitHub](https://github.com/)** - used as a hosting service and for future collaborations.
* **[Heroku](https://id.heroku.com/login)** - my GitHub repo for this project had been connected to Heroku app to enable management and deployment of this app.


## Features
___
### Implemented Features

**Features available accross all pages**
* **Navigation Bar**
* The website Header features navigation menu, website logo, search bar, My Bag, My Account and My Favourites links.    
* Responsive main navigation bar was created using Bootstrap Navbar and is designed to collapse into a hamburger menu on medium and smaller screen sizes. 
* Bag and Account icons remain always visible to the user, and on large screens users also able to see bag total, to keep informed on how much they are spending. 
* Brand Logo is centered and visible on all screen sizes and serves as a link to the Home Page, which is particularly convenient when accessing the site on smaller screen size devices. 
* My Account is a dropdown menu that displays links to the Register and Log In pages for all unauthorised / guest users; My Profile, My Wishlist and Logout for authorised users and an additional Product Management link for an admin user.

* **Toast Messages**
* Django pop up toast messages displayed to keep the users informed.

**Page specific features**
- [x] **Home Page**
* Contains a main jumbotron that features colorful and bright image to draw attention and call to action to shop the latest collection. Two additional jumbotrons also styled in similar fashion and invite users to shop. 
* *Handpicked Favourites* section is added for extra interactivity and is a Bootstrap carousel that cycles through cards containing product images and details. 
* Responsive *Footer* is visible on Home Page and contains website motto, delivery information and social media icons. Icons are hoverable to let users know they are clickable and linked to the external websites and open in new tabs when clicked.
* *Copyright* section is directly below the Footer and contains Copyright information.

- [x] **Bag Page**
* This feature allows users to add products to the bag and view the bag, as well as adjusting the quantity of the items or removing it altogether from the bag. A toast message containing a snippet of product and costs information pops up to confirm when product is added to the bag.  

- [x] **Checkout Page**
* Contains a crispy form for user details and delivery address.
* Order summary is displayed to keep users informed and contains products details, subtotal, delivery charges and total for the bag. 
* Links provided to create an account for all new users or to log in for existing users to.
* Logged in users can save their details for faster checkout next time. 
* Users can securely fill their credit card details into the form.
* Checkout success page displays order details as well as sending it to the email provided. Users get notified via a toast message. 

- [x] **Products Page**
* Products are displayed in a responsive grid layout and provide the best shopping experience no matter what device user is using to shop. 
* Products display can be sorted alphabetically, by price and by category for the user's convenience. 
* It features back to top button to allow users to get to the top of the page if there are a lot of products on the page.
* When users click on a product that they are interested in it opens in a new Product detail page. This page contains a product image and details and allows users to select product size and quantity before adding the product to the bag. 
* Product reviews and ratings for the selected product are displayed on the bottom of the page to give users chance to learn other customers feedback.
* Logged in users are encouraged to leave their own reviews.

- [x] **Profile Page**
* This page is only available for registered users.
* It allows users to save default delivery info for an easier checkout and update it if need be. 
* Order History section contains all previous orders details. Users can click on individual order number to view full details.

- [x] **Django allauth features**
* *Register* - allows new users to create an account to access website's full features by filling out the registration form. A verifification email is sent to the email provided for confirmation. 
* *Log In* - registered users can log in using their username and password. 
* *Password reset* - a link to reset password is provided if users forgot their password.
* *Logout* - a Sign Out button allows users to log out of the website for added security. 


### Future Features
-  Add additional payment options, such as PayPal and Apple Pay to widen customer base and increase sales, so site users who don't want to use credit card can still make purchases.
-  Integrate Google Sign-In into the website to reduce the burden of login for customers and increase safety and security. 
-  Offer weekly newsletters to all subscribed customers to advertise new products, communicate any events and to offer marketing discount codes. 

## Information Architecture 

## Testing
___
Testing documentation can be found [HERE](TESTING.md)


## Deployment
---

### Local Deployment

- [x] **Requirements**
* *Python3* to write the code and run the application
* *PIP* to install packages
* *Git* for version control
* *GitPod* was used for this project 
* *Stripe* as a secure payment processing platform.
* *AWS* cloud storage and S3 to store and retrieve media and static files.

- [x] **Project Creation**
* This project was created using the CI recommended Gitpod Full Template.
* Click on Use this template button and enter a short and memorable name of your choice for your repo and select Create repository from template.
* Once created, click on green Gitpod button to open your new workspace.

- [x] **Deployment to Heroku**
* 


## Credits
___
### Code
* 

### Content
* The website was inspired by CI Project- Boutique Ado
* The website design was inspired by [Desenio](https://desenio.co.uk/)
* All images are taken from [Unsplash](https://unsplash.com/) and [Pexels](https://www.pexels.com/)
* Favicon icon is from [ICONS8](https://icons8.com/)

## Acknowledgements

* I would like to thank my mentor Excellence Ilesanmi for his continuous support and guidance.
* Big thanks to all tutors from Tutor Support.
* Thanks to the wonderful Slack community for their time and sharing their knowledge!
* A big thank you to my family and friends for their enormous support!

[:top:](#poster-panda)