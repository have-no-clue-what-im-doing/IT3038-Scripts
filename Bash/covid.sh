#!/bin/bash
# This script downloads covid data and displays it

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
neg=$(echo $DATA | jq '.[0].negative')
death=$(echo $DATA | jq '.[0].death')
deathinc=$(echo $DATA | jq '.[0].deathIncrease')
TODAY=$(date)

echo "On $TODAY, there were $POSITIVE positive COVID cases and $neg negative cases. There are currently $death deaths with an increase of $deathinc"
