.PHONY: clean all install

all:
	cd string; $(MAKE)
	cd misc; $(MAKE)
	cd config; $(MAKE)
	cd filesystem; $(MAKE)
	cd math; $(MAKE)
	cd time; $(MAKE)
	cd socket; $(MAKE)
	cd distr; $(MAKE)
	cd libantlr3c-3.1.3; $(MAKE)
	install -d ../include/antlr31
	install -m0644 libantlr3c-3.1.3/include/* ../include/antlr31/
	install -m0644 libantlr3c-3.1.3/antlr3config.h ../include/antlr31/
	install -d ../../lib
	install -m0644 libantlr3c-3.1.3/.libs/libantlr3c.so ../../lib

clean:
	cd string; $(MAKE) clean
	cd config; $(MAKE) clean
	cd filesystem; $(MAKE) clean
	cd time; $(MAKE) clean
	cd socket; $(MAKE) clean
	cd distr; $(MAKE) clean
	cd libantlr3c-3.1.3; $(MAKE) clean

