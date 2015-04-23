# -*- coding: utf-8 -*-

# Scrapy settings for eduline project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'eduline'

SPIDER_MODULES = ['eduline.spiders']
NEWSPIDER_MODULE = 'eduline.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'eduline (+http://www.yourdomain.com)'

# PipeLines settings
ITEM_PIPELINES = {
    'eduline.pipelines.SpecialityPipeline': 1,
}

# Log Settings
LOG_FILE = 'gkcx.eol.cn.log'
LOG_LEVEL = 'INFO'

# Download delay settings
DOWNLOAD_DELAY = 0.5  # According to Random mechanism, delay will be 0.5 * (0.5~1.5)