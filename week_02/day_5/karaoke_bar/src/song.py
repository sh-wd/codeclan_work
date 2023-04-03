class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        

    def create_a_new_song(self):
        title = input("Enter the song's title: ")
        artist = input("Enter the song's artist: ")
        self.add_song_to_list(title, artist)
        return Song(title, artist)

    def add_song_to_list(self, title, artist):
        self.songs.append(
            {
            "title" : title,
            "artist" : artist
            }
        )