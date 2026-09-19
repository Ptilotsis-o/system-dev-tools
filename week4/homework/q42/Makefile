.PHONY: all clean

all: final.md

book.md: chapter1.md chapter2.md combine.py
	python combine.py

final.md: book.md toc.py
	python toc.py

clean:
	rm -f book.md final.md
