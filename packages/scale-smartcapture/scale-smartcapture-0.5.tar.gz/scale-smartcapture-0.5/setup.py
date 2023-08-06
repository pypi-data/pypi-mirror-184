from distutils.core import setup
setup(
  name='scale-smartcapture',
  packages=['smartcapture'],
  version='0.5',
  license='MIT',
  description='The official Python client library for Smart Capture',
  author='Scale AI Smartcapture Team',
  url='https://github.com/scaleapi/smart-capture-sdk',
  download_url='https://github.com/scaleapi/smart-capture-sdk/archive/refs/tags/v0.5.tar.gz',
  keywords=['smartcapture', 'scale'],
  install_requires=[
        'requests',
        'numpy',
    ],
)
