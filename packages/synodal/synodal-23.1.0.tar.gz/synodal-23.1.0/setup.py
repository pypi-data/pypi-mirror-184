from setuptools import setup

SETUP_INFO = dict(
    name='synodal',
    version='23.1.0',
    install_requires=[],
    scripts=['synodal.py'],
    description="Information about the SynodalSoft project",
    license_files=['COPYING'],
    author='Luc Saffre',
    author_email='luc.saffre@gmail.com')

SETUP_INFO.update(classifiers="""\
Programming Language :: Python
Programming Language :: Python :: 3
Development Status :: 4 - Beta
Intended Audience :: Developers
License :: OSI Approved :: GNU Affero General Public License v3
Natural Language :: English
Operating System :: OS Independent""".splitlines())

SETUP_INFO.update(long_description=open("README.rst").read())

if __name__ == '__main__':
    setup(**SETUP_INFO)
