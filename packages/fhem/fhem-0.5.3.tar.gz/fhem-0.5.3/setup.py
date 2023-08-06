from setuptools import setup

setup(name='fhem',
      version='0.5.3',
      description='Python API for FHEM home automation server',
      long_description='Uses socket or http(s) communication to set and get states from FHEM home automation server with optional SSL encryption and password support',
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
      ],
      keywords='fhem home automation',
      url='http://github.com/domschl/python-fhem',
      author='Dominik Schloesser',
      author_email='dsc@dosc.net',
      license='MIT',
      packages=['fhem'],
      zip_safe=False)
