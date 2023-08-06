from setuptools import setup

with open('README.md', encoding='utf-8') as f:
    long_desc = f.read()

setup(
    name='hc-varoperhelper',
    author='HC',
    author_email='jiyungen@haocang.com',
    version='1.0.2',
    description='hc-varoperhelper',
    url='http://www.haocang.com',
    license='MIT',
    long_description=long_desc,
    packages=['VarOperHelper'],
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent', ],
    python_requires='~=3.7',
    install_requires=['requests'],
)
