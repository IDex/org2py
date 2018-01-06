from setuptools import setup
setup(
    name="org2py",
    version="0.1",
    py_modules=["org2py"],
    entry_points={
        'console_scripts': [
            'org2py=org2py:main',
        ],
    },
)
