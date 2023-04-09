import os
from glob import glob
from setuptools import setup

package_name = 'balance_webots'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*.launch.py'))),
        (os.path.join('share', package_name, 'urdf'), glob(os.path.join('urdf', '*.*'))),
        (os.path.join('share', package_name, 'meshes'), glob(os.path.join('meshes', '*.*'))),
        (os.path.join('share', package_name, 'rviz'), glob(os.path.join('rviz', '*.rviz'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hxzp',
    maintainer_email='hxzp@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'balance = balance_webots.balance:main'
        ],
    },
)
