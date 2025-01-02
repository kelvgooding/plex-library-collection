"""
Author: Kelv Gooding
Created: 2022-06-23
Updated: 2025-01-02
Version: 1.2
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

plex_media_list('Animation')
plex_media_list('Anime Films')
plex_media_list('Anime')
plex_media_list('Docuseries')
plex_media_list('Films')
plex_media_list('TV')
