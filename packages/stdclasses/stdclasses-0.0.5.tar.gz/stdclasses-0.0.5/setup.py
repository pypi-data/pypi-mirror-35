from setuptools import setup

setup(
    name='stdclasses',
    description='Ia to help',
    long_description='Ia to help students',
    version='0.0.5',
    url='https://github.com/guimartino/stdclasses',
    author='Guilherme Martino',
    author_email='gui.martino@hotmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3'
    ],
    packages=['stdclasses'],
    install_requires=['pandas>=0.23.4']
)