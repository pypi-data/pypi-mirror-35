import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(name='xmlrpccomp',
                 version='1.0.0',
                 author='tj',
                 author_email='bjtj10@gmail.com',
                 description='xmlrpc comp (python2 and 3)',
                 long_description=long_description,
                 long_description_content_type='text/markdown',
                 url='https://github.com/bjtj/xmlrpccomp',
                 packages=setuptools.find_packages(),
                 classifiers=[
                     'Programming Language :: Python :: 3',
                     'License :: OSI Approved :: MIT License',
                     'Operating System :: OS Independent',
                 ],
)
