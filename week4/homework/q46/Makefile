.PHONY: all clean

SRCS := $(wildcard images/*.txt)
THUMBS := $(SRCS:.txt=.thumb.txt)

all: $(THUMBS)

%.thumb.txt: %.txt
	python thumbnail.py $<

clean:
	rm -f images/*.thumb.txt
