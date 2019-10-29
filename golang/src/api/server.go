package main

import (
	"./handler"

	"./cache"
	"./config"
	"github.com/labstack/echo"
	"github.com/labstack/echo/middleware"
)

func init() {
	config.SetEnvironment()
	cache.Initialize()
}

func main() {
	// Echoのインスタンス作る
	e := echo.New()

	e.Use(middleware.Logger())
	e.Use(middleware.Recover())

	// ルーティング
	// イベント情報を返すAPI
	e.GET("/event/info", handler.EventInfoGet)

	// サーバー起動
	e.Start(":1333")
}
