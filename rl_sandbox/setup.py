from setuptools import setup, find_packages

setup(name='rl_sandbox',
      version='3.0.0+vpace',
      packages=[package for package in find_packages()
                if package.startswith('rl_sandbox')],
      install_requires=['gym>=0.15.4,<=0.23.0',
                        'numpy==1.26.4',
                        'tensorboard',
                        'torch==1.13',
                        'manipulator_learning @ git+ssh://git@github.com/vpace-anon/manipulator-learning@main#egg=manipulator_learning',
                        'ConfigArgParse',
                        'PyYAML']
      )
