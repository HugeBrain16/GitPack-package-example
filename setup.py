from setuptools import setup

setup(
name='Gitpack-pkgex',
version='0.0.1',
author='HugeBrain16',
author_email='joshtuck373@gmail.com',
description='Gitpack package example',
long_description=open('README.md').read(),
long_description_content_type='text/markdown',
keywords='package-example gitpack lol',
url='https://github.com/HugeBrain16/GitPack-package-example',
license='MIT',
packages=['lolpack'],
classifiers=[
		"Development Status :: 3 - Alpha",
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 3',
		'Intended Audience :: Developers'
	]
)