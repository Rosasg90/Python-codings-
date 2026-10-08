# Josue Rosas 
# Student ID: 877784637 
# Section: 08
# Module 6 Assignment 2
def make_album( artist, album_title, numsongs = 'None'):
     album_dict = {
          'artist' : artist,
          'title': album_title,
          'number of songs:': numsongs
 }
     return album_dict 

while True:
    album_title = input(f"What is the title of the ablum (or q for quit) ?")
    if album_title == 'q' or album_title == 'quit':
         break 
    artist = input(f"What is the name of the artist? ")
    print(make_album(artist , album_title))