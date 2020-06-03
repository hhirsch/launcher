package:
	rm -f launcher-ui.zip
	cd lib; zip -r launcher-ui.zip *.py;
	cd ..;
	mv lib/launcher-ui.zip ./;

serve:
	python -m http.server --directory web
