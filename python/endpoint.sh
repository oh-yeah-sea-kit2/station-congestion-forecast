echo "Start script 'endpoint.sh'"
# source ~/.bashrc
# pyenv install anaconda3-5.3.1
# pyenv global anaconda3-5.3.1

cd ~
pip install --upgrade pip
pip install scrapy

scrapy version

pip install psycopg2-binary==2.8.3

# scrapy-do
pip install cryptography
pip install scrapy-do
mkdir -p /home/user/my-scrapy-do-data
cd /home/user/my-scrapy-do-data
scrapy-do scrapy-do
yum install -y unzip

cd /root/app/ten_min_scrapy/
scrapy-do-cl push-project

scrapy-do-cl schedule-job --project ten_min_scrapy --spider scrapy_m-messe --when "every hour at 00:15"
