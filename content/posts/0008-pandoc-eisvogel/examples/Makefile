.PHONY: all clean

all: simple-generic.pdf simple-eisvogel.pdf complex.pdf

simple-generic.pdf: simple.md
	pandoc $< -o $@ --metadata date="`date +%F`"

simple-eisvogel.pdf: simple.md
	pandoc $< -o $@ --metadata date="`date +%F`" --template eisvogel --listings

complex.pdf: complex.md
	pandoc $< -o $@ --template eisvogel --listings

clean:
	rm -f *.pdf
