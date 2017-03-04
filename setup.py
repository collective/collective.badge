from setuptools import setup, find_packages

version = '1.0.2.dev0'

long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.rst').read()
    + '\n' +
    open('CHANGES.rst').read()
    + '\n')

setup(
    name='collective.badge',
    version=version,
    description="A basic member badge system for Plone",
    long_description=long_description,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 5.0",
        "Framework :: Plone :: 5.1",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='plone badge',
    author='David Glick',
    author_email='david@glicksoftware.com',
    url='https://github.com/collective/collective.badge',
    license='GPL',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['collective', ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'collective.workspace',
        'plone.api',
        'Products.CMFPlone',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
        ],
        'develop': [
            'zest.releaser',
        ],
    },
    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
