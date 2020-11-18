# Django-Personal-Website-Blog
A full-featured personal website with a blog, made by django.
<br>You can check the website out on www.hossshakiba.com
## Blog
There's a blog for sharing your thoughts and knowledge with others and people can comment their ideas on each post.
You can make your posts look prettier and more professional, using a powerful rich text editor that is implemented in the code and comes very handy for developers.
<br>There is search bar, which makes it possible to search through posts and find your desired ones based on their title and text.
<br>
## Resume
You can write a short bio about yourself on resume page and make others aware of your skills and experiences.
## contact-me
People can make contact with you and also hire you as a develper.

## Installation
There are a few steps to take before running the website on your localhost :
<ul style="line-height:180%">
  <li>Clone the repository</li>
  <li>Launch a virtual environment</li>
  <li>Install the requirements</li>
  <li>Create a database</li>
  <li>Run the project on localhost</li>
</ul>
<br>

### Clone the repository

```bash
git clone https://github.com/hossshakiba/Django-Personal-Website-Blog.git
```
### Launch a virtual environment

```bash
virtualenv venv
```
```bash
source venv/bin/activate
```
### Install the requirements
```bash
pip install -r requirements.txt
```

### Create a database

```bash
python manage.py migrate
```
### Run the project on localhost

```bash
python manage.py runserver
```



