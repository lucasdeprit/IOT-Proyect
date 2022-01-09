############################################################
#
# InfluxDB SELECT sample
#
############################################################
# Version   Date        Author          Description
############################################################
# 1.0.0     2019-05-31  dorbae          Initialize
############################################################

import requests
from influxdb import DataFrameClient
url = 'https://corlysis.com:8086/query'
params = {"db": "Technology_Health_Computing", "u": "token", "p": "ecbef8c057c4ebac95399b37189bcf5e"}

client = DataFrameClient(host='corlysis.com', port=8086, username='', password='ecbef8c057c4ebac95399b37189bcf5e')
client.switch_database('Technology_Health_Computing')

def main():
    """Instantiate a connection to the InfluxDB."""
    
    results = client.query('SELECT * FROM meas_test')
    df = results['meas_test']
    print(df)
    #payload = 'meas_testce=bad' + ' value=' + str(distance)
    #r = requests.get(url ,params)

    #print("Querying data: " + str(r.json))
    #result = client.query(query)

    #for point in result.get_points():
    #    print(point)

if __name__ == '__main__':
    main()