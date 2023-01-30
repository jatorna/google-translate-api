# Google Translate Python API
A Python FASTApi application which wraps data from Google Translate.

## Files
For the development of the backend, Hexagonal Architecture has been used

```
.
├── backend                                                              # Backend folder
│   ├── infra                                                            # Infrastructure Layer
│   │   └── database                                                     # Database Infra  
│   │       ├── database.py                                              # Database engine
│   │       └── models.py                                                # Database models
│   ├── internal                                                         # Intenal Layer
│   │   ├── adapters                                                     # Adapters
│   │   │   └── outputs                                                  # Output adapters
│   │   │       ├── api                                                     
│   │   │       │   └── googletranslate                                     
│   │   │       │       └── google_translate_extended_api_adapter.py     # Google translate API adapter
│   │   │       └── database     
│   │   │           └── word         
│   │   │               └── word_storage.py                              # Word storage adapter
│   │   └── core                                                         # Core Layer
│   │       ├── entities                                                        
│   │       │   └── schemas.py                                           # Schemas
│   │       ├── ports              
│   │       │   └── word         
│   │       │       └── word_ports.py                                    # Word use case ports
│   │       └── usecases 
│   │           └── word         
│   │               └── word_usecase.py                                  # Word use case
│   ├── scripts                                                          # Useful scripts
│   │   └── javascript                                                   # Javascript scripts 
│   │       └── google_translate_extended_api.js                         # google-translate-extended-api script                                                     
│   ├── Dockerfile                                                       # Backend Dockerfile         
│   ├── main.py                                                          # main file to run the api
│   └── requirements.txt                                                 # Python requirements file
├── grafana                                                              # Grafana config files
│   ├── dashboards                                  
│   │   └── dashboard.json                                               # App dashboard
│   ├── datasources              
│   │   └── datasource.yml                                               # App datasource for Grafana
│   └── dashboard.yaml           
├── prometheus                                                           # Prometheus config files
│   └── prometheus.yml                                                   # Prometheus config file
├── docker-compose.yml                                                   # Docker compose file to app deployment
├── env.example                                                          # .env example file
├── LICENSE                                                              # License file
├── Makefile                                                             # Makefile file
└── README.md                                                            # Readme file
```

## Deploy!
```bash
cp env.example .env
docker-compose up -d
```


### Endpoints
- API endpoint: `localhost:8888/api/v1`
- Metrics endpoint: `localhost:8888/metrics`
- Prometheus endpoint: `localhost:9090`
- Grafana Endpoint: `localhost: 3000`

Login into grafana using the creds mentioned in the `.env` file and open the dashboard.


## Play!
http://jatornahost.ddns.net:8888/api/v1/

## Future Improvements
- Unit testing
- Logging monitoring (e.x. Elastic + Kibana)
- Authorization system
- E2E testing
