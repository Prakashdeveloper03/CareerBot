#!/bin/bash

[ -f "./data/courses/coursera/coursera.csv" ] && mv "./data/courses/coursera/coursera.csv" "./data/courses.csv" && echo "File moved successfully." || echo "Coursera CSV file does not exist."
[ -d "./data/courses/" ] && rm -rf "./data/courses/" && echo "Directory 'courses' removed successfully." || echo "Directory 'courses' does not exist."