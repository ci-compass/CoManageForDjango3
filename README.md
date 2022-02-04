# (Very) Minimal Example of using CoManage to provide InCommon authentication for Django-based Web Applications

Here you will find three directories, each with a more progressively built-out application. The application itself
is trivially simple - it asks the user for their MAC address and stores it in a database table for later use.

The first directory to look at is "macregister". This is as simple as the application can be under Django.

The second directory is "macregauth". This doesn't use CoManage, but instead uses Django's own built-in
Identity Management. To use this in any secure fashion would require IT staff to create user accounts and
manage passwords locally. This is precisely what we want to avoid.

The third directory is "macregcomanage". This uses CoManage to present a Shibboleth login screen,
much like what someone would see if they were accessing their home institution's library.
Users log in using their username and password from their home institution. Staff at the Major Facility
never has to deal with usernames and passwords for visiting researchers again!

Each directory contains its own README.md explaing what is going on in that sample.


Erik Scott, CI Compass
escott@renci.org


