"""Static assest"""
from flask import current_app as app
from flask_assets import Bundle


def assemble_static(assets):
    assets.auto_build = True
    assets.debug = False
    gen_bundle = Bundle(
        'src/less/*.less',
        filters='less, cssmin',
        output='dist/css/style.css',
        extra={'rel':   'stylesheet/less'}
    )
    assets.register('gen_bundle', gen_bundle)
    gen_bundle.build()
    return assets
