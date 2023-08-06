import sys
from setuptools import setup, find_packages

version = '1.2.13'

# pypi publishing
# 1. set $HOME/.pypirc
#      [distutils]
#      index-servers =
#          pypi
#
#      [pypi]
#      username: <name>
#      password: <password>
# 2. deactivate  // if there's an active env
# 3. cd pycharmenv3; source bin/activate
# 4. pip3 install --upgrade wheel setuptools twine
# 5. cd <whatever_to>/foxyproxy
# 6. rm -rf dist/*
# 7. python3 setup.py dist bdist_wheel
# 8. twine upload dist/<latest>.tar.gz
# 9. you can test it with "pip3 install --upgrade --no-cache-dir foxyproxy"


install_requires = [
    'cryptography>=1.5.2',
    'idna<2.7,>=2.5',
    'requests>=2.11.1',
    'coloredlogs>=9.0',
    'setuptools>=39.0'
]

if sys.version_info < (3,):
    # install_requires.append('scapy-ssl_tls')
    pass
else:
    # install_requires.append('scapy-python3')
    pass

setup(
    name='foxyproxy',
    version=version,
    packages=find_packages(),
    namespace_packages=['foxyproxy'],
    include_package_data=True,
    install_requires=install_requires,
    url='http://cloudfoxy.com',
    long_description=open('README.md', 'r').read(),
    license=open('LICENSE', 'r').read(),
    author='Enigma Bridge Ltd, Smart Arcs Ltd',
    author_email='support@smartarchitects.co.uk',
    description='TCP proxy for Cloud Foxy - cloud platform for smart cards',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Security',
        'Topic :: System :: Networking',
        'Topic :: Internet :: Proxy Servers'
    ],
    extras_require={
        # 'dev': dev_extras,
        # 'docs': docs_extras,
    },

    entry_points={
        'console_scripts': [
            'foxyproxy=foxyproxy.run_proxy:main'
        ],
    }
)
