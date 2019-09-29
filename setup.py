#!/usr/bin/env python
# encoding: utf-8

# amy j alexander's customization of below scripts and package to
# 1) allowing analyzing only partial files in ffmpeg mode.
# 2) allow skipping of gender classification, so only speech vs. music is classified
# Nothing's been changed within the neural net files.
########
# The MIT License

# Copyright (c) 2018 Ina (David Doukhan - http://www.ina.fr/)

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


import os
from setuptools import setup, find_packages


KEYWORDS = '''
speech-segmentation
audio-analysis
music-detection
speech-detection
speech-music
gender-equality
gender-classification
speaker-gender
speech
music
voice-activity-detection'''.strip().split('\n')

CLASSIFIERS=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Intended Audience :: Education',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3',
    'Topic :: Multimedia :: Sound/Audio',
    'Topic :: Multimedia :: Sound/Audio :: Analysis',
    'Topic :: Multimedia :: Sound/Audio :: Speech',
    'Topic :: Scientific/Engineering',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Topic :: Sociology',
]

DESCRIPTION='CNN-based audio segmentation toolkit. Does voice activity detection, speech detection, music detection, speaker gender recognition.'
LONGDESCRIPTION='''Split audio signal into homogeneous zones of speech and music, and detect speaker gender.

inaSpeechSegmenter has been presented at the IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) 2018 conference in Calgary, Canada. If you use this toolbox in your research, you can cite the following work in your publications :


```bibtex
@inproceedings{ddoukhanicassp2018,
  author = {Doukhan, David and Carrive, Jean and Vallet, Félicien and Larcher, Anthony and Meignier, Sylvain},
  title = {An Open-Source Speaker Gender Detection Framework for Monitoring Gender Equality},
  year = {2018},
  organization={IEEE},
  booktitle={Acoustics Speech and Signal Processing (ICASSP), 2018 IEEE International Conference on}
}
```

inaSpeechSegmenter won MIREX 2018 speech detection challenge.
http://www.music-ir.org/mirex/wiki/2018:Music_and_or_Speech_Detection_Results
Details on the speech detection submodule can be found bellow:


```bibtex
@inproceedings{ddoukhanmirex2018,
  author = {Doukhan, David and Lechapt, Eliott and Evrard, Marc and Carrive, Jean},
  title = {INA’S MIREX 2018 MUSIC AND SPEECH DETECTION SYSTEM},
  year = {2018},
  booktitle={Music Information Retrieval Evaluation eXchange (MIREX 2018)}
}
```
'''

setup(
    name = "inaSpeechSegmenter",
    version = "0.1.1",
    author = "David Doukhan",
    author_email = "david.doukhan@gmail.com",
    description = DESCRIPTION,
    license = "MIT",
    install_requires=['numpy', 'keras', 'scikit-image', 'sidekit==1.2.4', 'pyannote.algorithms'],
 #   keywords = "example documentation tutorial",
    url = "https://github.com/ina-foss/inaSpeechSegmenter",
#    packages=['inaSpeechSegmenter'],
    keywords = KEYWORDS,
    packages = find_packages(),
    package_data = {'inaSpeechSegmenter': ['*.hdf5']},
    include_package_data = True,
    data_files = ['LICENSE'],
    long_description=LONGDESCRIPTION,
    long_description_content_type='text/markdown',
    scripts=[os.path.join('scripts', script) for script in \
             ['ina_speech_segmenterAJA.py']],
    classifiers=CLASSIFIERS,
    python_requires='>=3',
)
