import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pyajax',
    version='0.0.5',
    url='https://github.com/washim/pyajax',
    license='BSD',
    author='Washim Ahmed',
    author_email='washim.ahmed@gmail.com',
    description='Develop ajax based analytical dashboard without writing any javascript.',
    long_description=long_description,
    packages=setuptools.find_packages(),
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)