# Analysis of Citi Bike Live Station Feed

Data Source: https://data.cityofnewyork.us/NYC-BigApps/Citi-Bike-Live-Station-Feed-JSON-/p94q-8hxh 

Number of Data: 104,832 
Number of Station: 936
To Run:
```
docker-compose up -d
```
```
docker-compose build pyth
```
```
docker-compose run -v $(pwd):/app -e APP_TOKEN=$(cat app_token) pyth python get_data.py page_size=1000 num_pages=10 output=results
```
```
docker-compose run pyth python main.py results
```
```
docker-compose down
```
![ScreenShot](https://github.com/xianchen2/citi_bike_live_station_fed/blob/master/Kiban-dashboard.png)

http://localhost:5601/app/kibana#/dashboard?_g=(refreshInterval:('$$hashKey':'object:395',display:'30%20seconds',pause:!t,section:1,value:30000),time:(from:now-12h,mode:quick,to:now))&_a=(description:'',filters:!(),fullScreenMode:!f,options:(darkTheme:!f,hidePanelTitles:!f,useMargins:!t),panels:!((embeddableConfig:(),gridData:(h:15,i:'2',w:24,x:24,y:0),id:'57a7fc10-8384-11ea-a8ae-2bd09f702392',panelIndex:'2',type:visualization,version:'6.3.2'),(embeddableConfig:(),gridData:(h:15,i:'4',w:24,x:24,y:15),id:'17b83300-8388-11ea-a8ae-2bd09f702392',panelIndex:'4',type:visualization,version:'6.3.2'),(embeddableConfig:(mapCenter:!(40.73685214795608,-73.96373748779298),mapZoom:11),gridData:(h:15,i:'5',w:24,x:0,y:0),id:'4e2d5360-837f-11ea-a8ae-2bd09f702392',panelIndex:'5',type:visualization,version:'6.3.2'),(embeddableConfig:(),gridData:(h:15,i:'6',w:24,x:0,y:15),id:e6552bb0-8382-11ea-a8ae-2bd09f702392,panelIndex:'6',type:visualization,version:'6.3.2')),query:(language:lucene,query:''),timeRestore:!f,title:'New%20Dashboard',viewMode:edit)
