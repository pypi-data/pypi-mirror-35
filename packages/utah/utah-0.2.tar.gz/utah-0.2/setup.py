from setuptools import setup


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name='utah',
    version='0.2',
    description='The official module for Utah Python / SLCPython',
    long_description=readme(),
    classifiers=[
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License'
    ],
    keywords='utah meetup slc',
    url='http://github.com/slcpython/utah',
    author='Faris Chebib',
    author_email='faris@theluckybead.com',
    license='MIT',
    packages=['utah'],
    zip_safe=False,
    test_suite='nose.collector',
    test_require=['nose']
)
