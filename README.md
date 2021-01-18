# COVID-19 Vaccination Milestone Notifications / Web Data Scraper

Scrape Data and Send COVID-19 Populace Vaccination Percentage Notifications via Python.

Dr. Fauci has said that as countries reach a 70% vaccination rate amongst the populace we can exepect a slow return to normalcy. I want to go to concerts, so each time we reach a vaccination milestone I want to know about it. 

This script scrapes Canadian COVID-19 vaccination data and logs it to a database. It sets benchmarks/milestones and sends an email notification when certain vaccination benchmarks are hit. Simply connect to a SQL database, import the included sample database, set up a cron job and set it to run once every day.

The mailer function uses the MailGun API, you may sign up for a free mailgun account and input your MailGun API key. 
