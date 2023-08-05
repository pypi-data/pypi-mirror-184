import pathlib

from setuptools import setup, find_packages


def read(file_name):
    return pathlib.Path(pathlib.Path.cwd() / file_name).read_text()


setup(
    name='flask-bigapp',
    version='1.5.7',
    url='http://github.com/mbr/flask-bootstrap',
    license='GNU General Public License v2 or later (GPLv2+)',
    author='David Carmichael',
    author_email='carmichaelits@gmail.com',
    description='A Flask auto importer that allows your Flask apps to grow big.',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment', 'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Operating System :: OS Independent', 'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Natural Language :: English',
    ],
    install_requires=[
        'Flask',
        'toml',
    ],
    zip_safe=False,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
)
