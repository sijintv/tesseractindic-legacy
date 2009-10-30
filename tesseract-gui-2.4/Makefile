# Makefile install script for linuxsms

SCRIPT  = tesseract-gui.py
BASEDIR = /usr/

DESKTOPDIR = share/applications/
ICONDIR  = share/icons/
FILESDIR = share/
BINDIR = bin/

default:
	@echo "make install installs the script into /usr"
	@echo "make uninstall removes all files."

install:
	@echo  "creating dirs under /usr, "
	@echo  "copying files, " 
	@cp -f $(BINDIR)$(SCRIPT) $(BASEDIR)$(BINDIR)
	@echo  "copying "$(BASEDIR)$(BINDIR)
	@cp -f $(DESKTOPDIR)tesseract-gui.desktop $(BASEDIR)$(DESKTOPDIR)
	@echo  "copying "$(BASEDIR)$(DESKTOPDIR)
	@cp -f $(ICONDIR)tesseract-gui-icon.svg $(BASEDIR)$(ICONDIR)
	@echo  "copying "$(BASEDIR)$(ICONDIR)
	@cp -fr $(FILESDIR)tesseract-gui/ $(BASEDIR)$(FILESDIR)
	@echo  "copying "$(BASEDIR)$(FILESDIR)
	@echo "ok"

uninstall:
	@echo "removing files and dirs, "
	@rm -f $(BASEDIR)$(BINDIR)$(SCRIPT)
	@rm -f $(BASEDIR)$(ICONDIR)tesseract-gui-icon.svg
	@rm -f $(BASEDIR)$(ICONDIR)tesseract-gui-icon.svg
	@rm -fdR $(BASEDIR)$(FILESDIR)tesseract-gui/
	@rm -f $(BASEDIR)$(DESKTOPDIR)tesseract-gui.desktop
	@echo "ok"
