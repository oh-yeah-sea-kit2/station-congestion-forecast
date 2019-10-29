package handler

import (
	"net/http"

	"github.com/k0kubun/pp"
	"github.com/labstack/echo"
)

// EventInfoGet イベント情報を得る。現在日付からdays分未来の範囲のイベント情報を返す
func EventInfoGet(c echo.Context) error {
	const (
		nameDays = "days"
	)
	days := c.QueryParam(nameDays)
	pp.Println(days)
	// 整数チェック
	// checkResult := CheckNumber(days)
	// if checkResult {
	// 	c.JSON(http.StatusInternalServerError, message.Get("ERR_SYSTEM_ERROR")})
	// }

	// レスポンス定義
	// {
	// 	"result": 1,
	// 	"event": [
	// 		{
	// 			"valid_time": "2019-10-31T19:00",
	// 			"title": "test",
	// 			"place": "aaa"
	// 		}
	// 	]
	// }

	return c.String(http.StatusOK, days)
}
