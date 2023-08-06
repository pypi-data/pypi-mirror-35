import os
from subprocess import check_call
from setuptools import find_packages, setup
from setuptools.command.install import install


with open(os.path.join(os.path.dirname(__file__), 'djangoplus/README.md')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


class PostInstallCommand(install):

    def run(self):
        check_call("/bin/bash djangoplus/bin/setpath".split())
        install.run(self)


setup(
    name='djangoplus',
    version='0.0.69',
    packages=find_packages(),
    install_requires=[
        'Django==2.0.3', 'xhtml2pdf==0.2.1', 'python-dateutil==2.7.1', 'selenium==3.14.0', 'xlwt==1.3.0',
        'xlrd==1.1.0', 'unicodecsv==0.14.1', 'qrcode==6.0'
    ],
    extras_require={
        'deploy': ['Pillow==5.0.2','cryptography==2.2.1', 'Fabric3==1.14.post1', 'dropbox==8.7.1']
    },
    scripts=[
        'djangoplus/bin/startproject', 'djangoplus/bin/runserver', 'djangoplus/bin/sync',
        'djangoplus/bin/install-djangoplus-tools','djangoplus/bin/test-djangoplus-tools', 'djangoplus/bin/setpath'
    ],
    include_package_data=True,
    license='BSD License',
    description='Metadata-based web framework for the development of management information systems',
    long_description='',  # README,
    cmdclass={
        'install': PostInstallCommand,
    },
    url='http://djangoplus.net/',
    author='Breno Silva',
    author_email='brenokcc@yahoo.com.br',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
