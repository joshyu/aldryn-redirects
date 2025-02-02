from setuptools import find_packages, setup

from aldryn_redirects import __version__

REQUIREMENTS = [
    'tablib',
    'django-parler',
    'aldryn-translation-tools',
]

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]

setup(
    name='aldryn-redirects-fil',
    version=__version__,
    description='A modified version of django.contrib.redirects with multilingual target URLs.',
    author='Fidelity International',
    author_email='',
    url='https://github.com/aldryn/aldryn-redirects',
    packages=find_packages(),
    license='LICENSE.txt',
    platforms=['OS Independent'],
    install_requires=REQUIREMENTS,
    classifiers=CLASSIFIERS,
    include_package_data=True,
    zip_safe=False,
    test_suite='tests.settings.run',
)
