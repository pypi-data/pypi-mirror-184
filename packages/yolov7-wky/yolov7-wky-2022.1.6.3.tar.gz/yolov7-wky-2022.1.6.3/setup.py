import glob
import setuptools

VERSION = '2022.01.06.003'


def setup():
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()

        setuptools.setup(
            packages=setuptools.find_packages(),
            install_requires=requirements,
            python_requires='>=3.10',
            include_package_data=True,
            author='biantsh',
            version=VERSION,
            name='yolov7-wky',
            scripts=glob.glob('*.py')
        )


if __name__ == '__main__':
    setup()
