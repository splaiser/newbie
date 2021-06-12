def make_album(musician_name,album_name):
    album = {'musician': musician_name,'album': album_name}

    return album
while True:
    print('\nTell me your favorite musician and album')
    print("(enter 'q' if you want to stop)")

    mus_name = input("Enter musician name: ")
    if mus_name == 'q':
        break
    alb_name = input("Enter album name: ")
    if alb_name == 'q':
        break
    correct_name = make_album(mus_name,alb_name)
    print(f"\nHello, your favorit musician and album is:{correct_name}")