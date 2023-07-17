
<h1 align="center">Quack 3 Parser</h1>

<p align="center">
  <i align="center">Instantly read and parse your Quake 3 game log into valuable data. 🚀</i>
</p>

<h4 align="center">
  <a href="https://github.com/lucasmatsui/quake3-parser/actions/workflows/analysis.yaml">
    <img src="https://img.shields.io/github/actions/workflow/status/lucasmatsui/quake3-parser/analysis.yaml?branch=main&label=unit%20tests&style=flat-square" alt="continuous integration">
  </a>
  <a href="https://github.com/lucasmatsui/quake3-parser/graphs/contributors">
    <img src="https://img.shields.io/github/contributors-anon/lucasmatsui/quake3-parser?color=yellow&style=flat-square" alt="contributers">
  </a>
</h4>

<p align="center">
    <img src="https://github.com/lucasmatsui/quake3-parser/assets/31348487/cf66d8fc-ae9f-42ec-9056-3b930e1615fc" alt="dashboard"/>
</p>

## Development
<details>
<summary>
Pre-requisites
</summary> <br />
To be able to start development on quake3-parser make sure that you have the following pre-requisites installed:

- Docker
- Docker compose
- Git
</details>

<details open>
<summary>
Setup
</summary> <br />

1. Clone the repository:
```shell
git clone https://github.com/lucasmatsui/quack3-parser.git && cd quack3-parser
```

2. Run build with docker compose:
```shell
docker compose build --no-cache
```

3. Run run container:
```shell
docker compose compose up -d
```

4. If everything goes well, you will see this output:
```shell
docker logs -f quake3-parser
```
```logs
INFO:     Will watch for changes in these directories: ['/usr/src/application']
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [1] using WatchFiles
2023-07-16 19:27:51.516 | INFO     | app:<module>:5 - [*] Env Started!
2023-07-16 19:27:52.154 | INFO     | app.app_builder:__start_debugpy:17 - [*] Debug Started!
2023-07-16 19:27:52.156 | INFO     | app.app_builder:__start_fastapi:28 - [*] FastApi Started!
2023-07-16 19:27:52.156 | INFO     | app.app_builder:__start_load_routes:31 - [*] Load Routes Started!
2023-07-16 19:27:52.226 | INFO     | app.shared.config.start_load_routes:__bind_routes:48 - Loaded routes from app.quake3.ui.routes.import_log_file_route
INFO:     Started server process [8]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```
</details>

<details>
<summary>
Run Tests
</summary> <br />

1. Access the container:
```shell
docker exec -it quake3-parser bash
```

2. Run:
```shell
pytest -v
```
Visualization example:
```shell
platform linux -- Python 3.11.2, pytest-7.2.1, pluggy-1.2.0 -- /usr/local/bin/python
cachedir: .pytest_cache
rootdir: /usr/src/application, configfile: pyproject.toml
plugins: httpx-0.21.2, mock-3.10.0, cov-4.0.0, asyncio-0.20.3, anyio-3.7.1
asyncio: mode=Mode.AUTO
collected 8 items

tests/domain/model/game_test.py::test_game_creation PASSED                                                                                         [ 12%]
tests/domain/model/game_test.py::test_connect_player PASSED                                                                                        [ 25%]
tests/domain/model/game_test.py::test_connect_more_than_one_player PASSED                                                                          [ 37%]
tests/domain/model/game_test.py::test_connect_when_player_change_team PASSED                                                                       [ 50%]
tests/domain/model/game_test.py::test_when_player_die_to_world PASSED                                                                              [ 62%]
tests/domain/model/game_test.py::test_when_dead_by_himself PASSED                                                                                  [ 75%]
tests/domain/model/game_test.py::test_when_player_kill_enemies PASSED                                                                              [ 87%]
tests/domain/model/game_test.py::test_end_game PASSED
```
</details>

<details open>
<summary>
Features
</summary> <br />

1. Teams visualization
2. Map settings
3. Performance metrics (time, memory used)
4. Ranking within teams
5. Player infos
6. Kills by means

```shell
POST /v1/quack3/logs (200 OK)
{
  "time":"Duration: -0.11640238761901855s",
  "memory":"Allocate: 0 bytes",
  "count-games":21,
  "games":[
    {
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
        "free":[
          {
            "client_id":4,
            "ping":0,
            "score":20,
            "nickname":"Zeh",
            "character":"sarge/default",
            "health":100,
            "history_of_weapons":[

            ]
          },
          {
            "client_id":3,
            "ping":0,
            "score":19,
            "nickname":"Isgalamido",
            "character":"uriel/zael",
            "health":100,
            "history_of_weapons":[

            ]
          },
          {
            "client_id":5,
            "ping":0,
            "score":11,
            "nickname":"Assasinu Credi",
            "character":"sarge",
            "health":100,
            "history_of_weapons":[

            ]
          },
          {
            "client_id":2,
            "ping":0,
            "score":5,
            "nickname":"Dono da Bola",
            "character":"sarge",
            "health":95,
            "history_of_weapons":[

            ]
          }
        ],
        "blue":[

        ],
        "red":[

        ],
        "specs":[

        ]
      },
      "kills_by_means":{
        "MOD_TRIGGER_HURT":9,
        "MOD_FALLING":11,
        "MOD_ROCKET":20,
        "MOD_RAILGUN":8,
        "MOD_ROCKET_SPLASH":51,
        "MOD_MACHINEGUN":4,
        "MOD_SHOTGUN":2
      }
    }
  ]
}
```
</details>

## Contributers

<!---
npx contributer-faces --exclude "*bot*" --limit 70 --repo "https://github.com/amplication/amplication"

change the height and width for each of the contributors from 80 to 50.
--->

[//]: contributor-faces
<a href="https://github.com/lucasmatsui"><img src="https://avatars.githubusercontent.com/u/31348487?s=96&v=4" title="lucasmatsui" width="50" height="50"></a>

[//]: contributor-faces
