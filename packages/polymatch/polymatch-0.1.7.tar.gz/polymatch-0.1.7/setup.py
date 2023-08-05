from setuptools import setup, find_packages

import polymatch

setup(
    name='polymatch',
    version='.'.join(map(str, polymatch.__version__)),
    python_requires=">=3.4",
    description="A polymorphic pattern matching library for Python",
    url='https://github.com/TotallyNotRobots/polymatch',
    author='linuxdaemon',
    author_email='linuxdaemon@snoonet.org',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='library utility pattern-matching',
    packages=find_packages(),
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'regex'],
)
