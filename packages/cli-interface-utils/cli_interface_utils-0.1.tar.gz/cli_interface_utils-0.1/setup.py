# http://python-packaging.readthedocs.io/en/latest/minimal.html#picking-a-name

from setuptools import setup

setup(
    name='cli_interface_utils',
    version='0.1',
    description='create a CliInterface, extends AbstractCliWorker, now you have a working cli application',
    url='https://github.com/FabioCingottini/cli_interface_utils',
    author='Fabio Cingottini',
    author_email='fabio.cingottini@gmail.com',
    license='MIT',
    packages=['cli_interface_utils'],
    zip_safe=False,
    classifiers=(
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    )
)
