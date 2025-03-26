#!/bin/bash
# $1  "/path/to/symlink/to/A Real Mame Rom.zip"
# Call mame with appropritate shorname from pointed file:

RP=$(realpath "$@")
BN=$(basename "$RP" .zip)

\pushd '/storage/nas/SSD_2TB2/Games/MAME/MAME-current/DIST/mame-current/current' || exit 1
./mame -snapname %g "$BN"
