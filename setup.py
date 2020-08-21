from setuptools import find_packages, setup

setup(
    name="dateline",
    version="0.1",
    packages=find_packages(),
    license="Private",
    description="Dateline ",
    author="sukhbinder",
    author_email="sukh2010@yahoo.com",
    entry_points={
        'console_scripts': ['dateline = dateline.main:main', 
                            'timewords = dateline.main:main_tw'],
    },

)
