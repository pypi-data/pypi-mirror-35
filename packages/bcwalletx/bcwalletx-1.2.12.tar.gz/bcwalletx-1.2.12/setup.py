# https://youtu.be/kNke39OZ2k0?t=65

from setuptools import setup

setup(
        name='bcwalletx',
        version='1.2.12',
        description='Simple BIP32 HD cryptocurrecy command line wallet',
        author='David Bergen',
        author_email='david.bergen@gmx.net',
        url='https://github.com/dalijolijo/bcwalletx/',
        py_modules=['bcwalletx'],
	install_requires=[
            'clint==0.4.1',
            'blockcypher==1.0.69',
            'bitmerchantx==0.1.9',
            'tzlocal==1.2',
            ],
        entry_points='''
            [console_scripts]
            bcwalletx=bcwalletx:invoke_cli
        ''',
        packages=['bcwalletx'],
        )
