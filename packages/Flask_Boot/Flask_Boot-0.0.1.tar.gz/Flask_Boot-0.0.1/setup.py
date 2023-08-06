from setuptools import setup, find_packages
import flask_boot

entry_points = {
    "console_scripts": [
        "flask_boot = flask_boot.flask_cli:main",
    ]
}

with open("requirements.txt") as f:
    requires = [l for l in f.read().splitlines() if l]

setup(
    name='Flask_Boot',
    version=flask_boot.__version__,
    packages=find_packages(),
    include_package_data=True,
    description='Flask application generator for boosting your development.',
    long_description=open('README.rst').read(),
    url='https://github.com/wuxirenshi/flask-boot',
    author='xxd',
    author_email='369404843@qq.com',
    license='MIT',
    keywords='flask sample generator',
    install_requires=requires,
    entry_points=entry_points,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)