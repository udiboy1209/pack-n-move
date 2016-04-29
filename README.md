Pack-n-Move
===========

A script for helping you pack everything and move from your home to another. 
Your linux home, not the actual one!
A script for your actual home will require some more ingenuinity :wink:!

Features
--------

It is a python script which lists all the packages you currently have 
installed in your current home and generates a shell script which reinstalls 
them on your new home.

This is done using modules in the [listers](listers/) package, which follow a standard template.

Listers
-------

The currently implemented ones are

 - [AptLister](listers/apt.py): for apt packages on a Debian system. Only lists down manually installed packages
 - [PipLister](listers/pip.py): for python packages installed using pip
 - [GemLister](listers/gem.py): for ruby packages installed using gem
 - [NpmLister](listers/npm.py): for Node.js packages installed using npm
