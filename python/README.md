

# spider追加
- scrapy genspider {spider名} {対象ドメイン名？}
## 例
- scrapy genspider scrapy_blog_spider blog.scrapinghub.com


# scrapy-do
## scrapy-do JOB追加
- scrapy-do-cl schedule-job --project {Project名} --spider {spider名} --when {"スケージュール"}
### スケジュールは以下参照のもと設定
- https://scrapy-do.readthedocs.io/en/latest/basic-concepts.html#scheduling-specs
### 例
- scrapy-do-cl schedule-job --project ten_min_scrapy --spider scrapy_m-messe --when "every hour at 00:15"

## scrapy-do JOB停止方法
- scrapy-do-cl cancel-job --job-id {identifier}

## JOB identifier 確認方法
- scrapy-do-cl list-jobs

## scrapy-do projects
- scrapy-do-cl list-projects
## scrapy-do spiders
- scrapy-do-cl --project {Project名} list-spiders
## scrapy-do 説明ページ
- https://scrapy-do.readthedocs.io/en/latest/


## scrapy shell
- fetch("https://www.marines.co.jp/game/schedule/201909/index.html")
