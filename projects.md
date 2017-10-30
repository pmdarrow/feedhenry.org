---
layout: projects
title: Projects
permalink: /projects/
---

Here's an overview of the components that make up FeedHenry.

<div class="project-title" markdown="1">

## Client SDKs

Native and hybrid SDKs for mobile app development.

</div>

<div class="project-text" markdown="1">

FeedHenry supports a wide range of mobile development technologies. We provide
support for native iOS, Android, Windows, Xamarin, Cordova, and
other HTML5 app frameworks.

{% include repos.html repos="fh-ios-sdk,fh-ios-swift-sdk,fh-android-sdk,fh-dotnet-sdk,fh-js-sdk" %}

</div>



<div class="project-title" markdown="1">

##  App Templates

Starting points for building your applications with FeedHenry.

</div>

<div class="project-text" markdown="1">

We've developed app templates for iOS, Android, Xamarin, Cordova;
OAuth2 and SAML examples, push notification and data synchronization examples,
and many more. We've highlighted a few of the popular ones below.

{% include repos.html repos="helloworld-app,appforms-project-client,sync-cloud,blank-cordova-app,welcome-cloud" %}

Find a complete list of templates [here](https://github.com/feedhenry-templates/).
</div>



<div class="project-title" markdown="1">

## Push Notifications

Integration with [AeroGear] for sending push notifications to any device,
regardless of platform or network.

</div>

<div class="project-text" markdown="1">

<img src="{{ "/assets/images/aerogear.svg" | relative_url }}" alt="AeroGear Logo" class="project-logo" />

In 2012, Red Hat launched its first mobile related research project, titled
[AeroGear]. AeroGear's goal is to provide flexible, extensible libraries and
server side components that simplify mobile development and infrastructure setup
across platforms.

In December 2015, the [UnifiedPush Server] from the AeroGear project was
integrated into FeedHenry. This provides FeedHenry users the ability to
send push notifications to any device, regardless of platform or network.

[AeroGear]: https://www.aerogear.org/
[UnifiedPush Server]: https://aerogear.org/push

{% include repos.html repos="aerogear-unifiedpush-server,aerogear-ios-push,aerogear-android-push,aerogear-cordova-push,aerogear-windows-push,aerogear-js-push" %}

</div>

<div class="project-title" markdown="1">

## RainCatcher

WorkForce Management Platform

</div>

<div class="project-text" markdown="1">

<img src="{{ "/assets/images/raincatcher.svg" | relative_url }}" alt="RainCatcher Logo" class="project-logo" />

* [RainCatcher project website](http://raincatcher.feedhenry.io)
* [feedhenry-raincatcher mailing list](http://www.redhat.com/mailman/listinfo/feedhenry-raincatcher)
* [RainCatcher chat](https://gitter.im/FeedhenryRaincatcher/Lobby)

</div>

<div class="project-title" markdown="1">

## MBaaS

The FeedHenry Mobile Backend as a Service is a set of services to support applications that serve as a backend for Mobile Apps.

</div>

<div class="project-text" markdown="1">

#### Components

{% include repos.html repos="fh-openshift-templates,fh-mbaas,fh-messaging,fh-stats" %}


</div>

<div class="project-title" markdown="1">

## Data Synchronization

A set of Mobile SDKs & Node.js module for client/server data synchronization with offline support.

</div>

<div class="project-text" markdown="1">

#### Overview

The FeedHenry Data Synchronization framework includes the following features:

* Allows mobile apps to use and update data offline (local cache)
* Provides a mechanism to manage bi-directional data synchronization from multiple Client Apps using the Cloud App and into back-end data stores
* Allows data updates (that is, deltas) to be distributed from the Cloud App to connected clients
* Enables data collision management from multiple updates in the cloud
* Allows Apps to seamlessly continue working when the network connection is lost, and allows them to recover when the network connection is restored.

#### Community

* [feedhenry-dev mailing list](http://www.redhat.com/mailman/listinfo/feedhenry-dev)
* [IRC: #feedhenry on Freenode](irc://irc.freenode.net/feedhenry)


#### Node.js Module

{% include repos.html repos="fh-sync" %}

#### Client SDK's

##### Browser (javascript)

{% include repos.html repos="fh-sync-js" %}

##### Android

#### Coming Soon
{: .tag .tag-info}

##### iOS

#### Coming Soon
{: .tag .tag-info}

##### .NET

#### Coming Soon
{: .tag .tag-info}


</div>

<div class="project-title" markdown="1">
## Build Farm

A suite of tools and modules that can be used to automate the process of building mobile applications on Kubernetes/OpenShift using Jenkins.
</div>
<div class="project-text" markdown="1">

### Modules

{% include repos.html repos="aerogear-digger,aerogear-digger-java-client" %}



### Installer 

Ansible scripts that can be used to install/provision the required tools, SDKs and services. Work in progress.

Coming Soon
{: .tag .tag-info}


</div>
