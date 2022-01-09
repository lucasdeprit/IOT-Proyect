#!/bin/bash
curl -H "Accept: application/json" -G 'https://corlysis.com:8086/query'  --data-urlencode "db=Technology_Health_Computing" -u token:ecbef8c057c4ebac95399b37189bcf5e --data-urlencode "q=select * from meas_test where time >= now() - 10000s" | json_pp >> "data_$(date +%F)".json 
exit
