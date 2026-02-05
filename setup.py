from distutils.core import setup
setup(
  name = 'MyQR',
  packages = ['MyQR','MyQR.mylibs'],
  version = '0.1',
  license='MIT',
  description = 'QR Code Making Library forked from sylnsfar/qrcode',
  author = 'Sumanjay',
  author_email = 'cyberboysumanjay@gmail.com',
  url = 'https://github.com/cyberboysumanjay/qrcode',
  download_url = 'https://github.com/cyberboysumanjay/qrcode/archive/v_01.tar.gz',
  keywords = ['ARTISTIC', 'QR', 'CODE'],
  install_requires=[
          'imageio',
          'numpy',
          'Pillow'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha', 
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)
