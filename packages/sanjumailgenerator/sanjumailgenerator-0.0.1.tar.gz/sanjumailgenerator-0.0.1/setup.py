from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='sanjumailgenerator',
    version='0.0.1',
    description='A script to send automated mails.',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Sanooj Babu',
    author_email='sanooj.kakkoth@onebillsoftware.com',
    license='MIT',
    classifiers=classifiers,
    keywords='calculator',
    packages=find_packages(),
    install_requires=['configparser', 'os', 'smtplib', 'email.mime.text', 'email.mime.multipart', 'ast',
                      'email.mime.application']
)
