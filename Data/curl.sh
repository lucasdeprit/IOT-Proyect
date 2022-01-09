#!/bin/bash
curl -H "Accept: application/json" -G 'https://corlysis.com:8086/query'  --data-urlencode "db=Technology_Health_Computing" -u token:1dba55a4bca39916c0264efd2af30c63 --data-urlencode "q=select * from meas_test where time >= now() - 10000s" | json_pp >> "data_$(date +%F)".json 
curl -H "Accept: application/csv" -G 'https://corlysis.com:8086/query'  --data-urlencode "db=Technology_Health_Computing" -u token:1dba55a4bca39916c0264efd2af30c63 --data-urlencode "q=select * from meas_test where time >= now() - 10000s" >> "data_$(date +%F)".csv 
exit
