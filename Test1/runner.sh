#!/bin/bash

for i in {1..15}
do
	python3 split.py url.csv 800000 >> results3.txt
done
