from setuptools import setup
import platform

setup(name='obnl-wrapper',
      version='0.4.0',

      maintainer='The OBNL Team',
      maintainer_email='gillian.basso@hevs.ch',

      url='https://github.com/IntegrCiTy/obnl',
      download_url='https://github.com/IntegrCiTy/obnl',

      platforms=[platform.platform()],  # TODO indicate really tested platforms

      install_requires=['pika', 'protobuf', 'obnl-core'],

      packages=['obnl.wrapper'],

      description='An open tool for co-simulation',
      long_description='README.md',

      license='Apache License 2.0',

      keywords='co-simulation,RabbitMQ,OBNL',

      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Console',
                   'Intended Audience :: Science/Research',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: Apache License 2.0',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 3.5',
                   'Topic :: Scientific/Engineering :: Energy Simulation'
                   ],
      zip_safe=False
      )
