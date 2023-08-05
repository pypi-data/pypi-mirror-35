from setuptools import setup

setup(name='pytaoassets',
      version='0.4.6',
      description='Python implementation of the PeerAssets protocol for the Tao blockchain.',
      keywords=["blockchain", "digital assets", "protocol"],
      url='https://github.com/taoassets/pytaoassets',
      author='PeerAssets',
      author_email='peerchemist@protonmail.ch',
      license='BSD',
      packages=['pytaoassets', 'pytaoassets.provider'],
      install_requires=['protobuf', 'taoassets-taopy'],
      extras_require={
        'rcp_provider': ['python-taorpc>=1.0']
                        }
      )
