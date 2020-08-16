#!/bin/bash

project_location="/home/vagrant/project"

if [ $pwd==project_location ]; then
	export GOPATH=/home/vagrant/project/tldrusstock/tldr/stockData/goGetStockData
	go run /home/vagrant/project/tldrusstock/tldr/stockData/goGetStockData/src/main/main.go &
	python3 ./tldrusstock/manage.py runserver 0.0.0.0:8000
else
	echo "Please change to project directory and run this again. Thanks!"
	exit 1
fi
