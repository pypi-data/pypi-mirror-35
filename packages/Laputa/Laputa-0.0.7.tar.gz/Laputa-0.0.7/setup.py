#encoding: utf-8
from setuptools import find_packages, setup
setup(

        name='Laputa',
        version='0.0.7',
        description='Laputa',
        license='MIT',
        author='KingMckay',
        author_email='kingmckay58@gmail.mmdminterface',
        url='https://github.com/mckay58/Laputa',
        packages=find_packages(),
        install_requires=["PyMySQL", "xlrd", "sshtunnel", "requests", "PyYAML", "xmlrunner"],
        classifiers=[
            # How mature is this project? Common values are
            #   3 - Alpha
            #   4 - Beta
            #   5 - Production/Stable
            'Development Status :: 3 - Alpha',

            # Indicate who your project is intended for
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Build Tools',

            # Pick your license as you wish (should match "license" above)
             'License :: OSI Approved :: MIT License',

            # Specify the Python versions you support here. In particular, ensure
            # that you indicate whether you support Python 2, Python 3 or both.
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
        ],

)
