init:
	python3 -m venv venv
	venv/bin/pip install -r requirements.txt

run:
	venv/bin/python -m src.main $(url)