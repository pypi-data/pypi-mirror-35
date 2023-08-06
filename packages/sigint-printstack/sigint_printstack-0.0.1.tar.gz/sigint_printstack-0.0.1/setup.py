from setuptools import setup, find_packages

setup(
    name='sigint_printstack',
    version='0.0.1',
    keywords=('sigint print_stack'),
    description='a small debug tool, invoke trackback.print_stack when received sigint.',
    license='MIT License',
    install_requires=[],

    author='Yana',
    author_email='fhsxfhsx@126.com',

    packages=find_packages(exclude=['*.md', '*.yml', '*.pyc']),
    platforms='any',

    url='https://github.com/yangyangxcf/sigint_printstack',
    include_package_data=True,
)
