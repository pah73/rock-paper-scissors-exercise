# This README file has been adapted from the run-the-app exercise README file shown in class and available on our course GitHub

# rock-paper-scissors-exercise

Instructions about running the rock-paper-scissors app

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Forking the repo 
  Fork this [remote repository](INSERT REPOSITORY LINK !) under your own control, then "clone" or download your remote copy onto your local computer.

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

## Command line instructions 

```sh
cd rock-paper-scissors-exercise # directory to where repo is stored locally
```

Use Anaconda to create and activate a new virtual environment, perhaps called "my-game-env":

```sh
conda create -n my-game-env python=3.8 #run an updated version of pythong
conda activate my-game-env
```
## Install packages ?? 
From inside the virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```



## Setup

In in the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your desired username:

    USER_NAME="John Snow"

> NOTE: the ".env" file is usually the place for passing configuration options and secret credentials, so as a best practice we don't upload this file to version control (which is accomplished via a corresponding entry in the [.gitignore](/.gitignore) file)

## Usage

Run the game script and play !

```py
python game.py

The game will prompt the user to select rock, paper, or scissors by typing it out. If the selection is invalid, the game will quit and you can restart by using the command above.


