#!/bin/bash

for i in {1..3}
do
	python3 split.py url.csv >> times3.txt
done
