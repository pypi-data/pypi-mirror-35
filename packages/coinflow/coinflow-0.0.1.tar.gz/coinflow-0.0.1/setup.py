from setuptools import setup

setup(name='coinflow',
      #to supmit new version just modify version number
      version='0.0.1',
      description='give dicreption',
      url='https://github.com/AmienKhaled/zoldyck',
      author='Klaus Glueckert',
      author_email='wfskmoney@gmail.com',
      license='MIT',
      packages=['coinflow'],
      #in install_requires but the dependencies example below
      install_requires=["numpy","pandas"],
      python_requires='>=3',
	  include_package_data=True,
	  zip_safe=False)

