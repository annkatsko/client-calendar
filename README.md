
## 🚀 About Me
I'm a python developer and a fitness coach as well. I have been working in the gym for 5 years. That's why I wanted to create the usefull project for my job.

[![Linkedin Badge](https://img.shields.io/badge/-HannaKatsko-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/midhruvjaink/)](https://www.linkedin.com/in/hanna-katsko-a4319222b)
 
# 🏋️ Client Web Calendar 

Client Web Calendar is a Django Web Site for coach's clients.
The main function of this Web site is to provide clients with the information of upcoming workout sessions. 

It provides Time and Date of a session. 
This information comes from a coach's Google calendar. So this Web site uses Google calendar api. 
Web site provides the Django authorization system. 

A client can sign up and log in, add his profile information to make coach learn more about him. 

The main fields of client's profile is first and last name as Google Calendar Api uses it to get the session Date and Time and show it to the client. 
IMPORTANT!
A coach has to use client's first and last name in his own calendar as a header of the event. 

A few screenshots 👇👇👇

![Image alt](https://github.com/annkatsko/client-calendar-readme-img/raw/main/img1.png)


![Image alt](https://github.com/annkatsko/client-calendar-readme-img/raw/main/img2.png)

## 👨‍💻 Project stack
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)

[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://docs.djangoproject.com/en/4.1/)

![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

![HTML](https://img.shields.io/badge/HTML-239120?style=for-the-badge&logo=html5&logoColor=white)

![CSS](https://img.shields.io/badge/CSS-239120?&style=for-the-badge&logo=css3&logoColor=white)

![JS](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

![Bootstrap](	https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)


## 	🚀 Deployment
You need Python 3.10.8 and pip (the package installer for Python). 

To deploy this project run

```bash
  pip install -r requirements.txt
```
After finishing installation you have to visit https://console.cloud.google.com , create your Google account. 
Than follow instructions from https://developers.google.com/workspace/guides/create-project?hl=en to create your project. 

Than go to project Library. 

![Image alt](https://github.com/annkatsko/client-calendar-readme-img/raw/main/img4.png)


Search for Google calendar Api and enable it.

![Image alt](https://github.com/annkatsko/client-calendar-readme-img/raw/main/img5.png)

Visit Credentials reference. 

![Image alt](https://github.com/annkatsko/client-calendar-readme-img/raw/main/img7.png)

And create credentials. Choose OAuth client ID and select Desktop App. After that download credentials-json file, put it into the root of your project directory. Rename this file to "credentials.json". 

![Image alt](https://github.com/annkatsko/client-calendar-readme-img/raw/main/img6.png)  
.

Now it is time to take down all other credentials to configs/settings.py




## Settings.py

```python
SECRET_KEY = "generate your secret key"
```

```python

# database configs
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'your database name',
        'USER': 'your database user',
        'PASSWORD': 'your database password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# timezone configs
TIME_ZONE = 'Europe/Minsk'

# email configs
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'your email'
EMAIL_HOST_PASSWORD = "your email passwords"
```

Note:
it's worth storing all credentials in .env file.
Example:
```python
import environ
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()
EMAIL_HOST_USER = env("EMAIL_USER")
```

You should take your Contact info down into home_page/templates/home_page/contacts.html your own contact information and links. 

![Image alt](https://github.com/annkatsko/client-calendar-readme-img/raw/main/img8.png)


Than run next commands in the console from the root directory:
```python
python manage.py makemigrations
```
```python
python manage.py migrate
```
```python
python manage.py runserver
```

Congratulations 🎉  You have done it 🥇






## ✏️ Contributing
1. Fork it (https://github.com/annkatsko/client-calendar/fork). 
2. Create your feature branch (git checkout -b feature/fooBar). 
3. Commit your changes (git commit -am ‘Add some fooBar’). 
4. Push to the branch (git push origin feature/fooBar). 
5. Create a new Pull Request. 


## 🦸‍♀️ Authors

- [@annkatsko](https://github.com/annkatsko)


 
