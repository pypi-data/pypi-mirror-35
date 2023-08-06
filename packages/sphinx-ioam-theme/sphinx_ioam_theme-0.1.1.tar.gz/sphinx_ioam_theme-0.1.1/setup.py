from setuptools import setup

import versioneer

setup_args = dict(
    name='sphinx_ioam_theme',
    version=versioneer.get_version(),
    url="https://github.com/ioam/sphinx_ioam_theme",
    description="For nbsite",
    license="BSD-3",
    zip_safe=False,
    packages=['sphinx_ioam_theme'],
    package_data={'sphinx_ioam_theme': [
        'theme.conf',
        '*.html',
        'includes/*.html',
        'static/css/*.css',
        'static/js/*.js',
        'static/images/*.*'
    ]},
    include_package_data=True,
    entry_points = {
        'sphinx.html_themes': [
            'sphinx_ioam_theme = sphinx_ioam_theme',
        ]
    },
    python_requires = ">=2.7",

    install_requires =[
        "sphinx"
    ]
)

if __name__=="__main__":
    setup(**setup_args)
