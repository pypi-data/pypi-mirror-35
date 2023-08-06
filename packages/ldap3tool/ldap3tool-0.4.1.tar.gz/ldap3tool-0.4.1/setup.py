"""
ldap3tool
--------------
Simple wrapper for ldap3
"""
from setuptools import setup

setup(
    name='ldap3tool',
    version='0.4.1',
    url='https://github.com/lixxu/ldap3tool',
    license='BSD',
    author='Lix Xu',
    author_email='xuzenglin@gmail.com',
    description='Simple wrapper for ldap3',
    long_description=__doc__,
    packages=['ldap3tool'],
    zip_safe=False,
    platforms='any',
    install_requires=['ldap3'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
