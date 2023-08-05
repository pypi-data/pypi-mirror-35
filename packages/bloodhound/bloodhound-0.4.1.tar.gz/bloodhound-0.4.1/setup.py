from setuptools import setup

setup(name='bloodhound',
      version='0.4.1',
      description='Python based ingestor for BloodHound',
      author='Edwin van Vliet, Dirk-jan Mollema, Matthijs Gielen',
      author_email='edwin.vanvliet@fox-it.com, dirkjan.mollema@fox-it.com, matthijs.gielen@fox-it.com',
      url='https://github.com/fox-it/bloodhound.py',
      packages=['bloodhound',
                'bloodhound.ad',
                'bloodhound.enumeration'],
      license='MIT',
      install_requires=['dnspython', 'impacket', 'ldap3>=2.4.1', 'pyasn1>=0.4'],
      classifiers=[
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7'
      ],
      entry_points= {
        'console_scripts': ['bloodhound-python=bloodhound:main']
      }
      )
