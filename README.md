# Disclaimer
This is a student project for non-commercial use
This Project retrives news articles from  many news feed (News Stories) provided by 
1) Times of India (https://timesofindia.indiatimes.com/rssfeeds/1221656.cms)
2) The Hindu(http://www.thehindubusinessline.com/news/?service=rss)
3) BBC (http://feeds.bbci.co.uk/news/world/asia/rss.xml)

The Author does not take any responsibility for any news .

Any commercial use of this project should be done only by seeking the permission of the
News portal mention above.

All credit of news goes to the  online portals of The Times of India , The Hindu,
and BBC. 

# NewsATFingerTip



# Application Overview
	This Application retrives the RSS feeds of Multiple News Portals and Displays them .
In The back ground  the Application uses tkinter for GUI , requests to get RSS FEEDS and ElementTree to 
parse XML.

# Tools Used
1) Spyder( python 3.6 )

#Features
1) Client can Get Current Top News From Multiple News Portal 
2) Automatic Update Of news as Soon as Updates At Portal

#Steps to run the program:
1) Download The Script and Run In python

#prerequisite
1) python 3.x or higher
2) tkinter 
3) ElementTree 
4) requests 

#Bugs and limitations:
1)Did not handle exceptions all exceptions
2)Tested for only few days
3) Depends on RSS feeds provided by news Portal (Any changes in Url and project have to be modifies)

# References
1) Graphical User Interfaces with Tk  
   retrived form :https://docs.python.org/3/library/tk.html
2)Programming GUIs and windows with Tkinter and Python Introduction
  retrived from : https://pythonprogramming.net/tkinter-depth-tutorial-making-actual-program/
3) Geeks For Geeks  -XML Parsing
   retrived from - http://www.geeksforgeeks.org/xml-parsing-python/
5) Python software foundation - for The ElementTree XML API
   retrived from - https://docs.python.org/2/library/xml.etree.elementtree.html#finding-interesting-elements
5) Tutorials Point - for Xpath Query Examples 
   retrived from - https://www.tutorialspoint.com/xpath/xpath_expression.htmv
6) Python For Beginners [ Request Library In Python ]
   retrived from http://www.pythonforbeginners.com/requests/using-requests-in-python
