from setuptools import setup

setup(name='shale',
      version='0.2',
      description='Shale token substitution utility',
      url='https://github.com/mgangl/shale',
      author='Mike Gangl',
      author_email='mike.gangl@gmail.com',
      license='MIT',
      packages=['shale'],
      scripts=['bin/shale'],
      zip_safe=False)
