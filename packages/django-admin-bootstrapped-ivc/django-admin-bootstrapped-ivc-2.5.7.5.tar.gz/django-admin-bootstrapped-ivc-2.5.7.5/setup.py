from setuptools import setup, find_packages
import os

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]

setup(
    author="Riccardo Forina",
    author_email="riccardo@forina.me",
    maintainer="Riccardo Magliocchetti",
    maintainer_email="riccardo.magliocchetti@gmail.com",
    name='django-admin-bootstrapped-ivc',
    version='2.5.7.5',
    description='A Bootstrap theme for Django Admin',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    url='https://github.com/ivc-inform/django-admin-bootstrapped.git',
    license='BSD License',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=[
        'setuptools',
        'Django>=1.11.15',
    ],
    test_suite='django_admin_bootstrapped.runtests.runtests',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False
)
