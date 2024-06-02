from setuptools import setup, find_packages

setup(
    name="fibonacci_project",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # List your project's dependencies here
    ],
    entry_points={
        'console_scripts': [
            'fibonacci=fibonacci.fibonacci:main',
        ],
    },
    test_suite='tests',
)

