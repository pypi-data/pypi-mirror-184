from setuptools import setup

setup(
    name='philbot-voice',
    version='0.1.0',
    description='A example Python package',
    url='https://github.com/plengauer/Philbot',
    author='Philipp Lengauer',
    author_email='p.lengauer@gmail.com',
    license='MIT',
    packages=['philbot-voice'],
    install_requires=[
        'flask',
        'websocket-client',
        'numpy',
        'pynacl',
        'pyogg',
        'youtube_dl'
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.11',
    ],
)
