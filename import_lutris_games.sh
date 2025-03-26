#!/usr/bin/env bash
WD="$(pwd)"

rm -Rf ROMs
lutris_query_pga.sh "SELECT slug FROM games WHERE platform='Windows' AND runner='wine'; " | while read -r i; do
	F="${i:0:1}"
	GAME="${i//-/ }"
	mkdir -p "$WD/ROMs/$F"
	touch "$WD/ROMs/$F/$GAME.txt"
done
lutris_query_pga.sh "SELECT slug FROM games WHERE platform='Linux' AND runner='linux'; " | while read -r i; do
	F="${i:0:1}"
	GAME="${i//-/ }"
	mkdir -p "$WD/ROMs/$F"
	touch "$WD/ROMs/$F/$GAME.txt"
done
lutris_query_pga.sh "SELECT slug FROM games WHERE platform='Linux' AND runner='zdoom'; " | while read -r i; do
	F="${i:0:1}"
	GAME="${i//-/ }"
	mkdir -p "$WD/ROMs/$F"
	touch "$WD/ROMs/$F/$GAME.txt"
done
lutris_query_pga.sh "SELECT slug FROM games WHERE platform='MS-DOS' AND runner='dosbox'; " | while read -r i; do
	F="${i:0:1}"
	GAME="${i//-/ }"
	mkdir -p "$WD/ROMs/$F"
	touch "$WD/ROMs/$F/$GAME.txt"
done
lutris_query_pga.sh "SELECT slug FROM games WHERE platform='Web' AND runner='web'; " | while read -r i; do
	F="${i:0:1}"
	GAME="${i//-/ }"
	mkdir -p "$WD/ROMs/$F"
	touch "$WD/ROMs/$F/$GAME.txt"
done
