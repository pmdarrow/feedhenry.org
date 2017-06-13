---
layout: page
title: Getting Started with the FeedHenry Sync Framework
permalink: /hero-sync/
---

# Data synchronization using fh-sync & javascript applications

This quick-start guide will document what you need is needed to start using the FeedHenry Sync framework to synchronize data between a javascript client app and server.


## Sync Framework

The sync framework is a pragmatic framework
* init on client side
* init on cloud side (dataListHandler on cloud side looks after the data being synced & driven by your logic)
  * can handle mutliple datasets
* 2 tutorials
  * setting up a client that simply receives sync updates from a defined dataset from a server
    * configuring a client to act on these updates
  * setting up a server to push to client apps
    * configuring the data handlers on an express server
    

## Overview 

Using the FeedHenry Sync framework with your applications will involve two components, fh-sync, and a client sync adapter. 

### fh-sync

The heavy lifting of data synchronization will be performed through the fh-sync library. This will be installed on the server side. 


### Client sync adapter 

To interface with fh-sync on the server side, a sync client adapter will need to be installed in the client app. 

At present sync client functionality is provided through the FeedHenry SDK libraries (fh-js-sdk/ fh-ios-sdk/ etc), and the appropriate SDK will need to be installed in your client app. In the future sync-specific client adapters will be made available so installation of the full SDK will not be required. 


## Prerequisites

* Javascript client application
* Node.js server application


## FeedHenry sync demo apps

A set of client and server apps to demonstrate sync may be found here:

* [Sample FeedHenry sync-client app][sync-client-template]
* [Sample FeedHenry sync-cloud app][sync-cloud-template]

Documentation on getting them running can be seen in the readme sections of both repos.


## Wiring up your client

Configure and initialize your client app by:

* Initializing the sync-client
* Assigning data-sync handlers in your client code

A simple html client showing how sync would being integrated on client-side can be seen [here][fh-sync-js-example].

## Available sync api methods 

* `sync.init(options);`
  * Initialise the client data sync service.
* `sync.notify(callback(data));`
  * Register a callback function to be invoked when the sync service has notifications to communicate to the client.
* `sync.manage(dataset_id, options, query_params, meta_data, callback);`
  * Put a dataset under the management of the sync service. Calling manage multiple times for the same dataset will update the options and query_params but will not result in the dataset syncing multiple times.
* `sync.doList(dataset_id, success, failure);`
  * Get a list of the records for the dataset.
* `sync.doCreate(dataset_id, data, success, failure);`
  * Update the data associated with the unique id.
* `sync.doRead(dataset_id, uid, success, failure);`
  * Read a single data record.
* `sync.doUpdate(dataset_id, uid, data, success, failure);`
  * Update the data associated with the unique id.
* `sync.doDelete(dataset_id, uid, success, failure);`
  * Delete the data associated with the unique id.
* `sync.startSync(dataset_id, success, failure);`
  * Start the sync loop if 'sync_active' option is set to false.
* `sync.stopSync(dataset_id, success, failure);`
  * Stop the sync loop for a dataset.
* `sync.doSync(dataset_id, success, failure);`
  * Run the sync loop almost immediately (within next 500 ms) if sync_active is true.
* `sync.forceSync(dataset_id, success, failure);`
  * Run the sync loop almost immediately (within next 500 ms) even if sync_active is false.
  

## Wiring up your server

Configure sync in your server application by:

* Importing the fh-sync library
* Assign an api sync route that clients can call when syncing data
* Configure/ connect sync to your data source 

A simple express.js showing fh-sync being integrated on the server-side can be seen [here][fh-sync-example].


## Tips/ Troubleshooting


## Further reading

links to existing & more in-depth sync docs to be linked



[sync-client-template]: https://github.com/feedhenry-templates/sync-cordova-app
[sync-cloud-template]: https://github.com/feedhenry-templates/sync-cloud
[fh-sync-js-example]: https://github.com/feedhenry/fh-sync-js/blob/master/example/index.html
[fh-sync-example]: https://github.com/feedhenry/fh-sync/tree/master/examples/basic-express-example