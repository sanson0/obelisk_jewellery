![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome sanson0,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **September 1, 2021**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!

# Introduction
This project is for an e-commerce jewellery store called Obelisk Jewellery.
It utilizes Django full stack frameworks. Frameworks enable fast development of 
new projects.

This project is the milestone 4 project for Code Institute's Full Stack Development Diploma
# Reasons for site
The jewellery store Obelisk has been set up to enable shoppers to purchase a range of jewellery
## User stories

A full list of user stories is provided in the pdf

# Features
Features across pages and features for individual pages are listed. A link to the wireframe is provided. The wireframe shows mock-ups of the main pages of the app including views on devices of different screen widths.
## Features across all pages
### Header
The header contains the 
* title
* Navbar with My account, basket, my orders, home, product management (superusers only) and logout
* Free delivery banner
* Categories navbar with necklaces, bracelets, rings brooches, earrings, combos and sale
* Search bar
### Footer
The footer contains the
* Useful info Navbar with contact us, delivery options,, payment options, terms & conditions,
returns & refunds and manufacture
* Payment methods
* Social media links
* Copyright statement
## Features on home page
The home page contains an image of an attractive piece of jewellery
## Features on product display page
The product display page appears when a category/ subcategory is clicked or the search bar is used. Each product is displayed including image, title, description, rating and price.
The products are displayed side by side on desktop but one below the other on mobile view. There is a display of number of products found at the top of the page.
There is a dropdown menu also at the top of the page which allows shoppers to sort the products
by rating, by cost or alphabetically by title.
There is a button to take the shopper back to the top of the page
## Features on product selected page
The product selected page appears when a product is selected by clicking on it in the product display page.
The product is displayed in a larger view and the view coontains the image, title, description,
rating, price, size (rings only) and quantity selector.
There are buttons at the bottom of the product information, one for 'keep shopping' and one for
'Add to basket'
## Features on basket page
The basket page appears when 'Add to basket' is clicked on the 'product selected' page.
The product is displayed in a larger view and the view coontains the image, title, description,
quantity, price and size (rings only).
There are buttons for 'sign in', 'checkout' and 'delete item'.
Signing in/ creating an account is optional but it allows the shopper to track orders and save 
card details for next time. There is a statement at the top of the page to inform shoppers of this.
## Features on the login page

## Features on the create account page
## Features on checkout page
## Features on payment page
## Features on confirmation page
Thank you for your order
confirmation email
order number
order details
* title of product
* cost of product
* size of product if applicable
Delivering to :-
* Full name
* Address
* County
* Town or city
* Postcode
* Country
* Phone number
* Order total
* Delivery cost
* Grand total
## Features on orders page
## Features on contact page
## Features on delivery page
## Features on terms & conditions
## Features on returns & refunds
## Features on payment methods
## Features on manufacture page
## Features on product management page
## Features on add product page
## Features on edit product page
# Data design
## Product data
All items will have a: -
* Title
* Description
* Rating in terms of 1 to 5 stars
* Price
* Size if applicable (for rings only)

All items will be assigned an SKU (Stock Keeping Unit) identifier, unique for each distinct product that can be purchased.

The site will have the ability to search words in the title and description of each item
for key words such as metal type, gem name, colours, shapes.

The site will contain categories and subcategories. 
Main categories include necklaces, bracelets, rings, brooches, earrings, combinations (matching necklace, earrings and ring) and sale items 
The products for each category and 
subcategory are loaded based on a search for key words in their titles. 'Gem' or 'Glass' 
go in one subcategory, 'Silver', 'Gold', 'Titanium', 'Stainless Steel' go in the metallic 
category.

The site has CRUD ability (Create, Read, Update and Delete) because the operators of the 
site need to be able to add, update and delete products on the site, plus everyone needs 
to be able to read data on the site (shoppers as well as site operators)

Django officially supports five database backends: PostgreSQL, MySQL, MariaDB, SQLite and Oracle.

The type used in this project is PostGreSQL
PostgreSQL is a powerful, open source object-relational database system that uses and extends the SQL language combined with many features that safely store and scale the most complicated data workloads. PostgreSQL runs on all major operating systems, has been ACID-compliant since 2001.

In computer science, ACID (atomicity, consistency, isolation, durability) is a set of properties of database transactions intended to guarantee data validity despite errors, power failures, and other mishaps. In the context of databases, a sequence of database operations that satisfies the ACID properties (which can be perceived as a single logical operation on the data) is called a transaction.

PostgreSQL comes with many features aimed to help developers build applications, administrators to protect data integrity and build fault-tolerant environments, and help manage data no matter how big or small the dataset. In addition to being free and open source, PostgreSQL is highly extensible. Data types can be defined, custom functions built out, even code written from different programming languages without recompiling the database.

## Site data

### Returns & Refunds

Thanks for purchasing our products at Obelisk Jewellery operated by Obelisk Ltd. In order to be eligible for a refund, you have to return the product within 30 calendar days of your purchase. The product must be in the same condition that you receive it and undamaged in any way. 

After we receive your item, we will inspect it and process your refund. The money will be refunded to the original payment method you've used during the purchase. For credit card payments it may take 5 to 10 business days for a refund to show up on your credit card statement. 

If the product is damaged in any way, or you have initiated the return after 30 calendar days have passed, you will not be eligible for a refund.

If anything is unclear or you have more questions feel free to contact our customer support team.

Sample Return and Refund Policy Template [Free Download]
from [websitepolicies.com](https://www.websitepolicies.com/blog/sample-return-refund-policy-template)

### Terms & Conditions
#### What is a Terms and Conditions Agreement?

A terms and conditions agreement outlines the website administrator’s rules regarding user behaviour, and provides information about the actions the website administrator can and will perform.
Your terms and conditions text is a contract between your website and its users. In the event of a legal dispute, arbitrators will look to this agreement to determine whether each party acted within their rights.

Terms and conditions are not required by law, but are extremely important to the long-term success and viability of your website. Terms and conditions give you control over your site and legal reinforcement if users try to take advantage of your operations.

Creating the best terms and conditions page possible will protect your business from the following:
Abusive users — Terms and conditions allow you to establish what constitutes appropriate activity on your site or app, so you can remove abusive users and content that violates your guidelines.
Intellectual property theft — Asserting your claim to the creative assets of your site in your terms and conditions will prevent ownership disputes and copyright infringement.
Potential litigation — If a user lodges a legal complaint against your business, showing that they were presented with clear terms and conditions before they used your site will help you immensely in court.

In short, terms and conditions give you control over your site and legal reinforcement if users try to take advantage of your operations.

A generic copy of some terms & conditions is taken from the website 'Termly'

## Payment methods
There are four payment methods: -
* Paypal
* Visa
* Mastercard
* American Express

## Delivery options
Free Standard Delivery over £??, otherwise standard delivery of £??
This takes 5-7 working days
Express Delivery £??
Delivery next working day
## Manufacture
[Image](https://cdn.pixabay.com/photo/2018/03/31/12/23/hand-3278027_960_720.jpg
)

Our goods are hand crafted to the highest standard. We strive to create quality items for every budget. We use a large range of raw materials, particularly gems. This makes our jewellery pieces stand out from the crowd, they are so different from pieces bought from well-known, larger companies.

We hope you enjoy your purchases from us!

# Technologies used
* [HTML](https://www.w3schools.com/html)
* [CSS](https://www.w3.org/Style/CSS/Overview.en.html)
* [JQUERY](https://jquery.com)
* [Python](https://www.python.org)
* [Bootstrap](https://getbootstrap.com)
* [Django](https://www.djangoproject.com)

# Deployment
# Testing

## Manual testing
Across all pages, the nav bar shows a menu of Home, Create Account, Login.

If user creates an account or logs in, the nav bar menu adjusts to show Home, Wildlife Surveys, People's Projects, Profile, Add own project, Logout.

If user is an administrator, the menu shows Home, Wildlife Surveys, People's Projects, Profile, Add own project, Manage Categories, Contact Users and Logout.

The footer links should open into pages, 'contact us', 'delivery', 'payment option', 'terms & conditions', 'returns & refunds' and 'Manufacture'.
### Login
### Create Account
### Profile/ Orders page
### Product Management
#### Add Product
#### Edit product
#### Delete product
### Logout
### Responsiveness
### Web browsers
## Testing tools
# Bugs
# Credits
## Media
[IMG 2 GO](https://www.img2go.com) site was used to reduce file sizes of images for inclusion in the project.

[Pixabay](https://pixabay.com) was used to obtain photos of jewellery

Boutique Ado project Chris Z from [Code Institute](https://www.codeinstitute.net)

[Stack overflow](https://stackoverflow.com)

Termly terms and conditions website
[Termly](termly.io/resources/templates/terms-and-conditions-template/)

Hoverable dropdown menu from [W3Schools](https://www.w3schools.com)

Scroll back to top button from [W3Schools](https://www.w3schools.com)

