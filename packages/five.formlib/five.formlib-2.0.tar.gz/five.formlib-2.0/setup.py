from setuptools import setup

version = '2.0'

setup(
    name='five.formlib',
    version=version,
    url='http://pypi.python.org/pypi/five.formlib',
    license='ZPL 2.1',
    description='zope.formlib integration for Zope.',
    author='Zope Foundation',
    author_email='zope-dev@zope.org',
    long_description=(open("README.rst").read() + "\n" +
                      open("CHANGES.rst").read()),
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Zope :: 4',
        'License :: OSI Approved :: Zope Public License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ],
    keywords='zope zope4 five formlib',
    packages=['five', 'five.formlib'],
    package_dir={'': 'src'},
    namespace_packages=['five'],
    include_package_data=True,
    install_requires=[
        'setuptools',
        'transaction',
        'zope.app.form',
        'zope.browser',
        'zope.browsermenu',
        'zope.component',
        'zope.event',
        'zope.formlib>=4.4',
        'zope.i18nmessageid',
        'zope.interface',
        'zope.lifecycleevent',
        'zope.location',
        'zope.publisher',
        'zope.schema',
        'ExtensionClass',
        'Zope',
    ],
    zip_safe=False,
)
