---
layout: page
title: Getting Started with Sync
permalink: /hero-sync/
---

# Data synchronisation using fh-sync & javascript applications

This quick-start guide will document what you need is needed to start using the FeedHenry Sync framework to synchronize data between a javascript client app and server.


## Overview 

Using the FeedHenry Sync framework with your applications will involve two components, fh-sync, and a client sync adapter. 

### fh-sync

The heavy lifting of data synchronisation will be performed through the fh-sync library. This will be installed on the server side. 


### Client sync adapter 

To interface with fh-sync on the server side, a sync client adapter will need to be installed in the client app. 

At present sync client functionality is provided through the FeedHenry SDK libraries (fh-js-sdk/ fh-ios-sdk/ etc), and the appropriate SDK will need to be installed in your client app. In the future sync-specific client adapters will be made available so installation of the full SDK will not be required. 


## Prerequisites

* Javascript client application
* Node.js server application


## Feedhenry sync demo apps

A set of client and server apps to demonstrate sync may be found here:

* [Sample feedhenry sync-client app][sync-client-template]
* [Sample feedhenry sync-cloud app][sync-cloud-template]

Documentation on getting them running can be seen in the readme sections of both repos.


## Wiring up your client

Configure and initialise your client app by:

* Initialising the sync-client
* Assigning data-sync handlers in your client code

A simple html client showing how sync would being integrated on client-side can be seen [here][fh-sync-js-example].


## Wiring up your server

Configure sync in your server application by:

* Importing the fh-sync library
* Assign an api sync route that clients can call when syncing data
* Configure/ connect sync to your data source 

A simple express.js showing fh-sync being integrated on the server-side can be seen [here][fh-sync-example].


## Tips/ Troubleshooting


## Further reading

links to existing & more indepth sync docs to be linked



[sync-client-template]: https://github.com/feedhenry-templates/sync-cordova-app
[sync-cloud-template]: https://github.com/feedhenry-templates/sync-cloud
[fh-sync-js-example]: https://github.com/feedhenry/fh-sync-js/blob/master/example/index.html
[fh-sync-example]: https://github.com/feedhenry/fh-sync/tree/master/examples/basic-express-example