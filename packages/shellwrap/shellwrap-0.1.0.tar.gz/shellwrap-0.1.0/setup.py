import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='shellwrap',
                 version='0.1.0',
                 description='Python and shell scripts interaction library',
                 author='Rodrigo Valin',
                 author_email='licorna@gmail.com',
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 url='https://gitlab.com/licorna/shellwrap',
                 packages=setuptools.find_packages(),
                 data_files=[("", ["LICENSE.txt"])])
