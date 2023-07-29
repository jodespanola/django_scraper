# Django and Scrapy Project

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

This projects demonstrates my knowledge in Python, Django, Django Rest Framework and webscraping using Scrapy.

## Table of contents

- [Requirements](#requirements)
- [Usage](#usage)
- [Documentation](#documentation)
- [My process](#my-process)
  - [Start line](#creating-the-django-application-and-preparing-the-postgresql-database.)
  - [Building the API](#creating-the-api-endpoint-for-the-rest-framework.)
  - [Scrapy](#creating-the-scraper.)
  - [All together](#integrating-the-scraper-with-the-django-application.)
  - [Testing](#testing.)
- [What I hade Trouble with](#what-i-had-troubled-with)
- [References](#references)

## Requirements

python==3.11.4 &nbsp;
PostgreSQL >= 11

## Usage

1. &emsp;Start by creating a virtual environment. This will make sure that the third party libraries that will be installed for the demonstration/use of this project won't affect already installed libraries on your local computer.

1. &emsp;```python -m pip install -r requirements.txt```

1. &emsp;On your PostgresSQL create a database with the schema.sql included on this project.

1. &emsp;Depending on how your PostgreSQL is setup, you might have to edit the values on the .env file. This file usually should be not included in repositories since it contains sensitive information but since this is mainly for demonstration adding the file shouldn't be a big deal. 

1. &emsp;```cd django_scraper```

1. &emsp;```python manage.py makemigrations```

1. &emsp;```python manage.py migrate```

1. &emsp;```python manage.py crawl```

1. &emsp;```python manage.py runserver```

## Documentation

The API that I created can perform both get and post requests. 

* **URL**

    &emsp;/product/

* **Method**

    &emsp;`GET` | `POST`

* **URL Params**

    &emsp;None

* **DATA Params**

    **Required:**

    &emsp;`name=[string]`
    `price=[string]`
    `URL=[URL]`
    `image_url=[URL]`

* **Sample Call:**

```
curl -X GET http://127.0.0.1:8000/product/```

## My Process

The way I come about on doing the project is by dividing the task into smaller chunks and starting off of stuff I am most comfortable with. These steps corresponds to the first four of my commits on the repository.

### Creating the Django Application and preparing the PostgreSQL database.

This step of course starts with creating a virtual environment for the project.
After which, the installation of python libraries I know I would use for the projecct. 

Then its a routine procedure of creating a django application, creating the product app and the model for our data.

Once done, the settings.py for the Django application should be configured to match the database that the project would populate. For myself, I created a PostgreSQL database called product_scraper. The credentials used for this database are then stored in a .env file to hide sensitive information that would normally be left on the settings.py

Once the database has been setup, run the following commands:
```cmd
    python manage.py makemigrations
    python manage.py migrate
```

Once confirmed that all is well, time to move to the next step.

### Creating the API endpoint for the REST framework.

This is almost a routine too. From the data model, create a serializer to talk between the JSON response and the python data types. 

Then is just a matter of updating the views and urls. On the views, other than the all too familiar get and post, I also added context to make the form on the API endpoint a little bit more user friendly.

### Creating the scraper.

Suprisingly, creating the scraper with scrapy is fairly straightforward than what I imagined it to be. Start the scraper with scrapy's 'startproject' to create the project template we can start on.

Then create the spider through the genspider command. I initially use the default spider but I later on switched to using CrawlSpider as my parent class that my spider would inherit off of to. I just find the syntax and structure for this a bit cleaner.

Then make sure that the spider works by running:

```scrapy crawl __spider_name___```

### Integrating the scraper with the Django Application.

This step is perhaps the most difficult for me. Although, I can consider myself lucky that I come in contact with django-item. It took a lot of stuff that I was dreading on doing when I first tried to think of ways on integrating scrapy with Django. 

This step is mostly configuring the paths on each import that I previously did on the scraper. And also configuring the scraper's pipeline and settings.

Then I created the Django Command that will run the spider scraper that I created and from the data that it gathered, populate the database.

### Testing.

During the creation of this README, I also created a simple unittest to check the functionality of my DRF API. Good thing too because i discovered that I had a bug on my post method. 

## What I had troubled with

Its my first time trying to integrate web scraping with a Django application so I had encountered lots of problem when I tried mixing the two. 

When I first tried to run the crawl django command that I created, I was met with a verbose error that seemed intimidating but its just a matter of changing the way files on the scraper are imported since I think the entry point or the place in which it is called is different when I was just running it separately from the Django Application.

This one took more time that I'd like to admit but essentially the process that I created on the pipeline that saves the data object, created off of the scraped data, to the database is not working properly since it needs to run asynchronously. 

And I spent a lot of time reading forums and documentations on this to try to understand how to make it run asynchronously. In the end, a one line decorator fixed the issue.

## References

- [Scrapy Documentation](https://docs.scrapy.org/)
- [DRF](https://www.django-rest-framework.org/)
- [Django Coding Style](https://docs.djangoproject.com/en/4.1/internals/contributing/writing-code/coding-style/#model-style)