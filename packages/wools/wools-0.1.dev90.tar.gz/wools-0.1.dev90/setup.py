from setuptools import setup, find_packages


setup(
    name='wools',
    description="ADVA-Certified Alpakka Wools",

    author="ADVA Optical Networking",
    maintainer="Thomas Szyrkowiec",
    maintainer_email="tszyrkowiec@advaoptical.com",

    license="Apache License 2.0",

    setup_requires=open('requirements.setup.txt'),
    install_requires=['alpakka', 'jinja2'],

    use_scm_version={'local_scheme': lambda _: ''},

    packages=find_packages(include=['wools', 'wools.*']),

    entry_points={'alpakka_wools': [
        'Java=wools.java',
        'Akka=wools.java.akka',
        'Jersey=wools.java.jersey',
    ]},

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Telecommunications Industry',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Utilities',
    ],
    keywords=[
        'alpakka', 'pyang', 'yang', 'wrappers', 'wrapper', 'wools', 'wool',
        'templates', 'template', 'jinja2', 'jinja', 'python3',
    ],
)
