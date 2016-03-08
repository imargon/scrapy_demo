# -*- coding: utf-8 -*-

# Scrapy settings for lagou_python project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'lagou_python'

SPIDER_MODULES = ['lagou_python.spiders']
NEWSPIDER_MODULE = 'lagou_python.spiders'
WEBKIT_DOWNLOADER=['lagou']
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'lagou_python (+http://www.yourdomain.com)'

DOWNLOAD_DELAY=3
ITEM_PIPELINES = {
    'lagou_python.pipelines.LagouPythonPipeline':300
}

COOKIES_ENABLED = False
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'TBBKAnalysis (+http://www.yourdomain.com)'
DOWNLOADER_MIDDLEWARES = {
     'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
     'lagou_python.spiders.rotate_useragent.RotateUserAgentMiddleware' :400,
     'lagou_python.spiders.middleware.WebkitDownloader':543
}


LOG_LEVEL = 'DEBUG'
LOG_FILE = 'log.txt'