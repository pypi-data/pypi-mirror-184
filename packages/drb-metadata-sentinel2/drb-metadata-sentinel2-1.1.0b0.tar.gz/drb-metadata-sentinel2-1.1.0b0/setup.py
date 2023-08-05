import versioneer
from setuptools import find_namespace_packages, setup


with open('README.md') as file:
    README = file.read()

with open('requirements.txt') as file:
    REQUIREMENTS = file.readlines()


setup(
    name="drb-metadata-sentinel2",
    description="Sentinel-2 Product Metadata",
    long_description=README,
    long_description_content_type="text/markdown",
    author="GAEL Systems",
    author_email="drb-python@gael.fr",
    url="https://gitlab.com/drb-python/metadata/add-ons/sentinel-2",
    python_requires=">=3.8",
    install_requires=REQUIREMENTS,
    packages=find_namespace_packages(include=['drb.*']),
    classifiers=[
        "Programming Language :: Python :: 3.8",
    ],
    package_data={'drb.addons.metadata.sentinel2': ['cortex.yml']},
    data_files=[('.', ['requirements.txt'])],
    entry_points={
        'drb.metadata': ['sentinel2=drb.addons.metadata.sentinel2']
    },
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
)
