# Brain Wave Cafe
## This is an application that allows users to make blogs,comment and view the  available posts.


## Author
Vincent Ouma

## Description
This is an application that allows users to make blogs,comment and view the  available posts and also comment on them only after signing in for an account.Users also can subscribe to the website.

## User Stories
1. As a user one can view the blog posts submitted
2. As a user one can comment on blog posts
3. As a user one can view the most recent posts
4. As a user one can be alerted when a new post is made by joining a subscription.
5. As a writer one can sign in to the blog.
6. As a writer one can create a blog from the application.
7. As a writer one can delete comments that they find insulting or degrading.
8. As a writer one can update or delete blogs they have created.
## Specifications
| Behavior        | Input           | Output  |
| ------------- |:-------------:| -----:|
| Click On SignUp | Your email : vinceobindi@gmail.com.com <br> Username : vin <br> Password : 123 | New user is registered |
| Sign in/Log in | Your email : vinceobindi@gmail.com <br> Password : 123 | Signed in |
| View posts | Displays on home page | List of available posts |
| View comments | **Click** a view button | Navigates to the selected post |
| Create a post | **Click On Add a Blog Post** | The authenticated user is navigated to the blog form to fill in |
| Comment on a post | **Click Comment** | User navigates to the comment form  |

### Prerequisites
This web application requires the following software tools to operate
-Python version 3.6
-Flask
-Pip
-virtualenv
-A text  Editor
-SQLALCHEMY/Database
## Getting Started
* Clone https://github.com/vincentouma/Blog.git  to your local computer.
* Ensure you have python3.6 installed in your computer.
* From the terminal navigate to the cloned project folder.
* Create a virtual environment and access the folder via your virtual machine
 
 * run python3.6 manage.py server on the project directory
* Run ```chmod +x start.sh``` followed by ``` ./start.sh ``` while in the project folder to start the project.
* Once started, the project can be accessed on your localhost using the address: ``` localhost:5000 ```.
* This application can also be accessed by clicking the following link: https://vinny-blog.herokuapp.com 




## Technologies Used
- Python3.6
- Flask
- Postgres Database
- CSS/Bootstrap
- HTML

### License

Copyright 2019 < Vincent Ouma >

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

