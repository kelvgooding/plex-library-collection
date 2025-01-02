# Plex API

## Description

Plex API is a project which allows the user to view information on their personal Plex Server. There are two files which are:

- **plex-server-info.py**

This will show the Plex version number, last updated date/time, the number of users, which devices are authorised to watch content on the Plex Server.

- **plex-contents.py**

This will show all media content for the groups of your choosing.

> **Requirements**

A Plex Account is required, along with a Plex X-Token (Refer to the following link for further instructions) https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/

**auth.py**

This application requires user credentials. This file is representative of any personal details which you would like to keep private.
Within the plex_content.py and plex_server_info.py scripts, auth.py will be referenced, and the variables will be found in this file.
The auth.py file will be left blank by default. Therefore, this information must be entered before using this application.

## Other

- **Issue Tracker**: https://github.com/kelvgooding/plex-api/issues
- **Asana Tracker**: https://app.asana.com/0/1208845689816750/board
- **Contact**: kelvin.gooding@livelifeautomate.co.uk
