import pathlib

import setuptools

setuptools.setup(
    name='iftg',
    version='1.0.9',
    description='IFTG (ImageFromTextGenerator) is a Python package that simplifies creating robust datasets for OCR models. Generate images from text, apply over 10 built-in noise effects, and customize fonts and layouts. IFTG supports all languages and offers endless noise combinations, including custom noise creation.',
    long_description=pathlib.Path('README.md').read_text(),
    long_description_content_type='text/markdown',
    url='https://github.com/OmarSamirz/ImageFromTextGenerator/tree/main',
    author='Omar Samir',
    author_email='omarsamir1300@gmail.com',
    license='MIT',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
    ],
    project_urls={
        "Source": 'https://github.com/OmarSamirz/ImageFromTextGenerator/tree/main'
    },
    python_requires='>=3.10,<3.13',
    install_requires=['numpy>=2.1.1',
                      'opencv-python>=4.10.0',
                      'pillow>=10.4.0',
                      'scipy>=1.14.1',
                     ],
    packages=setuptools.find_packages(),
    include_package_data=True,
)