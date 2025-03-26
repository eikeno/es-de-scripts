DESTDIR  = ~/ES-DE

install:
	install -m 0755 GenGameLists.py $(DESTDIR)/GenGameLists.py
	install -m 0755 GenSsystemFiles.py $(DESTDIR)/GenSsystemFiles.py
	install -m 0755 import_lutris_games.sh $(DESTDIR)/import_lutris_games.sh
	install -m 0755 run-lutris-by-slug_esde.sh $(DESTDIR)/run-lutris-by-slug_esde.sh
	install -m 0755 mame_run_from_fullname.sh $(DESTDIR)/mame_run_from_fullname.sh
