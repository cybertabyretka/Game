# Game
Game for the second semester of study at UrFU
<br /> <br />
## Navigation
- [Installing the project on PC](#download_project)
- [Project settings](#project_settings)
- [Core technologies and frameworks](#frameworks)
- [Controls](#controls)
- [Notes](#notes)
<br /> <br />

<a name="download_project"></a> 
## Installing the project on PC
1. Откройте консоль, вбив в поисковике ПК: `cmd`;
2. Перейдите в директорию, куда хотите установить проект, пропишите следующую команду в консоль: `cd N:\Путь\до\папки\с\проектами`;
3. Введите следующую команду: `git clone https://github.com/cybertabyretka/Game.git`;
4. В скачанном репозитории по пути `BaseVariables/Paths.py` измените переменную `BASE_PATH` на ваш путь до проекта.
<br /> <br />

<a name="project_settings"></a>
## Project settings
 - Версия Python: 3.11
 - После скачивания проекта к себе на компьютер установите необходимые зависимости, прописав к консоли команду:  `pip install -r requirements.txt`
<br /> <br />

<a name="frameworks"></a>
## Core technologies and frameworks
 - `Pickle` - Module for serialization and deserialization. Serialization is the process of converting a `Python` object into a stream of bytes, which can then be stored on disk or transmitted over the network. Deserialization is the reverse process where a stream of bytes is converted back into a `Python` object;
 - `Pygame` - `Python` module for game creating;
 - `MVC` - The project uses `MVC`, almost all modules used in the game are divided into three components (Model, View, Controller);
 - `A*` - The `A*` algorithm is used to find the path to the player from the NPC;
 - `Singleton` - This template is used for some modules in the project.
<br /> <br />

<a name="controls"></a>
## Controls
 - `W` - go up;
 - `A` - go left;
 - `S` - go down;
 - `D` - go right;
 - `E` - open inventory or loot something that you can loot;
 - `F` - go through a door (only possible if all NPCs on the level are dead);
 - `P` - pause the game;
 - `esc` - the ability to exit to the main menu or save the game.
<br /> <br />

<a name="notes"></a>
## Notes
 - All images in the project are test images.
