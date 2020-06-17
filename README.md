# Django Frameworks

[![Build Status]()](https://travis-ci.org/)

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

### The application
An application that allows users to browse products to enhance or begin a hobby. 
Create and account to purchase hobby products as well as create reviews.
Allows users to purchase products using Stripe.

[Deployed on Heroku](.herokuapp.com)

## UX
A responsive app ?? 

### Users
At this stage the intended users are anyone that would like to browse or purchase products for a hobby.
This app allows a business for all types of hobby products to advertised and sell their stock. 
The app could be used to gather customer sentiment and feedback through the reviews.  

### User Stories.
- As a business owner I want an online platform to increase sales and allow customers and potential customers to 
have ease of access to the products for sale as well as all the information about the products. 
- As a business owner I want my customers to share their experience of a product to aid business decisions regarding stock levels.
This in time will create a business with a strong reputation for quality. 

### Wireframe
Wireframe can be found [here](/WIREFRAME.md "Wireframe")

### Design
For the color palate I used this 

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


`sudo pip3 install django=1.11` The framework used. - CHECK VERSION

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
- Logo made using [Paint.NET.](https://www.getpaint.net/) 

## Acknowledgements
- Code Institute for the lessons and basis for the app.
- Code Institute tutors from helping me out of difficult spots.
- Stack Overflow and W3Schools for finding answers to issues I was having, or to brush up on the basics.