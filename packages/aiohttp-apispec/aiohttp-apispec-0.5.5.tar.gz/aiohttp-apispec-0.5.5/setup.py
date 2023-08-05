from setuptools import find_packages
from setuptools import setup


def readme(fname):
    with open(fname) as fp:
        content = fp.read()
    return content


setup(
    name='aiohttp-apispec',
    version='0.5.5',
    description='Build and document REST APIs with aiohttp and apispec',
    long_description=readme('README.md'),
    long_description_content_type="text/markdown",
    author='Danilchenko Maksim',
    author_email='dmax.dev@gmail.com',
    packages=find_packages(exclude=('test*',)),
    package_dir={'aiohttp_apispec': 'aiohttp_apispec'},
    include_package_data=True,
    install_requires=['aiohttp', 'apispec<=0.38.0', 'webargs'],
    license='MIT',
    url='https://github.com/maximdanilchenko/aiohttp-apispec',
    zip_safe=False,
    keywords='aiohttp marshmallow apispec swagger',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
)
