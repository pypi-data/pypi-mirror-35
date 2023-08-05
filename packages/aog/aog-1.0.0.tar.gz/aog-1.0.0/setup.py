from setuptools import setup

# reading long description from file
with open('DESCRIPTION.txt') as file:
    long_description = file.read()


# specify requirements of your package here


# some more details
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Internet',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5'
    ]

# calling the setup function 
setup(name='aog',
      version='1.0.0',
      description='Python client library for actions on google',
      long_description=long_description,
      url='https://github.com/DeveloperBibin/python-aog/blob/master/README.md',
      author='Bibin Benny',
      author_email='bibinbenny@icloud.com',
      license='MIT',
      packages=['aog'],
      classifiers=CLASSIFIERS,
      keywords='actions on google python client'
      )
