from setuptools import setup
from setuptools import find_packages

setup(
    name='conveyer',
    version='0.0.1',
    description='',
    author='Yusuke Sugomori',
    author_email='me@yusugomori.com',
    url='https://github.com/yusugomori/conveyer',
    download_url='',
    install_requires=['numpy>=1.13.3',
                      'scikit-learn>=0.19.1'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='machine learning',
    packages=find_packages()
)
