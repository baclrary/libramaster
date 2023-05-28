
![Logo](https://img.icons8.com/external-others-inmotus-design/512/external-S-alphabet-others-inmotus-design-7.png)

    
# LibraMaster 📚


Welcome to the Django Library Project! This project was conceived and developed during my studies at SoftServe Academy, as part of the coursework to gain real-world experience. Our main objective is to simplify the management of a library through a robust, intuitive, and user-friendly web application.

The project was developed in a team, however, the old GitHub repository may be removed soon by our organisation. The models were written by our mentors, and everything else was done by our team. It has been a long time, and I can now see what can be changed and improved. If there is a request, I will refactor this project.



## Screenshots

Hero page

![img](README_images/1.png)

Registration form

![img](README_images/2.png)

List of users

![img](README_images/3.png)

Book's detail page

![img](README_images/4.png)

Author's detail page

![img](README_images/5.png)

List of orders

![img](README_images/6.png)

# Stack 🧰

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/downloads/release/python-390/) 

[![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)](https://docs.djangoproject.com/en/4.2/releases/4.1/)

[![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)](https://www.django-rest-framework.org/)

[![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://django-tailwind.readthedocs.io/en/latest/installation.html)

## Installation

### Database

Setup postgres (v. 14) server.

Create database


### Project

Navigate to .env_example file directory
#### Then create .env file from template and fill in your credentials:
```bash
cp .env_example .env
```



#### Create and activate virtual enviroment

```bash
virtualenv venv
```

For MacOS
```bash
source venv/bin/activate
```
For Windows
```bash
venv\Scripts\activate
```

#### Then install requirement project's packages

```bash
pip install -r requirements.txt
```

## Run Project

#### Go to the folder with manage.py file and run the following commands


```bash
python manage.py makemigrations 
```
```bash
python manage.py migrate 
```
```bash
python manage.py createsuperuser 
```
```bash
python manage.py runserver 
```

## Contacts
Email - ihorprotsak@gmail.com

Telegram - @the_coffin_is_my_new_room