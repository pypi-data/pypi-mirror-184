from setuptools import setup

setup(
    name='dot-center-finder',
    version='0.1',
    py_modules=['dot_center_finder'],
    install_requires=['numpy', 'matplotlib', 'csv', 'opencv-python'],
    entry_points={
        'console_scripts': [
            'dot-center-finder=dot_center_finder:main'
        ]
    }
)
