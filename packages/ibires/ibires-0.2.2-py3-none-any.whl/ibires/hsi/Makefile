.PHONY: all
all: clean merged.json

1.json:
	echo "" > hsi1.json
	scrapy runspider -L'INFO' 1.py -o 1.json

2.json:
	echo "" > hsi2.json 
	scrapy runspider -L'INFO' 2.py -o 2.json

merged.json: 1.json 2.json
	python3 merge.py

clean:
	rm -f 1.json 2.json merged.json
