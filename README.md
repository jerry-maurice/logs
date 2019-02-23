Created by Jerry Maurice

Description
This program is an internal report tool that use information from the database to discover what kind of articles the site's readers like. This psql database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. What the program does is answering these 3 questions below:
1. What are the most popular three articles of all times?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

How to run the program
Before this application was created, vagrant and virtualbox were installed. First, this link is provided to download virtual box - www.virtualbox.org and this www.vagrantup.com is to download vagrant. Once installed to quickly start just clone this repository found at https://github.com/udacity/fullstack-nanodegree-vm. Because everything is already installed, no need to install other packages. We only need to copy the files I provided.
It's time to run the project.
First vagrant need to be running:
Step to do it
1. Vagrant up
2. Vagrant ssh
Once running
1. cd /vagrant
After completed the above step, we need to download the data. I provided this file and it's called newdata.sql. We need to load the data into the local database. Since we are already in the vagrant folder use the command psql -d news -f newsdata.sql which connect to the  database name news and load the info from the newdata.sql file to this database. 
the logs_projectFinal.py is the python3 written program that will generate the report. In order to run the program type python3 logs_projectFinal.py to the command line. A sample output.txt file is provided to see an example of the output of the program

About the python program
The program import the psycopg2 and the datetime library. The datetime library has been imported to manipulate the time value from the query result and the psycopg2 library is to connect to a psql database

It is divided into four method one is the main and the other answer the three questions above. Each one connect to the database and once the query has been fetch it closes the connection and return a list. On the main method it calls each method and return the calculated value from each
