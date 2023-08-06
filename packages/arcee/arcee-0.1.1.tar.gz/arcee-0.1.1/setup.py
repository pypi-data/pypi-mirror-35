from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='arcee',
    version='0.1.1',
    author='tdkihrr',
    author_email='huanghezhao@outlook.com',
    url='https://github.com/tdkihrr/arcee',
    keywords='parser-generator',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    python_requires='>=3.4.0',
    description='LL(1) parser generator',
    platforms='any',
    packages=[
        'arcee', 'arcee.generator', 'arcee.utils', 'arcee.lexer', 'arcee.parser'
    ],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'arcee=arcee:arcee'
        ]
    }
)
