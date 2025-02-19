.PHONY: all clean

all: simple.pdf complex.pdf

simple.pdf: simple.md
	pandoc $< -o $@ --template eisvogel --listings --metadata date="`date +%F`"

complex.pdf: complex.md
	pandoc $< -o $@ --template eisvogel --listings --metadata date="`date +%F`"

clean:
	rm -f simple.pdf complex.pdf
