from setuptools import setup

setup(name='bluetorch',
      version='0.111',
      description='Pytorch Blue Print for Research Project',
      url='https://github.com/dspoka/bluetorch.git',
      author='Daniel Spokoyny',
      author_email='dspoka@gmail.com',
      license='MIT',
      packages=['bluetorch', 'bluetorch.logger', 'bluetorch.saver', 'bluetorch.experiment', 'bluetorch.base'],
      zip_safe=False)