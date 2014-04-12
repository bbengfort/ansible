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

<!-- References -->
[ansible.png]: http://www.endersansible.com/wp-content/uploads/2012/05/Darians_Battleschool.jpg
