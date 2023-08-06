from setuptools import setup

setup(name='ludicrousdns',
      version='0.1',
      description='The fastest DNS resolver in the universe',
      url='https://gitlab.com/sheddow/ludicrousdns',
      author='Sigurd Kolltveit',
      author_email='sigurd.kolltveit@gmx.com',
      license='MIT',
      packages=['ludicrousdns'],
      install_requires=[
          'aiodns>=1.1.1',
      ],
      zip_safe=False)
