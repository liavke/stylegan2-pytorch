import sys
from distutils.core import setup
import importlib.util
import os

# Manually load version
spec = importlib.util.spec_from_file_location("version", "stylegan2_pytorch/version.py")
version_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(version_module)
__version__ = version_module.__version__

setup(
  name = 'stylegan2_pytorch',
  packages = ['stylegan2_pytorch'],
  entry_points={
    'console_scripts': [
      'stylegan2_pytorch = stylegan2_pytorch.cli:main',
    ],
  },
  version = __version__,
  license = 'MIT',
  description = 'StyleGan2 in Pytorch',
  long_description_content_type = 'text/markdown',
  author = 'Phil Wang',
  author_email = 'lucidrains@gmail.com',
  url = 'https://github.com/lucidrains/stylegan2-pytorch',
  download_url = 'https://github.com/lucidrains/stylegan2-pytorch/archive/v_036.tar.gz',
  keywords = [
    'generative adversarial networks',
    'artificial intelligence'
  ],
  install_requires=[
    'aim',
    'einops>=0.8.0',
    'contrastive_learner>=0.1.0',
    'fire',
    'kornia>=0.5.4',
    'numpy',
    'retry',
    'tqdm',
    'torch>=2.2',
    'torchvision',
    'pillow',
    'vector-quantize-pytorch==0.1.0'
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)