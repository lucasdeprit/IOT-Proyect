#!/bin/bash
curl -H "Accept: application/csv" -G 'https://corlysis.com:8086/query'  --data-urlencode "db=Technology_Health_Computing" -u  token:3f7e15aa74f0d3b3a82917297b280976 --data-urlencode "q=select * from meas_test " >> "/home/pi/IOT-Proyect/Data/data_$(date +%F)".csv 

curl -H "Accept: application/csv" -G 'https://corlysis.com:8086/query'  --data-urlencode "db=Technology_Health_Computing" -u  token:3f7e15aa74f0d3b3a82917297b280976 --data-urlencode "q=select * from temp_test " >> "/home/pi/IOT-Proyect/Data/data_temp_$(date +%F)".csv 

curl -H "Accept: application/csv" -G 'https://corlysis.com:8086/query'  --data-urlencode "db=Technology_Health_Computing" -u  token:3f7e15aa74f0d3b3a82917297b280976 --data-urlencode "q=select * from humi_test  " >> "/home/pi/IOT-Proyect/Data/data_humi_$(date +%F)".csv 

python /home/pi/IOT-Proyect/Data/mail.py

exit
