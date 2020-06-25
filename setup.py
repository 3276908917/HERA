from setuptools import setup, find_packages

# this whole file could benefit from bells and whistles,
    # once the package reaches a less sorry state,
    # regarding functionality and utility
# also, in the long term, we should rename the package to
    # something more unique

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='flux',
    # the very first version was 1!1.1a1
    # I will always start with ones and end with nines because I think
        # that is cleaner
    version='1!1.1a5',
    author='Lukas Finkbeiner, C. D. Nunhokee, Aaron Parsons',
    author_email='lfinkbeiner@berkeley.edu',
    description='Primitive source handling functions',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/3276908917/HERA',
    packages=find_packages(),
    package_data={'': ['gleam_with_alpha.txt', 'ant_dict.pk', 'J.npy']},
    include_package_data=True,
    install_requires=[], #I definitely need to come back and fix this
)
