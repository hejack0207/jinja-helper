all:

test:
python setup.py test

docs:
python setup.py docs

.PHONY: test docs
