#!/bin/bash

LU="${HOME}/.local/share/lutris/coverart"

\pushd "${HOME}/ES-DE/downloaded_media/PC Games - Lutris/covers/ROMs" ||  exit 2

find "$LU" -type f -name "*.jpg" | while read -r R; do
	echo "R = $R"
	LOC="${R//-/ }"
		echo -n "Importing $R -> "
		cp --update "$LU/$R" "$LOC"
		echo $?

done


