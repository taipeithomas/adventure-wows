# coding: utf-8

"""
    settings
    ~~~~~~~~

    Global settings for project.

    :copyright: (c) 2015 by Roman Zaiev.
    :license: BSD, see LICENSE for more details.
"""

import os


class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = "MY_VERY_SECRET_KEY"
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
    CSRF_ENABLED = False
    ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
    
    SITE_REFERENCES = [
	    u'Adenture Wow!', 
	    u'秘境與自然生態探索專家', 
	    [u'/about', u'關於我們'], 
	    [u'/about', u'為何選擇我們'], 
	    [u'/about', u'FB官網'], 
	    [u'/about', u'了解WaxiRiver'], 
	    [u'/about', u'客製化行程'], 
	    [u'http://www.google.com.tw', u'戶外裝備網'], 
	    [u'/member', u'會員專區'], 
	    [u'Welcome to Adenture Wow!', u'我們提供最深度的探索行程， 行程都是獨家開發的， 以最佳、最深入方式，探索當地特色以及自然與歷史人文，不會淪為走馬看花。我們擁有最多的戶外探索專業領隊與教練，每個行程依人數多寡，配置多位學有專精的領隊與安全教練。'],
	    [u'今夏最夯', u'上山下海窮究人煙罕至的美景']
    ]

    BLUEPRINTS = [
        'base.base',
        'info.info',
    ]

    EXTENSIONS = [
        'ext.db',
        'ext.assets',
        'ext.login_manager',
        'ext.gravatar',
        'ext.toolbar',
        # If you want Flask-RESTPlus out of the box
        # 'ext.api',
    ]

    CONTEXT_PROCESSORS = [
        'base.context_processors.common_context',
        'base.context_processors.navigation',
        'base.context_processors.common_forms',
    ]
    
    CSS_BASE_BUNDLE = [
        'css/bootstrap.min.css',
        'css/font-awesome.min.css',
        'css/bootstrapValidator.min.css',
        'css/skel.css',
        'css/style.css'
    ]

    JS_BASE_BUNDLE = [
        'js/jquery.min.js',
        'js/bootstrap.min.js',        
        'js/bootstrapValidator.min.js',
        'js/jquery.dropotron.min.js',
        'js/skel.min.js',
        'js/skel-layers.min.js',
        'js/init.js'
    ]
    
    EVENT_BASE_BUNDLE = [
		[True, u'烏岩角探索', u'烏岩角露營溯海與獨木舟', u'本行程必須配合海象與天候，且南方四島(東西吉、東西嶼坪)生活較為簡易、古樸原始，依照國家公園揭櫫的生態旅遊原則，我們當融入並體驗當地純樸的生活，並多與當地的歷史人文自然特色互動，但又不打擾居民生活。當地生活起居，不若台灣本島便利，此為其特色，亦是引入勝之處，這點仍請大家多體諒與配合，讓我們一起攜手探訪澎湖南方四島國家公園以及七美與望安的自然生態與歷史人文之美，謝謝大家。', 'img/pic01.jpg'], 
		[True, u'澎湖南方四島探索', u'澎湖藍洞與南方四島國家公園自然生態探索', u'本行程必須配合海象與天候，且南方四島(東西吉、東西嶼坪)生活較為簡易、古樸原始，依照國家公園揭櫫的生態旅遊原則，我們當融入並體驗當地純樸的生活，並多與當地的歷史人文自然特色互動，但又不打擾居民生活。當地生活起居，不若台灣本島便利，此為其特色，亦是引入勝之處，這點仍請大家多體諒與配合，讓我們一起攜手探訪澎湖南方四島國家公園以及七美與望安的自然生態與歷史人文之美，謝謝大家。', 'img/pic02.jpg'], 
		[True, u'澎湖東北海新祕境', u'澎湖東北海新秘境自然生態探索', u'本行程必須配合海象與天候，且南方四島(東西吉、東西嶼坪)生活較為簡易、古樸原始，依照國家公園揭櫫的生態旅遊原則，我們當融入並體驗當地純樸的生活，並多與當地的歷史人文自然特色互動，但又不打擾居民生活。當地生活起居，不若台灣本島便利，此為其特色，亦是引入勝之處，這點仍請大家多體諒與配合，讓我們一起攜手探訪澎湖南方四島國家公園以及七美與望安的自然生態與歷史人文之美，謝謝大家。', 'img/pic03.jpg'], 
		[True, u'野溪溫泉探索', u'野溪溫泉自然生態探索', u'本行程必須配合海象與天候，且南方四島(東西吉、東西嶼坪)生活較為簡易、古樸原始，依照國家公園揭櫫的生態旅遊原則，我們當融入並體驗當地純樸的生活，並多與當地的歷史人文自然特色互動，但又不打擾居民生活。當地生活起居，不若台灣本島便利，此為其特色，亦是引入勝之處，這點仍請大家多體諒與配合，讓我們一起攜手探訪澎湖南方四島國家公園以及七美與望安的自然生態與歷史人文之美，謝謝大家。', 'img/pic01.jpg'],
		[False, u'美國大峽周邊秘境探索', u'美國大峽周邊秘境探索', u'本行程必須配合海象與天候，且南方四島(東西吉、東西嶼坪)生活較為簡易、古樸原始，依照國家公園揭櫫的生態旅遊原則，我們當融入並體驗當地純樸的生活，並多與當地的歷史人文自然特色互動，但又不打擾居民生活。當地生活起居，不若台灣本島便利，此為其特色，亦是引入勝之處，這點仍請大家多體諒與配合，讓我們一起攜手探訪澎湖南方四島國家公園以及七美與望安的自然生態與歷史人文之美，謝謝大家。', 'img/pic02.jpg']
    ]
    
    SCHEDULE_BASE_BUNDLE = [
        [1, u'烏岩角溯海與獨木舟過當日團', '2017-7-1', '2017-7-2'], 
        [1, u'烏岩角露營溯海與獨木舟過夜兩天團', '2017-7-1', '2017-7-2'], 
        [3, u'澎湖東北海新祕境自然生態探索三天團', '2017-7-1', '2017-7-2'], 
        [2, u'澎湖藍洞與南方四島國家公園生態教育團', '2017-7-1', '2017-7-2'], 
        [2, u'澎湖藍洞與南方四島國家公園親子團', '2017-7-1', '2017-7-2'], 
        [2, u'澎湖藍洞與南方四島國家公園五天團', '2017-7-1', '2017-7-2'], 
        [2, u'澎湖藍洞與南方四島國家公園三天團', '2017-7-1', '2017-7-2'], 
        [2, u'澎湖藍洞與南方四島國家公園兩天團', '2017-7-1', '2017-7-2'], 
        [2, u'澎湖藍洞與南方四島國家公園當日團', '2017-7-1', '2017-7-2']
    ]
    

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    DEBUG_TB_PROFILER_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
