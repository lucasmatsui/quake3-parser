# Quake 3 Parser

# Setup
```log
docker compose build --no-cache\
docker compose up -d

INFO:     Will watch for changes in these directories: ['/usr/src/application']
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [1] using WatchFiles
2023-07-16 10:14:40.388 | INFO     | app:<module>:5 - [*] Env Started!
2023-07-16 10:14:40.995 | INFO     | app.app_builder:__start_debugpy:17 - [*] Debug Started!
2023-07-16 10:14:40.998 | INFO     | app.app_builder:__start_fastapi:28 - [*] FastApi Started!
2023-07-16 10:14:40.998 | INFO     | app.app_builder:__start_load_routes:31 - [*] Load Routes Started!
2023-07-16 10:14:41.031 | INFO     | app.shared.config.start_load_routes:__bind_routes:48 - Loaded routes from app.quake3.ui.routes.import_log_file_route
INFO:     Started server process [8]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### Tests
```bash
docker exec -it quake3-parser bash
pytest -v
```

### Routes
```js
POST /v1/quake3/logs
```
##### Response:
```json
{
  "time":"Duration: -0.022905349731445312s",
  "memory":"Allocate: 0 bytes",
  "count-games":2,
  "games":[
    {
      "id":"23a6dcd2-16f5-40d6-9804-fbd38130c448",
      "total_kills":100,
      "started_match":"1:47",
      "ended_match":"12:13",
      "settings":{
        "mapname":"q3dm17",
        "mode":"ALL",
        "time_limit":15,
        "frag_limit":20,
        "capture_limit":8,
        "max_ping_allowed":0,
        "min_ping_allowed":0,
        "max_total_players":0,
        "max_active_players":16
      },
      "teams":{
        "free":{
          "4":{
            "client_id":4,
            "ping":0,
            "score":20,
            "nickname":"Zeh",
            "character":"sarge/default",
            "team":0,
            "health":100,
            "history_of_weapons":[
              
            ]
          },
          "3":{
            "client_id":3,
            "ping":0,
            "score":19,
            "nickname":"Isgalamido",
            "character":"uriel/zael",
            "team":0,
            "health":100,
            "history_of_weapons":[
              
            ]
          },
          "5":{
            "client_id":5,
            "ping":0,
            "score":11,
            "nickname":"Assasinu Credi",
            "character":"sarge",
            "team":0,
            "health":100,
            "history_of_weapons":[
              
            ]
          },
          "2":{
            "client_id":2,
            "ping":0,
            "score":5,
            "nickname":"Dono da Bola",
            "character":"sarge",
            "team":0,
            "health":95,
            "history_of_weapons":[
              
            ]
          }
        },
        "red":{
          
        },
        "blue":{
          
        },
        "specs":{
          
        }
      },
      "kill_by_means":{
        "MOD_TRIGGER_HURT":9,
        "MOD_FALLING":11,
        "MOD_ROCKET":20,
        "MOD_RAILGUN":8,
        "MOD_ROCKET_SPLASH":51,
        "MOD_MACHINEGUN":4,
        "MOD_SHOTGUN":2
      }
    },
    {
      "id":"1337581d-5c57-4fe7-8311-cf35f0750963",
      "total_kills":151,
      "started_match":"2:33",
      "ended_match":"10:28",
      "settings":{
        "mapname":"Q3TOURNEY6_CTF",
        "mode":"CAPTURE_THE_FLAG",
        "time_limit":15,
        "frag_limit":20,
        "capture_limit":8,
        "max_ping_allowed":0,
        "min_ping_allowed":0,
        "max_total_players":0,
        "max_active_players":16
      },
      "teams":{
        "free":{
          
        },
        "red":{
          "2":{
            "client_id":2,
            "ping":0,
            "score":22,
            "nickname":"Isgalamido",
            "character":"uriel/zael",
            "team":1,
            "health":100,
            "history_of_weapons":[
              
            ]
          },
          "7":{
            "client_id":7,
            "ping":0,
            "score":16,
            "nickname":"Assasinu Credi",
            "character":"james",
            "team":1,
            "health":100,
            "history_of_weapons":[
              
            ]
          },
          "3":{
            "client_id":3,
            "ping":0,
            "score":3,
            "nickname":"Dono da Bola",
            "character":"sarge",
            "team":1,
            "health":95,
            "history_of_weapons":[
              
            ]
          }
        },
        "blue":{
          "5":{
            "client_id":5,
            "ping":0,
            "score":11,
            "nickname":"Oootsimo",
            "character":"razor/id",
            "team":2,
            "health":100,
            "history_of_weapons":[
              
            ]
          },
          "6":{
            "client_id":6,
            "ping":0,
            "score":11,
            "nickname":"Chessus",
            "character":"visor/blue",
            "team":2,
            "health":100,
            "history_of_weapons":[
              
            ]
          },
          "4":{
            "client_id":4,
            "ping":0,
            "score":9,
            "nickname":"Zeh",
            "character":"sarge/default",
            "team":2,
            "health":100,
            "history_of_weapons":[
              
            ]
          },
          "8":{
            "client_id":8,
            "ping":0,
            "score":-8,
            "nickname":"Mal",
            "character":"james",
            "team":2,
            "health":100,
            "history_of_weapons":[
              
            ]
          }
        },
        "specs":{
          
        }
      },
      "kill_by_means":{
        "MOD_TRIGGER_HURT":37,
        "MOD_RAILGUN":38,
        "MOD_ROCKET_SPLASH":35,
        "MOD_BFG_SPLASH":8,
        "MOD_ROCKET":25,
        "MOD_MACHINEGUN":7,
        "MOD_BFG":8,
        "MOD_FALLING":2
      }
    }
  ]
}
```
