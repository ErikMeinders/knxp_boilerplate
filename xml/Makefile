/tmp/prog.tmp:  template/template.in ApplicationProgram
	python3 ./tools/subst.py $< ApplicationProgram $@

%.xml:  /tmp/prog.tmp template/template.cfg
	python3 ./tools/mkxml.py /tmp/prog.tmp template/template.cfg $@

