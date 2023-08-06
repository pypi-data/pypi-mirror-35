import sys
from setuptools import setup, find_packages

version = '0.1'

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
# 4. pip3 install --upgrade wheel setuptools
# 5. pip3 install --upgrade setuptools
# 6. cd .../foxy_tcpproxy
# 6. python3 setup.py sdist bdist_wheel upload
# 7. you can test it with "pip3 install --upgrade --no-cache-dir foxy_tcpproxy"


install_requires = [
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
    name='keychestbot',
    version=version,
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    url='http://keychest.net',
    long_description=open('README.md').read(),
    license=open('LICENSE').read(),
    author='Radical Prime Limited',
    author_email='support@radicalprime.com',
    description='Client bot for KeyChest monitoring service',
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
            'keychestbot=keychestbot.bot:main'
        ],
    }
)
