<h1 align="center">Auto PY to EXE</h1>
<p align="center">A .py to .exe converter using a simple graphical interface built using <a href="https://github.com/ChrisKnott/Eel">Eel</a> and <a href="http://www.pyinstaller.org/">PyInstaller</a> in Python.</p>

<p align="center">
    <img src="https://i.imgur.com/EuUlayC.png" alt="Empty interface">
</p>

<p align="center">This is the PyPI package of <a href="https://github.com/brentvollebregt/auto-py-to-exe">auto-py-to-exe</a></p>

<p align="center">
    <a href="https://pypi.org/project/auto-py-to-exe/"><img src="https://img.shields.io/pypi/v/auto-py-to-exe.svg" alt="PyPI Version"></a>
    <a href="https://pypi.org/project/auto-py-to-exe/"><img src="https://img.shields.io/pypi/pyversions/auto-py-to-exe.svg" alt="PyPI Supported Versions"></a>
    <a href="https://pypi.org/project/auto-py-to-exe/"><img src="https://img.shields.io/pypi/l/auto-py-to-exe.svg" alt="License"></a>
    <a href="http://pepy.tech/project/auto-py-to-exe"><img src="http://pepy.tech/badge/auto-py-to-exe" alt="Downloads"></a>
</p>

## Installation

### Prerequisites
 - Python : Python 2.7, 3.3 - 3.6

*To have the interface displayed in the images, you will need chrome. If chrome is not installed or --no-chrome is supplied, the default browser will be used.*

### Via [PyPI](https://pypi.org/project/auto-py-to-exe/)
```
$ pip install auto-py-to-exe
```

### Via [GitHub](https://github.com/brentvollebregt/auto-py-to-exe-pypi)
```
$ git clone https://github.com/brentvollebregt/auto-py-to-exe-pypi.git
$ cd auto-py-to-exe-pypi
$ python setup.py install
```

## Usage
Simply run the application by calling it in the terminal:
```
$ auto-py-to-exe
```

You can also pass a file as an argument to pre-fill the script location field:
```
$ auto-py-to-exe my_script.py
```

If you don't want to use Chromes app mode, use the ```--no-chrome``` flag (this will open the default browser):
```
$ auto-py-to-exe --no-chrome my_script.py
```

*If you don't have chrome installed, you do not need to declare this as it will just open the default browser*

### Using the GUI
1. Select your script location (paste in or use a file explorer)
    - Outline will become blue when file exists
2. Select other options and add things like an icon or other files
3. Click the big blue button at the bottom to convert
4. Find your converted files in /output when completed

## Issues
Please report any issues to [auto-py-to-exe](https://github.com/brentvollebregt/auto-py-to-exe) as this package mimics the original repo with some additions to make it available on PyPI.

If there are issues with the changes made to the original repo, they can be reported on [auto-py-to-exe-pypi's GitHub page](https://github.com/brentvollebregt/auto-py-to-exe-pypi).

## Video
If you need something visual to help you get started, [I made a video for the original release of this project](https://youtu.be/OZSZHmWSOeM?t=1m30s); some things may be different but the same concepts still apply.

## Screenshots
![Empty interface](https://i.imgur.com/dd0LC2n.png)

![Filled out](https://i.imgur.com/f3TEnZI.png)

![Converting](https://i.imgur.com/MjdONcC.png)