from datetime import datetime
from elasticsearch import Elasticsearch
from requests import get
from time import sleep


def creat_and_update_index(index_name, doc_type):
	es = Elasticsearch()
	try:
		es.indices.create(index=index_name)
	except Exception:
		pass
	
	es.indices.put_mapping(
		index = index_name,
		doc_type = doc_type,
		body = {doc_type:{'properties':{'location':{'type':'geo_point'}}}})

	return es


def get_data():
	url = "https://feeds.citibikenyc.com/stations/stations.json"
	r = get(url)
	r.raise_for_status()
	result = r.json()
	stations = result['stationBeanList']
	
	return stations

if __name__ == '__main__':
	
	#step 1: create an elastic search index to store data
	es = creat_and_update_index('citibike-index', 'stations')

	i = 0
	while True:
		i += 1
		#step 2: fetch data from the internets
		docks = get_data()

		#step 3: push data into elastic searc

		for dock in docks:
			dock['lastCommunicationTime'] = datetime.strptime(
				dock['lastCommunicationTime'],
				'%Y-%m-%d %I:%M:%S %p')

			dock['location'] = {
			'lat':dock['latitude'],
			'lon':dock['longitude']}

			res = es.index(index='citibike-index', doc_type='stations', body=dock)
			print(res['result'])

		print(f"DONE LOADING {i}, SLEEPING...")
		sleep(30)





