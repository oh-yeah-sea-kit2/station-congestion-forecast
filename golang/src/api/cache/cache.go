package cache

import (
	"time"

	"../config"

	gocache "github.com/patrickmn/go-cache"
)

const (
	EventInfo = "event_info"
)

type CacheSet struct {
	Cache   *gocache.Cache
	MaxSize int
}

var caches map[string]CacheSet

func Initialize() {
	caches = map[string]CacheSet{}
	for key, value := range config.Config.Cache {
		if value.Enable {
			expiration := time.Duration(value.Expiration) * time.Second
			cleanup := time.Duration(value.Cleanup) * time.Second
			c := gocache.New(expiration, cleanup)
			cache := CacheSet{c, value.Size}
			caches[key] = cache
		}
	}
}

func Get(typeName, key string) (interface{}, bool) {
	if c, ok := caches[typeName]; ok {
		return c.Cache.Get(key)
	}
	return nil, false
}

func Set(typeName, key string, value interface{}) {
	if c, ok := caches[typeName]; ok {
		if c.Cache.ItemCount() < c.MaxSize {
			c.Cache.SetDefault(key, value)
		}
	}
}
