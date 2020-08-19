# Cross Platform App Launcher
Great for LAN-Parties. Just write your launcher config once and the players just have to
push a button to launch the game and can launch mods with the push of a button by selecting
them from a list.
## Download
Download the launcher from https://github.com/hhirsch/launcher/releases
no need to unzip because python can run zip files directly.
## Config Files
### Configuring launcher
The minimum config you need is a launcher.json in the root directory of the launcher.
For that just rename launcher.example.json to launcher.json.

When you start the launcher now you should get an empty window without games.
## Adding games
### Add image
Create a directory data/images in the launcher's root directory. 
Add the image for your game in ppm format with the dimensions 215x460.
The image name needs to be the same as the directory name of the game later on.

You can find suitable images on https://www.steamgriddb.com but you have to convert them to ppm.
### Add game files
Create a directory games in the launcher root directory.
Put your game in a directory that is some abreviation of the game. 
Don't use white spaces in the name (rather names like starcraft, anno, ut, jedi-knight).
### Add launcher.json for game
Put a launcher.json in the game's directory.
Provide minimal information on how to launch the game.
Path is not needed if the game is not in a subdirectory of the game's directory.

```json
{
  "title": "Unreal Tournament",
  "description": "Fast paced multiplayer action fps.",
  "windows": {
    "path": "System",
    "exe": "UnrealTournament.exe"
  }
}

``` 
## Running
You need to be in the launcher directory.
```
python launcher-ui.zip
``` 


