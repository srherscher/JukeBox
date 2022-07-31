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

# Iterate directory
for path in os.listdir(dir_path):

    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        if path.endswith('.mp3'):
            a_tag = TinyTag.get(dir_path + "/" + path)
            artist = a_tag.artist
            songUrl = dir_path + "/" + path
            songName = path[:-4]
            mycursor.execute("SELECT * FROM songs WHERE SongName = '" + songName + "'")
            retrievedSongRecord = mycursor.fetchone()
            print(retrievedSongRecord)
            if retrievedSongRecord is None:

                query = "Insert into songs (SongName, FilePath, ArtistName, Decade) Values ('" + songName + "', '" + songUrl + "', '" + artist +"', 'null')"

                # print(path)
                # print(path[:-4])
                try:
                    mycursor.execute(query)
                    mydb.commit()
                    print("Committing")
                except:
                    print("Song ALready Inserted")

            else:
                print("Song Already Exists in Database")
