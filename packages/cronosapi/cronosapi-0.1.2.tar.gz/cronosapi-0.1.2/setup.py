from setuptools import setup

setup(
    name='cronosapi',
    version='0.1.2',
    description='Python Wrapper for Cronos API',
    url='https://github.com/JulienCoutault/cronos-api',
    author='Julien Coutault',
    author_email='cronos-api@juliencoutault.fr',
    keywords=['Cronos', 'API', 'CRO', 'Crypto.com', 'Blockchain'],
    license='MIT',
    packages=['cronosapi'],
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
