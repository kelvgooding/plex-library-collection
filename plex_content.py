"""
Author: Kelv Gooding
Created: 2022-06-23
Updated: 2025-07-13
Version: 1.3
"""

# Modules

import auth
from plexapi.server import PlexServer

# Variables

token = auth.api_auth['plex_x_token']
server = auth.api_auth['plex_server']
plex = PlexServer(server, token)

# Script

def plex_media_list(media_type):
    print(f'\n-----| {media_type} |-----\n')

    for item in plex.library.section(f'{media_type}').search():
        print(item.title)

# Names must made libraries created in Plex Media Server UI

plex_media_list('Animation')
plex_media_list('Animation Films')
plex_media_list('Anime Films')
plex_media_list('Anime')
plex_media_list('Films')
plex_media_list('TV Shows')
