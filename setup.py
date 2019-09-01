from setuptools import setup

requires = ['numpy', 'pyaudio'],

setup(name='etuner',
      version='0.0.1',
      description='Musical instrument tuner',
      long_description='Musical instrument tuner',
      author='Guo Xiaoyong',
      author_email='guo.xiaoyong@gmail.com',
      url='https://github.com/guoxiaoyong/etuner',
      install_requires=requires,
      setup_requires=requires,
      packages=['etuner'],
      include_package_data=True,
      entry_points={
         'console_scripts': ['etuner=etuner:main'],
      },
)
