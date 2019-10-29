package config

import (
	"io/ioutil"
	"os"

	yaml "gopkg.in/yaml.v2"
)

type (
	// Environment 環境
	Environment struct {
		Environment Conf `yaml:"environment"`
	}
	// Conf 設定
	Conf struct {
		Database Database         `yaml:"db"`
		Log      Log              `yaml:"log"`
		Cache    map[string]Cache `yaml:"cache"`
	}
	// Database データベース
	Database struct {
		// User       string `yaml:"user"`
		// Password   string `yaml:"password"`
		// Name       string `yaml:"name"`
		Connection string `yaml:"connection"`
	}
	// Log ログ
	Log struct {
		Level  string `yaml:"level"`
		Stdout bool   `yaml:"stdout"`
	}
	// Cache キャッシュ
	Cache struct {
		Size       int  `yaml:"size"`
		Expiration int  `yaml:"expiration"`
		Cleanup    int  `yaml:"cleanup"`
		Enable     bool `yaml:"enable"`
	}
)

// Config 設定の初期化
var Config Conf

// SetEnvironment 環境値のセット
func SetEnvironment() {
	env := os.Getenv("ENVIRONMENT")
	var filepath string
	if env == "local" {
		filepath = "../config/environment.yml"
	} else {
		filepath = "../config/environment.yml"
	}
	var environment Environment
	buf, err := ioutil.ReadFile(filepath)
	if err != nil {
		panic(err)
	}
	err = yaml.Unmarshal(buf, &environment)
	if err != nil {
		panic(err)
	}
	Config = environment.Environment
}
