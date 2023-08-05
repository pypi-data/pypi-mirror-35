from setuptools import setup, find_packages

setup(name = 'openbci_py101',
      version = '1.0.0',
      description = 'A lib for controlling OpenBCI Devices',
      author='Tushar Chaturvedi',
      author_email='tushar.chat192@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=['numpy'],
      url='https://github.com/tushar-c/openbci-fixed',  # use the URL to the github repo
      download_url='https://github.com/tushar-c/openbci-fixed/blob/master/OpenBCI_Python-1.0.0.tar.gz',
      keywords=['device', 'control', 'eeg', 'emg', 'ekg', 'ads1299', 'openbci', 'ganglion', 'cyton', 'wifi'],  # arbitrary keywords
      zip_safe=False)
