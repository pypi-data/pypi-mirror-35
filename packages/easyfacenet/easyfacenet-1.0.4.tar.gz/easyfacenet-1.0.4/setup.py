import setuptools

setuptools.setup(
    name="easyfacenet",
    version="1.0.4",
    maintainer='Tirmidzi Aflahi',
    maintainer_email='taflahi@gmail.com',
    include_package_data=True,
    description="A simple facenet interface",
    long_description="Simple interface for face recognition with Google's FaceNet deep neural network & TensorFlow",
    long_description_content_type="text/markdown",
    url="https://github.com/taflahi/facenet",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],install_requires=[
        'tensorflow==1.7', 'scipy', 'scikit-learn', 'opencv-python',
        'h5py', 'matplotlib', 'Pillow', 'requests', 'psutil'
    ]
)