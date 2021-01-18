# covid-vaccine-notifcations-canada
 Send COVID-19 Vaccination Percentage Notifications via Python

This script scrapes Canadian COVID-19 vaccination data and logs it to a database. It sets benchmarks/milestones and sends an email notification when certain vaccination benchmarks are hit. Simply connect to a SQL database, set up a cron job and set it to run once every day.

The mailer function uses the MailGun API, you may sign up for a free mailgun account and input your MailGun API key. 
