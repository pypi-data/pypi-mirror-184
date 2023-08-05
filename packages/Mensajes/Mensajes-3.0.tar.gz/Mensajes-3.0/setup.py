from setuptools import setup, find_packages

setup(
    name='Mensajes',
    version='3.0',
    description='un paquete para saludar y despedir',
    author='jhonatan Rincon',
    author_email='jeramix92@gmail.com',
    url='https://www.hektor.dev',
    packages=find_packages(),
    scripts=[],
    test_suite='tests',
    install_requires=[paquete.strip() for paquete in open("requirements.txt").readlines()]
)
