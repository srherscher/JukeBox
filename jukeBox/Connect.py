from pygame import mixer
import os
import mysql.connector
import time

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database='pibox'
)
print(mydb)


dir_path = 'C:/Users/EyeOf/Desktop'
mycursor = mydb.cursor()

# Iterate directory
for path in os.listdir(dir_path):

    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        if path.endswith('.mp3'):
            songUrl = dir_path + "/" + path
            songName = path[:-4]
            mycursor.execute("SELECT * FROM songs WHERE SongName = '" + songName + "'")
            retrievedSongRecord = mycursor.fetchone()
            print(retrievedSongRecord)
            if retrievedSongRecord is None:

                query = "Insert into songs (SongName, FilePath, ArtistName, Decade) Values ('" + songName + "', '" + songUrl + "', 'null', 'null')"

                print(path)
                print(path[:-4])
                try:
                    mycursor.execute(query)
                    mydb.commit()
                    print("Committing")
                except:
                    print("Song ALready Inserted")

                time.sleep(2)
            else:
                print("Song Already Exists in Database")


