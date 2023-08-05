
from setuptools import setup, find_packages

repo_name = 'litelab'

# generate requirements file with !pipreqs litelab --mode no-pin --force
install_requirements = open("litelab/requirements.txt").read().split()

setup(name=repo_name,
      version='0.0.1',
      description='Create lightweight configs for instantiating ML experiments',
      author='1lint',
      author_email='105617163+1lint@users.noreply.github.com',
      url=f'https://github.com/1lint/{repo_name}', 
      install_requires=install_requirements,
      packages=find_packages(exclude=('basic_gan', 'train_sd', 'interpolated_diffusion', 'configs')),
      entry_points={
            'console_scripts': [
                  "lite = litelab:main"
            ]
      },
      )

