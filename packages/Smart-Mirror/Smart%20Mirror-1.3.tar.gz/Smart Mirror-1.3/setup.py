from setuptools import setup

setup(
    name='Smart Mirror',
    version='1.3',
    entry_points = {
        "console_scripts": ['smart_mirror = smart_mirror.__main__:main']
        },
    long_description=__doc__,
    packages=['smart_mirror'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask>=1.0.2',
        'geocoder>=1.38.1',
        'Jinja2>=2.10',
        'weather-api==1.0.4'
    ],

    # metadata to display on PyPI
    author="Kushal Katta",
    author_email="kushal@katta.xyz",
    description="Smart Mirror Project",
    keywords="smart mirror intelligent system home automation",
    url="http://katta.xyz/SmartMirror/",
    project_urls={
        # "Bug Tracker": "https://bugs.example.com/HelloWorld/",
        # "Documentation": "https://docs.example.com/HelloWorld/",
        "Source Code": "https://github.com/KushalKatta/SmartMirror",
    }

    # could also include long_description, download_url, classifiers, etc.
)
