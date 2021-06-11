def make_album(musician_name,album_name,amount_track=None):
    album = {'musician': musician_name,'album': album_name}
    if amount_track:
        album['amount_track'] = amount_track
    return album
album_info = make_album('Anacondaz','Дети и радуга')
print(album_info)
album_info = make_album('Король и шут','Мертвый Анархист')
print(album_info)
album_info = make_album('System of a down','Chop Suey!',amount_track=4)
print(album_info)
