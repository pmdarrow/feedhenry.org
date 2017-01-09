---
layout: page
title: Overview
permalink: /overview/
---

### What is FeedHenry?

FeedHenry is a cloud-based enterprise mobile application platform that enables
users to design, develop, deploy and manage applications for mobile devices. The
platform specializes in extending enterprise systems to mobile devices, and
provides mobile-specific services for security, notifications and data
synchronization. Developers can easily build backend logic that supports their
mobile applications—all in a secure, scalable manner.  

### Background

FeedHenry was initially built by a mobile application services company of the
same name based in Waterford, Ireland. In September 2014, Red Hat acquired
FeedHenry, and in keeping with their [philosophy](http://community.redhat.com/software/),
began the process of open-sourcing the platform. Following the acquisition,
FeedHenry's supported offerings were released under the
[Red Hat Mobile Application Platform](https://www.redhat.com/en/technologies/mobile/application-platform)
brand, and the "FeedHenry" name was retained for releasing related open source
projects.

### Components

For most of its life, FeedHenry has been a closed-source SaaS product. Therefore
the open-sourcing process has been gradual. Here are the components that make up
FeedHenry:

| Component | Description | Source Code
| -
| [Client SDKs]({{ "/projects/#client-sdks" | relative_url }}) | Native and hybrid SDKs for client app development on iOS, Android, Windows, Xamarin, Appcelerator, Cordova, and in web apps. | <span class="tag tag-success">Available</span>
| [Push Notifications]({{ "/projects/#push-notifications" | relative_url }}) | Integration with AeroGear for sending push notifications to any device, regardless of platform or network. | <span class="tag tag-success">Available</span>
| [App Templates]({{ "/projects/#app-templates" | relative_url }}) | Starting points for building your applications with FeedHenry, including templates for iOS, Android, Xamarin, Appcelerator, Cordova; OAuth2 and SAML examples, push notification and data synchronization examples, and many more. | <span class="tag tag-success">Available</span>
| [RainCatcher]({{ "/projects/#raincatcher" | relative_url }}) | A set of Node.js modules that can be used with FeedHenry to develop workforce management applications. | <span class="tag tag-success">Available</span>
| [Core]({{ "/projects/#core" | relative_url }}) | The core components that make up FeedHenry, including drag & drop forms builder, application lifecycle management, reporting, analytics, user management, and more. | <span class="tag tag-info">Coming soon</span>
| [MBaaS]({{ "/projects/#mbaas" | relative_url }}) | Provides the Node.js runtime environment for high-performance server-side apps (cloud apps) and enables secure integrations with internal systems behind the firewall. | <span class="tag tag-info">Coming soon</span>
| [Build Farm]({{ "/projects/#build-farm" | relative_url }}) | Automates the app build process, maintains a history of previous builds, and provides the ability to create builds for platforms without requiring the associated infrastructure and tools (e.g. building iOS binaries from a Linux OS). | <span class="tag tag-info">Coming soon</span>
{: .table .components}
