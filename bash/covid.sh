#!/bin/bash
# This script downloads covid data and displays it

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
TODAY=$(date)
NEGATIVE=$(echo $DATA | jq '.[0].negative')
DEATH=$(echo $DATA | jq '.[0].death')
HOS=$(echo $DATA | jq '.[0].hospitalized')

echo "on $TODAY, there were $POSITIVE positive COVID cases, $NEGATIVE negative tests $DEATH deaths and $HOS hostpitalized"
