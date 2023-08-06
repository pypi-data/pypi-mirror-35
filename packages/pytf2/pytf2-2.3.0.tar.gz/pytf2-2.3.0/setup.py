from distutils.core import setup

setup(
    name='pytf2',
    version='2.3.0',
    packages=['pytf2'],
    url='https://github.com/mninc/pytf',
    license='MIT',
    author='manic',
    author_email='manicminer106@gmail.com',
    description='An API wrapper for everything TF2-related',
    install_requires=['requests', 'lxml', 'steam-trade', 'aiohttp', 'cfscrape'],
    python_requires='>=3'
)
