# This README file has been adapted from the run-the-app exercise README file from Professor Rossetti shown in class and available on our course GitHub

# rock-paper-scissors-exercise

Instructions about running the rock-paper-scissors app

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip
  + A text editor and command line tool (I use VSCode and Terminal on MacOS)

## Forking the repo 
  Fork this [remote repository](https://github.com/pah73/rock-paper-scissors-exercise) under your own control, then "clone" or download your remote copy onto your local computer.

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

## Command line instructions & Setup

```sh
cd rock-paper-scissors-exercise # directory to where repo is stored locally
cd Documents/GitHub/rock-paper-scissors-exercise #my personal file location
```

Use Anaconda to create and activate a new virtual environment in the command line:

```sh
conda create -n my-game-env python=3.8 #run an updated version of python (at least 3.7)
conda activate my-game-env #activating once created
```
## Installing Packages & Username Customization
Create two different files:
+ .env file
+ requirements.txt file
From inside the virtual environment, install package dependencies:

Add customization options, such as username, in the .env file. The username name can be updated to whatever you would like !

```sh
USER_NAME = "Player 1"
```
add the dotenv package to the requirements.txt file and install the package in the command line with this command:

```sh
pip install -r requirements.txt
```

> NOTE: the ".env" file is usually the place for passing configuration options and secret credentials, so as a best practice we don't upload this file to version control (which is accomplished via a corresponding entry in the [.gitignore](/.gitignore) file)

## Usage

Run the game script and play !

```py
python game.py

The game will prompt the user to select rock, paper, or scissors by typing it out. If the selection is invalid, the game will quit and you can restart by using the command above.


