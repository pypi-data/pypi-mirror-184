import platform
import os
from setuptools import setup, find_packages

path_to_my_project = os.path.dirname(__file__)  # Do any sort of fancy resolving of the path here if you need to


install_requires = [
    'PyYAML',
]
packages = find_packages(exclude=['tests'])

setup(name='ceotr_common_utilities',
      version='1.0.3',
      description="Common Python",
      author="CEOTR",
      author_email="support@ceotr.ca",
      url="https://gitlab.oceantrack.org/ceotr-public/ceotr_app_common/ceotr_common_utilities",
      packages=packages,
      include_package_data=True,
      python_requires='>=3.5',
      license="GNU General Public License v3 (GPLv3)",
      install_requires=install_requires,
      zip_safe=True
      )
