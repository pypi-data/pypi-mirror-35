from setuptools import setup

setup(
        name='broker-cli',
        version='0.0.3',
        author = "Johannes Daniel Nuemm",
        author_email = "daniel.nuemm@blacktre.es",
        description = ("Executing scripts on a remote broker-shell"),
        license = "MIT",
        url = "http://blacktre.es",
        py_modules=['broker'],
        install_requires=[],
        entry_points='''
            [console_scripts]
            broker=broker:cli
        ''',
)
