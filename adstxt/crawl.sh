#!/bin/bash
if [ ! -d "csv" ]
then
    echo "Adding directory csv in `pwd`"
    mkdir -p csv
    echo "Added directory successfully."
fi
scrapy crawl -a fileInfo=$1 adstxt
lastStatusCode=$(echo $?)
if [ $lastStatusCode -ne 0 ]
then
    echo "******************************************************************************" >> crawl.sh.log
    echo "Something went wrong here. Please check scrapy.log" >> crawl.sh.log
    echo "******************************************************************************" >> crawl.sh.log
else
    jobId=`echo $1 | awk -F ":" '{print $1}'`
    echo "Done crawling for jobId $jobId." >> crawl.sh.log
    python schedule_zip.py $jobId
fi
