## ! DO NOT MANUALLY INVOKE THIS setup.py, USE CATKIN INSTEAD

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

# fetch values from package.xml
setup_args = generate_distutils_setup(
    packages=[
            "airsim_base",
            "airsim_gym",
            "open3d_point_cloud"
            ],
    package_dir={"": "src/modules"})


setup(**setup_args)