##
# Makefile for the xml directory
#
# Edit template/template.cfg to configure the XML file
# Edit ApplicationProgram to configure the application program
#
# The XML file is generated from the template file 
# template/template.in and the configuration file
# template/template.cfg
#
# The application program is merged with the template
# variables in the ApplicationProgram are substituted

DEFAULT_TARGETS = all

PROD=foobar.xml

all:  ${PROD}

almost_clean:
	rm /tmp/prog.tmp

clean:  almost_clean
	rm ${PROD}

# make a tempfile with template and ApplicationProgram combined

/tmp/prog.tmp:  template/template.in ApplicationProgram
	python3 ./tools/subst.py $< ApplicationProgram $@

# to create .xml file,
# substitute all variables in temporary file using values in cfg

%.xml:  /tmp/prog.tmp template/template.cfg
	python3 ./tools/mkxml.py /tmp/prog.tmp template/template.cfg $@

