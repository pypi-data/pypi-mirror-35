from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = ['ply']

setup(
    author="Francesco Fuggitti",
    author_email='francesco.fuggitti@gmail.com',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    description="Python .dot parser specific for MONA dfa output",
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords='dotpy',
    name='dotpy',
    packages=find_packages(include=['dotpy*']),
    url='https://github.com/Francesco17/dotpy',
    version='0.0.1',
)