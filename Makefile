package:
	rm -f launcher-ui.zip
	cd lib; zip -r launcher-ui.zip ui/*.py *.py;
	cd ..;
	mv lib/launcher-ui.zip ./;

serve:
	python -m http.server --directory web

run: package
	python launcher-ui.zip
