from setuptools import setup,find_packages

setup(name="imageai-org",
      version='2.1.6',
      description='This project is a fork of ImageAI project from https://github.com/OlafenwaMoses/ImageAI. '
                  'In this fork, dependency versions are relaxed to allow usage with other packages in same environment',
      url="https://github.com/organon-gitadmin/ImageAI",
      author='Moses Olafenwa and John Olafenwa (forked by OrganonAnalytics)',
      author_email='support@organonanalytics.com',
      license='MIT',
      packages= find_packages(),
      install_requires=['numpy>=1.19.3','scipy>=1.4.1','pillow>=8.1.1',"matplotlib>=3.3.2", "h5py>=2.10.0", "keras-resnet>=0.2.0", "opencv-python", "keras>=2.4.3"],
      zip_safe=False
      )