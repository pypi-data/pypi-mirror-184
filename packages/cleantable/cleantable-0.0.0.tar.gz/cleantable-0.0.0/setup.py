from setuptools import setup

setup(
    name="cleantable",
    version="0.0.0",
    license="AGPLv3+",
    python_requires=">=3.7",
    # What does your project relate to?
    keywords="nlp cv text_data issue_detection data_quality image_quality machine_learning data_cleaning",
    packages=[],
    package_data={
        "": ["LICENSE"],
    },
    license_files=("LICENSE",),
    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        "Pillow >= 8.4",
        "numpy>=1.11.3",
        "pandas>=1.0.0",
        "imagehash>=4.2.0",
        "tqdm>=4.53.0",
    ],
    author_email='ulyana@cleanlab.ai',
    classifiers=['Development Status :: 1 - Planning'],
)
