from setuptools import setup,find_packages
from pathlib import Path

setup(
    name='pro_video_tools_pilot',
    version=1.0,
    description='Este pacote irá fornecer ferramentas de processamento de vídeo',
    long_description=Path('README.md').read_text(),
    author='Ciroc_1995',
    author_email='cicero.cordeiro1995@gmail.com',
    keywords=['camera', 'video', 'processamento'],
    packages=find_packages()
)