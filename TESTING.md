# Testing 
---
---
#### Table of contents 


## Code Validity
---
- HTML Markup Validation - [](https://validator.w3.org/nu/)
- CSS Validation - [](https://jigsaw.w3.org/css-validator/)
- JavaScript Code Quality Tool JSHint - [](https://jshint.com/)
- PEP8 - [](http://pep8online.com/)


**[back to top](#testing)**

## Testing User Stories
---

- [x] **First-Time / Casual Visitor** 

| User Story | Testing | 
|:-----------|:--------|
| Navigate the site intuitively and easily access all available website features from different screen size devices.  | The website is fully responsive and designed to provide an optimal user experience, no matter what device users are accessing it from.|
| See list of all the products offered on the site and use sorting and filters to narrow down the search for posters that I am interested in purchasing.| Users can easily navigate from the navigation menu to the Products page to view all products. They can filter products by categories, from the main menu or sort them using *Sort by..* feature placed on top of the page.|
| See the new collections and other featured favourites to be inspired and informed on latest trends.| New and other featured collections are displayed on the Home page jumbotrons with bright colourful background images to draw users attention and also feature call to action buttons to prompt users to view the featured products.|
| Search products by name or description to quickly find the product that I need.| The search box is clearly labelled and easily accessible from the Home Page.| 
| View individual product details on a separate page including price, image, description, product rating, reviews and available sizes.| Users can click on the product to view the product details on a new page.|
| View ratings and reviews for the product to help me decide, add the products that I like to the bag, select the quantity and view the total amount for the items in the bag to be able to see the costs before I decide to checkout.| *Product detail* page also allows users to select the product size, add it to the bag, view ratings and reviews (if any). They get confirmation of their actions as well as the bag items preview and a subtotal on a toast message.|
| Easily sign-up for an account and create a profile for faster checkout in the future and keeping track of order details and history.| The *Register* button is easily accessible for the users who wish to sign up to enable faster checkouts in the future as well as accessing their order history.|



- [x] **Registered / Returning Visitor**

| User Story | Testing | 
|:-----------|:--------|
| Get a confirmation email upon successful registration to be certain that my account has been created.| When users submit the registration form successfully, they receive an email to confirm it.|
| Easily reset the password if I forget it so I can recover access to my account.| There is a *Forgot password* link in the Log In page which users can click on to request a password reset. They will recieve an email with a link to reset the password.|
|Easily login to view my profile and access my personal information and logout from my account to ensure personal data protection and security.| Users can view their profile by clicking on *My Account* link, which is easily accessible from the main navbar on larger screens hamburger menu on mobile screens.|
| View all items in the bag as well as delivery charges and order total to be aware of the costs before I go through the checkout process.| Bag items snippets, subtotal as well as delivery charges can be viewed on the *Shopping Bag* page. |
| Adjust quantity of the products in the bag so I can make changes easily before purchasing.| Users can easily adjust quantity of the products in the bag.|
| Remove items in the bag so I can purchase only the ones that I really want. | There is a *remove* button / link under each product in the bag, so users can easily remove unwanted item/s from the bag before proceeding to the payment. |
| Save my personal information when checking out for the first time, so it can safely be stored in my account to ensure faster and hussle free checkout next time.| Users have an option to select if they wish their details to be saved for faster checkout in the future.|
| Securely enter my card details when checking out. | Users are prompted to enter their card details on the *Checkout* page before completing the purchase. |
| See an instant confirmation of the order on the site and receive an email confirming that the order has been placed successfully for proof of purchase and peace of mind. | Order confirmation is displayed when checkout is completed successfully and a copy is sent to the email provided by the user.|
| Easily view my current order details and previous orders history, all saved in one place - my account.| On the *My Profile* page logged in users can view their Order History details.|
| Leave reviews for the products to interract and provide feedback to the store, encourage them make product improvements if neccessary and offer valuable guidance to other shoppers and make it easier for them to decide.| Users can click on the *Add Review* button on the Product Detail page to leave their rating and review the product. |
|Edit and delete my reviews if I change my mind or if they are no longer relevant. | Logged in users are provided with *Edit* and *Delete* links under their reviews.|
| Save items in my wishlist, to create a personilised collection of posters that I like and might consider purchasing in the future.| Logged In user can use *Add to Wishlist* feature to add their favourite items to the wishlist and view all products in *My Wishlist* page. |
| Remove items that I am no longer interested in from my wishlist. | Items no longer wanted in the wishlist can easily be removed .....................|


- [x] **Store owner / Superuser**

| User Story | Testing | 
|:-----------|:--------|
| Add products to enable me to add new items to the store. | Superuser can access *Product Management* page when logged in to allow them to add new products to the site.|
| Edit and update products to enable me to update prices, descriptions, images and apply any discounts, if applicable.| Logged in Superuser is provided with *Edit* button under each product to allow them to make changes to the product.|
| Delete products, if they are no longer available, to keep the stocks up to date.| Logged in Superuser is provided with a *Delete* button under each product, which they can use to remove a product/s from the store if need be. |



## Functionality Testing
---
**Navigation Bar**
* The responsive navbar stays visible accross all pages. On screen sizes =< 992px it collapses into a compact mobile navbar that contains the hamburger menu button, brand logo and *Search*, *My Wishlist* and *Bag* buttons. 
* When clicked, the hamburger menu dropdown displays featured page links, filtering by categories and sorting products by category, price and rating. All of the above have been tested by clicking and are working as desired.
* *My Account* link can also be accessed through the hamburger menu and displays *Log In* and *Register* links if the user is not logged in and *My Profile* and *Logout* links for authenticated users. All above mentioned links are working as intended and take users to the appropriate pages. 
* On large screen users are offered extended navbar for easier access to the links. It is working as expected.  
* All the links on the main navbar were tested by clicking and are working as intended, allowing users to jump to the linked pages.
* *Posters* link dropdown is activated when clicked and displays product categories. All category links are working as intended allowing products to be filtered correctly. 
* *All Products* link dropdown is activated when clicked and displays options for sorting the products. The sorting options were tested by clicking and are working correctly.
* The *Brand Logo* link is displayed on all screen sizes and was tested by clicking and is working correctly, as it takes users back to the Home page from anywhere on the site.
* *Search bar*:
    * On large screens users can enter the search word on the *Search box* displayed and on medium and smaller screens search bar dropdown is activated when the search button is clicked. 
    * It is accessible from all pages and correctly returns all products that contain the seached key word in their name or description on the *Products* page. 
    * If search returns no matching results, users are notified by a message on the *Products* page. 
    * If an empty search form is submitted, users get an error *toast* message to notify them.
* *My Wishlist* button takes unauthorised users to the *Log In* page when clicked. Logged in users are able to see a list of items that they previosly added to their wishlist. Users can also click on the heart icon and see how many products they currently have in their wishlist. All above features are working as desired.
* The *Bag* button is working as intended and takes users to their shopping bag page when clicked. 



**Toast Messages**
* Django pop up toast messages are displayed correctly and contain notification messages according to their type.


- [x] **Home Page**
* Home page is responsive and all the items displaying as intended on different screen sizes.
* Jumbotrons are displayed correctly and call to action buttons are working as they should, taking the users to the appropriate pages.
* *Handpicked Favourites* owl-carousel is working as desired by automatically looping through the shuffled products cards, displaying the correct amount of cards depending on the screen size and displaying a navigation on small screen sizes. If the card is clicked, it takes users to the *Product Detail* page.
* *Footer* is responsive and contains Social media icons.
* Change of colour and transition effects on hovering over Social icons are working as intended. Social icons were tested by clicking on them, all links to the external websites are functioning as intended and open in new tabs.
* Copyright section is center-aligned and located directly below the Footer as intended.


- [x] **Products Page**
* The *Product Page* correctly dispays all products cards in a responsive grid layout. The amount of cards in each row varies depending on screen sizes.
* The total products count is displayed on top of the page for users convenience.
* The *Sort by...* box is located on top of the page and allows users to sort results by Price, Rating, Name and Category in ascending and descending orders. It was tested by selecting each option from the dropdown menu and is working as intended.
* Each Product Card displays a product image, product name, price and category.
Additionally, *edit* and *delete* buttons are displayed for the admin user. 
* *Back to top* button is working as intended and takes users to the top of the page. 
* When users click on the product card, it navigates them to the Product Detail page for the selected product. 

- [x] **Product Detail Page**
* The *Product Detail* page is correctly displaying product image, name, category as well as the full description for the product.
* Users can select a value between 1 and 99 by *manually* entering it, by using *up* or *down* arrows or *+* and *-* buttons provided, in order for them to add the desired product quantity to the bag. Arrows and buttons are disabled functionally and style wise to stop users from increasing / decreasing values outside the valid numbers.
* If value of less than 1 or greater than 99 is selected, the form validation error message is displayed informing users. 
* If user manually enters a value of 0 or greater than 100 and click on the *Add to bag* button, an error form validation message is displayed and quantity not added.
* When a valid quantity is selected and *Add to Bag* button is clicked, the product is added to the bag. Users then see a confirmation toast message containing product image, price quantity and subtotal.
* The *Add to Wishlist* button allows users to add the selected product to their wishlist. It is working as intended.

* All website users can read reviews left by other customers. Reviews (if any) are displayed below the product description. 
* *Add a review* button is displayed only for logged in users and admin. 
* Authenticated users can click on the *Add a review* button and open up form containing *Review Headline*, *Your Comments* and a *rating* required fields. If the form is submitted successfully, users get a toast notification confirming it.
* Users can only review each product once. 
* Logged in users and admin can *edit* and *delete* their reviews. *Edit* form is similar to the *Add review* form and the *Delete Review* is displayed in a modal asking users to confirm before deleting the review or cancel. All of the above described review CRUD operations have been extensively tested and working as intended.

* *Keep shopping* button takes users back to the *Products* page. 

- [x] **Profile Page**
* Authenticated users are able to access *My Profile* page by clicking on *My Account* button on the main navbar on larger screens or clicking on the hamburger menu button and selecting it from the dropdown menu on medium and small screens. 
* The page renders the form where users defaul delivery information is saved (if they choose to) when they checkout for the first tima. This information can be updated by submitting an amended form and if successful, users see a confirmation toast message. 
* *Order History* section allows users to view their previous order details.   

- [x] **Bag Page**
* Items added to the bag can be viewed in the *Bag* page. 
* The number of items in the bag is correctly displayed next to the bag icon.  
* The page contains details of the products added to the bag and also allows users to adjust the product quantity or remove the item completely from the bag. 
* When quantity is amended and *update* button is clicked or *remove* button is clicked to remove the product from the bag, users get a toast notification to confirm their action has been successful. Subtotal, delivery charges and total are automatically re-calculated. This has been tested to verify that it's working as intended.
* After adding all the products they wouls like to purchase, users can click either on the *Go to secure checkout* button on the confirmation toast or on the *Secure Checkout* button to go to the *Checkout* page.
* If *Keep Shopping* button is clicked, users are navigated to the products page. 


- [x] **Checkout Page**
* This page contains the checkout form for user details, delivery information and payment details for users who are not logged in. 
* Logged in users can choose to save this information by ticking the appropriate box when checking out for the first time for faster future checkouts. The credit card information will not be stored for security purposes and has to be re-entered on each checkout.
* The *Order Summary* section contains summary of the products in the bag, delivery charges, if any and transaction total. 
* *Adjust Bag* button takes users back to the *Bag* page. 
* When all the requested information is provided, including credit card details, user can click on *Complete Order* button to complete the purchase. A confirmation email containing order details is sent to the user email.


- [x] **Django allauth features**
* *Registration*: 
    * Users can click on the *Register* button on the *My Account* dropdown menu.
    * The allauth registration form is rendered as expected. As all the fields are required in the form, leaving any of them unfilled prompts an allauth validation error.
    * Allauth validation errors could also be caused by entering unmatched emails, already registered email, unmatching passwords, short password (less than 8 characters), too easy password, existing username, etc.
    * When the valid form is submitted, users are required to verify their email address by clicking on the link in the email sent to the newly registered email address. 

* *Login*:
    * 

    





## Defensive Design Testing 
---







**[back to top](#testing)**

## Responsiveness
---



## Usability Testing
---

## Performance Testing
---



## Browser Compatibility Testing
---


### Known Bugs 
---


**[back to top](#testing)**