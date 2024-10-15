class track:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

class collection:
    def __init__(self):
        self.tracks = []
        self.length = 0

    def addTrack(self, track):
        self.tracks.append(track)
        self.length += 1

    def showTracks(self):
        for x in range(len(self.tracks)):
            print(self.tracks[x].title)

favMusic = collection()

romanticiseThis = track("Romanticise This", "James Marriott")
madIQs = track("Mad IQs", "IDKHOW")
betterThanMe = track("Better Than Me", "The Brobecks")

favMusic.addTrack(romanticiseThis)
favMusic.addTrack(madIQs)
favMusic.addTrack(betterThanMe)

favMusic.showTracks()