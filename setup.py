from setuptools import setup, find_packages
setup(
    name="org2py",
    version="0.1",
    packages=find_packages(),
    # scripts=['org2py.py'],
    entry_points={
        'console_scripts': [
            'org2py=org2py:main',
        ],
    },
)
