from setuptools import setup

setup(
    name='micropython-dftds',
    version='0.0.1',
    description='MicroPython library for the TDS meter sensor',
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    url='https://github.com/WendelHime/micropython-dftds',
    project_urls={
        'github': 'https://github.com/WendelHime/micropython-dftds',
    },
    author='Wendel Hime Lino Castro',
    author_email='wendelhime@hotmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: Implementation :: MicroPython',
    ],
    keywords=[
        'micropython',
        'electronics',
    ],
    packages=['dftds'],
)
