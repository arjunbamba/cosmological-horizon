## ✨ Cosmological Horizon Plotting/Visualization Tool 💫

### 🌱 Introduction 🚀
Physics 495 (Senior Project) - Fall 2021
Project Mentor: Professor Vera Gluscevic
Developer: Arjun Bamba
Contact: arjunbam@usc.edu

This tool enables you to plot and visualize either all 3 universes (Hyperbolic, Euclidean, Spherical) using default parameters or just the Euclidean universe alone using custom parameters.


### 💻 Running the project ⚡️
1. Clone this github repository or download as ZIP.
2. Import to PyCharm:
    * Open PyCharm
    * From the main menu bar, choose File > Open
    * In the dialog that opens, select the directory that contains the desired source code. In our case, this is simply the root directory that was cloned/downloaded from GitHub.
    * Click Open/OK.
    * If there's a pop-up asking you to specify whether you want the new project to be opened in a separate window, click 'New Window'.
3. The primary files in this project assume that you have certain packages/dependencies installed (e.g. matplotlib, numpy, opencv-python, scipy, ffmpeg, etc.). If you do not have these packages installed in PyCharm, please continue with step 4. Otherwise, if you do have these packages installed, skip to step 8.
4. To install the needed dependencies, from the main menu bar, select PyCharm > Preferences. 
5. In the window that opens, navigate to and open the 'Project: cosmological-horizon-...' submenu on the left side. Within the submenu, select Python Interpreter.
6. Click the '+' icon to add new packages. Please make sure you have the following packages installed: matplotlib, numpy, opencv-python, scipy. Others that may be needed due to dependencies: astropy, pandas.
    * Please refer to Figure 1 that shows all packages in my environment for reference and to debug any dependency/package issues. Note: not all the packages that I have are likely needed.
    * Also, note here that my Python Interpreter is Python 3.9.
7. Now, to install ffmpeg, open terminal and run `brew install ffmpeg`. This command assumes that you have the Mac package manager, Homebrew, installed on your computer; if you don't, please refer to guide (b) to install homebrew first and then return to install ffmpeg.
    * a. Reference guide to install ffmpeg: https://formulae.brew.sh/formula/ffmpeg
    * b. Reference guide to install homebrew: https://brew.sh
8. In the project panel in PyCharm, please ensure there is a `videos` subdirectory located within the root directory. This should already be there but if not, please create a new directory called `videos` in the project root directory: right-click on the root directory in the project panel and then go to New > Directory to create the `videos` subdirectory. It is in this `videos` subdirectory that the project visualization videos will be later saved.
9. Open the 'Cosmic_Horizon.py' file.
10. Right-click on the open 'Cosmic_Horizon.py' tab and click on `Run 'Cosmic_Horizon'`. 
11. Follow the on-screen instructions in the console - the following information will be displayed in the console at the start of the program to explain how the tool functions:
    Using this tool, you will have the option to plot and visualize either all 3 universes (Hyperbolic, Euclidean, Spherical) using default parameters or just the Euclidean universe alone using custom parameters.
    You will be asked 3-4 questions: 
    * Question 1 will ask whether you would like to plot all 3 universes using default parameters.
        * --> If you answer 'yes', it will proceed to plot all 3 universes using the following default parameters: 
        Hyperbolic Universe Parameters: Ω<sub>k</sub> > 0, Ω<sub>m</sub> = 0.9, Ω<sub>r</sub> = 10<sup>-4</sup>, Ω<sub>l</sub> = 0 
        Euclidean Universe Parameters: Ω<sub>k</sub> = 0, Ω<sub>m</sub> = 0.3, Ω<sub>r</sub> = 10<sup>-4</sup>, Ω<sub>l</sub> = (1 - Ω<sub>m</sub> - Ω<sub>r</sub>) 
        Spherical Universe Parameters: Ω<sub>k</sub> < 0, Ω<sub>m</sub> = 0.3, Ω<sub>r</sub> = 10<sup>-4</sup>, Ω<sub>l</sub> = 0.8
        * --> If you answer 'no', it will (later) ask you for your custom Omega_m and Omega_r parameters to plot/visualize a Euclidean universe.
    * Question 2 will ask until what redshift would you like to plot/visualize. This must be any number (integer or decimal) between the given bounds: 10 <= redshift <= 1100. You will be asked in Question 3 whether you would like to make a visualization/movie. These redshift bounds are to simply ensure that the visualization renders appropriately (should you choose to go that route). 
    * Question 3 will ask whether you would like to make a visualization/movie.
        * --> If you answer 'yes', depending on how you answered Question 1, it will proceed to make a visualization for either all 3 universes or only the Euclidean one. Image frames will be saved in automatically created directories named 'images_[type of universe]' and the visualization video will be stored in the 'videos' directory with name 'Visualization_[type of universe]'.
        * --> If you answer 'no', it will proceed to simply plot the universe(s).


### 🔭 Extraneous Files 👣

There are 2 extraneous scripts that I coded while developing this project; although ***not applicable*** to this project, they could be used for either further development of this project or for any other purpose. The 2 extraneous scripts are:
* cosmic_visualization.py - visualizing our solar system in 2D using Python Turtle Graphics
* cosmic_visualization_v2.py - visualizing our solar system in 3D using Python Turtle Graphics. Allows you to change perspective using up and down arrows.

Feel free to run these scripts, if you'd like, to view the solar system visualizations.

### 🛠 &nbsp;Tech Stack

#### 👉 Programming
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
* Packages:
    * ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
    * ![SciPy](https://img.shields.io/badge/SciPy-%230C55A5.svg?style=for-the-badge&logo=scipy&logoColor=%white)
    * matplotlib
    * opencv-python

FFMPEG

#### 👉 Developer Tools & Hosting
![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)