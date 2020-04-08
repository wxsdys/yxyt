#!/bin/bash
mkdir /mysqlbak
cd /mysqlbak/webmsp/
rm -rf webmsp_$(date +%Y%m%d)
mkdir webmsp_$(date +%Y%m%d)
cd webmsp_$(date +%Y%m%d)
mysqldump -h 40.0.0.110 -uroot -pAsiainfomsp@123  identity > identity_$(date +%Y%m%d).sql

cd /mysqlbak/prdcmp/
rm -rf  cmp_$(date +%Y%m%d)
mkdir  cmp_$(date +%Y%m%d)
cd cmp_$(date +%Y%m%d)
mysqldump -h 40.0.0.20 -uroot -pAsiaInfo -P 13306   identity > identity_$(date +%Y%m%d).sql
mysqldump -h 40.0.0.20 -uroot -pAsiaInfo -P 13306   clouds > clouds_$(date +%Y%m%d).sql
mysqldump -h 40.0.0.20 -uroot -pAsiaInfo -P 13306   settings > settings_$(date +%Y%m%d).sql



cd /mysqlbak/wikijira/
rm -rf wiki_$(date +%Y%m%d)
mkdir wiki_$(date +%Y%m%d)
cd wiki_$(date +%Y%m%d)
mysqldump -h 40.0.0.123 -uroot -pasiainfomsp -P 13306 confluence > confluence_$(date +%Y%m%d).sql
mysqldump -h 40.0.0.123 -uroot -pasiainfomsp -P 13306 jiradb > jiradb_$(date +%Y%m%d).sql
 
aws s3 sync /mysqlbak/webmsp s3://webmsp --delete
aws s3 sync /mysqlbak/prdcmp s3://prdcmp --delete
aws s3 sync /mysqlbak/wikijira  s3://wikijira --delete





