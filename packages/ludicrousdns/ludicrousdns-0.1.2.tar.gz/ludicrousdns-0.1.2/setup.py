import setuptools


with open('README.rst') as f:
    readme = f.read()

setuptools.setup(
    name='ludicrousdns',
    version='0.1.2',
    description='The fastest DNS resolver in the universe',
    long_description=readme,
    url='https://gitlab.com/sheddow/ludicrousdns',
    author='Sigurd Kolltveit',
    author_email='sigurd.kolltveit@gmx.com',
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires=[
        'aiodns>=1.1.1',
    ],
    python_requires='>=3.5',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=False)
