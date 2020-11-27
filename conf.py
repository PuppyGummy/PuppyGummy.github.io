# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = "Galileo"
enable_jsdelivr = {
    "enabled": True,
    "repo": "PuppyGummy/PuppyGummy.github.io@gh-pages"
}

# 站点设置
site_name = "Kami的Blog"
site_logo = "${static_prefix}icon.png"
site_build_date = "2020-11-27T16:42+08:00"
author = "卡咪"
email = "815918091@qq.com"
author_homepage = ""
description = "能吃是福"
key_words = ['K@M1', 'Blog']
language = 'zh-CN'
external_links = [
    {
        "name": "我的质问箱",
        "url": "https://www.pomeet.com/puppy509",
        "brief": "来匿名提问吧"
    },
    {
        "name": "我的bilibili",
        "url": "https://space.bilibili.com/1723019",
        "brief": "有时会直播教学C语言"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com/chokorekami",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/PuppyGummy",
        "icon": "gi gi-github"
    },
    {
        "name": "Weibo",
        "url": "https://weibo.com/2485411230/",
        "icon": "gi gi-weibo"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
