#!/bin/bash
RP="$(realpath "$0")"
WD="$(dirname "$RP")"

LU="${HOME}/.local/share/lutris/coverart"

\pushd "${HOME}/ES-DE/downloaded_media/PC Games - Lutris/covers/ROMs" &>/dev/null || exit

find $LU -type f -name "*.jpg" | sed "s;$LU;;" | while read -r R; do

	LOC="$WD/${R//-/ }"
	if [ ! -r "$LOC" ]; then
		echo -n "Importing $R -> "
		cp "$LU/$R" "$LOC"
		echo $?
	fi
done


