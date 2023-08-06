from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='isitdarkoutside',
      version='0.2.0',
      description="A simple tool which makes use of location and sunrise/sunset timings to determine whether it's dark outside or not.",
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2 :: Only',
        'Topic :: System :: Networking :: Time Synchronization',
      ],
      author='Aaditya Prasad',
      author_email='aadityaprasad04@gmail.com',
      license='MIT',
      packages=['isitdarkoutside'],
      install_requires=[
          'python-dateutil',
          'geocoder',
      ],
      entry_points = {
        'console_scripts': ['isitdarkoutside=isitdarkoutside.command_line:main'],
      },
      zip_safe=False)
