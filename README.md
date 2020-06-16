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
- With the admin feature, the admin can log in and add/remove courses from the database. 
- They can also remove reviews.
- They can check any orders that have been made. Within the order they can see the address of the customer, when they ordered and what they ordered. If necessary, they can add or remove items from the order 

#### Course Display
- Customers can browse training courses.

#### Login/Register
- Cusotmers need to log in before purchasing services or leaving reviews.

#### Pagination
- Customers when browsing will be displayed 6 services max at a time.

#### Search
- Customers can search the database for courses.

#### Sort
- Customers can sort the courses by name or cost, by ascending or descending.

#### Leave Review
- Customers can leave reviews for services. They can be rated out of 5. The results of all the reviews are used to show the average. This can be useful for customers when picking a service.

#### Payments
- Customers can pay for orders using and API called Stripe (However at the moment it is in testing mode)
- To "pay" use 4242 4242 4242 4242 as the card number.

#### Account Reset
- If users would like to reset their password they can go to their profile and select the option to do so. They will then recieve a link to change their password by email.

### Future Features

#### Sort by review
- In future customers will have the option to sort services by review, either in ascendeing or descending order.

#### Upload profile image
- An option to upload a profile picture to users accounts.

#### Payment information
- The ability to retain card information for future payments.

#### Confirmation emails
- Once a user places an order they will recieve a confirmation email with their order summary.

#### Deactivate account
- Ability for users to deactivate account.

#### Expanded website
- An expanded website to include utensils that would be needed for a pizza shop.
- An area of the website to place an order of ingredients.

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
 - [AWS cloud9](https://aws.amazon.com/cloud9/)
 -- An online IDE.
 - [GitHub](https://github.com/)
 -- Provides hosting for software development version control using Git.
 - [Responsive Design](http://ami.responsivedesign.is/)
 -- Used to screenshot web application on different devices.
 - [Google Fonts](https://fonts.google.com/)
 -- Used for 'Nunito' font.
 - [Heroku](https://www.heroku.com)
 -- Used to deploy, and host app.
 - [Bootstrap](https://getbootstrap.com/)
 -- Used for premade CSS styling
 - [Font Awesome](https://fontawesome.com/)
 -- Used for premade icons.
 - [Travis](https://travis-ci.org/)
 -- A hosted continuous integration service used to build and test software projects hosted at GitHub
 - [Stripe](https://stripe.com)
 -- An API that allows individuals and businesses to make and receive payments over the Internet.
 - [AWS](https://aws.amazon.com)
 -- Used for hosting images and static data. 
 - [Postgres](https://www.postgresql.org/)
 -- A free and open-source relational database management system emphasizing extensibility and technical standards compliance.

## Testing

### Responsiveness
[Chrome](https://www.google.co.uk/chrome/?brand=CHBD&gclid=CjwKCAjwg-DpBRBbEiwAEV1_-HRKc5kuXoGrUIbi1QWzng3ZEvw3Obv1qmhUoXJa2iqrfZ4IxfgntRoC_hYQAvD_BwE&gclsrc=aw.ds)
Was used to test:
- Galaxy S5
- Pixel 2
- Pixel 2XL
- iPhone 5/SE
- iPhone 6/7/8
- iPhone 6/7/8 Plus
- iPhone X
- iPad
- iPad Pro
- Desktop
Page is fully responsive.

### Code Testing
[HTML Validator](https://www.freeformatter.com/html-validator.html) -- No issues

[CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) -- No issues

### User Testing
Tested a small group of people (3-4)

### Known Bugs
- Pagination does not yet work correctly when using the search function. 
- After submitting a review you are redirected to the courses page rather than the course review page.

## Deployment
- The code was developed locally using the AWS Cloud9 IDE.
- Code was then pushed to GitHub.
- Static files and user uploads where then configured to be hosted by AWS S3 buckets.
- Travis was then used for continuous integration.
- Code was then deployed on heroku.

Deployed app can be viewed [here.](https://pizza-the-pie.herokuapp.com)

GitHub Repo [here](https://github.com/kennedydmb/pizza-the-pie/)

### For local deployment
- Clone the project:
` git clone https://github.com/kennedydmb/pizza-database-project`
- Arrange contents so that the cloned document is in the root of the environment.
- Following need to be installed

`sudo pip3 install django=1.11` The framework used.

`sudo pip3 install Pillow` A python package that allows images to be uploaded. 

`sudo pip3 install django-forms-bootstrap` To render our forms with bootstrap styling.

- Create AWS account. Configure an S3 bucket for public access as a place to store user uploads and static files.

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
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY

- Link up GitHub
- Run deploy.

### Content
- Data created using current pizza shop knowledge. 
- Course images sourced from [Unsplash.](https://unsplash.com/)
- Logo made using [Paint.NET.](https://www.getpaint.net/) 

## Acknowledgements
- Code Institute for the lessons and basis for the app.
- Code Institute tutors from helping me out of difficult spots.
- Code Institues student Slack, extremely helpful for picking up ideas and debugging issues.
- Stack Overflow and W3Schools for finding answers to issues I was having, or to brush up on the basics.