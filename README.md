# Analysis of Citi Bike Live Station Feed Data

Leverage docker-compose to spin up an ElasticSearch+Kibana service, load all the data into ElasticSearch, and visualize/analyze with Kibana.

**To Run:**
```
docker-compose up -d
```

ElasticSearch: http://localhost:9200 Kibana: http://localhost:5601

```
docker-compose run pyth python main.py 
```
Shutting off:
```
docker-compose down
```

![ScreenShot](https://github.com/xianchen2/citi_bike_live_station_fed/blob/master/Kiban-dashboard.png)

Data Source: https://data.cityofnewyork.us/NYC-BigApps/Citi-Bike-Live-Station-Feed-JSON-/p94q-8hxh 

Number of Data: 104,832  


