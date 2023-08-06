# setup.py
from setuptools import setup, find_packages

# Read in the requirements
with open('requirements.txt') as f:
    requirements = list(map(str, f.read().splitlines()))

with open('README.md') as f:
    readme = f.read()

setup(
    version='1.0.0',
    name="gps_uvsq_utils",
    author="UVSQ Datascale students",
    long_description=readme,
    long_description_content_type='text/markdown',
    description="Private Python library who provides incredible features.",
    packages=find_packages(),
    include_package_data=True,
    license="GPL",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Topic :: System :: Operating System',
    ],
    python_requires='>=3.8',
    setup_requires=['setuptools-git-versioning'],
    version_config={
        "dirty_template": "{tag}",
    },

    install_requires=[
        'pandas',
        'numpy',
        'streamlit',
        'geopy',
    ],
    zip_safe=False,
    package_data={
        'gps_uvsq_utils': ['assets/*'],
    },
    url="https://gitlab.com/abdoufermat5/gps_utils"
)
