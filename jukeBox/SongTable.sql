Create database IF NOT EXISTS PiBox


Create TABLE IF NOT EXISTS pibox.songs (
	SongId INTEGER PRIMARY KEY AUTO_INCREMENT,
    SongName varchar(30),
    FilePath varchar(40),
    ArtistName varchar(30),
    unique (SongName)
);

drop table pibox.songs

Insert into pibox.songs (SongName, FilePath, ArtistName)
Values ('Brent', 'C:/Users/EyeOf/Desktop/Rent.mp3', null);

Insert into pibox.songs (SongName, FilePath, ArtistName)
Values ('Spaghet', 'C:/Users/EyeOf/Desktop/Spahget.mp3', null);