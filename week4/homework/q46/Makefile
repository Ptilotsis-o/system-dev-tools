.PHONY: all clean

SRCS := $(filter-out %.thumb.txt,$(wildcard images/*.txt))
THUMBS := $(SRCS:.txt=.thumb.txt)

all: $(THUMBS)

%.thumb.txt: %.txt
	python thumbnail.py $<

clean:
	rm -f images/*.thumb.txt
