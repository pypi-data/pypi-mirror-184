import glob
import os
import setuptools
import shutil

VERSION = '2022.01.06'


def setup():
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
        requirements = [req for req in requirements
                        if not req.startswith('--')]

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

        # Remove installation artifacts
        build_path = '../yolov7/build/'
        if os.path.exists(build_path):
            shutil.rmtree(build_path)

        egg_info_path = '../yolov7/yolov7.egg-info'
        if os.path.exists(egg_info_path):
            shutil.rmtree(egg_info_path)


if __name__ == '__main__':
    setup()
