# Django Frameworks for Full Stack Web Development 

[![Build Status] NEED TO CHECK 

![Hobby Hunt Logo](https://github.com/murphya14/Hobby_Hunt-/blob/master/static/images/logo.png)


## Milestone 4: Hobby Hunt
### Aim of the project
Build a fullstack web application for an ecommerce business that requires authentication and utilised as an advertising and sales platform.

External users goals
- Find inspiration to pursue hobbys 
- Be able to browse the current stock as well as browse the stock by their choice of category.
- Have clear access to information about the stock.
- Have the ability to read other customer reviews as well as create a review. 
- Be able to make a secure payment.
- Be able to review their cart and remove any items that they no longer wish to purchase. 

Site owners goals
- Earn money selling products on the ecommerce platform. 
- Advertise effectively
- Gather feedback from customers which will inform business descisions such as stock control. 

Consumers want to be inspired and challenged. Hobby Hunt meets this need by being the one-stop-shop for 
all hobby needs. By stocking beginner-advance products, it is accessible to all ages and skill levels.

Welcome to [Hobby Hunt!](https://hobbyhunt.herokuapp.com/)

### The application -lOOKAT
An application that allows users to browse products to enhance or begin a hobby. 
Create and account to purchase hobby products as well as create reviews.
Allows users to purchase products using Stripe.

[Deployed on Heroku](.herokuapp.com)

## UX -NEED TO ADD IN THE WIREFRAMES 
The basis for the UX started with a mobile first approach and afterwards, the larger screens as shown in the 
[wireframes.](https://github.com//mockups_wireframes).
The design is simple in order to showcase the products and provide a straight-forward/familar layout to users. 

To determine the goals for the website, the following user stories were taken into account:

1. I want a site where I can buy a product specifically for a hobby.
2. I want to be able to specify the hobby through category in order to filter the products.
3. I want to understand how other consumers felt about the product.
4. I want to buy off of a transparent company and so, be able to leave a review on my purchases.
5. I want to be able to see more detail about the product (more than just the image and price.)
6. I want to be able to use a search engine to filter products.
7. I want to able to have pagination on pages.
8. I want to be able to view my cart and remove items if needed.
9. I want to be able to pay securely. 
10. I want to be able to register and log in to my personal account. 
11. I want to be able to navigate easily throughout the site by using back buttons and obvious links.
12. As a business owner I want an online platform to increase sales and allow customers and potential customers to 
have ease of access to the products for sale as well as all the information about the products. 
13. As a business owner I want my customers to share their experience of a product to aid business decisions regarding stock levels.
This in time will create a business with a strong reputation for quality. 
 

The navbar and the footer are both responsive. The navbar becomes a burger menu when reduced in size.
Based on the authentication of the user, the links can vary. If the user is not logged in "Registration" and "Login" are in the navbar.
If the user is logged in, then "My Profile", "Logout" and "Cart" appear in the navbar. 
The footer is centered at the bottom of the page and is a simple footer that has the social media icons and the copyright.

When the user first navigates to the site, they are directed to the login page. Here there is the option to register and create an account or log in with existing credentials.
The main logo is above the login page and a caption entended to encourage users to go further into the site. 
The forms are in the same format. All are very plain with the logo displaying prominently on the page. 

Once the user is logged in, they are directed to the Home page. Here the use of the site is outlined and there is a carousel of products to advertise the range of products.
There is a Mark Twain quote to portray the atmosphere of adventure and curiosity to the user. 
There is a call to action button "Start Exploring" that navigates the user to the pages of products available.
This page is consistent in it's simplicity in order to gently guide the user and convey the ease of use to the user.

The pages "Find a Hobby" and "Category" display cards that contain an image, average rating calculated from reviews and the price.
It is a very simple and clear way of displaying consistent information for all products. 

The reviews are laid out so the consumer can easily read the comments while also being encouraged to add to cart as the option is there.

The shopping cart gives a clear and transparent view of all items added. This then shows a total.
The number of items in the cart is visible from the navbar as the cart icon will display a number (if not zero.)

### Design
The colour scheme is a playful blue, white and yellow. These soft colours are in line with the fun and curiousity that a hobby ignites.
There is aspects of purples and pinks to call attention to particular buttons and pieces of information. These colours fit in with the playful nature of the sites. 

## Features

### Existing Features

#### Admin
- With the admin feature, the superuser can control the products displayed with all the information. 
- The super user can remove reviews which allows for filtering of appropriate reviews.
- The super user has the ability to remove users if required.
- The super user has the ability to see orders which includes all the postal information. If required, the superuser can delete the order.

#### Product Display
- Customers can browse the products. 
- As often customers will have a specific hobby in mind, the customer has the option to search by category. 
- The customer can gather more information regarding the product by selecting it and rendering the details page. 
This contains a link to the reviews, displays the average review rating and expands on information regarding the specific product.

#### Login/Register
- Customers need to register and log in before they have the ability to leave a review or purchase an item.
- Customers who need to reset their password, can do so on the login page or if they wish to changed it while they are logged in, can do so on their profile page.

#### Pagination
- Customers when browsing will be displayed 6 products max at a time.

#### Search
- Customers can search the database for products.

#### Leave Review
- Customers can leave reviews for products by rating them out of 5. 
The average is calculated from all of the reviews and the result is displayed on the browse card so customers can become easily informed. 

#### Cart
- As Customers add to the cart, their Total is calculated and displayed in the cart.
- There is a summary of all the items shown in the cart.
- The customer can remove items from the cart if required. 

#### Payments
- Customers can pay for orders using and API called Stripe

### Future Features

#### Sort by review
- Allow customers the option of sorting by review, either in ascendeing or descending order.

#### Customize profile 
- An option to upload a profile picture to users accounts.
- Be part of a group based on the hobby e.g list the hobbies you are interested in and this then filters the preference specified. 

#### Payment information
- The ability to retain card information for future payments and implement stronger security measures e.g. send a code through text to verify payment. 

#### Confirmation emails
- After the payment has been made, the customer receives a confirmation email which contains the cart summary.

#### Deactivate account
- Ability for users to deactivate account.

#### Track stock
- Ability for the business owner to track stock. 



## Technologies Used
The project makes use of:
 - [HTML](https://www.w3schools.com/html/)
 -- To build the structure of the content.
 - [CSS](https://www.w3schools.com/css/default.asp) 
 -- To style the content.
 - [Django](https://www.djangoproject.com/)
 -- The framework used to put this project together.
 - [Chrome](https://www.google.co.uk/chrome/?brand=CHBD&gclid=CjwKCAjwg-DpBRBbEiwAEV1_-HRKc5kuXoGrUIbi1QWzng3ZEvw3Obv1qmhUoXJa2iqrfZ4IxfgntRoC_hYQAvD_BwE&gclsrc=aw.ds)
 -- A cross-platform web browser developed by Google. Used as the main browser for dev tools, and to test responsiveness.
 - [Gitpod](https://gitpod.io/workspaces/)
 -- An online IDE.
 - [GitHub](https://github.com/)
 -- Provides hosting for software development version control using Git.
 - [Heroku](https://www.heroku.com)
 -- Used to deploy, and host app.
 - [Bootstrap](https://getbootstrap.com/)
 -- Used for premade CSS styling
 - [MDBootstrap](https://mdbootstrap.com/snippets/)
 -- Used for premade CSS styling
 - [Font Awesome](https://fontawesome.com/)
 -- Used for premade icons.
 - [Travis](https://travis-ci.org/)
 -- A hosted continuous integration service used to build and test software projects hosted at GitHub
 - [Stripe](https://stripe.com)
 -- An API that allows individuals and businesses to make and receive payments over the Internet.
 - [Postgres](https://www.postgresql.org/)
 -- A free and open-source relational database management system emphasizing extensibility and technical standards compliance.
 - Google Chrome Developer Tools

## Functionality 

### Apps

#### Accounts
This was created using Django built-in authentication for login and register for users. 
Additionally, I created a profile for the user.  

*Note to assessors, please use the following to log into the admin dashboard: assessor / assessor

**Note to assessors, To view as a user, Please use the following accounts:

mary / mary
john / john


#### Home 
The function of this app is the render a Home page. 

#### Hobby Product
This app contains the vast majority of the CRUD elements of the site. It interacts with other apps.
In hindsight, the naming of this app was too similar to the project and this caused issues. 

#### Cart
The cart shows the amount of items the user has before purchase and also gives the user the ability to remove items from the cart. 

#### Checkout
Checkout is handled using the secure payment process implemented using Stripe.

#### Reviews
The Review app allows the user to browse other users reviews and if they hold an account, the user can also leave a review.
The review app also allows an average rating to be calculated based on consumers feedback. 

#### Search
The search app holds the logic for the different categories. 

## Testing

### Responsiveness
Used developer tools to verify the website is fully responsive.

### Code Testing
[HTML Validator](https://www.freeformatter.com/html-validator.html) -- No issues

[CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) -- No issues

### User Testing
Tested a small group of people (3-4)

### Known Bugs
NEED TO DO 

## Deployment
- The code was developed locally using Gitpod.
- Code was then pushed to GitHub.
- Travis was then used for continuous integration.
- Code was then deployed on heroku.

Deployed app can be viewed [here.](INPUT)

GitHub Repo [here](INPUT)


`sudo pip3 install django=1.11.29` The framework used.

`sudo pip3 install Pillow` A python package that allows images to be uploaded. 

`sudo pip3 install django-forms-bootstrap` To render our forms with bootstrap styling.

`sudo pip3 install django-storages` To set up media and static transfer on S3

`python3 manage.py collectstatic` To send all media and static directories to S3

`sudo pip3 install psycopg2`
`sudo pip3 install dj-database-url==0.5.0` To handle postgres database.

- Create a new app on Heroku and link to your local repo.
- Create a requirements.txt and Procfile.

`sudo pip3 freeze --local > requirements.txt` To tell Heroku what packages are required to run this program.

`echo web: python app.py > Procfile` To tell Heroku what type of application this is.

- Push to github
- Create a new app on Heroku.
- Add postgres database as a resource.

Set up environment variables on Heroku for:
- STRIPE_PUBLISHABLE
- STRIPE_SECRET
- EMAIL_ADDRESS
- EMAIL_PASSWORD

- Link up GitHub
- Run deploy.

### Content
- Course images sourced from [Unsplash.](https://unsplash.com/)
- Logo made using [Canva.com.](https://www.canva.com/) 
- Tab icon was made using [Favicon.com.](https://favicon.io/) 

## Acknowledgements
- Code Institute for the lessons and basis for the app.
- Code Institute tutors from their guidance and expertise. 
- Stack Overflow and W3Schools for trouble-shooting. 

## Disclaimer 
This is for educational purpose only 