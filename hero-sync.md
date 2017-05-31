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

steps & code examples to be added


## Wiring up your server

steps & code examples to be added


## Tips/ Troubleshooting


## Further reading

links to existing & more indepth sync docs to be linked



[sync-client-template]: https://github.com/feedhenry-templates/sync-cordova-app
[sync-cloud-template]: https://github.com/feedhenry-templates/sync-cloud