Добро пожаловать!
Это мой первый проект с использованием github, следовательно и первое readme.
Представляю вам таймер на пк с прикольным интерфейсом и рингтоном.

сборка на windows: pyinstaller index.py --onefile --windowed --name "таймер" --add-data "style.css;." --add-data "fonts;fonts" --add-data "sound;sound" --add-data "pics;pics"
сборка на mac: pyinstaller index.py --onefile --windowed --name "таймер" --add-data "style.css:." --add-data "fonts:fonts" --add-data "sound:sound" --add-data "pics:pics"

