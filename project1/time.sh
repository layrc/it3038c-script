#!/bin/bash

echo "The current time in Eastern Time Zone is: $(TZ=US/Eastern date +%r)"
echo "The current time in Central Time Zone is: $(TZ=US/Central date +%r)"
echo "The current time in Mountain Time Zone is: $(TZ=US/Mountain date +%r)"
echo "The current time in Pacific Time Zone is: $(TZ=US/Pacific date +%r)"
echo "The current time in Alaska Time Zone is: $(TZ=US/Alaska date +%r)"
echo "The current time in Hawaii-Aleutian Time Zone is: $(TZ=US/Hawaii date +%r)"
