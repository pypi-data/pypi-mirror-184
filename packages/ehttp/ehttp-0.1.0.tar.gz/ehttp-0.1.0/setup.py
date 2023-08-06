from setuptools import setup, find_packages

setup_args = dict(
    name='ehttp',
    version='0.1.0',
    description='Tool for easy creating http api',
    license='MIT',
    packages=find_packages(),
    author='Andrey Shcarev',
    author_email='wex335@yandex.ru',
    keywords=['http', 'ehttp', 'easyhttp'],
    url='https://gitlab.com/cuciki/ehttp',
    download_url='https://pypi.org/project/ehttp/'
)

install_requires = [
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
