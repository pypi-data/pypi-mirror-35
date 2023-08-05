with open('version', 'r') as f:
    version = f.read()

if __name__ == '__main__':
    from numpy.distutils.core import setup

    setup(
        name='fem',
        version=version,
        description='pipe',
        long_description='pipe',
        author='jpm',
        author_email='joepatmckenna@gmail.com',
        url='http://joepatmckenna.github.io',
        packages=['pipe'])
