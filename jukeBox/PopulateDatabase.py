from pygame import mixer
import os
import mysql.connector
import time
from tinytag import TinyTag

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database='pibox'
)
print(mydb)

# if it fails with unicode error, change aroud the slashes
dir_path = 'C:/Users/Scott/Desktop/Songs/SpotiFlyer/Playlists/JukeboxSongs'
mycursor = mydb.cursor()
songList = []

# Iterate directory
for path in os.listdir(dir_path):

    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        if path.endswith('.mp3'):
            a_tag = TinyTag.get(dir_path + "/" + path)
            artist = a_tag.artist
            songUrl = dir_path + "/" + path
            songName = path[:-4]
            songList.append([songName, songUrl, artist])
newSongList = sorted(songList,key=lambda x: x[2])

for songInfo in newSongList:
    mycursor.execute("SELECT * FROM songs WHERE SongName = '" + songInfo[0] + "'")
    retrievedSongRecord = mycursor.fetchone()
    print("Retrieved Record:", retrievedSongRecord)
    if retrievedSongRecord is None:
        songInfoName = songInfo[0]
        query = "Insert into songs (SongName, FilePath, ArtistName, Decade) Values ('" + songInfo[0] + "', '" + \
                songInfo[1] + "', '" + songInfo[2] + "', 'null')"
        try:
            mycursor.execute(query)
            mydb.commit()
            print("Committing")
        except:
            print("Song ALready Inserted")

    else:
        print("Song Already Exists in Database")
