Ansible
=======
**A Twisted-Django Data Ingestion and Visualization Application**

[![Ansible][ansible.png]][ansible.png]

Taking a queue from Allen, who likes to record all data, I've decided to try to come up with a simple Twisted/Django app to learn Twisted in particular. The idea is along the lines of Nathan Yau's [Flowing Data](http://your.flowingdata.com/home/) - where he uses Twitter feeds to rapidly collect data that he visualizes in real time. The twitter feeds are simple action/value predicate pairs, for example:

    weigh 160
    drank 2 water
    goodnight 11:00 PM

These simple statements are then recorded into action logs and values with various data types. For example, Categorical, Event, Counter, and Measurement data types.

As Twitter is a text feed, it seems perfectly reasonable to be able to program something like this using a chat-like client rather than going through Twitter. In particular, since I want to learn Twisted for other projects, it seems like a Twisted ingestion server for these action predicates would be very cool and useful! They do allow complete flexibility in what you create (like a chat room) but the Twisted server could then give back useful responses to the various sensors that might be streaming data to the server.

The Django App will be used to visualize this data in real time. I imagine that we could use this app to do things like put together a mapping from Foursquare etc. (Using If This Then That or similar), we could probably explore all kinds of cool and useful things with this tool!

## Running the Demo ##

Currently, there is a simple demo to show how everything works. To install/run this demo follow the following steps.

1. Download/clone the repository:

        $ git clone https://github.com/bbengfort/ansible.git
        $ cd ansible

2. Create a virtual environment and install dependencies:

        $ virtualenv venv
        $ source venv/bin/activate
        $ pip install -r requirements.txt
        
3. Set the following environment variable (sorry). You can also add export statements to the end of the bin/activate script to do this automatically if you have to do this often. 

        $ export DJANGO_SETTINGS_MODULE=philote.settings.development

4. Sync the database and run the server. (You can add a super user if you'd like, that's fine!) If you get an error about the database path, make sure there is a directory called `fixtures` in the root of the repository. 

        $ python philote/manage.py syncdb
        $ python philote/manage.py runserver

5. You should be able to open a browser and navigate to http://127.0.0.1/ and see the Django app. Don't click on the link quite yet.

6. Next, you need to run the ansible server- the twisted server that accepts streaming data from various ingestion sources. To do this run the following commands in a different terminal window:

        $ source venv/bin/activate
        $ bin/mazer listen
        
    This will start the server in the browser, you shouldn't be seeing much happen though at this point. 
    
7. In the browser, go ahead and click on the `Simple Counter` link to see the detail page of the counter. You probably won't be seeing too much, but as you follow the next steps, keep an eye on this page. 

8. In yet another terminal window, do the following:

        $ source venv/bin/activate
        $ bin/mazer generate

    You should now be seeing data flowing across the screen in the browser, the chart updating for every 10 time points. All your terminals should be filling up with data now! Repeat step 8 as many times as you would like to add data sources and streams. 
    
9. To quit the demo- in each of the terminal windows type `CTRL+C` and close the browser window. 

### So what did I just see? ###

This demo might have been interesting, sure - but what you just saw was the connection of a custom twisted TCP protocol to a Django app. In particular, the Twisted server was listening for statements in the form of action predicates - it then rebroadcasted incoming statements to any clients that asked for them. 

The generate clients were examples of data streams. They created random, associated data and sent the data to the ingestor as action predicate statements. The ansible server listened for the predicates and stored the last ten statements in memory. 

The Django is another type of client. Rather than send data (which is possible, but you'll note that the post command isn't there yet) it ingested the data each second and displayed it on the screen in real time using Ajax long polling. The browser itself didn't connect with the Twisted server, but rather the Django backend did in much the same way it might connect to a database server. 

WHEW! 

That may not seem like a lot, but it demonstrated a lot of moving pieces. The questions now are whether or not Twisted is something we want to use to connect to Django or to put together scientific backends for modeling. 

<!-- References -->
[ansible.png]: http://www.endersansible.com/wp-content/uploads/2012/05/Darians_Battleschool.jpg
