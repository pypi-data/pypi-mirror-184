import glob
import setuptools

VERSION = '2022.01.06.004'


def setup():
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()

    with open('README.dst') as f:
        long_description = f.read()

    setuptools.setup(
        packages=setuptools.find_packages(),
        install_requires=requirements,
        python_requires='>=3.10',
        include_package_data=True,
        author='biantsh',
        version=VERSION,
        name='yolov7-wky',
        scripts=glob.glob('*.py'),
        long_description=long_description,
        long_description_content_type="text/markdown"
    )


if __name__ == '__main__':
    setup()
