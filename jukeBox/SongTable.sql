Create database IF NOT EXISTS PiBox


Create TABLE IF NOT EXISTS pibox.songs (
	SongId INTEGER PRIMARY KEY AUTO_INCREMENT,
    SongName varchar(50) not null,
    FilePath varchar(50),
    ArtistName varchar(30),
    Decade varchar(30),
    unique (SongName)
);


drop table pibox.songs

Insert into pibox.songs (SongName, FilePath, ArtistName, Decade)
Values ('Drent', 'C:/Users/EyeOf/Desktop/Rent.mp3', null, null);

Insert into pibox.songs (SongId, SongName, FilePath, ArtistName, Decade)
Values (14, 'Spaghet2', 'C:/Users/EyeOf/Desktop/Spahget.mp3', null. null