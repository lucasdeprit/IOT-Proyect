import requests

#    curl -H "Accept: application/csv" -G 'https://corlysis.com:8086/query'  
#--data-urlencode "db=Technology_Health_Computing" -u token:ecbef8c057c4ebac95399b37189bcf5e 
#--data-urlencode "q=select * from meas_test where time >= now() - 10000s"
url = 'https://corlysis.com:8086/query'

h = {
"Accept":"application/json",
"Authorization": "ecbef8c057c4ebac95399b37189bcf5e"
}
params = {
    "db":"Technology_Health_Computing",
    "q":"select * from meas_test where time >= now() - 10000s"
}

r = requests.get(url, headers=h, params=params)
print(r)
