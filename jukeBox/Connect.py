from pygame import mixer
import os
import mysql.connector
import time

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="JukeBox",
  database='pibox'
)
print(mydb)
# First thing it does is should play music so I know if its on


dir_path = 'C:/Users/EyeOf/Desktop'
mycursor = mydb.cursor()

# Iterate directory
for path in os.listdir(dir_path):

    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        if path.endswith('.mp3'):
            songUrl = dir_path + "/" + path
            songName = path[:-4]
            # query = "INSERT INTO MachineInfo (SongName, FilePath, ArtistName) WHERE id = ID VALUES (" + songName + "," +songUrl + ","")"
            query = "Insert into songs (SongName, FilePath, ArtistName) Values ('"+ songName + "', '" + songUrl +"', 'null')"
            # args = [songName, songUrl, ""]
            # fullStatement = query, args
            # print(query)

            print(path)
            print(path[:-4])
            try:
              mycursor.execute(query)
            except:
              print("Song ALready Inserted")


            time.sleep(2)
mydb.commit()