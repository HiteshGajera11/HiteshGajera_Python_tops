"""
--->What is Django URLs?

-Django runs through each URL pattern, in order, 
and stops at the first one that matches the requested URL, 
matching against path_info.

Once one of the URL patterns matches,
Django imports and calls the given view, 
which is a Python function (or a class-based view).

URL is a path through which a specific web-based application and one 
particular page in that web application can be reached. 
So for any web-oriented application setting these url paths is a very key necessity. 
Django manages the necessary URLs in the urls.py section of the framework, 
following various techniques to maintain them throughout the application.
The methods used to keep the URLs organized in Django are discussed below.

--->How to Create a Django URL?

1. Creating a url USING PATH()
Django introduced the path method and re_path() method in version 2.0, 
allowing for the inclusion of an element as a URL pattern within a tuple 
that can be used for URL patterns.

Syntax: 

path(route, view, name)

"""