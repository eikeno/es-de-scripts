# Scripts for use alongside ES-DE (Emulation Station Desktop Edition)

## Prerequisites

- An operationnal ES-DE setup
- Python3 (any 3.8 version should OK)
- The __fzf__ command if using __es-de-select__ wrapper (fzf package should be available on most distros).

## import_lutris_games.sh

This script parses Lutris' __pga.db__ sqlite file and creates for each game of each platform (wine, linux, zdoom, MS-DOS and web) a corresponding __./ROMs/ \<game\>.txt__ file.

These empty text files can then be used for importation in ES-DE by using **GenSsystemFiles.py** and then **GenGameLists.py**

When a game is selected in ES-DE in the __"PC Games - Lutris"__ category, Lutris will be launched with the game as parameter.

_Edit as needed to support more or less of Lutris platforms._

### Usage

Simply invoke the script from desired location. 
```
cd /home/johndoe/gaming/LutrisESDE
bash /home/johndoe/gaming/LutrisESDE/import_lutris_games.sh"
```
**ROMs** directory will be created in the current directory (i.e: __/home/johndoe/gaming/LutrisESDE/ROMs__)

Then make sure to edit **GenSsystemFiles.py** to modify **PC Games - Lutris** system by replacing:
```
f"{NI_TOPD}/0-Overlay/Lutris - PC Games",
```

by something that points to where ROMs folder was created. For example, if it was created as __/home/johndoe/gaming/LutrisESDE/ROMs__ you must replace with:
```
"/home/johndoe/gaming/LutrisESDE",
```

## GenGameLists.py
Script for generating selectively gamelist for indicated systems.

### Usage
Edit the file and modify __GEN_SYSTEMS__ tuple to your needs.
System names to use are those used in GenSsystemFiles.py

By default, only __PC Games - Lutris__ system is present, change according to your needs (in my case, I avoid pre-generated gamelists as much as possible).

For the gamelist __PC Games - Lutris__ to be properly generated, extra steps are required (see [above](#import_lutris_games.sh]).

For most other systems, no extra steps are required, apart proper ES-DE configuration and correct variables set at the top of __GenSsystemFiles.py__

## GenSsystemFiles.py

### Why use this ?
This might be of interest if you want to consolidate systems management, games paths, command definitions etc. in one central file, to ease maintenance in case of often changing or large setup.

When using this, you don't have to modify numerous individuals system files, just this script.

It also makes possible to run ES-DE via __es-de-select \<system\>__ to load either only one system (reduce loading time) or __all__.


This script will generate:
- an XML file per enabled system under __./custom_systems/__
- a global XML file with all systems (to be used with __es-de-all__ or __es-de-select all__ - see below).

### Usage
```
cd ~/ES-DE
python3 GenSsystemFiles.py
```


Before proceeding, it's imperative that you edit the file to:
- modify variables at the top to values that make sense for your local setup.
- comment out unneeded systems.
- uncomment systems that are commented and you might want. 
- check that only systems you have configured are enabled.
- check that the system tuples hold values that make sense for you.

I'd suggest to maybe start by enabled only one system, see how it goes, and enable more gradually if works fine.

### Multiple commands are supported
You can check system tuple for __switch__ for an example. You can implement similar approah in any other system were you need more than one command.

## es-de-select

A simple wrapper to the ES-DE comment, that will manage __custom/systems/es_systems.xml__ as a symlink to the requested __system__ or __all__ to enable all systems (this one might take longer to load on large setups.)

### Usage
```
es-de-select
```

Will let you choose which system to load in __fzf__

```
es-de-select nes
```
Will only load the __nes__ system, provided it it enabled and correctly configured.

```
es-de-selct all
```
Will load all configured systems.

```
es-de-all --resolution 1920 1080
```
Same as above, but let you pass options to ES-DE if needed.


## mame_run_from_fullname.sh
Wrapper to MAME Referenced in __GenSsystemFiles.py__.

## run-lutris-by-slug_esde.sh
Wrapper to Lutris referenced in __GenSsystemFiles.py__.

## Final word
Remind to backup any important configuration files before testing, one never can be careful enough.


And also, have fun !
