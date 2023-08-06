from setuptools import setup

setup(
    name='minio_handler',
    version='0.0.5',
    description='an abstraction on top of the minio package to make basic functions easier',
    url='https://github.com/ReinierNel/opstools/tree/main/libraries/python3/minio_handler',
    author='Reinier Nel',
    author_email='hi@reinier.co.za',
    license='MIT License',
    packages=['minio_handler'],
    install_requires=['minio>=7.1.12'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.11',
    ],
)
