"""
create_playlist.py
creates a playlist in user librabry and returns the playlist id
parameters: auth token, list of tracks to add 
"""
def create_playlist(sp, songs):
    
    user_id = sp.me()['id']

    #temp names feel free to change or ask for user input on playlist name?
    playlist_name = "Recs"
    playlist_description = "Reccomedation playlist genreated by Spotify Open Reccomnedation Engine"
    
    #create playlist 
    playlist = sp.user_playlist_create(user_id, playlist_name, public=True, collaborative=False, description = playlist_description ) 
   
    #add tracks to playlist 
    playlist_id = playlist['id']
    sp.user_playlist_add_tracks(user_id, playlist_id = playlist_id, tracks = songs)

    return playlist_id
