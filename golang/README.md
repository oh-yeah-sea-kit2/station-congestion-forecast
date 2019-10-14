# Golang
## コンテナビルド、起動
- docker-compose build
	- docker-compose build --no-cache
- docker-compose up -d --build

## コンテナに入る
- docker-compose exec golang bash

## Log確認
- docker-compose logs <service name>
	- 文字化けとかあるかも…
- docker logs <container name> -f
- docker logs station_congestion_forecast_golang_1 -f


## コンテナ一覧 Status
- docker-compose ps

## goenv update
バージョン上げないように…。上がるとGoのversionごとにディレクトリを切ってしまう問題？がある。
- cd $GOENV_ROOT
- git pull origin master
- goenv install -l

