from setuptools import setup


setup(
    name='blog_quantum',
    version='1.0',
    packages=['blog'],
    include_package_data=True,
    install_requires=[
        'Django>=1.8.1,<1.12',
        'wagtail>=1.0,<2.0',
    ],
    url='https://github.com/QuantumEnergyE/blog_quantum',
    author='quantum',
    author_email='quantumenergye@gmail.com ',
)
