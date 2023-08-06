# GameCore Integrations Library

This is the library responsible for GameCore integrations.  
Async code is used whenever possible, with synchronous code being "converted" and run in the main loop thread.

While closely related to GameCore needs, this library can be used on it's own to support different services.  
Most integrations are based on third-party open source libraries, so you may prefer to use these instead.

- [GameCore Integrations Library](#gamecore-integrations-library)
  - [Integrations](#integrations)


## Integrations

Integrations are what power GameCore's search, playtime queries, user libraries, etc.

We have plans to support and integrate the following services:

- [ ] IGDB  
This is our main search provider.
Developed in-house.

- [ ] HowLongToBeat  
For playtime related information.

- [ ] Steam  
Integration for populating user libraries with Steam games and achievements.

- [ ] PSN  
Integration for populating user libraries with PSN games and achievements.  

Powered by the [psnawp](https://github.com/isFakeAccount/psnawp) Python library.

- [ ] Xbox Live  
Integration for populating user libraries with Xbox Live games and achievements

