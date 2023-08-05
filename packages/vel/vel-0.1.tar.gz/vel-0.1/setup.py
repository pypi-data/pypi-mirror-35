from setuptools import setup, find_packages


setup(
    name='vel',
    version='0.1',
    description="Velocity in deep-learning research",
    url='https://github.com/MillionIntegrals/vel',
    author='Jerry Tworek',
    author_email='jerry@millionintegrals.com',
    license='MIT',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=[
        'pyyaml',
        'numpy',
        'pandas',
        'scikit-learn',
        'torch >= 0.4.1',
        'torchvision',
        'opencv-python',
        'pillow-simd',
        'tqdm'
    ],
    extras_require={
        'visdom': ['visdom'],
        'mongo': ['pymongo'],
        'gym': ['gym[all]'],
    },
    entry_points={
        'console_scripts': [
            'vel = vel.launcher:main',
        ],
    },
    scripts=[]
)
