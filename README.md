# My-Blog
# Author
[Maryam-Muchai](https://github.com/MaryamMuchai/My-Blog.git)
# Live Link
https://marya-myblog.herokuapp.com/
# Description
 This is a flask application of a personal blogging website where you can create and share your opinions and other users can read and comment on them. Additionally, the application displays random quotes to inspire users. 
# User Story in Pictures
### User view
* User can view blog posts on the sites
* User can see random quotes on the site
* User can view the most recent posts
* User can subscribe to blog mailing list and receives an email alert when a new post is made.
* User can comment on blog posts
![Screenshot from 2021-05-06 00-15-09](https://user-images.githubusercontent.com/78798386/117212633-432ba200-ae03-11eb-82e1-879978e461f7.png)

### Blog view
* Sign in to the blog
* Create a blog from the application
* Update/change on the blogs created
![Screenshot from 2021-05-05 21-58-46](https://user-images.githubusercontent.com/78798386/117206035-05c31680-adfb-11eb-896a-f4085047f228.png)
### Profile page
* Can update on their profile description
![Screenshot from 2021-05-05 21-51-03](https://user-images.githubusercontent.com/78798386/117205941-eb893880-adfa-11eb-9238-0828689c9dcc.png)

 # Behaviour Driven Development
 |Input    | Behaviour | Output |
 ----------|-----------|--------|
 |Subscribe to mail list| Input the email | Redirect to the index page|
 |User Login | Takes you to the homepage | Redirects you to the home page|
 | Create a blog form | Write your blog and post it to the blogs | Blog is displayed in index page |
 | User comment on the Blog post| Write your feedback and post it | Feedback is displayed under the blog post |
 |Writer updates a blog post | Updating the blog post in database | The blog post will be updated |

# Development Installation
To get the code..
### 1.Cloning the repository:
https://github.com/MaryamMuchai/My-Blog.git
### 2.Move to the folder and install requirements
> cd My-Blog

>pip install -r requirements.txt
### 3.Exporting Configurations
>export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
### 4.Running the application
>python manage.py server
### 5.Testing the application
>python3 manage.py test

>Open the application on your browser 127.0.0.1:5000.


# Technology used
* Python3
* Flask
* Heroku
* Flask
* HTML5
* CSS3
* Javascript
* Font Awesome
* SQLAlchemy
* PostgreSQL
# Contact Information
* Incase of any question or contributions, email: maryammuchai@gmail.com
# License
### MIT [License](LICENSE)
### Copyright (c) 2021 Maryam Muchai
