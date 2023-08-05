# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).


## [Unreleased]
## [1.10.0] - 2018-08-24
## Configured 
- make improvements to setup.py

## Added 
- add functions to work with sqlite databases
- add more parameter to ontology_object 

## [1.9.0] - 2018-08-10
## Configured 
- make improvements to setup.py and pyinstaller.py 

## Added 
- add multiprocessing functions with process bar 

## [1.8.0] - 2018-08-02
## Configured 
- add imgkit to install_requires
- delete old version file, the version is now controlles by git tags 
- move converting function for html to jpg to own submodule 
- modifiy the function get_list_of_files so that the returned list is only with the given filetype 

## Added 
- add class to work with ontologies that loads owl file and has functions to get subclass instances
- add submodule visualization with functions to work on images and functions to plot data 

## [1.7.0] - 2018-07-25
## Added 
- new class to convert html files into jpg images
- new prototype class too compare ontologies (not working at the moment)

## [1.6.0] - 2018-07-23
## Added 
- new functions and classes to work with ontologies and owlready2
- add new variable log to debug class that can hold all messages of the new debug level doku. Note this level is now behind level zero and no more the level development

## [1.5.1] - 2018-06-16
## Fixed
- fix problem with syntax

## [1.5.0] - 2018-06-16
## Fixed
- fix problem with the pyinstaller build on linux

## [1.4.0] - 2018-03-01
## Added 
- add class that delegates the style of a selected item in the qtreeview
- add function to check value if there is comma and if so replace it with a dot

## [1.3.0] - 2018-02-28
### Added 
- Add function to clean layout
- Add function to wait on boolean mutex in the pyqt enviorment
- Add fuctions to to wait on signal, clear layout from widget 
- Add new function to open file or url in correct browser

## Fixed 
- fix problem with resource_path function that is pointing to wrong path

## [1.2.0] - 2018-02-23
### Added 
- Add functions to work with OpenCV 3.4

## [1.1.0] - 2018-02-09
### Added 
- New function to check for prefix in text and remove if existing
- New function to change the keyname of an xml item
- New fuction to update xml key value pair in the attributes
- New fuction to create executable with pyinstaller (works!)

## [1.0.0] - 2017-12-11
### Configured 
- restructure of pylibcklb package 

## [0.9.0] - 2017-12-10
### Added 
- add function to get relative path to target path from current working path
- add function to print message in green and red for success or error
### Fixed
- Make CreateDir and CreateFile more safety through call submethods in try-except-block

## [0.8.0] - 2017-11-29
### Added
- Rezise start dialog and info dialog to 0.5 of the display size
- Add method to create menu bar and the entry 'Edit'
- Add classes to create main window without anything else and with pre created stuff

## [0.7.0] - 2017-11-25
### Added
- add function to save changes of dict back to file to make them static
- add checkbox to info dialog and start dialog

## [0.6.0] - 2017-11-23
### Added
- add new dialog classes for startscreen dialog and info dialog

### Fixed
- There are some fixes to the previous version for import bugs and other things

## [0.5.0] - 2017-11-22
### Added
- new class to get thread for searching specific filetypes in directory
- add new classes to handle toolbars and undo and redo in the toolbar 
- add function to set drag drop mode of an qtreeview element

## [0.4.0] - 2017-11-14
### Added
- Add first work on script library for installer like pyinstaller

## [0.3.0] - 2017-11-10
### Added
- Add LGPLv3 License 

## [0.2.0] - 2017-11-07
### Added
- Add new functions to create a file and and directory
- Add new comments to save and load folder function
- Add new functions to create message boxes for error, warning, information and questions

## 0.1.0 - 2017-06-02
### Added
- Init commit and push of different elements to new repository

[Unreleased]: https://gitlab.ecklebe.de/open-source/pylibcklb/compare/v1.10.0...master
[1.10.0]: https://gitlab.ecklebe.de/open-source/pylibcklb/compare/v1.9.0...v1.10.0
[1.9.0]: https://gitlab.ecklebe.de/open-source/pylibcklb/compare/v1.8.0...v1.9.0
[1.8.0]: https://gitlab.ecklebe.de/open-source/pylibcklb/compare/v1.7.0...v1.8.0
[1.7.0]: https://gitlab.ecklebe.de/open-source/pylibcklb/compare/v1.6.1...v1.7.0
[1.6.0]: https://gitlab.ecklebe.de/open-source/pylibcklb/compare/v1.5.1...v1.6.0
[1.5.1]: https://gitlab.ecklebe.de/open-source/pylibcklb/compare/v1.5.0...v1.5.1
[1.5.0]: https://gitlab.ecklebe.de/open-source/pylibcklb/compare/v1.4.0...v1.5.0
[1.4.0]: https://gitlab.ecklebe.de/open-source/pylibcklb/compare/v1.3.0...v1.4.0
[1.3.0]: https://gitlab.ecklebe.de/open-source/pylibcklb/compare/v1.2.0...v1.3.0
[1.2.0]: https://gitlab.ecklebe.de/open-source/pylibcklb/compare/v1.1.0...v1.2.0
[1.1.0]: https://gitlab.ecklebe.de/open-source/pylibcklb/compare/v1.0.0...v1.1.0
[1.0.0]: https://gitlab.ecklebe.de/open-source/pylibcklb/compare/v0.9.0...v1.0.0
[0.9.0]: https://gitlab.ecklebe.de/open-source/pylibcklb/compare/v0.8.0...v0.9.0
[0.8.0]: https://gitlab.ecklebe.de/open-source/pylibcklb/compare/v0.7.0...v0.8.0
[0.7.0]: https://gitlab.ecklebe.de/open-source/pylibcklb/compare/v0.6.0...v0.7.0
[0.6.0]: https://gitlab.ecklebe.de/open-source/pylibcklb/compare/v0.5.0...v0.6.0
[0.5.0]: https://gitlab.ecklebe.de/open-source/pylibcklb/compare/v0.4.0...v0.5.0
[0.4.0]: https://gitlab.ecklebe.de/open-source/pylibcklb/compare/v0.3.0...v0.4.0
[0.3.0]: https://gitlab.ecklebe.de/open-source/pylibcklb/compare/v0.2.0...v0.3.0
[0.2.0]: https://gitlab.ecklebe.de/open-source/pylibcklb/compare/v0.1.0...v0.2.0