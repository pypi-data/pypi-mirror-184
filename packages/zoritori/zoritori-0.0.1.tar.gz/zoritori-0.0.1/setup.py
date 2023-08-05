# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zoritori', 'zoritori.recognizers']

package_data = \
{'': ['*']}

install_requires = \
['ConfigArgParse>=1.5.3,<2.0.0',
 'PyAutoGUI>=0.9.53,<0.10.0',
 'PyOpenGL>=3.1.6,<4.0.0',
 'SudachiDict-core>=20220519,<20220520',
 'SudachiPy>=0.6.5,<0.7.0',
 'glfw>=2.5.3,<3.0.0',
 'google-cloud-vision>=2.7.3,<3.0.0',
 'opencv-python>=4.6.0,<5.0.0',
 'pytesseract>=0.3.9,<0.4.0',
 'skia-python>=87.4,<88.0']

extras_require = \
{':platform_system != "Windows"': ['jamdict', 'jamdict-data'],
 ':platform_system == "Windows"': ['pywin32', 'jisho-api>=0.1.8,<0.2.0']}

setup_kwargs = {
    'name': 'zoritori',
    'version': '0.0.1',
    'description': 'yet another tool to help you read text in Japanese video games',
    'long_description': '# zōritori 草履取り\n\nyet another tool to help Japanese language learners read text in video games\n\n## features\n\n* annotate kanji with furigana\n* color code proper nouns (like NHK News Web Easy)\n* look up words on mouse hover, or open Jisho or Wikipedia\n* automatically collect vocabulary with context\n* (optional) English subtitles via machine translation\n\n![Taiko Risshiden V](/screenshots/taiko1.png?raw=true "Taiko Risshiden V")\n\nThis is a work in progress and is rough around the edges.\n\n## requirements:\n\n* Windows, Linux, or Mac (tested on Windows 10, Ubuntu 22.04, and macOS Montery\n* Python 3.10.x)\n* either Tesseract or a Google Cloud Vision API account\n* *(optional) DeepL API account for machine translated subtitles*\n* *(Linux only) scrot, python3-tk, python3-dev. X11 only for now, Wayland may not work*\n\n## installation:\n\n* install Python 3.10.x\n* install `zoritori` via pip (optionally via pipx, recommended)\n* download the example config file from [here](https://github.com/okonomichiyaki/zoritori/blob/main/config.ini)\n* if using Tesseract, [follow these instructions](https://github.com/tesseract-ocr/tesseract) to install it, then configure it by specifying the path to the `tesseract` binary in `config.ini`\n* if using Google Cloud Vision, [follow these steps](https://cloud.google.com/vision/docs/detect-labels-image-client-libraries) to create a project and download a credentials JSON file. then add that as an environment variable: `$env:GOOGLE_APPLICATION_CREDENTIALS="C:\\path\\to\\json"`\n\n## usage\n\n* start: `zoritori -e <tesseract|google> -c /path/to/config.ini`\n* an invisible window (with title "zoritori") should appear. make sure this window has focus\n* identify the region of the screen containing text you want to read\n* using your mouse, (left) click and drag a rectangle around the text\n* after a moment, you should see furigana over any kanji in the region, and proper nouns highlighted (blue, orange, and green boxes). hovering over words inside the region should display a dictionary result, if one is found\n\n### keyboard shortcuts\n\n| key | Description |\n| ----------- | ----------- |\n| T | toggle translation    |\n| C | manual refresh        |\n| J | open Jisho search for word under cursor |\n| W | open Japanese Wikipedia search for word under cursor |\n| E | open English Wikipedia search for word under cursor  |\n| R + mouse-drag | select main region when in click through mode |\n| Q + mouse-drag | select one time lookup when in click through mode |\n\n## more options/etc\n\n### secondary clipping\n\nAfter selecting a region, `zoritori` will watch that area for changes, and refresh if any are detected. If you want to select a new region, just click and drag again. If you want to keep your original region, but want to do a one-time look up a word outside the region, right click and drag around the word.\n\n### click through mode\n\nBy default, the transparent overlay won\'t send clicks through to underlying applications, including your game. It will steal focus if you click anywhere on the screen. On Windows only (for now) you can enable click through mode in the `config.ini` file or command-line parameters. On Mac and Linux, this is not supported at the moment.\n\nWhen click through mode is enabled, use R (without mouse clicking) to drag select a region, and use Q to select a region for a one-time lookup.\n\n### comparing OCR engines\n\nTesseract is free, open source, and works offline. Unfortunately, in my experience it has less accurate recognition, and sometimes returns very messy bounding box data, making it difficult to accurately place furigana.\n\nGoogle Cloud Vision has [per usage costs](https://cloud.google.com/vision/pricing), but should be free for low usage, and is closed source and requires an Internet connection (the selected region is sent as an image to Google for processing)\n\n### saving vocabulary\n\nBy default nothing is saved. But if you want to save vocabulary words, add a folder name in the `config.ini` file or command-line parameters. \n\nWith only `NotesFolder` set, all vocabulary will be saved in one folder. Fullscreen screenshots are saved each time OCR runs, along with a markdown file that include new vocabulary found, for later review.\n\nWith only `NotesRoot` set, vocabulary will be saved as above but inside individual folders for each session (once for each time you start `zoritori`) to make review less cumbersome.\n\nWith both `NotesFolder` and `NotesRoot` set, `NotesFolder` behavior takes precedence (everything saved in one folder).\n',
    'author': 'michiaki yamada',
    'author_email': 'okonomichiyaki@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/okonomichiyaki/zoritori',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
