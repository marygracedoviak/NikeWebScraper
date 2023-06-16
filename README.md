# Nike Web Scraper
## Description
This project was created as a way to track the price of a specific product, so that you can buy when the price is at it's lowest. The program pulls the title and price of an item once per day and sends an email if it drops below a certain price.
First I used the requests package to scrap the webpage. Then I used BeautifulSoup in order to make the content more legible. I used .content and .prettify to organize the webpage content. Then I inspected the HTML on the webpage and found the names of the title and price, then searched for that using .find and .get_text. 
I used the CSV module to create a CSV file and write the scraped data to the file. 
In order to be alerted when the price drops, I utilized the SMTPLIB module to send an email to myself when the price drops below a certain number. 
To execute the program, I created an infinite while loop that checks the price every 24 hours. This program will run until manually interrupted. 

## To run the program
A few things will need to be altered in order to run on your machine. 
Depending on your environment, you might to install some python packages, including requests, bs4 and pandas. All other libraries should be included in python. 
The headers on line 14 need to be changed to match your system. These can be found at https://httpbin.org/get and simply copy and paste the information next to "User-Agent". 
If you want to use the email function, you'll need to input your desired emails and password. This function only works for Gmail. In order to bypass Gmail's security, you'll need to use an app password instead of your regular Gmail password. To get an app password, go to your google settings, enable and set up 2-step verification, then you should see the option to create an app password. 
Lastly, you'll need to change the path where the CSV file is read from on line 69 if you want to read the file using pandas. 
