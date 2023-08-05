from setuptools import setup, find_packages

setup(
    name='Mensajes-mumanator',
    version='6.0',
    description='un paquete para saludar y despedir',
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    author='jhonatan Rincon',
    author_email='jeramix92@gmail.com',
    url='https://www.hektor.dev',
    license_file=['LICENSE'],
    packages=find_packages(),
    scripts=[],
    test_suite='tests',
    install_requires=[paquete.strip() 
                    for paquete in open("requirements.txt").readlines()],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.9',
        'Topic :: Utilities',
    ],
)
