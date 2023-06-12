"""
Author: Kelvin Gooding
Created: 2022-06-23
Updated: 2023-06-12
Version: 1.1
"""

# Modules

import auth
from plexapi.server import PlexServer

# Variables

token = auth.api_auth['token']
server = auth.api_auth['server']
plex = PlexServer(server, token)

# Script

print("-----| System Information |-----\n")
print(f"Plex Version: {plex.version[:11]}")
print(f"Last Updated: {plex.updatedAt}")

print('\n-----| List of Accounts |-----')
for i in plex.systemAccounts():
    print(i.name)

print('\n-----| List of Devices |-----')
for device in plex.systemDevices():
    print(device.name.upper())
