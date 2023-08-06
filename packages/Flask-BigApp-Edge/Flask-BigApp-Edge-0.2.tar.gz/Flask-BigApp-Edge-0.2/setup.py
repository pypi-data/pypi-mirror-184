import pathlib
from setuptools import setup, find_packages

readme = pathlib.Path(pathlib.Path.cwd() / "README.md").read_text()



setup(
    name='Flask-BigApp-Edge',
    version=f'0.2',
    url='https://github.com/CheeseCake87/Flask-BigApp/tree/edge',
    license='GNU General Public License v2 or later (GPLv2+)',
    author='David Carmichael',
    author_email='carmichaelits@gmail.com',
    description='This is the edge build of Flask-BigApp, this built '
                'may be very unstable, or not work at all. Version numbers will change a lot!',
    long_description=f'{readme}',
    long_description_content_type='text/markdown',
    platforms='any',
    classifiers=[
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
        'Flask-SQLAlchemy',
        'toml',
    ],
    zip_safe=False,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'flask-bigapp-edge = flask_bigapp_edge_cli:cli',
        ]
    }
)
