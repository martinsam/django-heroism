# -*- coding: utf-8 -*-
from your_project import settings

""" When browser use ssl connection / https all media are redefine """
def ssl_media(request):
    if request.is_secure():
        ssl_media_url = settings.MEDIA_URL.replace('http://', 'https://')
        ssl_media_img_url = settings.MEDIA_IMG_URL.replace('http://', 'https://')
        ssl_media_data_url = settings.MEDIA_DATA_URL.replace('http://', 'https://')
        ssl_media_css_url = settings.MEDIA_CSS_URL.replace('http://', 'https://')
        ssl_media_js_url = settings.MEDIA_JS_URL.replace('http://', 'https://')
		# ssl_foo_url ...
        return {
                'MEDIA_URL': ssl_media_url,
                'MEDIA_IMG_URL': ssl_media_img_url,
                'MEDIA_DATA_URL' : ssl_media_data_url,
                'MEDIA_CSS_URL' : ssl_media_css_url,
                'MEDIA_JS_URL' : ssl_media_js_url,
                #MEDIA_FOO_URL ....
                }
    else:
        return {'': ''}
