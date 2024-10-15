class track:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

class collection:
    def __init__(self, size):
        self.tracks = [None] * size
        self.size = size

    def showTracks(self):
        for x in range(len(self.tracks)):
            print(self.tracks[x].title)

favMusic = collection(3)

favMusic.tracks[0] = (track("Romanticise This", "James Marriott"))
favMusic.tracks[1] = (track("Mad IQs", "IDKHOW"))
favMusic.tracks[2] = (track("Better Than Me", "The Brobecks"))

favMusic.showTracks()