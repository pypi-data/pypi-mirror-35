from setuptools import setup, find_packages

setup(
    name='rustcfg',
    version='0.0.2',
    description='Rust cfg expression parser in python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Zbigniew Jędrzejewski-Szmek',
    author_email='zbyszek@in.waw.pl',
    license='MIT',
    url='https://pagure.io/fedora-rust/python-rustcfg',
    packages=find_packages(),
    install_requires=['pyparsing'],
    extras_require={
        'test': ['pytest'],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        "Programming Language :: Python :: 3 :: Only",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Utilities',
    ],
)
