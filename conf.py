# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/Blog-With-GitHub-Boilerplate/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = "Kepler"
enable_jsdelivr = {
    "enabled": True,
    "repo": "PuppyGummy/Blog-With-GitHub-Boilerplate@gh-pages"
}

# 站点设置
site_name = "Kami的Blog"
site_logo = "${static_prefix}印章.png"
site_build_date = "2020-11-27T16:42+08:00"
author = "卡咪"
email = "815918091@qq.com"
author_homepage = ""
description = "能吃是福"
key_words = ['K@M1', 'Blog']
language = 'zh-CN'
external_links = [
    {
        "name": "",
        "url": "",
        "brief": ""
    },
    {
        "name": "",
        "url": "",
        "brief": ""
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
        "url": "https://twitter.com/AlanDecode",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/AlanDecode",
        "icon": "gi gi-github"
    },
    {
        "name": "Weibo",
        "url": "https://weibo.com/5245109677/",
        "icon": "gi gi-weibo"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
