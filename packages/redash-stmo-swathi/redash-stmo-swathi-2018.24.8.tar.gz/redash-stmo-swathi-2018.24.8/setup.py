from setuptools import setup, find_packages

setup(
    name='redash-stmo-swathi',
    setup_requires=['setuptools_scm'],
    install_requires=[
        'dockerflow>=2018.4.0',
        'requests',
    ],
    version='2018.24.8',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    description="Extensions to Redash by Mozilla",
    author='Mozilla Foundation',
    author_email='dev-webdev@lists.mozilla.org',
    url='https://github.com/mozilla/redash-stmo',
    license='MPL 2.0',
    entry_points={
        'redash.extensions': [
            'dockerflow = redash_stmo.dockerflow:dockerflow',
            'datasource_health = redash_stmo.health:datasource_health',
            # 'api_endpoint = redash_stmo.api_endpoint:api_endpoint'
            'optimizer_endpoint = redash_stmo.optimizer_endpoint:optimizer_endpoint'
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment :: Mozilla',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
    ],
    zip_safe=False,
)
