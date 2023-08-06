from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='grewritingpool',
    version='0.0.3',
    description='Python Web Sidper for GRE Writing Pool',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=['grewritingpool'],
    author='callmepk',
    author_email='wotingwu@live.com',
    install_requires=[
          'lxml','beautifulsoup4','requests'
      ],
    keywords=['gre','writing'],
    url='https://github.com/patrick330602/grewritingpool'
)
