sudo apt install mariadb-server

sudo mysql_secure_installation

sudo mysql -u root -p jukebox

Create database IF NOT EXISTS PiBox
use PiBox


set path=%PATH%;C:\Program Files\MySQL\MySQL Server 8.0\bin;

#admin  JukeBox

mysql -u root --password JukeBox



Create TABLE IF NOT EXISTS pibox.test (
	SongId INTEGER PRIMARY KEY AUTO_INCREMENT,
    SongName varchar(30) not null,
    FilePath varchar(40),
    ArtistName varchar(30),
    Decade varchar(30),
    unique (SongName)
)
echo DOIT


#pip3 install mysql-connector-python

