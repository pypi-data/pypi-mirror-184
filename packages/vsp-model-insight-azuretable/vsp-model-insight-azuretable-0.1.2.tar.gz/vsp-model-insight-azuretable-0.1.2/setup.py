from setuptools import find_packages, setup

setup(
    name='vsp-model-insight-azuretable',
    version='0.1.2',  # noqa
    author='he ke zhang',
    author_email='yxzhk@hotmail.com',
    classifiers=[
        'Intended Audience :: End Users/Desktop',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    description='Model Performance Metrics Monitor Exporter',
    include_package_data=True,
    long_description=open('README.rst').read(),
    install_requires=[
        'azure_data_tables >= 12.4.1'
    ],
    extras_require={},
    license='Apache-2.0',
    packages=find_packages(exclude=('examples', 'tests',)),
    namespace_packages=[],
    url='https://pypi.org/project/vsp-model-insight-azuretable/',  # noqa: E501
    zip_safe=False,
)
