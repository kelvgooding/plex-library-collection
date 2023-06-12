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
plex = PlexServer(server, token)

# Script

def plex_media_list(media_type):
    print(f'\n-----| {media_type} |-----\n')

    for item in plex.library.section(f'{media_type}').search():
        print(item.title)

plex_media_list('Films')
plex_media_list('Anime')
plex_media_list('TV Series')
plex_media_list('Docuseries')

