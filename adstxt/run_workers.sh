#!/bin/bash

crawlerLimit=$1
zipLimit=$2

for ((i=1; i<=$crawlerLimit; i++))
do
    python crawl_worker.py &
done

for ((i=1; i<=$zipLimit; i++))
do
    python zip_worker.py &
done
