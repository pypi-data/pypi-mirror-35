from setuptools import setup, find_packages

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name='pingstats',
    version='0.4.3',
    description='Simple ping visualization on the CLI',
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url='http://gitlab.com/eclectickmediasolutions/pingstats',
    author='Ariana Giroux',
    author_email='ariana.giroux@gmail.com',
    license='MIT',
    packages=find_packages(),
    zip_safe=True,
    entry_points={
        'console_scripts': ['pingstats=pingstats:run'],
    },
    classifiers=(
                "Programming Language :: Python :: 3",
                "License :: OSI Approved :: MIT License",
                "Operating System :: OS Independent",
                "Development Status :: 4 - Beta",
                "Environment :: Console",
                "Intended Audience :: Developers",
                "Intended Audience :: End Users/Desktop",
                "Intended Audience :: Information Technology",
                "License :: OSI Approved :: MIT License",
                "Operating System :: Unix",
                "Topic :: System :: Networking :: Monitoring",
                "Topic :: Utilities",
    ),
)
