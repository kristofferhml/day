from setuptools import find_packages, setup

package_name = 'day'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kristoffer',
    maintainer_email='kristofferhumle@gmail.com',
    description='Controls sun rise and sun set',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'start = day.main:main', 
        ],
    },
)
