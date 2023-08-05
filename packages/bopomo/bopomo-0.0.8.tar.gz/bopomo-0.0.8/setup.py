import setuptools

def readme():
    with open('README.md',encoding='utf8') as f:
        return f.read()

setuptools.setup(
    name="bopomo",
    version="0.0.8",
    author="Hsin-Min Lu, Jian-Long Liao",
    author_email="slingan127@gmail.com",
    include_package_data=True,
    description="This is a package to translate a chinese sentence into bopomofo letters",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=(
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6"
    ),
    install_requires=['python-crfsuite','jieba'],
    python_requires='>=3',
    package_data={'':['data/*', 'model/*']}
)


