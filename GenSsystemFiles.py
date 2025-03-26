#!/usr/bin/env python3
import os
import sys

from typing import TextIO

#=== Top path for most games
NI_TOPD = "/storage/NVME_4TB1/Games/No-Intro ROM Set/"

#=== Where some emulators, configs, wrapper, assets etc. are stored:
EMUDIR = "/storage/GAMES_MASTER"

#=== Runners
# yay -S cemu
CEMU = "cemu"

# yay -S mandarine-git
MANDARINE ="/usr/bin/mandarine"

# yay -S dolphin-emu
DOL = "/usr/bin/dolphin-emu"

EMULATOR_SUPERMODEL = f"{EMUDIR}/EMULATORS/SUPERMODEL/start-supermodel.sh"
FLYCAST = "flycast" # alias to /usr/bin/flycast

# pacman -S hatari
HATARI="/usr/bin/hatari"
HATARI_TOS_IMG = f"{os.environ.get('HOME')}/.hatari/bios/tos.img"

# # yay -S love-git
# LOVE = "/usr/bin/love-git" // having issues with this one ATM

# pacman -S lutris
LUTRIS = f"{os.environ.get('HOME')}/ES-DE/run-by-slug_esde.sh"

# LUTRIS_SUPERMODEL = f"{LUTRIS} supermodel"
# yay -S supermodel-git
SUPERMODEL="/usr/bin/supermodel" # A Sega Model 3 Arcade Emulator
LUTRIS_MODEL2 = f"{EMUDIR}/EMULATORS/LUTRIS/MODEL2/runwithargs.sh" # support for argument via "lutris -b" script

# pacman -S mame
MAME = "mame" # wrapper in ~/bin if exists, or use /usr/bin otherwise
# Where are your 'cfg', 'ini', 'roms' folders or links:
MAMEDIR = "/storage/nas/SSD_2TB2/Games/MAME/MAME-current/DIST/mame-current/current"
# MAME's software list:
MAMESL = "/storage/nas/SSD_2TB2/Games/MAME/MAME-current/SL/mame-sl"
MAME_RUN_FROM_FULLNAME = f"{os.environ.get('HOME')}/ES-DE/mame_run_from_fullname.sh" # wrapper

# yay -S pcsx2-latest-bin
PCSX2 = "/usr/bin/pcsx2"

# PSP = f"{os.environ.get('HOME')}/bin/ppsspp-flatpak-runner.sh"
# yay -S ppsspp-git
PSP = "/usr/bin/PPSSPPSDL"

# RA = "org.libretro.RetroArch" // for flatpak
# pacman -S retroarch
RA = "/usr/bin/retroarch"
# RA_CORESDIR = f"{EMUDIR}/RETROARCH/cores"

#RPCS3 = f"{os.environ.get('HOME')}/bin/rpcs3-flatpak-runner.sh"
# yay -S rpcs3-latest-bin
RPCS3 = "/usr/bin/rpcs3"

# yay -S ryujinx sudachi-bin torzu-git
RYUJINX = "ryujinx" # works also with appimage installed via bauh
SUDACHI = "/usr/bin/sudachi"
TORZU = "/usr/bin/yuzu" # replaces yuzu / suyu

# ADD VITA3K
# yay -S vita3k-git
VITA3K = "/usr/bin/vita3k"

SYSTEMS = (
	(
	"nes", "Nintendo - Nintendo Entertainment System", f"{NI_TOPD}//0-Overlay/Nintendo - Nintendo Entertainment System/ROMs_NO-INTRO/_NES Unheadered Restricted",
	".nes .NES .zip",
	f"{RA} -L mesen_libretro.so %ROM%",
	"Libretro Nintendo Entertainment System", "nes", "nes"),
	
	(
	"oric", "Tangerine Computer Systems - Oric", f"{NI_TOPD}/0-Overlay//Tangerine Computer Systems - Oric/ROMS",
	".dsk .DSK .ort .ORT .tap .TAP .wav .WAV .zip",
	f"{MAME} orica -window -rompath '{NI_TOPD}/0-Overlay/Tangerine Computer Systems - Oric/ROMS' -autoboot_command \"CLOAD \\\"\\\"\\n\" -autoboot_delay 5 -cass '%ROM%'",
	"MAME Oric", "oric", "oric"),
	
	(
	"3do", "3DO Interactive Multiplayer",  f"{NI_TOPD}/0-Overlay/3DO Interactive Multiplayer/ROMs",
	".iso .bin .chd .cue .zip",
	f"{RA} -L opera_libretro.so %ROM%",
	"Libretro 3DO", "3do", "3do"),
	
	(
	"amstradcpc", "Amstrad CPC", f"{NI_TOPD}/Amstrad - CPC",
	".cdt .CDT .cpr .CPR .dsk .DSK .kcr .KCR .m3u .M3U .sna .SNA .tap .TAR .voc .VOC .7z .7Z .zip .ZIP",
	f"{MAME} cpc6128 -flop1 %ROM%",
	"MAME amstradcpc", "amstradcpc", "amstradcpc"),
	
	(
	"atari2600", "Atari 2600", f"{NI_TOPD}/Atari - 2600",
	".a26 .A26 .bin .BIN .7z .7Z .zip .ZIP",
	f"{RA} -L stella_libretro.so %ROM%",
	"Libretro atari2600", "atari2600", "atari2600"),
	
	(
	"atari5200", "Atari 5200", f"{NI_TOPD}/Atari - 5200",
	".a52 .A52 .atr .ATR .atx .ATX .bin .BIN .car .CAR .cas .CAS .cdm .CDM .rom .ROM .xex .XEX .xfd .XFD .7z .7Z .zip .ZIP",
	f"{RA} -L atari800_libretro.so %ROM%",
	"Libretro atari5200", "atari5200", "atari5200"),
	
	(
	"atari7800", "Atari 7800", f"{NI_TOPD}/Atari - 7800",
	".a78 .A78 .bin .BIN .7z .7Z .zip .ZIP",
	f"{RA} -L stella_libretro.so %ROM%",
	"Libretro stella", "atari7800", "atari7800"),
	
	(
	"atarijaguar", "Atari Jaguar", f"{NI_TOPD}/Atari - Jaguar",
	".abs .ABS .bin .BIN .cdi .CDI .cof .COF .cue .CUE .j64 .J64 .jag .JAG .prg .PRG .rom .ROM .7z .7Z .zip .ZIP",
	f"{RA} -L virtualjaguar_libretro.so %ROM%",
	"Libretro atarijaguar", "atarijaguar", "atarijaguar"),
	
	(
	"atarilynx", "Atari Lynx", f"{NI_TOPD}/Atari - Lynx",
	".lnx .LNX .o .O .7z .7Z .zip .ZIP",
	f"{RA} -L mednafen_lynx_libretro.so %ROM%",
	"Libretro atarilynx", "atarilynx", "atarilynx"),
	
	(
	"atarist", "Atari ST", f"{NI_TOPD}/Atari - ST",
	".st .ST .msa .MSA .stx .STX .dim .DIM .ipf .IPF .m3u .M3U .7z .7Z .zip .ZI",
	# f"{HATARI} --tos '{HATARI_TOS_IMG}' --window --zoom 2 --borders false --statusbar true --joy0 none --joy1 real --disk-a %ROM% --disk-b 'NONE'  --fastfdc 1 --fast-boot 1",
	f"{HATARI} --tos '{HATARI_TOS_IMG}' --window --borders false --statusbar true --joy0 none --joy1 real --disk-a %ROM% --disk-b 'NONE'  --fastfdc 1 --fast-boot 1",
	"Standalone Hatari", "atarist", "atarist"),
	
	(
	"wonderswan", "Bandai - WonderSwan", f"{NI_TOPD}/Bandai - WonderSwan",
	".pc2 .PC2 .ws .WS .7z .7Z .zip .ZIP",
	f"{RA} -L mednafen_wswan_libretro.so %ROM%",
	"Libretro wonderswan", "wonderswan", "wonderswan"),
	
	(
	"wonderswancolor", "Bandai - WonderSwan Color", f"{NI_TOPD}/Bandai - WonderSwan Color",
	".pc2 .PC2 .ws .WS .wsc .WSC .7z .7Z .zip .ZIP",
	f"{RA} -L mednafen_wswan_libretro.so %ROM%",
	"Libretro wonderswancolor", "wonderswancolor", "wonderswancolor"),
	
	(
	"pocketchallengev2", "Benesse - Pocket Challenge V2", f"{NI_TOPD}/Benesse - Pocket Challenge V2",
	".pc2 .PC2 .ws .WS .wsc .WSC .7z .7Z .zip .ZIP",
	f"{RA} -L mednafen_wswan_libretro.so %ROM%",
	"Libretro pocketchallengev2", "wonderswan", "pocketchallengev2"), # this model is compat w/ wonderswan,

	(
	"pocketchallengew", "Benesse - Pocket Challenge W", f"{NI_TOPD}/Benesse - Pocket Challenge W",
	".pc2 .PC2 .ws .WS .wsc .WSC .7z .7Z .zip .ZIP",
	f"{MAME} pockchal -cart1 %ROM%",
	"Libretro pocketchallengew", "pocketchallengew", "pocketchallengew"), # this one is not.
	
	(
	"casioloopy", "Casio - Loopy", f"{NI_TOPD}/Casio - Loopy",
	".bin .zip",
	f"{MAME} casloopy -cart %ROM%",
	"MAME casioloopy", "casioloopy", "casioloopy"),
	
	(
	"casiopv1000", "Casio - PV-1000", f"{NI_TOPD}/Casio - PV-1000",
	".bin .zip",
	f"{MAME} pv1000 -cart %ROM%",
	"MAME casiopv1000", "casiopv1000", "casiopv1000"),
	
	(
	"colecovision", "Coleco - ColecoVision", f"{NI_TOPD}/Coleco - ColecoVision",
	".bin .BIN .cas .CAS .col .COL .cv .CV .dsk .DSK .m3u .M3U .mx1 .MX1 .mx2 .MX2 .ri .RI .rom .ROM .sc .SC .sg .SG .7z .7Z .zip .ZIP",
	f"{RA} -L gearcoleco_libretro.so %ROM%",
	"Libretro colecovision", "colecovision", "colecovision"),
	
	(
	"commodore64", "Commodore 64", f"{NI_TOPD}/Commodore - 64",
	".bin .BIN .cmd .CMD .crt .CRT .d2m .D2M .d4m .D4M .d64 .D64 .d6z .D6Z .d71 .D71 .d7z .D7Z .d80 .D80 .d81 .D81 .d82 .D82 .d8z .D8Z .g41 .G41 .g4z .G4Z .g64 .G64 .g6z .G6Z .gz .GZ .lnx .LNX .m3u .M3U .nbz .NBZ .nib .NIB .p00 .P00 .prg .PRG .t64 .T64 .tap .TAP .vfl .VFL .vsf .VSF .x64 .X64 .x6z .X6Z .7z .7Z .zip .ZIP",
	f"{RA} -L vice_x64sc_libretro.so %ROM%",
	"Libretro commodore64", "c64", "c64"),

	(
	"commodoreamiga", "Commodore Amiga", f"{NI_TOPD}/Commodore - Amiga",
	".adf .ADF .adz .ADZ .ccd .CCD .chd .CHD .cue .CUE .dms .DMS .fdi .FDI .hdf .HDF .hdz .HDZ .ipf .IPF .iso .ISO .lha .LHA .m3u .M3U .mds .MDS .nrg .NRG .rp9 .RP9 .uae .UAE .7z .7Z .zip .ZIP",
	f"{RA} -L puae2021_libretro.so %ROM%",
	"Libretro commodoreamiga", "amiga", "amiga"),
	
	(
	"commodoreplus4", "Commodore Plus-4", f"{NI_TOPD}/Commodore - Plus-4",
	".bin .BIN .cmd .CMD .crt .CRT .d2m .D2M .d4m .D4M .d64 .D64 .d6z .D6Z .d71 .D71 .d7z .D7Z .d80 .D80 .d81 .D81 .d82 .D82 .d8z .D8Z .g41 .G41 .g4z .G4Z .g64 .G64 .g6z .G6Z .gz .GZ .lnx .LNX .m3u .M3U .nbz .NBZ .nib .NIB .p00 .P00 .prg .PRG .t64 .T64 .tap .TAP .vfl .VFL .vsf .VSF .x64 .X64 .x6z .X6Z .7z .7Z .zip .ZIP",
	f"{RA} -L vice_xplus4_libretro.so %ROM%",
	"Libretro commodoreplus4", "plus4", "plus4"),
	
	(
	"commodorevic20", "Commodore VIC-20", f"{NI_TOPD}/Commodore - VIC-20",
	".bin .BIN .cmd .CMD .crt .CRT .d2m .D2M .d4m .D4M .d64 .D64 .d6z .D6Z .d71 .D71 .d7z .D7Z .d80 .D80 .d81 .D81 .d82 .D82 .d8z .D8Z .g41 .G41 .g4z .G4Z .g64 .G64 .g6z .G6Z .gz .GZ .lnx .LNX .m3u .M3U .nbz .NBZ .nib .NIB .p00 .P00 .prg .PRG .t64 .T64 .tap .TAP .vfl .VFL .vsf .VSF .x64 .X64 .x6z .X6Z .7z .7Z .zip .ZIP",
	f"{RA} -L vice_xvic_libretro.so %ROM%",
	"Libretro", "vic20", "vic20"),

	(
	"advision", "Entex - Adventure Vision", f"{NI_TOPD}/Entex - Adventure Vision",
	".bin .zip .ZIP",
	f"{MAME} advision -cart %ROM%",
	"MAME advision", "advision", "advision"),

	# (
	# "vpinball", "Visual Pinball", f"{NI_TOPD}/Visual Pinball",
	# ".vpt .VPT .vpx .VPX",
	# "%EMULATOR_VISUAL-PINBALL% -Minimized -Play %ROM%",
	# 'Libretro vpinball', "vpinball", "vpinball"),

	# (
	# "lowresnx", "LowRes NX Fantasy Console", f"{NI_TOPD}/LowRes NX Fantasy Console",
	# ".nx .NX",
	# "{RA} -L lowresnx_libretro.so %ROM%",
	# 'Libretro lowresnx', "lowresnx", "lowresnx"),

	# (
	# "nds", "Nintendo DS", f"{NI_TOPD}/Nintendo DS",
	# ".app .APP .bin .BIN .nds .NDS .7z .7Z .zip .ZIP",
	# "{RA} -L desmume_libretro.so %ROM%",
	# 'Libretro nds', "nds", "nds"),

	(
	"wiiu", "Nintendo - Wii U", f"{NI_TOPD}/0-Overlay/Nintendo - Wii U/ROMs",
	".rpx .RPX .wua .WUA .wud .WUD .wux .WUX",
	f"{CEMU} -g %ROM%".format(CEMU = CEMU),
	"Standalone wiiu", "wiiu", "wiiu"),

	# (
	# "megadrivejp", "Sega Mega Drive", f"{NI_TOPD}/Sega Mega Drive",
	# ".32x .32X .68k .68K .bin .BIN .bms .BMS .chd .CHD .cue .CUE .gen .GEN .gg .GG .iso .ISO .m3u .M3U .md .MD .mdx .MDX .sg .SG .sgd .SGD .smd .SMD .sms .SMS .7z .7Z .zip .ZIP",
	# "{RA} -L genesis_plus_gx_libretro.so %ROM%",
	# "Libretro megadrivejp", "megadrive", "megadrivejp"),

	# (
	# "ports", "Ports", f"{NI_TOPD}/Ports",
	# ".AppImage .desktop .exe .EXE .game .GAME .phd .PHD .psx .PSX .sh",
	# "%ENABLESHORTCUTS% %EMULATOR_OS-SHELL% %ROM%",
	# 'Libretro ports', "", "ports"),

	# (
	# "lutro", "Lutro Game Engine", f"{NI_TOPD}/Lutro Game Engine",
	# ".lua .LUA .lutro .LUTRO .7z .7Z .zip .ZIP",
	# "{RA} -L lutro_libretro.so %ROM%",
	# 'Libretro lutro', "lutro", "lutro"),

	# (
	# "sega32xna", "Sega Genesis 32X", f"{NI_TOPD}/Sega Genesis 32X",
	# ".32x .32X .68k .68K .bin .BIN .cue .CUE .gen .GEN .iso .ISO .md .MD .smd .SMD .sms .SMS .7z .7Z .zip .ZIP",
	# "{RA} -L picodrive_libretro.so %ROM%",
	# 'Libretro sega32xna', "sega32x", "sega32xna"),

	(
	"segapico", "Sega - Pico", f"{NI_TOPD}/Sega - Pico",
	".md .MD .bin .BIN .7z .7Z .zip .ZIP",
	f"{RA} -L picodrive_libretro.so %ROM%",
	"Libretro segapico", "pico", "segapico"),

	(
	"sega32x", "Sega - 32X", f"{NI_TOPD}/Sega - 32X",
	".32x .32X .68k .68K .bin .BIN .cue .CUE .gen .GEN .iso .ISO .md .MD .smd .SMD .sms .SMS .7z .7Z .zip .ZIP",
	f"{RA} -L picodrive_libretro.so %ROM%",
	"Libretro sega32xna", "sega32x", "sega32xna"),

	# (
	# "symbian", "Symbian", f"{NI_TOPD}/Symbian",
	# ".sis .SIS .sisx .SISX .symbian",
	# "%EMULATOR_EKA2L1% --fullscreen --device RH-29 --run "%BASENAME%"",
	# 'Libretro symbian', "ngage", "symbian"),

	# (
	# "laserdisc", "LaserDisc Games", f"{NI_TOPD}/LaserDisc Games",
	# ".daphne .ogv .OGV .singe .7z .7Z .zip .ZIP",
	# "%EMULATOR_HYPSEUS-SINGE% %BASENAME% vldp -framefile %GAMEDIR%/%BASENAME%.txt %INJECT%=%BASENAME%.commands",
	# 'Libretro laserdisc', "", "laserdisc"),

	(
	"msx2", "Microsoft - MSX", f"{NI_TOPD}/Microsoft - MSX",
	".cas .CAS .col .COL .di1 .DI1 .di2 .DI2 .dmk .DMK .dsk .DSK .fd1 .FD1 .fd2 .FD2 .m3u .M3U .mx1 .MX1 .mx2 .MX2 .ogv .OGV .ri .RI .rom .ROM .sc .SC .sg .SG .wav .WAV .xsa .XSA .7z .7Z .zip .ZIP",
	f"{RA} -L bluemsx_libretro.so %ROM%",
	"Libretro msx2", "msx2", "msx2"),

	# (
	# "atomiswave", "Sammy Corporation Atomiswave", f"{NI_TOPD}/Sammy Corporation Atomiswave",
	# ".bin .BIN .dat .DAT .elf .ELF .lst .LST .7z .7Z .zip .ZIP",
	# "{RA} -L flycast_libretro.so %ROM%",
	# 'Libretro atomiswave', "arcade", "atomiswave"),

	(
	"wii", "Nintendo - Wii", f"{NI_TOPD}/0-Overlay/Nintendo - Wii",
	".ciso .CISO .dff .DFF .dol .DOL .elf .ELF .gcm .GCM .gcz .GCZ .iso .ISO .json .JSON .m3u .M3U .rvz .RVZ .tgc .TGC .wad .WAD .wbfs .WBFS .wia .WIA .7z .7Z .zip .ZIP",
	f"{DOL} %ROM%",
	"Standalone Dolphin Wii", "wii", "wii"),

	# (
	# "msxturbor", "MSX Turbo R", f"{NI_TOPD}/MSX Turbo R",
	# ".cas .CAS .col .COL .di1 .DI1 .di2 .DI2 .dmk .DMK .dsk .DSK .fd1 .FD1 .fd2 .FD2 .m3u .M3U .mx1 .MX1 .mx2 .MX2 .ogv .OGV .ri .RI .rom .ROM .sc .SC .sg .SG .wav .WAV .xsa .XSA .7z .7Z .zip .ZIP",
	# "{RA} -L bluemsx_libretro.so %ROM%",
	# 'Libretro msxturbor', "msxturbor", "msxturbor"),

	# (
	# "model2", "Sega Model 2", f"{NI_TOPD}/Sega Model 2",
	# ".7z .7Z .zip .ZIP",
	# "{RA} -L mame_libretro.so %ROM%",
	# 'Libretro model2', "arcade", "model2"),

	(
	"model2", "Sega Model 2", f"{NI_TOPD}/0-Overlay/Sega - Model 2",
	".7z .7Z .zip .ZIP",
	f"{LUTRIS_MODEL2} %BASENAME%",
	"Lutris model2", "arcade", "model2"),

	(
	"dos", "DOS (PC)", f"{NI_TOPD}/0-Overlay/DOS (PC)",
	".bat .BAT .com .COM .conf .CONF .cue .CUE .dosz .DOSZ .exe .EXE .iso .ISO .7z .7Z .zip .ZIP",
	f"{RA} -L dosbox_pure_libretro.so %ROM%",
	"Libretro dos", "dos", "dos"),

	# (
	# "atari800", "Atari 800", f"{NI_TOPD}/Atari 800",
	# ".a52 .A52 .atr .ATR .atx .ATX .bin .BIN .car .CAR .cas .CAS .cdm .CDM .rom .ROM .xex .XEX .xfd .XFD .7z .7Z .zip .ZIP",
	# "{RA} -L atari800_libretro.so %ROM%",
	# 'Libretro atari800', "atari800", "atari800"),

	(
	"sg-1000", "Sega - SG-1000", f"{NI_TOPD}/Sega - SG-1000",
	".68k .68K .bin .BIN .bms .BMS .chd .CHD .cue .CUE .gen .GEN .gg .GG .iso .ISO .m3u .M3U .md .MD .mdx .MDX .ri .RI .rom .ROM .sg .SG .sgd .SGD .smd .SMD .sms .SMS .7z .7Z .zip .ZIP",
	f"{RA} -L genesis_plus_gx_libretro.so %ROM%",
	"Libretro sg-1000", "sg-1000", "sg-1000"),

	# (
	# "satellaview", "Nintendo Satellaview", f"{NI_TOPD}/Nintendo Satellaview",
	# ".bml .BML .bs .BS .fig .FIG .sfc .SFC .smc .SMC .swc .SWC .st .ST .7z .7Z .zip .ZIP",
	# "{RA} -L snes9x_libretro.so %ROM%",
	# 'Libretro satellaview', "satellaview", "satellaview"),

	# (
	# "sega32x", "Sega Mega Drive 32X", f"{NI_TOPD}/Sega Mega Drive 32X",
	# ".32x .32X .68k .68K .bin .BIN .cue .CUE .gen .GEN .iso .ISO .md .MD .smd .SMD .sms .SMS .7z .7Z .zip .ZIP",
	# "{RA} -L picodrive_libretro.so %ROM%",
	# 'Libretro sega32x', "sega32x", "sega32x"),

	(
	"scv", "Epoch - Super Cassette Vision", f"{NI_TOPD}/Epoch - Super Cassette Vision",
	".0 .bin .BIN .7z .7Z .zip .ZIP",
	f"{MAME} scv -cart \"%ROMRAW%\"",
	"MAME scv", "scv", "scv"),

	# (
	# "samcoupe", "MGT SAM Coupé", f"{NI_TOPD}/MGT SAM Coupé",
	# ".dsk .DSK .mgt .MGT .sad .SAD .sbt .SBT .7z .7Z .zip .ZIP",
	# "%EMULATOR_SIMCOUPE% %ROM%",
	# 'Libretro samcoupe', "samcoupe", "samcoupe"),

	(
	"cps1", "Capcom - Play System I", f"{NI_TOPD}/0-Overlay/Capcom - Play System I",
	".7z .7Z .zip .ZIP",
	f"{MAME}  %BASENAME%",
	"MAME cps1", "arcade", "cps1"),

	# (
	# "tg-cd", "NEC TurboGrafx-CD", f"{NI_TOPD}/NEC TurboGrafx-CD",
	# ".ccd .CCD .chd .CHD .cue .CUE .img .IMG .iso .ISO .m3u .M3U .pce .PCE .sgx .SGX .toc .TOC .7z .7Z .zip .ZIP",
	# "{RA} -L mednafen_pce_libretro.so %ROM%",
	# 'Libretro tg-cd', "pcenginecd", "tg-cd"),

	# (
	# "wasm4", "WASM-4 Fantasy Console", f"{NI_TOPD}/WASM-4 Fantasy Console",
	# ".wasm .WASM",
	# "{RA} -L wasm4_libretro.so %ROM%",
	# 'Libretro wasm4', "wasm4", "wasm4"),

	# (
	# "amiga1200", "Commodore Amiga 1200", f"{NI_TOPD}/Commodore Amiga 1200",
	# ".adf .ADF .adz .ADZ .ccd .CCD .chd .CHD .cue .CUE .dms .DMS .fdi .FDI .hdf .HDF .hdz .HDZ .ipf .IPF .iso .ISO .lha .LHA .m3u .M3U .mds .MDS .nrg .NRG .rp9 .RP9 .uae .UAE .7z .7Z .zip .ZIP",
	# "{RA} -L puae_libretro.so %ROM%",
	# 'Libretro amiga1200', "amiga", "amiga1200"),

	(
	"psp", "Sony - PlayStation Portable", f"{NI_TOPD}/0-Overlay/Sony - PlayStation Portable",
	".chd .CHD .cso .CSO .elf .ELF .iso .ISO .pbp .PBP .prx .PRX .7z .7Z .zip .ZIP",
	f"{PSP} %ROM%",
	"Standalone psp", "psp", "psp"),

	(
	"ngpc", "SNK - Neo Geo Pocket Color", f"{NI_TOPD}/SNK - Neo Geo Pocket Color",
	".ngc .NGC .ngp .NGP .ngpc .NGPC .npc .NPC .7z .7Z .zip .ZIP",
	f"{RA} -L mednafen_ngp_libretro.so %ROM%",
	"Libretro ngpc", "ngpc", "ngpc"),

	# (
	# "msx1", "MSX1", f"{NI_TOPD}/MSX1",
	# ".cas .CAS .col .COL .di1 .DI1 .di2 .DI2 .dmk .DMK .dsk .DSK .fd1 .FD1 .fd2 .FD2 .m3u .M3U .mx1 .MX1 .mx2 .MX2 .ogv .OGV .ri .RI .rom .ROM .sc .SC .sg .SG .wav .WAV .xsa .XSA .7z .7Z .zip .ZIP",
	# "{RA} -L bluemsx_libretro.so %ROM%",
	# 'Libretro msx1', "msx", "msx1"),

	# (
	# "fpinball", "Future Pinball", f"{NI_TOPD}/Future Pinball",
	# ".fpt .FPT",
	# "PLACEHOLDER %ROM%",
	# 'Libretro fpinball', "fpinball", "fpinball"),

	# (
	# "naomi", "Sega NAOMI", f"{NI_TOPD}/Sega NAOMI",
	# ".bin .BIN .dat .DAT .elf .ELF .lst .LST .7z .7Z .zip .ZIP",
	# "{RA} -L flycast_libretro.so %ROM%",
	# 'Libretro naomi', "arcade", "naomi"),

	(
	"gamecom", "Tiger - Game.com", f"{NI_TOPD}/Tiger - Game.com",
	".tgc .TGC .7z .7Z .zip .ZIP",
	f"{MAME} gamecom  -cartridge1 \"%ROMRAW%\"",
	"Libretro gamecom", "gamecom", "gamecom"),

	( # presse F3 then Q after boot to clear display
	  # check how to run properly 
	"visicom", "Toshiba - Visicom", f"{NI_TOPD}/Toshiba - Visicom",
	".bin .BIN .7z .7Z .zip .ZIP",
	f"{MAME} visicom  -cartridge1 \"%ROMRAW%\"",
	"Libretro visicom", "visicom", "visicom"),

	# (
	# "atarixe", "Atari XE", f"{NI_TOPD}/Atari XE",
	# ".a52 .A52 .atr .ATR .atx .ATX .bin .BIN .cas .CAS .cdm .CDM .xex .XEX .xfd .XFD .7z .7Z .zip .ZIP",
	# "{RA} -L atari800_libretro.so %ROM%",
	# 'Libretro atarixe', "atarixe", "atarixe"),

	# (
	# "openbor", "OpenBOR Game Engine", f"{NI_TOPD}/OpenBOR Game Engine",
	# ".AppImage",
	# "%STARTDIR%=%GAMEDIR% %EMULATOR_OS-SHELL% -c "%ROM%"",
	# 'Libretro openbor', "openbor", "openbor"),

	(
	"cps3", "Capcom Play - System III", f"{NI_TOPD}/0-Overlay/Capcom - Play System III",
	".7z .7Z .zip .ZIP",
	f"{MAME} %BASENAME%",
	"MAME cps3", "arcade", "cps3"),

	(
	"dreamcast", "Sega Dreamcast", f"{NI_TOPD}/0-Overlay/Sega - Dreamcast",
	".cdi .CDI .chd .CHD .cue .CUE .dat .DAT .elf .ELF .gdi .GDI .iso .ISO .lst .LST .m3u .M3U .7z .7Z .zip .ZIP",
	f"{FLYCAST} %ROM%",
	"Standalone dreamcast", "dreamcast", "dreamcast"),

	# (
	# "moto", "Thomson MO/TO Series", f"{NI_TOPD}/Thomson MO/TO Series",
	# ".fd .FD .k7 .K7 .m5 .M5 .m7 .M7 .rom .ROM .sap .SAP .7z .7Z .zip .ZIP",
	# "{RA} -L theodore_libretro.so %ROM%",
	# 'Libretro moto', "moto", "moto"),

	# (
	# "chailove", "ChaiLove Game Engine", f"{NI_TOPD}/ChaiLove Game Engine",
	# ".chai .CHAI .chailove .CHAILOVE .7z .7Z .zip .ZIP",
	# "{RA} -L chailove_libretro.so %ROM%",
	# 'Libretro chailove', "love", "chailove"),

	# (
	# "megaduck", "Creatronic Mega Duck", f"{NI_TOPD}/Creatronic Mega Duck",
	# ".bin .BIN .7z .7Z .zip .ZIP",
	# "{RA} -L sameduck_libretro.so %ROM%",
	# 'Libretro megaduck', "megaduck", "megaduck"),

	 (
	"ps3", "Sony - PlayStation 3", f"{NI_TOPD}/0-Overlay/Sony - PlayStation 3/ROMs",
	".desktop .ps3 .PS3 .ps3dir .PS3DIR",
	f"{RPCS3} %ROM%",
	"Standalone ps3", "ps3", "ps3"),

	# (
	# "flash", "Adobe Flash", f"{NI_TOPD}/Adobe Flash",
	# ".swf .SWF",
	# "%EMULATOR_RUFFLE% --fullscreen %ROM%",
	# 'Libretro flash', "flash", "flash"),

	# (
	# "ps4", "Sony PlayStation 4", f"{NI_TOPD}/Sony PlayStation 4",
	# ".7z .7Z .zip .ZIP",
	# "PLACEHOLDER %ROM%",
	# 'Libretro ps4', "ps4", "ps4"),

	# (
	# "snesna", "Nintendo SNES (Super Nintendo)", f"{NI_TOPD}/Nintendo SNES (Super Nintendo)",
	# ".bin .BIN .bml .BML .bs .BS .bsx .BSX .dx2 .DX2 .fig .FIG .gd3 .GD3 .gd7 .GD7 .mgd .MGD .sfc .SFC .smc .SMC .st .ST .swc .SWC .7z .7Z .zip .ZIP",
	# "{RA} -L snes9x_libretro.so %ROM%",
	# 'Libretro snesna', "snes", "snesna"),

	# (
	# "xbox", "Microsoft Xbox", f"{NI_TOPD}/Microsoft Xbox",
	# ".iso .ISO",
	# "%INJECT%=%BASENAME%.esprefix %EMULATOR_XEMU% -dvd_path %ROM%",
	# 'Libretro xbox', "xbox", "xbox"),

	# (
	# "sufami", "Bandai SuFami Turbo", f"{NI_TOPD}/Bandai SuFami Turbo",
	# ".bml .BML .bs .BS .fig .FIG .sfc .SFC .smc .SMC .st .ST .7z .7Z .zip .ZIP",
	# "{RA} -L snes9x_libretro.so %ROM%",
	# 'Libretro sufami', "sufami", "sufami"),

	# (
	# "quake", "Quake", f"{NI_TOPD}/Quake",
	# ".desktop .pak .PAK .pk3 .PK3 .sh",
	# "{RA} -L tyrquake_libretro.so %ROM%",
	# 'Libretro quake', "", "quake"),

	(
	"intellivision", "Mattel - Intellivision", f"{NI_TOPD}/Mattel - Intellivision",
	".bin .BIN .int .INT .rom .ROM .7z .7Z .zip .ZIP",
	f"{RA} -L freeintv_libretro.so %ROM%",
	"Libretro intellivision", "intellivision", "intellivision"),

	(
	"gmaster", "Hartung - Game Master", f"{NI_TOPD}/Hartung - Game Master",
	".bin .BIN .7z .7Z .zip .ZIP",
	f"{MAME} gmaster -cart \"%ROMRAW%\"",
	"MAME gmaster", "gmaster", "gmaster"),

	(
	"beena", "Sega - Beena", f"{NI_TOPD}/Sega - Beena",
	".bin .BIN .7z .7Z .zip .ZIP",
	f"{MAME} beena -cart \"%ROMRAW%\"",
	"MAME beena", "beena", "beena"),

	# (  NON WORKING 
	# "picno", "Konami - Picno", f"{NI_TOPD}/Konami - Picno",
	# ".bin .BIN .7z .7Z .zip .ZIP",
	# "{MAME} picno -cart \"%ROMRAW%\"",
	# 'MAME picno', "picno", "picno"),

	# LeapFrog - LeapPad / NON WORKING; only 1 game
	# LeapFrog - Leapster Learning Game System / NON WORKING

	# (
	# "windows9x", "Microsoft Windows 9x", f"{NI_TOPD}/Microsoft Windows 9x",
	# ".AppImage .bat .BAT .desktop .dosz .DOSZ .sh .7z .7Z .zip .ZIP",
	# "%STARTDIR%=%GAMEDIR% %EMULATOR_DOSBOX-X% -defaultdir %GAMEDIR% %ROM%",
	# 'Libretro windows9x', "pcwindows", "windows9x"),

	# (
	# "to8", "Thomson TO8", f"{NI_TOPD}/Thomson TO8",
	# ".fd .FD .k7 .K7 .m5 .M5 .m7 .M7 .rom .ROM .sap .SAP .7z .7Z .zip .ZIP",
	# "{RA} -L theodore_libretro.so %ROM%",
	# 'Libretro to8', "moto", "to8"),

	# (
	# "doom", "Doom", f"{NI_TOPD}/Doom",
	# ".desktop .iwad .IWAD .pk4 .PK4 .pwad .PWAD .sh .wad .WAD",
	# "{RA} -L prboom_libretro.so %ROM%",
	# 'Libretro doom', "", "doom"),

	# (
	# "sgb", "Nintendo Super Game Boy", f"{NI_TOPD}/Nintendo Super Game Boy",
	# ".gb .GB .gbc .GBC .sgb .SGB .7z .7Z .zip .ZIP",
	# "{RA} -L mesen-s_libretro.so %ROM%",
	# 'Libretro sgb', "sgb", "sgb"),

	# (
	# "saturnjp", "Sega Saturn", f"{NI_TOPD}/Sega Saturn",
	# ".bin .BIN .ccd .CCD .chd .CHD .cue .CUE .iso .ISO .m3u .M3U .mds .MDS .toc .TOC .7z .7Z .zip .ZIP",
	# "{RA} -L mednafen_saturn_libretro.so %ROM%",
	# 'Libretro saturnjp', "saturn", "saturnjp"),

	# (
	# "amiga", "Commodore Amiga", f"{NI_TOPD}/Commodore Amiga",
	# ".adf .ADF .adz .ADZ .ccd .CCD .chd .CHD .cue .CUE .dms .DMS .fdi .FDI .hdf .HDF .hdz .HDZ .ipf .IPF .iso .ISO .lha .LHA .m3u .M3U .mds .MDS .nrg .NRG .rp9 .RP9 .uae .UAE .7z .7Z .zip .ZIP",
	# "{RA} -L puae_libretro.so %ROM%",
	# 'Libretro amiga', "amiga", "amiga"),

	# (
	# "macintosh", "Apple Macintosh", f"{NI_TOPD}/Apple Macintosh",
	# ".dsk .DSK .game .GAME",
	# "{MAME} -rompath %GAMEDIR%\;%ROMPATH%/macintosh macse -flop1 %ROM%",
	# 'Libretro macintosh', "macintosh", "macintosh"),

	(
	"psx", "Sony - PlayStation", f"{NI_TOPD}/0-Overlay/Sony - PlayStation",
	".bin .BIN .cbn .CBN .ccd .CCD .chd .CHD .cue .CUE .ecm .ECM .exe .EXE .img .IMG .iso .ISO .m3u .M3U .mdf .MDF .mds .MDS .minipsf .MINIPSF .pbp .PBP .psexe .PSEXE .psf .PSF .toc .TOC .z .Z .znx .ZNX .7z .7Z .zip .ZIP",
	f"{RA} -L mednafen_psx_hw_libretro.so %ROM%",
	"Libretro psx", "psx", "psx"),

	# (
	# "ags", "Adventure Game Studio Game Engine", f"{NI_TOPD}/Adventure Game Studio Game Engine",
	# ".desktop .sh",
	# "%STARTDIR%=%GAMEDIR% %ENABLESHORTCUTS% %EMULATOR_OS-SHELL% %ROM%",
	# 'Libretro ags', "pcwindows", "ags"),

	(
	"amigacd32", "Commodore Amiga CD32", f"{NI_TOPD}/0-Overlay/Commodore - Amiga CD32",
	".adf .ADF .adz .ADZ .ccd .CCD .chd .CHD .cue .CUE .dms .DMS .fdi .FDI .hdf .HDF .hdz .HDZ .ipf .IPF .iso .ISO .lha .LHA .m3u .M3U .mds .MDS .nrg .NRG .rp9 .RP9 .uae .UAE .7z .7Z .zip .ZIP",
	f"{RA} -L puae_libretro.so %ROM%",
	"Libretro amigacd32", "amigacd32", "amigacd32"),

	(
	"supracan", "Funtech - Super Acan", f"{NI_TOPD}/Funtech - Super Acan",
	".bin .BIN .7z .7Z .zip .ZIP",
	f"{MAME} supracan -cart \"%ROMRAW%\"",
	"MAME supracan", "supracan", "supracan"),

	(
	"gp32", "GamePark - GP32", f"{NI_TOPD}/GamePark - GP32",
	".gp32 .bin .BIN .7z .7Z .zip .ZIP",
	f"{MAME} gp32 -memc \"%ROMRAW%\"",
	"MAME gp32", "gp32", "gp32"),

	# (
	# "emulators", "Emulators", f"{NI_TOPD}/Emulators",
	# ".AppImage .desktop .sh",
	# "%ENABLESHORTCUTS% %EMULATOR_OS-SHELL% %ROM%",
	# 'Libretro emulators', "pcwindows", "emulators"),

	# (
	# "bbcmicro", "Acorn Computers BBC Micro", f"{NI_TOPD}/Acorn Computers BBC Micro",
	# ".dsd .DSD .img .IMG .ssd .SSD .7z .7Z .zip .ZIP",
	# "{MAME} -rompath %GAMEDIR%\;%ROMPATH%/bbcmicro bbcb -autoboot_delay "2" -autoboot_command "*cat\n\n*exec !boot\n" -flop1 %ROM%",
	# 'Libretro bbcmicro', "bbcmicro", "bbcmicro"),

	# (
	# "scummvm", "ScummVM Game Engine", f"{NI_TOPD}/ScummVM Game Engine",
	# ".scummvm .SCUMMVM .svm .SVM",
	# "{RA} -L scummvm_libretro.so %ROM%",
	# 'Libretro scummvm', "scummvm", "scummvm"),

	(
	"n64", "Nintendo - Nintendo 64", f"{NI_TOPD}/0-Overlay/Nintendo - Nintendo 64",
	".bin .BIN .d64 .D64 .n64 .N64 .ndd .NDD .u1 .U1 .v64 .V64 .z64 .Z64 .7z .7Z .zip .ZIP",
	f"{RA} -L mupen64plus_next_libretro.so %ROM%",
	"Libretro n64", "n64", "n64"),

	# (
	# "gamate", "Bit Corporation Gamate", f"{NI_TOPD}/Bit Corporation Gamate",
	# ".bin .BIN .7z .7Z .zip .ZIP",
	# "{RA} -L mame_libretro.so "gamate -rompath \"%GAMEDIRRAW%;%ROMPATH%/gamate\" -cart \"%ROMRAW%\""",
	# 'Libretro gamate', "gamate", "gamate"),

	# (
	# "segacd", "Sega CD", f"{NI_TOPD}/Sega CD",
	# ".68k .68K .bin .BIN .bms .BMS .chd .CHD .cue .CUE .gen .GEN .gg .GG .iso .ISO .m3u .M3U .md .MD .mdx .MDX .sg .SG .sgd .SGD .smd .SMD .sms .SMS .7z .7Z .zip .ZIP",
	# "{RA} -L genesis_plus_gx_libretro.so %ROM%",
	# 'Libretro segacd', "segacd", "segacd"),

	(
	"vectrex", "GCE - Vectrex", f"{NI_TOPD}/GCE - Vectrex",
	".bin .BIN .gam .GAM .vc .VC .vec .VEC .7z .7Z .zip .ZIP",
	f"{RA} -L vecx_libretro.so %ROM%",
	"Libretro vectrex", "vectrex", "vectrex"),

	(
	"supergrafx", "NEC - PC Engine SuperGrafx", f"{NI_TOPD}/NEC - PC Engine SuperGrafx",
	".ccd .CCD .chd .CHD .cue .CUE .pce .PCE .sgx .SGX .7z .7Z .zip .ZIP",
	f"{RA} -L mednafen_supergrafx_libretro.so %ROM%",
	"Libretro supergrafx", "supergrafx", "supergrafx"),

	(
	"tg16", "NEC - PC Engine - TurboGrafx 16", f"{NI_TOPD}/NEC - PC Engine - TurboGrafx 16",
	".ccd .CCD .chd .CHD .cue .CUE .img .IMG .iso .ISO .m3u .M3U .pce .PCE .sgx .SGX .toc .TOC .7z .7Z .zip .ZIP",
	f"{RA} -L mednafen_pce_libretro.so %ROM%",
	"Libretro tg16", "pcengine", "tg16"),

	# Nintendo - e-Reader  / check how to run this

	( # Most roms start with corrupted graphics, so hit F3 to clear the screen, then Q to start the game. 
	"studio2", "RCA - Studio II", f"{NI_TOPD}/RCA - Studio II",
	".gp32 .bin .BIN .7z .7Z .zip .ZIP",
	f"{MAME} studio2 -cart \"%ROMRAW%\"",
	"MAME studio2", "studio2", "studio2"),

	(
	"zxspectrum", "Sinclair - ZX Spectrum", f"{NI_TOPD}/Sinclair - ZX Spectrum",
	".dsk .DSK .gz .GZ .img .IMG .mgt .MGT .rzx .RZX .scl .SCL .sh .SH .sna .SNA .szx .SZX .tap .TAP .trd .TRD .tzx .TZX .udi .UDI .z80 .Z80 .7z .7Z .zip .ZIP",
	f"{RA} -L fuse_libretro.so %ROM%",
	"Libretro zxspectrum", "zxspectrum", "zxspectrum"),

	# (
	# "trs-80", "Tandy TRS-80", f"{NI_TOPD}/Tandy TRS-80",
	# ".cmd .CMD .dsk .DSK",
	# "%STARTDIR%=%GAMEDIR% %EMULATOR_SDL2TRS% -rom %ROMPATH%/trs-80/level2.rom -disk0 %ROMPATH%/trs-80/boot.dsk -disk1 %ROM%",
	# 'Libretro trs-80', "trs-80", "trs-80"),

	(
	"pcfx", "NEC - PC-FX", f"{NI_TOPD}/0-Overlay/NEC - PC-FX/japan",
	".ccd .CCD .chd .CHD .cue CUE .m3u .M3U .toc .TOC .7z .7Z .zip .ZIP",
	f"{RA} -L mednafen_pcfx_libretro.so %ROM%",
	"Libretro pcfx", "pcfx", "pcfx"),

	(
	"mastersystem", "Sega - Master System - Mark III", f"{NI_TOPD}/Sega - Master System - Mark III",
	".68k .68K .bin .BIN .bms .BMS .chd .CHD .col .COL .cue .CUE .gen .GEN .gg .GG .iso .ISO .m3u .M3U .md .MD .mdx .MDX .rom .ROM .sg .SG .sgd .SGD .smd .SMD .sms .SMS .7z .7Z .zip .ZIP",
	f"{RA} -L genesis_plus_gx_libretro.so %ROM%",
	"Libretro mastersystem", "mastersystem", "mastersystem"),

	# (
	# "famicom", "Nintendo Family Computer", f"{NI_TOPD}/Nintendo Family Computer",
	# ".3dsen .3DSEN .fds .FDS .nes .NES .unf .UNF .unif .UNIF .7z .7Z .zip .ZIP",
	# "{RA} -L mesen_libretro.so %ROM%",
	# 'Libretro famicom', "famicom", "famicom"),

	(
	"supervision", "Watara - Supervision", f"{NI_TOPD}/Watara - Supervision",
	".bin .BIN .sv .SV .7z .7Z .zip .ZIP",
	f"{RA} -L potator_libretro.so %ROM%",
	"Libretro supervision", "supervision", "supervision"),

	(
	"model3", "Sega - Model 3", f"{NI_TOPD}/0-Overlay/Sega - Model 3/ROMs/",
	".7z .7Z .zip .ZIP",
	f"{SUPERMODEL} %ROM%",
	"Supermodel", "arcade", "model3"),

	# (
	# "pcarcade", "PC Arcade Systems", f"{NI_TOPD}/PC Arcade Systems",
	# ".AppImage .desktop .exe .EXE .sh",
	# "%STARTDIR%=%GAMEDIR% %EMULATOR_WINE% %ROM%",
	# 'Libretro pcarcade', "arcade", "pcarcade"),

	(
	"PC Games - Lutris", "Lutris - PC Games", f"{NI_TOPD}/0-Overlay/Lutris - PC Games",
	".desktop .sh .txt",
	f"{LUTRIS} \"%BASENAME%\"",
	"Standalone lutris", "pcwindows", "pc"),

	# (
	# "love", "LÖVE - Game Engine", f"{NI_TOPD}/0-Overlay/LÖVE - Game Engine",
	# ".love",
	# f"{LOVE} \"%ROMRAW%\"",
	# "Standalone Löve", "love", "love"),

	(
	"gc", "Nintendo - GameCube", f"{NI_TOPD}/0-Overlay/Nintendo - GameCube/",
	".ciso .CISO .dff .DFF .dol .DOL .elf .ELF .gcm .GCM .gcz .GCZ .iso .ISO .json .JSON .m3u .M3U .rvz .RVZ .tgc .TGC .wad .WAD .wbfs .WBFS .wia .WIA .7z .7Z .zip .ZIP",
	f"{DOL} %ROM%",
	"Standalone gc", "gc", "gc"),

	# (
	# "pc98", "NEC PC-9800 Series", f"{NI_TOPD}/NEC PC-9800 Series",
	# ".2hd .2HD .88d .88D .98d .98D .d88 .D88 .d98 .D98 .cmd .CMD .dup .DUP .fdd .FDD .fdi .FDI .hdd .HDD .hdi .HDI .hdm .HDM .hdn .HDN .m3u .M3U .nhd .NHD .tfd .TFD .thd .THD .xdf .XDF .7z .7Z .zip .ZIP",
	# "{RA} -L np2kai_libretro.so %ROM%",
	# 'Libretro pc98', "pc98", "pc98"),

	(
	"ps2", "Sony - PlayStation 2", f"{NI_TOPD}/0-Overlay/Sony - PlayStation 2/ROMs",
	".arcadedef .bin .BIN .chd .CHD .ciso .CISO .cso .CSO .dump .DUMP .elf .ELF .gz .GZ .m3u .M3U .mdf .MDF .img .IMG .iso .ISO .isz .ISZ .ngr .NRG",
	f"{PCSX2} %ROM%",
	"Standalone ps2", "ps2", "ps2"),

	(
	"crvision", "VTech - CreatiVision", f"{NI_TOPD}/VTech - CreatiVision",
	".bin .BIN .rom .ROM .7z .7Z .zip .ZIP",
	f"{MAME} crvision -cart \"%ROMRAW%\"",
	"MAME crvision", "crvision", "crvision"),


	# (
	# "genesis", "Sega Genesis", f"{NI_TOPD}/Sega Genesis",
	# ".32x .32X .68k .68K .bin .BIN .bms .BMS .chd .CHD .cue .CUE .gen .GEN .gg .GG .iso .ISO .m3u .M3U .md .MD .mdx .MDX .sg .SG .sgd .SGD .smd .SMD .sms .SMS .7z .7Z .zip .ZIP",
	# "{RA} -L genesis_plus_gx_libretro.so %ROM%",
	# 'Libretro genesis', "genesis", "genesis"),


	# (
	# "android", "Google Android", f"{NI_TOPD}/Google Android",
	# ".7z .7Z .zip .ZIP",
	# "PLACEHOLDER %ROM%",
	# 'Libretro android', "android", "android"),


	# (
	# "coco", "Tandy Color Computer", f"{NI_TOPD}/Tandy Color Computer",
	# ".cas .CAS .ccc .CCC .dsk .DSK .rom .ROM",
	# "%EMULATOR_XROAR% -fs -default-machine coco2bus %ROM%",
	# 'Libretro coco', "coco", "coco"),


	(
	"fba", "FinalBurn Alpha", f"{NI_TOPD}/0-Overlay/FinalBurn - Alpha",
	".iso .ISO .7z .7Z .zip .ZIP",
	f"{RA} -L fbalpha2012_libretro.so %ROM%",
	"Libretro fba", "arcade", "fba"),

	(
	"gx4000", "Amstrad - GX4000", f"{MAMESL}/mame-sl/gx4000",
	".bin .BIN .cdt .CDT .cpr .CPR .dsk .DSK .kcr .KCR .m3u .M3U .sna .SNA .tap .TAR .voc .VOC .7z .7Z .zip .ZIP",
	f"{MAME} gx4000 %BASENAME%",
	"MAME gx4000", "gx4000", "gx4000"),


	# (
	# "steam", "Valve Steam", f"{NI_TOPD}/Valve Steam",
	# ".desktop .sh",
	# "%RUNINBACKGROUND% %ENABLESHORTCUTS% %EMULATOR_OS-SHELL% %ROM%",
	# 'Libretro steam', "steam", "steam"),


	# (
	# "type-x", "Taito Type X", f"{NI_TOPD}/Taito Type X",
	# ".AppImage .desktop .exe .EXE .sh",
	# "%STARTDIR%=%GAMEDIR% %EMULATOR_WINE% %ROM%",
	# 'Libretro type-x', "arcade", "type-x"),


	# (
	# "fmtowns", "Fujitsu FM Towns", f"{NI_TOPD}/Fujitsu FM Towns",
	# ".cdr .CDR .chd .CHD .cue .CUE .gdi .GDI .iso .ISO",
	# "{RA} -L mame_libretro.so "fmtownshr -rompath \"%GAMEDIRRAW%;%ROMPATH%/fmtowns\" -cdrom \"%ROMRAW%\""",
	# 'Libretro fmtowns', "fmtowns", "fmtowns"),


	# (
	# "palm", "Palm OS", f"{NI_TOPD}/Palm OS",
	# ".img .IMG .pqa .PQA .prc .PRC .7z .7Z .zip .ZIP",
	# "{RA} -L mu_libretro.so %ROM%",
	# 'Libretro palm', "palm", "palm"),


	(
	"MAME", "MAME Arcade", f"{NI_TOPD}/0-Overlay/MAME",
	".txt",
	f"{MAME} %BASENAME%",
	"MAME standalone", "arcade", "arcade"),


	# (
	# "uzebox", "Uzebox Open Source Console", f"{NI_TOPD}/Uzebox Open Source Console",
	# ".uze .UZE .7z .7Z .zip .ZIP",
	# "{RA} -L uzem_libretro.so %ROM%",
	# 'Libretro uzebox', "uzebox", "uzebox"),


	(
	"megadrive", "Sega - Mega Drive - Genesis", f"{NI_TOPD}/Sega - Mega Drive - Genesis",
	".32x .32X .68k .68K .bin .BIN .bms .BMS .chd .CHD .cue .CUE .gen .GEN .gg .GG .iso .ISO .m3u .M3U .md .MD .mdx .MDX .sg .SG .sgd .SGD .smd .SMD .sms .SMS .7z .7Z .zip .ZIP",
	f"{RA} -L genesis_plus_gx_libretro.so %ROM%",
	"Libretro megadrive", "megadrive", "megadrive"),


	# (
	# "zx81", "Sinclair ZX81", f"{NI_TOPD}/Sinclair ZX81",
	# ".p .P .tzx .TZX .7z .7Z .zip .ZIP",
	# "{RA} -L 81_libretro.so %ROM%",
	# 'Libretro zx81', "zx81", "zx81"),


	# (
	# "astrocde", "Bally Astrocade", f"{NI_TOPD}/Bally Astrocade",
	# ".7z .7Z .zip .ZIP",
	# "{RA} -L mame_libretro.so "astrocde -rompath \"%GAMEDIRRAW%;%ROMPATH%/astrocde\" -cart \"%ROMRAW%\""",
	# 'Libretro astrocde', "astrocde", "astrocade"),


	(
	"ngp", "SNK - Neo Geo Pocket", f"{NI_TOPD}/SNK - Neo Geo Pocket",
	".ngc .NGC .ngp .NGP .ngpc .NGPC .npc .NPC .7z .7Z .zip .ZIP",
	f"{RA} -L mednafen_ngp_libretro.so %ROM%",
	"Libretro ngp", "ngp", "ngp"),


	(
	"msx", "Microsoft - MSX", f"{NI_TOPD}/Microsoft - MSX",
	".cas .CAS .col .COL .di1 .DI1 .di2 .DI2 .dmk .DMK .dsk .DSK .fd1 .FD1 .fd2 .FD2 .m3u .M3U .mx1 .MX1 .mx2 .MX2 .ogv .OGV .ri .RI .rom .ROM .sc .SC .sg .SG .wav .WAV .xsa .XSA .7z .7Z .zip .ZIP",
	f"{RA} -L bluemsx_libretro.so %ROM%",
	"Libretro msx", "msx", "msx"),


	# (
	# "dragon32", "Dragon Data Dragon 32", f"{NI_TOPD}/Dragon Data Dragon 32",
	# ".cas .CAS .ccc .CCC .dsk .DSK .rom .ROM",
	# "%EMULATOR_XROAR% -fs -default-machine dragon32 %ROM%",
	# 'Libretro dragon32', "dragon32", "dragon32"),


	# (
	# "desktop", "Desktop Applications", f"{NI_TOPD}/Desktop Applications",
	# ".AppImage .desktop .sh",
	# "%ENABLESHORTCUTS% %EMULATOR_OS-SHELL% %ROM%",
	# 'Libretro desktop', "pcwindows", "desktop"),



	(
	"gba", "Nintendo - Game Boy Advance", f"{NI_TOPD}/Nintendo - Game Boy Advance",
	".agb .AGB .bin .BIN .cgb .CGB .dmg .DMG .gb .GB .gba .GBA .gbc .GBC .sgb .SGB .7z .7Z .zip .ZIP",
	f"{RA} -L mgba_libretro.so %ROM%",
	"Libretro gba", "gba", "gba"),


	(
	"virtualboy", "Nintendo - Virtual Boy", f"{NI_TOPD}/Nintendo - Virtual Boy",
	".bin .BIN .vb .VB .vboy .VBOY .7z .7Z .zip .ZIP",
	f"{RA} -L mednafen_vb_libretro.so %ROM%",
	"Libretro virtualboy", "virtualboy", "virtualboy"),


	# (
	# "arduboy", "Arduboy Miniature Game System", f"{NI_TOPD}/Arduboy Miniature Game System",
	# ".hex .HEX .7z .7Z .zip .ZIP",
	# "{RA} -L arduous_libretro.so %ROM%",
	# 'Libretro arduboy', "arduboy", "arduboy"),


	(
	"switch", "Nintendo - Switch", f"{NI_TOPD}/0-Overlay/Nintendo - Switch/ROMs",
	".nsp .NSP .xci .XCI",
		(
			("Ryujinx Switch emulator", f"{RYUJINX} %ROM%"),
			("Sudachi Switch emulator", f"{SUDACHI} %ROM%"),
			("Torzu Switch emulator", f"{TORZU} %ROM%"),
		),
	"Standalone Switch emulator", "switch", "switch"),


	# (
	# "sfc", "Nintendo SFC (Super Famicom)", f"{NI_TOPD}/Nintendo SFC (Super Famicom)",
	# ".bin .BIN .bml .BML .bs .BS .bsx .BSX .dx2 .DX2 .fig .FIG .gd3 .GD3 .gd7 .GD7 .mgd .MGD .sfc .SFC .smc .SMC .st .ST .swc .SWC .7z .7Z .zip .ZIP",
	# "{RA} -L snes9x_libretro.so %ROM%",
	# 'Libretro sfc', "snes", "sfc"),


	# (
	# "consolearcade", "Console Arcade Systems", f"{NI_TOPD}/Console Arcade Systems",
	# ".arcadedef .desktop .iso .ISO .sh .xbe .XBE .7z .7Z .zip .ZIP",
	# "{RA} -L mame_libretro.so %ROM%",
	# 'Libretro consolearcade', "arcade", "consolearcade"),


	# (
	# "spectravideo", "Spectravideo", f"{NI_TOPD}/Spectravideo",
	# ".cas .CAS .col .COL .dsk .DSK .m3u .M3U .mx1 .MX1 .mx2 .MX2 .ri .RI .rom .ROM .sc .SC .sg .SG .7z .7Z .zip .ZIP",
	# "{RA} -L bluemsx_libretro.so %ROM%",
	# 'Libretro spectravideo', "spectravideo", "spectravideo"),


	# (
	# "x1", "Sharp X1", f"{NI_TOPD}/Sharp X1",
	# ".2d .2D .2hd .2HD .88d .88D .cmd .CMD .d88 .D88 .dup .DUP .dx1 .DX1 .hdm .HDM .tap .TAP .tfd .TFD .xdf .XDF .7z .7Z .zip .ZIP",
	# "%STARTDIR%=%GAMEDIR% {RA} -L x1_libretro.so %ROM%",
	# 'Libretro x1', "x1", "x1"),


	# (
	# "psvita", "Sony PlayStation Vita", f"{NI_TOPD}/Sony PlayStation Vita",
	# ".psvita",
	# "%EMULATOR_VITA3K% -r %INJECT%=%BASENAME%.psvita",
	# 'Libretro psvita', "psvita", "psvita"),


	(
	"x68000", "Sharp - X68000", f"{NI_TOPD}/Sharp - X68000",
	".2hd .2HD .88d .88D .cmd .CMD .d88 .D88 .dim .DIM .dup .DUP .hdf .HDF .hdm .HDM .img .IMG .m3u .M3U .xdf .XDF .7z .7Z .zip .ZIP",
	f"{RA} -L px68k_libretro.so %ROM%",
	"Libretro x68000", "x68000", "x68000"),


	# (
	# "mess", "Multi Emulator Super System", f"{NI_TOPD}/Multi Emulator Super System",
	# ".chd .CHD .7z .7Z .zip .ZIP",
	# "{RA} -L mess2015_libretro.so %ROM%",
	# 'Libretro mess', "mess", "mess"),


	# (
	# "cdimono1", "Philips CD-i", f"{NI_TOPD}/Philips CD-i",
	# ".chd .CHD .cue .CUE .iso .ISO",
	# "{RA} -L same_cdi_libretro.so %ROM%",
	# 'Libretro cdimono1', "cdimono1", "cdimono1"),



	(
	"neogeocd", "SNK - Neo Geo CD", f"{NI_TOPD}/0-Overlay/SNK - Neo Geo CD",
	".chd .CHD .cue .CUE",
	f"{RA} -L neocd_libretro.so %ROM%",
	"Libretro neogeocd", "neogeocd", "neogeocd"),


	# (
	# "electron", "Acorn Electron", f"{NI_TOPD}/Acorn Electron",
	# ".1dd .1DD .adf .ADF .adl .ADL .adm .ADM .ads .ADS .bbc .BBC .bin .BIN .cqi .CQI .cqm .CQM .csw .CSW .d77 .D77 .d88 .D88 .dfi .DFI .dsd .DSD .dsk .DSK .hfe .HFE .imd .IMD .img .IMG .mfi .MFI .mfm .MFM .rom .ROM .ssd .SSD .td0 .TD0 .uef .UEF .wav .WAV .7z .7Z .zip .ZIP",
	# "{MAME} -rompath %GAMEDIR%\;%ROMPATH%/electron electron64 -autoboot_delay "2" -autoboot_command "*T.\nCH.\"\"\n" -cass1 %ROM%",
	# 'Libretro electron', "electron", "electron"),


	# (
	# "gameandwatch", "Nintendo Game and Watch", f"{NI_TOPD}/Nintendo Game and Watch",
	# ".mgw .MGW .7z .7Z .zip .ZIP",
	# "{MAME} -artpath %ROMPATH%/gameandwatch/artwork -rompath %GAMEDIR%\;%ROMPATH%/gameandwatch %BASENAME%",
	# 'Libretro gameandwatch', "gameandwatch", "gameandwatch"),


	# (
	# "cps", "Capcom Play System", f"{NI_TOPD}/Capcom Play System",
	# ".7z .7Z .zip .ZIP",
	# "{RA} -L mame_libretro.so %ROM%",
	# 'Libretro cps', "arcade", "cps"),


	(
	"gamegear", "Sega - Game Gear", f"{NI_TOPD}/Sega - Game Gear",
	".68k .68K .bin .BIN .bms .BMS .chd .CHD .col .COL .cue .CUE .gen .GEN .gg .GG .iso .ISO .m3u .M3U .md .MD .mdx .MDX .rom .ROM .sg .SG .sgd .SGD .smd .SMD .sms .SMS .7z .7Z .zip .ZIP",
	f"{RA} -L genesis_plus_gx_libretro.so %ROM%",
	"Libretro gamegear", "gamegear", "gamegear"),


	(
	"n3ds", "Nintendo 3DS", f"{NI_TOPD}/0-Overlay/Nintendo - 3DS",
	".3ds .3DS .3dsx .3DSX .app .APP .axf .AXF .cci .CCI .cxi .CXI .elf .ELF .7z .7Z .zip .ZIP",
	"Mandarine", f"{MANDARINE} %ROM%"
	"Standalone n3ds", "n3ds", "n3ds"),


	(
	"pico8", "PICO-8 Fantasy Console", "/media/eikeno/GAMES_5TB11/Games/PICO8/.lexaloffle/pico-8/carts", # doesn't work otherwise
	".p8 .P8 .png .PNG",
	"/home/eikeno/bin/pico8-flatpak-runner.sh -run %ROM%",
	"Standalone pico8", "pico8", "pico8"),

	(
	"saturn", "Sega Saturn", f"{NI_TOPD}/0-Overlay/Sega - Saturn",
	".bin .BIN .ccd .CCD .chd .CHD .cue .CUE .iso .ISO .m3u .M3U .mds .MDS .toc .TOC .7z .7Z .zip .ZIP",
	f"{RA} -L mednafen_saturn_libretro.so %ROM%",
	"Libretro saturn", "saturn", "saturn"),


	# (
	# "pcenginecd", "NEC PC Engine CD", f"{NI_TOPD}/NEC PC Engine CD",
	# ".ccd .CCD .chd .CHD .cue .CUE .img .IMG .iso .ISO .m3u .M3U .pce .PCE .sgx .SGX .toc .TOC .7z .7Z .zip .ZIP",
	# "{RA} -L mednafen_pce_libretro.so %ROM%",
	# 'Libretro pcenginecd', "pcenginecd", "pcenginecd"),


	# (
	# "adam", "Coleco Adam", f"{NI_TOPD}/Coleco Adam",
	# ".1dd .1DD .bin .BIN .col .COL .cqi .CQI .cqm .CQM .d77 .D77 .d88 .D88 .ddp .DDP .dfi .DFI .dsk .DSK .hfe .HFE .imd .IMD .mfi .MFI .mfm .MFM .rom .ROM .td0 .TD0 .wav .WAV .7z .7Z .zip .ZIP",
	# "{MAME} -rompath %GAMEDIR%\;%ROMPATH%/adam adam -flop1 %ROM%",
	# 'Libretro adam', "adam", "adam"),


	(
	"megacd", "Sega Mega-CD", f"{NI_TOPD}/0-Overlay/Sega - Mega-CD",
	".68k .68K .bin .BIN .bms .BMS .chd .CHD .cue .CUE .gen .GEN .gg .GG .iso .ISO .m3u .M3U .md .MD .mdx .MDX .sg .SG .sgd .SGD .smd .SMD .sms .SMS .7z .7Z .zip .ZIP",
	f"{RA} -L genesis_plus_gx_libretro.so %ROM%",
	"Libretro megacd", "segacd", "megacd"),


	# (
	# "daphne", "Daphne Arcade LaserDisc Emulator", f"{NI_TOPD}/Daphne Arcade LaserDisc Emulator",
	# ".daphne .ogv .OGV .singe .7z .7Z .zip .ZIP",
	# "%EMULATOR_HYPSEUS-SINGE% %BASENAME% vldp -framefile %GAMEDIR%/%BASENAME%.txt %INJECT%=%BASENAME%.commands",
	# 'Libretro daphne', "", "daphne"),


	# (
	# "mame-advmame", "AdvanceMAME", f"{NI_TOPD}/AdvanceMAME",
	# ".7z .7Z .zip .ZIP",
	# "%STARTDIR%=~/.advance %EMULATOR_ADVANCEMAME% %BASENAME%",
	# 'Libretro mame-advmame', "arcade", "mame-advmame"),


	# (
	# "tanodragon", "Tano Dragon", f"{NI_TOPD}/Tano Dragon",
	# ".cas .CAS .ccc .CCC .dsk .DSK .rom .ROM",
	# "%EMULATOR_XROAR% -fs -default-machine tano %ROM%",
	# 'Libretro tanodragon', "dragon32", "tanodragon"),



	# (
	# "gx4000", "Amstrad GX4000", f"{NI_TOPD}/Amstrad GX4000",
	# ".bin .BIN .cdt .CDT .cpr .CPR .dsk .DSK .kcr .KCR .m3u .M3U .sna .SNA .tap .TAR .voc .VOC .7z .7Z .zip .ZIP",
	# "{RA} -L cap32_libretro.so %ROM%",
	# 'Libretro gx4000', "gx4000", "gx4000"),


	# (
	# "xbox360", "Microsoft Xbox 360", f"{NI_TOPD}/Microsoft Xbox 360",
	# ". .desktop .iso .ISO .sh .xex .XEX",
	# "%STARTDIR%=%EMUDIR% %PRECOMMAND_WINE% %EMULATOR_XENIA-WINDOWS% %ROM%",
	# 'Libretro xbox360', "xbox360", "xbox360"),


	# (
	# "pcengine", "NEC PC Engine", f"{NI_TOPD}/NEC PC Engine",
	# ".ccd .CCD .chd .CHD .cue .CUE .img .IMG .iso .ISO .m3u .M3U .pce .PCE .sgx .SGX .toc .TOC .7z .7Z .zip .ZIP",
	# "{RA} -L mednafen_pce_libretro.so %ROM%",
	# 'Libretro pcengine', "pcengine", "pcengine"),


	# (
	# "pc", "IBM PC", f"{NI_TOPD}/IBM PC",
	# ".bat .BAT .com .COM .conf .CONF .cue .CUE .dosz .DOSZ .exe .EXE .iso .ISO .7z .7Z .zip .ZIP",
	# "{RA} -L dosbox_pure_libretro.so %ROM%",
	# 'Libretro pc', "pc", "pc"),

	# (
	# "sega32xjp", "Sega Super 32X", f"{NI_TOPD}/Sega Super 32X",
	# ".32x .32X .68k .68K .bin .BIN .cue .CUE .gen .GEN .iso .ISO .md .MD .smd .SMD .sms .SMS .7z .7Z .zip .ZIP",
	# "{RA} -L picodrive_libretro.so %ROM%",
	# 'Libretro sega32xjp', "sega32x", "sega32xjp"),


	# (
	# "tic80", "TIC-80 Fantasy Computer", f"{NI_TOPD}/TIC-80 Fantasy Computer",
	# ".tic .TIC",
	# "{RA} -L tic80_libretro.so %ROM%",
	# 'Libretro tic80', "tic80", "tic80"),


	# (
	# "naomigd", "Sega NAOMI GD-ROM", f"{NI_TOPD}/Sega NAOMI GD-ROM",
	# ".bin .BIN .dat .DAT .elf .ELF .lst .LST .7z .7Z .zip .ZIP",
	# "{RA} -L flycast_libretro.so %ROM%",
	# 'Libretro naomigd', "arcade", "naomigd"),


	# (
	# "archimedes", "Acorn Archimedes", f"{NI_TOPD}/Acorn Archimedes",
	# ".1dd .1DD .360 .adf .ADF .adl .ADL .adm .ADM .ads .ADS .apd .APD .bbc .BBC .chd .CHD .cqi .CQI .cqm .CQM .d77 .D77 .d88 .D88 .dfi .DFI .dsd .DSD .dsk .DSK .hfe .HFE .ima .IMA .imd .IMD .img .IMG .ipf .IPF .jfd .JFD .mfi .MFI .mfm .MFM .msa .MSA .ssd .SSD .st .ST .td0 .TD0 .ufi .UFI .7z .7Z .zip .ZIP",
	# "{MAME} -rompath %GAMEDIR%\;%ROMPATH%/archimedes aa4401 -flop1 %ROM%",
	# 'Libretro archimedes', "archimedes", "archimedes"),


	# (
	# "windows3x", "Microsoft Windows 3.x", f"{NI_TOPD}/Microsoft Windows 3.x",
	# ".AppImage .bat .BAT .desktop .dosz .DOSZ .sh .7z .7Z .zip .ZIP",
	# "%STARTDIR%=%GAMEDIR% %EMULATOR_DOSBOX-X% -defaultdir %GAMEDIR% %ROM%",
	# 'Libretro windows3x', "windows3x", "windows3x"),


	# (
	# "solarus", "Solarus Game Engine", f"{NI_TOPD}/Solarus Game Engine",
	# ".solarus",
	# "%EMULATOR_SOLARUS% %ROM%",
	# 'Libretro solarus', "solarus", "solarus"),


	# (
	# "fds", "Nintendo Famicom Disk System", f"{NI_TOPD}/Nintendo Famicom Disk System",
	# ".nes .NES .fds .FDS .unf .UNF .UNIF .UNIF .7z .7Z .zip .ZIP",
	# "{RA} -L mesen_libretro.so %ROM%",
	# 'Libretro fds', "fds", "fds"),


	# (
	# "j2me", "Java 2 Micro Edition (J2ME)", f"{NI_TOPD}/Java 2 Micro Edition (J2ME)",
	# ".jar .JAR .7z .7Z .zip .ZIP",
	# "{RA} -L squirreljme_libretro.so %ROM%",
	# 'Libretro j2me', "android", "j2me"),


	# (
	# "n64dd", "Nintendo 64DD", f"{NI_TOPD}/Nintendo 64DD"
	# ".bin .BIN .d64 .D64 .n64 .N64 .ndd .NDD .u1 .U1 .v64 .V64 .z64 .Z64 .7z .7Z .zip .ZIP",
	# "{RA} -L parallel_n64_libretro.so %ROM%",
	# 'Libretro n64dd', "n64", "n64dd"),


	(
	"snes", "Nintendo - Super Nintendo Entertainment System", f"{NI_TOPD}/0-Overlay/Nintendo - Super Nintendo Entertainment System/No-Intro_ROMs_restricted",
	".bin .BIN .bml .BML .bs .BS .bsx .BSX .dx2 .DX2 .fig .FIG .gd3 .GD3 .gd7 .GD7 .mgd .MGD .sfc .SFC .smc .SMC .st .ST .swc .SWC .7z .7Z .zip .ZIP",
	f"{RA} -L snes9x_libretro.so %ROM%",
	"Libretro snes", "snes", "snes"),


	(
	"videopac", "Philips - Videopac+", f"{NI_TOPD}/Philips - Videopac+",
	".bin .BIN .7z .7Z .zip .ZIP",
	f"{RA} -L o2em_libretro.so %ROM%",
	"Libretro videopac", "odyssey2", "videopac"),


	# (
	# "easyrpg", "EasyRPG Game Engine", f"{NI_TOPD}/EasyRPG Game Engine",
	# ".easyrpg .zip .ZIP",
	# "{RA} -L easyrpg_libretro.so %ROM%",
	# 'Libretro easyrpg', "easyrpg", "easyrpg"),


	# (
	# "apple2", "Apple II", f"{NI_TOPD}/Apple II",
	# ".do .DO .dsk .DSK .nib .NIB .po .PO",
	# "%EMULATOR_LINAPPLE% -f -b --d1 %ROM%",
	# 'Libretro apple2', "apple2", "apple2"),


	# (
	# "triforce", "Namco-Sega-Nintendo Triforce", f"{NI_TOPD}/Namco-Sega-Nintendo Triforce",
	# ".ciso .CISO .dff .DFF .dol .DOL .elf .ELF .gcm .GCM .gcz .GCZ .iso .ISO .json .JSON .m3u .M3U .rvz .RVZ .tgc .TGC .wad .WAD .wbfs .WBFS .wia .WIA .7z .7Z .zip .ZIP",
	# "%INJECT%=%BASENAME%.esprefix %EMULATOR_TRIFORCE% -b -e %ROM%",
	# 'Libretro triforce', "arcade", "triforce"),


	# (
	# "windows", "Microsoft Windows", f"{NI_TOPD}/Microsoft Windows",
	# ".AppImage .desktop .sh",
	# "%ENABLESHORTCUTS% %EMULATOR_OS-SHELL% %ROM%",
	# 'Libretro windows', "pcwindows", "windows"),


	# (
	# "multivision", "Othello Multivision", f"{NI_TOPD}/Othello Multivision",
	# ".bin .BIN .gg .GG .rom .ROM .sg .SG .sms .SMS .7z .7Z .zip .ZIP",
	# "{RA} -L gearsystem_libretro.so %ROM%",
	# 'Libretro multivision', "sg-1000", "multivision"),


	( # other folder: "ROMs" points to GAME_5TB11 (sourced from FBA or similar) __CHECKDUPS__
	"neogeo", "SNK - Neo Geo", f"{NI_TOPD}/0-Overlay/SNK - Neo Geo/NEOGEO_MAME_SL",
	".7z .7Z .zip .ZIP",
	f"{MAME_RUN_FROM_FULLNAME} %ROM%",
	"MAME neogeo", "neogeo", "neogeo"),

	(
	"vsmile", "VTech - V.Smile", f"{NI_TOPD}/VTech - V.Smile",
	".bin .BIN .7z .7Z .zip .ZIP",
	f"{MAME} vsmile -cart \"%ROMRAW%\"",
	"MAME vsmile", "vsmile", "vsmile"),


	(
	"stv", "Sega - Titan Video Game System", f"{NI_TOPD}/0-Overlay/Sega - Titan Video Game System",
	".7z .7Z .zip .ZIP",
	f"{RA} -L kronos_libretro.so %ROM%",
	"Libretro stv", "arcade", "stv"),


	(
	"pokemini", "Nintendo - Pokemon Mini", f"{NI_TOPD}/Nintendo - Pokemon Mini",
	".min .MIN .7z .7Z .zip .ZIP",
	f"{RA} -L pokemini_libretro.so %ROM%",
	"Libretro pokemini", "pokemini", "pokemini"),


	# (
	# "epic", "Epic Games Store", f"{NI_TOPD}/Epic Games Store",
	# ".desktop .sh",
	# "%RUNINBACKGROUND% %ENABLESHORTCUTS% %EMULATOR_OS-SHELL% %ROM%",
	# 'Libretro epic', "pcwindows", "epic"),


	# (
	# "ti99", "Texas Instruments TI-99", f"{NI_TOPD}/Texas Instruments TI-99",
	# ".rpk .RPK .7z .7Z .zip .ZIP",
	# "{MAME} -rompath %GAMEDIR%\;%ROMPATH%/ti99 ti99_4a -ioport peb -ioport:peb:slot3 speech -cart %BASENAME%",
	# 'Libretro ti99', "ti99", "ti99"),


	(
	"cps2", "Capcom - Play System II", f"{NI_TOPD}/0-Overlay/Capcom - Play System II",
	".7z .7Z .zip .ZIP",
	f"{MAME} %BASENAME%",
	"MAME cps2", "arcade", "cps2"),


	# (
	# "amiga600", "Commodore Amiga 600", f"{NI_TOPD}/Commodore Amiga 600",
	# ".adf .ADF .adz .ADZ .ccd .CCD .chd .CHD .cue .CUE .dms .DMS .fdi .FDI .hdf .HDF .hdz .HDZ .ipf .IPF .iso .ISO .lha .LHA .m3u .M3U .mds .MDS .nrg .NRG .rp9 .RP9 .uae .UAE .7z .7Z .zip .ZIP",
	# "{RA} -L puae_libretro.so %ROM%",
	# 'Libretro amiga600', "amiga", "amiga600"),


	# (
	# "pc88", "NEC PC-8800 Series", f"{NI_TOPD}/NEC PC-8800 Series",
	# ".88d .88D .cmt .CMT .d88 .D88 .m3u .M3U .t88 .T88 .u88 .U88",
	# "{RA} -L quasi88_libretro.so %ROM%",
	# 'Libretro pc88', "pc88", "pc88"),


	# (
	# "zxnext", "Sinclair ZX Spectrum Next", f"{NI_TOPD}/Sinclair ZX Spectrum Next",
	# ".nex .NEX .sna .SNA",
	# "%STARTDIR%=%GAMEDIR% MONO_IOMAP=all mono %EMULATOR_CSPECT% -fullscreen -s28 -vsync -60 -analytics -tv -zxnext -mmc=./ %ROM%",
	# 'Libretro zxnext', "zxnext", "zxnext"),


	# (
	# "ngage", "Nokia N-Gage", f"{NI_TOPD}/Nokia N-Gage",
	# ".ngage .zip .ZIP",
	# "%EMULATOR_EKA2L1% --fullscreen --device RH-29 --mount %ROM% --run "%BASENAME%"",
	# 'Libretro ngage', "ngage", "ngage"),



	(
	"gb", "Nintendo - Game Boy", f"{NI_TOPD}/Nintendo - Game Boy",
	".bs .BS .cgb .CGB .dmg .DMG .gb .GB .gbc .GBC .sgb .SGB .sfc .SFC .smc .SMC .7z .7Z .zip .ZIP",
	f"{RA} -L gambatte_libretro.so %ROM%",
	"Libretro gb", "gb", "gb"),


	# (
	# "neogeocdjp", "SNK Neo Geo CD", f"{NI_TOPD}/SNK Neo Geo CD",
	# ".chd .CHD .cue .CUE",
	# "{RA} -L neocd_libretro.so %ROM%",
	# 'Libretro neogeocdjp', "neogeocd", "neogeocdjp"),


	(
	"channelf", "Fairchild Channel F", f"{NI_TOPD}/Fairchild - Channel F",
	".bin .BIN .chf .CHF .7z .7Z .zip .ZIP",
	f"{RA} -L freechaf_libretro.so %ROM%",
	"Libretro channelf", "channelf", "channelf"),


	(
	"gbc", "Nintendo - Game Boy Color", f"{NI_TOPD}/Nintendo - Game Boy Color",
	".bs .BS .cgb .CGB .dmg .DMG .gb .GB .gbc .GBC .sgb .SGB .sfc .SFC .smc .SMC .7z .7Z .zip .ZIP",
	f"{RA} -L gambatte_libretro.so %ROM%",
	"Libretro gbc", "gbc", "gbc"),


	# (
	# "fbneo", "FinalBurn Neo", f"{NI_TOPD}/FinalBurn Neo",
	# ".7z .7Z .zip .ZIP",
	# "{RA} -L fbneo_libretro.so %ROM%",
	# 'Libretro fbneo', "arcade", "fbneo"),


	# (
	# "fm7", "Fujitsu FM-7", f"{NI_TOPD}/Fujitsu FM-7",
	# ".1dd .1DD .cqi .CQI .cqm .CQM .d77 .D77 .d88 .D88 .dfi .DFI .dsk .DSK .hfe .HFE .imd .IMD .mfi .MFI .mfm .MFM .t77 .T77 .td0 .TD0 .wav .WAV .7z .7Z .zip .ZIP",
	# "{MAME} -rompath %GAMEDIR%\;%ROMPATH%/fm7 fm7 -flop1 %ROM%",
	# 'Libretro fm7', "fm7", "fm7"),


	# (
	# "cdtv", "Commodore CDTV", f"{NI_TOPD}/Commodore CDTV",
	# ".ccd .CCD .chd .CHD .cue .CUE .iso .ISO .m3u .M3U .mds .MDS .nrg .NRG .rp9 .RP9 .7z .7Z .zip .ZIP",
	# "{RA} -L puae_libretro.so %ROM%",
	# 'Libretro cdtv', "cdtv", "cdtv"),


	(
	"naomi2", "Sega NAOMI 2", f"{NI_TOPD}/0-Overlay/Sega - NAOMI 2",
	".bin .BIN .dat .DAT .elf .ELF .lst .LST .7z .7Z .zip .ZIP",
	f"{FLYCAST} %ROM%",
	"Standalone naomi2", "arcade", "naomi2"),


	# (
	# "kodi", "Kodi Home Theatre Software", f"{NI_TOPD}/Kodi Home Theatre Software",
	# ".desktop .sh",
	# "%RUNINBACKGROUND% %ENABLESHORTCUTS% %EMULATOR_OS-SHELL% %ROM%",
	# 'Libretro kodi', "pcwindows", "kodi"),


	(
	"arcadia", "Emerson Arcadia 2001", f"{NI_TOPD}/Emerson - Arcadia 2001",
	".bin .BIN .7z .7Z .zip .ZIP",
	f"{MAME} arcadia -cart \"%ROMRAW%\"",
	"MAME arcadia", "arcadia", "arcadia"),


	# (
	# "lcdgames", "LCD Handheld Games", f"{NI_TOPD}/LCD Handheld Games",
	# ".mgw .MGW .7z .7Z .zip .ZIP",
	# "{MAME} -artpath %ROMPATH%/lcdgames/artwork -rompath %GAMEDIR%\;%ROMPATH%/lcdgames %BASENAME%",
	# 'Libretro lcdgames', "", "lcdgames"),


	# (
	# "zmachine", "Infocom Z-machine", f"{NI_TOPD}/Infocom Z-machine",
	# ".dat .DAT .z1 .Z1 .z2 .Z2 .z3 .Z3 .z4 .Z4 .z5 .Z5 .z6 .Z6 .z7 .Z7 .z8 .Z8 .zlb .ZLB .zblorb .ZBLORB",
	# "%EMULATOR_GARGOYLE% %ROM%",
	# 'Libretro zmachine', "zmachine", "zmachine"),


	# (
	# "mame", "Multiple Arcade Machine Emulator", f"{NI_TOPD}/Multiple Arcade Machine Emulator",
	# ".cmd .CMD .desktop .sh .7z .7Z .zip .ZIP",
	# "{RA} -L mame_libretro.so %ROM%",
	# 'Libretro mame', "arcade", "mame"),


	# (
	# "megacdjp", "Sega Mega-CD", f"{NI_TOPD}/Sega Mega-CD",
	# ".68k .68K .bin .BIN .bms .BMS .chd .CHD .cue .CUE .gen .GEN .gg .GG .iso .ISO .m3u .M3U .md .MD .mdx .MDX .sg .SG .sgd .SGD .smd .SMD .sms .SMS .7z .7Z .zip .ZIP",
	# "{RA} -L genesis_plus_gx_libretro.so %ROM%",
	# 'Libretro megacdjp', "segacd", "megacdjp"),


	# (
	# "mugen", "M.U.G.E.N Game Engine", f"{NI_TOPD}/M.U.G.E.N Game Engine",
	# ".mugen",
	# "%STARTDIR%=%GAMEDIR% %EMULATOR_OS-SHELL% -c "%ROM%"",
	# 'Libretro mugen', "mugen", "mugen"),


	(
	"apple2gs", "Apple IIGS", f"{NI_TOPD}/0-Overlay/Apple - Apple IIGS",
	".2mg .2MG .7z .7z .zip .ZIP",
	f"{MAME} apple2gs -flop3 \"%ROMRAW%\"",
	"MAME apple2gs", "apple2gs", "apple2gs"),


	(
	"odyssey2", "Magnavox - Odyssey 2", f"{NI_TOPD}/Magnavox - Odyssey 2",
	".bin .BIN .7z .7Z .zip .ZIP",
	f"{RA} -L o2em_libretro.so %ROM%",
	"Libretro odyssey2", "odyssey2", "odyssey2"),


	(
	"atarijaguarcd", "Atari Jaguar CD", f"{NI_TOPD}/0-Overlay/Atari - Jaguar CD",
	".abs .ABS .bin .BIN .cdi .CDI .cof .COF .cue .CUE .j64 .J64 .jag .JAG .prg .PRG .rom .ROM .7z .7Z .zip .ZIP",
	"lutris lutris:rungame/bigpemu \"%ROMRAW%\"",
	"Standalone WINE bigpemu", "atarijaguarcd", "atarijaguarcd"),

	# ( # black screen for now
	# "zeebo", "Zeebo - Zeebo", f"{NI_TOPD}/Zeebo - Zeebo",
	# ".bin .BIN .7z .7Z .zip .ZIP",
	# f"{MAME} zeebo -cart \"%ROMRAW%\"",
	# 'MAME zeebo', "zeebo", "zeebo"),


)

#=== Templates

OPEN_STRING = """<?xml version="1.0"?>
<systemList>
"""
CLOS_STRING = "</systemList>"
SYST_STRING = """
	<system>
		<name>{name}</name>
		<fullname>{fullname}</fullname>
		<path>{path}</path>
		<extension>{extension}</extension>
        <command label="{command_label}">{command}</command>
		<platform>{platform}</platform>
		<theme>{theme}</theme>
	</system>

"""
SYST_STRING_MULTICOMMANDS = """
	<system>
		<name>{name}</name>
		<fullname>{fullname}</fullname>
		<path>{path}</path>
		<extension>{extension}</extension>
        {commands_str}
		<platform>{platform}</platform>
		<theme>{theme}</theme>
	</system>

"""

ESHOME=f"{os.environ['HOME']}/ES-DE/custom_systems"
SYSFILE=os.path.join(ESHOME, "es_systems_all.xml")

#=== logic

def loopwrite(sys_t: tuple, sysfile_f: TextIO) -> None:
	""" Write system data to given file handler """

	# Manage case of multiple commands definitions:
	if type(sys_t[4]) is type(()): # tuple of multiple command is used in that case
		commands_str=""
		for i in sys_t[4]:
			commands_str += "<command label=\"" + i[0] +"\">" + i[1] + "</command>" + """
	"""
		try:
			sysfile_f.write(
			SYST_STRING_MULTICOMMANDS.format(
				name = 			sys_t[0],
				fullname = 		sys_t[1],
				path =			sys_t[2],
				extension =		sys_t[3],
				commands_str = 	commands_str,
				platform = 		sys_t[6],
				theme =			sys_t[7],
				)
			)
		except Exception as e:
			print("\n" + str(e)); sys.exit()

	# single command definitions:
	else:
		try:
			sysfile_f.write(
			SYST_STRING.format(
				name = 			sys_t[0],
				fullname = 		sys_t[1],
				path =			sys_t[2],
				extension =		sys_t[3],
				command = 		sys_t[4],
				command_label = sys_t[5],
				platform = 		sys_t[6],
				theme =			sys_t[7],
				)
			)
		except Exception as e:
			print("\n" + str(e)); sys.exit ()

def writesys(mode: str, SYSFILE: str) -> None:
	"""
	This will Write:
	- one XML file per declared system from SYSTEM tuple
	- one full XML with all systems

	Per system XML can be used with es-de-select script to load only
	on system and reduce loading times in case or large collections
	and/or if storing on a network or slow filesystem.

	To be run for the root of your home ES-DE configuration tree.
	"""

	if mode == "all":
		sysfile_f = open(SYSFILE, "w")
		sysfile_f.write(OPEN_STRING)

		for sys_t in SYSTEMS:
			loopwrite(sys_t, sysfile_f)

		sysfile_f.write(CLOS_STRING)

	elif mode == "singles":

		for sys_t in SYSTEMS:
			sysfile = SYSFILE.replace("all.xml", f"{sys_t[0]}.xml")
			sysfile_f = open(sysfile, "w")
			sysfile_f.write(OPEN_STRING)
			loopwrite(sys_t, sysfile_f)
			sysfile_f.write(CLOS_STRING)

# don't use '__main__' :
writesys("all", SYSFILE)
writesys("singles", SYSFILE)
