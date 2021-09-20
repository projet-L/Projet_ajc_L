#!/bin/bash
docker run --name test-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:latest

