from setuptools import setup

setup(
    name='Mensajes',
    version='1.0',
    description='un paquete para saludar y despedir',
    author='jhonatan Rincon',
    author_email='jeramix92@gmail.com',
    url='https://www.hektor.dev',
    packages=['Mensajes','Mensajes.hola','Mensajes.adios'],
    scripts=['Test.py']
)
