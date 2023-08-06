import glob
import setuptools

VERSION = '2022.01.06.005'

requirements = [
    'matplotlib>=3.2.2'
    'numpy>=1.18.5,<1.24.0'
    'opencv-python>=4.1.1'
    'Pillow>=7.1.2'
    'PyYAML>=5.3.1'
    'requests>=2.23.0'
    'scipy>=1.4.1'
    'torch==1.11.0'
    'torchvision==0.12.0'
    'tqdm>=4.41.0'
    'protobuf<4.21.3',
    'tensorboard>=2.4.1',
    'pandas>=1.1.4',
    'seaborn>=0.11.0',
    'ipython',
    'psutil',
    'thop'
]


def setup():
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
