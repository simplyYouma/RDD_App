{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "V8-yl-s-WKMG"
   },
   "source": [
    "# Object Detection API Demo\n",
    "\n",
    "<table align=\"left\"><td>\n",
    "  <a target=\"_blank\"  href=\"https://colab.sandbox.google.com/github/tensorflow/models/blob/master/research/object_detection/colab_tutorials/object_detection_tutorial.ipynb\">\n",
    "    <img src=\"https://www.tensorflow.org/images/colab_logo_32px.png\" />Run in Google Colab\n",
    "  </a>\n",
    "</td><td>\n",
    "  <a target=\"_blank\"  href=\"https://github.com/tensorflow/models/blob/master/research/object_detection/colab_tutorials/object_detection_tutorial.ipynb\">\n",
    "    <img width=32px src=\"https://www.tensorflow.org/images/GitHub-Mark-32px.png\" />View source on GitHub</a>\n",
    "</td></table>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "3cIrseUv6WKz"
   },
   "source": [
    "Welcome to the [Object Detection API](https://github.com/tensorflow/models/tree/master/research/object_detection). This notebook will walk you step by step through the process of using a pre-trained model to detect objects in an image."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "VrJaG0cYN9yh"
   },
   "source": [
    "> **Important**: This tutorial is to help you through the first step towards using [Object Detection API](https://github.com/tensorflow/models/tree/master/research/object_detection) to build models. If you just just need an off the shelf model that does the job, see the [TFHub object detection example](https://colab.sandbox.google.com/github/tensorflow/hub/blob/master/examples/colab/object_detection.ipynb)."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "kFSqkTCdWKMI"
   },
   "source": [
    "# Setup"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "awjrpqy-6MaQ"
   },
   "source": [
    "Important: If you're running on a local machine, be sure to follow the [installation instructions](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md). This notebook includes only what's necessary to run in Colab."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "p3UGXxUii5Ym"
   },
   "source": [
    "### Install"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "hGL97-GXjSUw"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: tensorflow==2.* in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (2.5.0)\n",
      "Requirement already satisfied: wrapt~=1.12.1 in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from tensorflow==2.*) (1.12.1)\n",
      "Requirement already satisfied: absl-py~=0.10 in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from tensorflow==2.*) (0.12.0)\n",
      "Requirement already satisfied: tensorboard~=2.5 in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from tensorflow==2.*) (2.5.0)\n",
      "Requirement already satisfied: h5py~=3.1.0 in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from tensorflow==2.*) (3.1.0)\n",
      "Requirement already satisfied: typing-extensions~=3.7.4 in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from tensorflow==2.*) (3.7.4.3)\n",
      "Requirement already satisfied: gast==0.4.0 in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from tensorflow==2.*) (0.4.0)\n",
      "Requirement already satisfied: tensorflow-estimator<2.6.0,>=2.5.0rc0 in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from tensorflow==2.*) (2.5.0)\n",
      "Requirement already satisfied: flatbuffers~=1.12.0 in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from tensorflow==2.*) (1.12)\n",
      "Requirement already satisfied: protobuf>=3.9.2 in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from tensorflow==2.*) (3.17.2)\n",
      "Requirement already satisfied: numpy~=1.19.2 in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from tensorflow==2.*) (1.19.5)\n",
      "Requirement already satisfied: opt-einsum~=3.3.0 in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from tensorflow==2.*) (3.3.0)\n",
      "Requirement already satisfied: google-pasta~=0.2 in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from tensorflow==2.*) (0.2.0)\n",
      "Requirement already satisfied: grpcio~=1.34.0 in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from tensorflow==2.*) (1.34.1)\n",
      "Requirement already satisfied: keras-preprocessing~=1.1.2 in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from tensorflow==2.*) (1.1.2)\n",
      "Requirement already satisfied: keras-nightly~=2.5.0.dev in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from tensorflow==2.*) (2.5.0.dev2021032900)\n",
      "Requirement already satisfied: wheel~=0.35 in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from tensorflow==2.*) (0.36.2)\n",
      "Requirement already satisfied: astunparse~=1.6.3 in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from tensorflow==2.*) (1.6.3)\n",
      "Requirement already satisfied: six~=1.15.0 in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from tensorflow==2.*) (1.15.0)\n",
      "Requirement already satisfied: termcolor~=1.1.0 in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from tensorflow==2.*) (1.1.0)\n",
      "Requirement already satisfied: markdown>=2.6.8 in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from tensorboard~=2.5->tensorflow==2.*) (3.3.4)\n",
      "Requirement already satisfied: google-auth-oauthlib<0.5,>=0.4.1 in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from tensorboard~=2.5->tensorflow==2.*) (0.4.4)\n",
      "Requirement already satisfied: requests<3,>=2.21.0 in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from tensorboard~=2.5->tensorflow==2.*) (2.25.1)\n",
      "Requirement already satisfied: tensorboard-data-server<0.7.0,>=0.6.0 in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from tensorboard~=2.5->tensorflow==2.*) (0.6.1)\n",
      "Requirement already satisfied: tensorboard-plugin-wit>=1.6.0 in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from tensorboard~=2.5->tensorflow==2.*) (1.8.0)\n",
      "Requirement already satisfied: setuptools>=41.0.0 in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from tensorboard~=2.5->tensorflow==2.*) (52.0.0.post20210125)\n",
      "Requirement already satisfied: werkzeug>=0.11.15 in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from tensorboard~=2.5->tensorflow==2.*) (1.0.1)\n",
      "Requirement already satisfied: google-auth<2,>=1.6.3 in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from tensorboard~=2.5->tensorflow==2.*) (1.30.1)\n",
      "Requirement already satisfied: pyasn1-modules>=0.2.1 in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from google-auth<2,>=1.6.3->tensorboard~=2.5->tensorflow==2.*) (0.2.8)\n",
      "Requirement already satisfied: rsa<5,>=3.1.4 in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from google-auth<2,>=1.6.3->tensorboard~=2.5->tensorflow==2.*) (4.7.2)\n",
      "Requirement already satisfied: cachetools<5.0,>=2.0.0 in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from google-auth<2,>=1.6.3->tensorboard~=2.5->tensorflow==2.*) (4.2.2)\n",
      "Requirement already satisfied: requests-oauthlib>=0.7.0 in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from google-auth-oauthlib<0.5,>=0.4.1->tensorboard~=2.5->tensorflow==2.*) (1.3.0)\n",
      "Requirement already satisfied: pyasn1<0.5.0,>=0.4.6 in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from pyasn1-modules>=0.2.1->google-auth<2,>=1.6.3->tensorboard~=2.5->tensorflow==2.*) (0.4.8)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from requests<3,>=2.21.0->tensorboard~=2.5->tensorflow==2.*) (2020.12.5)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from requests<3,>=2.21.0->tensorboard~=2.5->tensorflow==2.*) (1.26.4)\n",
      "Requirement already satisfied: idna<3,>=2.5 in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from requests<3,>=2.21.0->tensorboard~=2.5->tensorflow==2.*) (2.10)\n",
      "Requirement already satisfied: chardet<5,>=3.0.2 in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from requests<3,>=2.21.0->tensorboard~=2.5->tensorflow==2.*) (4.0.0)\n",
      "Requirement already satisfied: oauthlib>=3.0.0 in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from requests-oauthlib>=0.7.0->google-auth-oauthlib<0.5,>=0.4.1->tensorboard~=2.5->tensorflow==2.*) (3.1.0)\n",
      "Collecting tf_slim\n",
      "  Downloading tf_slim-1.1.0-py2.py3-none-any.whl (352 kB)\n",
      "Requirement already satisfied: absl-py>=0.2.2 in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from tf_slim) (0.12.0)\n",
      "Requirement already satisfied: six in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from absl-py>=0.2.2->tf_slim) (1.15.0)\n",
      "Installing collected packages: tf-slim\n",
      "Successfully installed tf-slim-1.1.0\n"
     ]
    }
   ],
   "source": [
    "!pip install -U --pre tensorflow==\"2.*\"\n",
    "!pip install tf_slim"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "n_ap_s9ajTHH"
   },
   "source": [
    "Make sure you have `pycocotools` installed"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "Bg8ZyA47i3pY"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting pycocotools\n",
      "  Downloading pycocotools-2.0.2.tar.gz (23 kB)\n",
      "Requirement already satisfied: setuptools>=18.0 in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from pycocotools) (52.0.0.post20210125)\n",
      "Requirement already satisfied: cython>=0.27.3 in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from pycocotools) (0.29.23)\n",
      "Requirement already satisfied: matplotlib>=2.1.0 in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from pycocotools) (3.3.4)\n",
      "Requirement already satisfied: pillow>=6.2.0 in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from matplotlib>=2.1.0->pycocotools) (8.2.0)\n",
      "Requirement already satisfied: numpy>=1.15 in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from matplotlib>=2.1.0->pycocotools) (1.19.5)\n",
      "Requirement already satisfied: python-dateutil>=2.1 in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from matplotlib>=2.1.0->pycocotools) (2.8.1)\n",
      "Requirement already satisfied: kiwisolver>=1.0.1 in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from matplotlib>=2.1.0->pycocotools) (1.3.1)\n",
      "Requirement already satisfied: pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.3 in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from matplotlib>=2.1.0->pycocotools) (2.4.7)\n",
      "Requirement already satisfied: cycler>=0.10 in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from matplotlib>=2.1.0->pycocotools) (0.10.0)\n",
      "Requirement already satisfied: six in c:\\users\\asf_portable\\anaconda3\\lib\\site-packages (from cycler>=0.10->matplotlib>=2.1.0->pycocotools) (1.15.0)\n",
      "Building wheels for collected packages: pycocotools\n",
      "  Building wheel for pycocotools (setup.py): started\n",
      "  Building wheel for pycocotools (setup.py): finished with status 'error'\n",
      "  Running setup.py clean for pycocotools\n",
      "Failed to build pycocotools\n",
      "Installing collected packages: pycocotools\n",
      "    Running setup.py install for pycocotools: started\n",
      "    Running setup.py install for pycocotools: finished with status 'error'\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "  ERROR: Command errored out with exit status 1:\n",
      "   command: 'c:\\users\\asf_portable\\anaconda3\\python.exe' -u -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '\"'\"'C:\\\\Users\\\\ASF_Portable\\\\AppData\\\\Local\\\\Temp\\\\pip-install-hd0n2mu9\\\\pycocotools_8a132abfc1b04713a33831c5bbf5ae79\\\\setup.py'\"'\"'; __file__='\"'\"'C:\\\\Users\\\\ASF_Portable\\\\AppData\\\\Local\\\\Temp\\\\pip-install-hd0n2mu9\\\\pycocotools_8a132abfc1b04713a33831c5bbf5ae79\\\\setup.py'\"'\"';f = getattr(tokenize, '\"'\"'open'\"'\"', open)(__file__) if os.path.exists(__file__) else io.StringIO('\"'\"'from setuptools import setup; setup()'\"'\"');code = f.read().replace('\"'\"'\\r\\n'\"'\"', '\"'\"'\\n'\"'\"');f.close();exec(compile(code, __file__, '\"'\"'exec'\"'\"'))' bdist_wheel -d 'C:\\Users\\ASF_Portable\\AppData\\Local\\Temp\\pip-wheel-hpm0nkk0'\n",
      "       cwd: C:\\Users\\ASF_Portable\\AppData\\Local\\Temp\\pip-install-hd0n2mu9\\pycocotools_8a132abfc1b04713a33831c5bbf5ae79\\\n",
      "  Complete output (16 lines):\n",
      "  running bdist_wheel\n",
      "  running build\n",
      "  running build_py\n",
      "  creating build\n",
      "  creating build\\lib.win-amd64-3.8\n",
      "  creating build\\lib.win-amd64-3.8\\pycocotools\n",
      "  copying pycocotools\\coco.py -> build\\lib.win-amd64-3.8\\pycocotools\n",
      "  copying pycocotools\\cocoeval.py -> build\\lib.win-amd64-3.8\\pycocotools\n",
      "  copying pycocotools\\mask.py -> build\\lib.win-amd64-3.8\\pycocotools\n",
      "  copying pycocotools\\__init__.py -> build\\lib.win-amd64-3.8\\pycocotools\n",
      "  running build_ext\n",
      "  cythoning pycocotools/_mask.pyx to pycocotools\\_mask.c\n",
      "  c:\\users\\asf_portable\\anaconda3\\lib\\site-packages\\Cython\\Compiler\\Main.py:369: FutureWarning: Cython directive 'language_level' not set, using 2 for now (Py2). This will change in a later release! File: C:\\Users\\ASF_Portable\\AppData\\Local\\Temp\\pip-install-hd0n2mu9\\pycocotools_8a132abfc1b04713a33831c5bbf5ae79\\pycocotools\\_mask.pyx\n",
      "    tree = Parsing.p_module(s, pxd, full_module_name)\n",
      "  building 'pycocotools._mask' extension\n",
      "  error: Microsoft Visual C++ 14.0 or greater is required. Get it with \"Microsoft C++ Build Tools\": https://visualstudio.microsoft.com/visual-cpp-build-tools/\n",
      "  ----------------------------------------\n",
      "  ERROR: Failed building wheel for pycocotools\n",
      "    ERROR: Command errored out with exit status 1:\n",
      "     command: 'c:\\users\\asf_portable\\anaconda3\\python.exe' -u -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '\"'\"'C:\\\\Users\\\\ASF_Portable\\\\AppData\\\\Local\\\\Temp\\\\pip-install-hd0n2mu9\\\\pycocotools_8a132abfc1b04713a33831c5bbf5ae79\\\\setup.py'\"'\"'; __file__='\"'\"'C:\\\\Users\\\\ASF_Portable\\\\AppData\\\\Local\\\\Temp\\\\pip-install-hd0n2mu9\\\\pycocotools_8a132abfc1b04713a33831c5bbf5ae79\\\\setup.py'\"'\"';f = getattr(tokenize, '\"'\"'open'\"'\"', open)(__file__) if os.path.exists(__file__) else io.StringIO('\"'\"'from setuptools import setup; setup()'\"'\"');code = f.read().replace('\"'\"'\\r\\n'\"'\"', '\"'\"'\\n'\"'\"');f.close();exec(compile(code, __file__, '\"'\"'exec'\"'\"'))' install --record 'C:\\Users\\ASF_Portable\\AppData\\Local\\Temp\\pip-record-lt76g8ex\\install-record.txt' --single-version-externally-managed --compile --install-headers 'c:\\users\\asf_portable\\anaconda3\\Include\\pycocotools'\n",
      "         cwd: C:\\Users\\ASF_Portable\\AppData\\Local\\Temp\\pip-install-hd0n2mu9\\pycocotools_8a132abfc1b04713a33831c5bbf5ae79\\\n",
      "    Complete output (14 lines):\n",
      "    running install\n",
      "    running build\n",
      "    running build_py\n",
      "    creating build\n",
      "    creating build\\lib.win-amd64-3.8\n",
      "    creating build\\lib.win-amd64-3.8\\pycocotools\n",
      "    copying pycocotools\\coco.py -> build\\lib.win-amd64-3.8\\pycocotools\n",
      "    copying pycocotools\\cocoeval.py -> build\\lib.win-amd64-3.8\\pycocotools\n",
      "    copying pycocotools\\mask.py -> build\\lib.win-amd64-3.8\\pycocotools\n",
      "    copying pycocotools\\__init__.py -> build\\lib.win-amd64-3.8\\pycocotools\n",
      "    running build_ext\n",
      "    skipping 'pycocotools\\_mask.c' Cython extension (up-to-date)\n",
      "    building 'pycocotools._mask' extension\n",
      "    error: Microsoft Visual C++ 14.0 or greater is required. Get it with \"Microsoft C++ Build Tools\": https://visualstudio.microsoft.com/visual-cpp-build-tools/\n",
      "    ----------------------------------------\n",
      "ERROR: Command errored out with exit status 1: 'c:\\users\\asf_portable\\anaconda3\\python.exe' -u -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '\"'\"'C:\\\\Users\\\\ASF_Portable\\\\AppData\\\\Local\\\\Temp\\\\pip-install-hd0n2mu9\\\\pycocotools_8a132abfc1b04713a33831c5bbf5ae79\\\\setup.py'\"'\"'; __file__='\"'\"'C:\\\\Users\\\\ASF_Portable\\\\AppData\\\\Local\\\\Temp\\\\pip-install-hd0n2mu9\\\\pycocotools_8a132abfc1b04713a33831c5bbf5ae79\\\\setup.py'\"'\"';f = getattr(tokenize, '\"'\"'open'\"'\"', open)(__file__) if os.path.exists(__file__) else io.StringIO('\"'\"'from setuptools import setup; setup()'\"'\"');code = f.read().replace('\"'\"'\\r\\n'\"'\"', '\"'\"'\\n'\"'\"');f.close();exec(compile(code, __file__, '\"'\"'exec'\"'\"'))' install --record 'C:\\Users\\ASF_Portable\\AppData\\Local\\Temp\\pip-record-lt76g8ex\\install-record.txt' --single-version-externally-managed --compile --install-headers 'c:\\users\\asf_portable\\anaconda3\\Include\\pycocotools' Check the logs for full command output.\n"
     ]
    }
   ],
   "source": [
    "!pip install pycocotools"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "-vsOL3QR6kqs"
   },
   "source": [
    "Get `tensorflow/models` or `cd` to parent directory of the repository."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "ykA0c-om51s1"
   },
   "outputs": [],
   "source": [
    "import os\n",
    "import pathlib\n",
    "\n",
    "\n",
    "if \"models\" in pathlib.Path.cwd().parts:\n",
    "  while \"models\" in pathlib.Path.cwd().parts:\n",
    "    os.chdir('..')\n",
    "elif not pathlib.Path('models').exists():\n",
    "  !git clone --depth 1 https://github.com/tensorflow/models"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "O219m6yWAj9l"
   },
   "source": [
    "Compile protobufs and install the object_detection package"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "PY41vdYYNlXc"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "W\u0000S\u0000L\u0000 \u00002\u0000 \u0000n\u0000é\u0000c\u0000e\u0000s\u0000s\u0000i\u0000t\u0000e\u0000 \u0000u\u0000n\u0000e\u0000 \u0000m\u0000i\u0000s\u0000e\u0000 \u0000à\u0000 \u0000j\u0000o\u0000u\u0000r\u0000 \u0000d\u0000e\u0000 \u0000s\u0000o\u0000n\u0000 \u0000c\u0000o\u0000m\u0000p\u0000o\u0000s\u0000a\u0000n\u0000t\u0000 \u0000n\u0000o\u0000y\u0000a\u0000u\u0000.\u0000 \u0000P\u0000o\u0000u\u0000r\u0000 \u0000p\u0000l\u0000u\u0000s\u0000 \u0000d\u0000\u0019 i\u0000n\u0000f\u0000o\u0000r\u0000m\u0000a\u0000t\u0000i\u0000o\u0000n\u0000s\u0000,\u0000 \u0000v\u0000i\u0000s\u0000i\u0000t\u0000e\u0000z\u0000 \u0000h\u0000t\u0000t\u0000p\u0000s\u0000:\u0000/\u0000/\u0000a\u0000k\u0000a\u0000.\u0000m\u0000s\u0000/\u0000w\u0000s\u0000l\u00002\u0000k\u0000e\u0000r\u0000n\u0000e\u0000l\u0000\r",
      "\u0000\r",
      "\u0000\n",
      "\u0000"
     ]
    },
    {
     "ename": "CalledProcessError",
     "evalue": "Command 'b'cd models/research/\\nprotoc object_detection/protos/*.proto --python_out=.\\n'' returned non-zero exit status 4294967295.",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mCalledProcessError\u001b[0m                        Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-4-99b2dbacc58a>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mget_ipython\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mrun_cell_magic\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'bash'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m''\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'cd models/research/\\nprotoc object_detection/protos/*.proto --python_out=.\\n'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\IPython\\core\\interactiveshell.py\u001b[0m in \u001b[0;36mrun_cell_magic\u001b[1;34m(self, magic_name, line, cell)\u001b[0m\n\u001b[0;32m   2397\u001b[0m             \u001b[1;32mwith\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mbuiltin_trap\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2398\u001b[0m                 \u001b[0margs\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m(\u001b[0m\u001b[0mmagic_arg_s\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcell\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 2399\u001b[1;33m                 \u001b[0mresult\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mfn\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   2400\u001b[0m             \u001b[1;32mreturn\u001b[0m \u001b[0mresult\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2401\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\IPython\\core\\magics\\script.py\u001b[0m in \u001b[0;36mnamed_script_magic\u001b[1;34m(line, cell)\u001b[0m\n\u001b[0;32m    140\u001b[0m             \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    141\u001b[0m                 \u001b[0mline\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mscript\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 142\u001b[1;33m             \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mshebang\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mline\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcell\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    143\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    144\u001b[0m         \u001b[1;31m# write a basic docstring:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\decorator.py\u001b[0m in \u001b[0;36mfun\u001b[1;34m(*args, **kw)\u001b[0m\n\u001b[0;32m    229\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[0mkwsyntax\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    230\u001b[0m                 \u001b[0margs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mkw\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mfix\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mkw\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0msig\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 231\u001b[1;33m             \u001b[1;32mreturn\u001b[0m \u001b[0mcaller\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfunc\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m*\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mextras\u001b[0m \u001b[1;33m+\u001b[0m \u001b[0margs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkw\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    232\u001b[0m     \u001b[0mfun\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m__name__\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mfunc\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m__name__\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    233\u001b[0m     \u001b[0mfun\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m__doc__\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mfunc\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m__doc__\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\IPython\\core\\magic.py\u001b[0m in \u001b[0;36m<lambda>\u001b[1;34m(f, *a, **k)\u001b[0m\n\u001b[0;32m    185\u001b[0m     \u001b[1;31m# but it's overkill for just that one bit of state.\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    186\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mmagic_deco\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0marg\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 187\u001b[1;33m         \u001b[0mcall\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;32mlambda\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m*\u001b[0m\u001b[0ma\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mk\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0ma\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mk\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    188\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    189\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mcallable\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0marg\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\IPython\\core\\magics\\script.py\u001b[0m in \u001b[0;36mshebang\u001b[1;34m(self, line, cell)\u001b[0m\n\u001b[0;32m    243\u001b[0m             \u001b[0msys\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mstderr\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mflush\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    244\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0margs\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mraise_error\u001b[0m \u001b[1;32mand\u001b[0m \u001b[0mp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mreturncode\u001b[0m\u001b[1;33m!=\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 245\u001b[1;33m             \u001b[1;32mraise\u001b[0m \u001b[0mCalledProcessError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mreturncode\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcell\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0moutput\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mout\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mstderr\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0merr\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    246\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    247\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m_run_script\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mp\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcell\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mto_close\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mCalledProcessError\u001b[0m: Command 'b'cd models/research/\\nprotoc object_detection/protos/*.proto --python_out=.\\n'' returned non-zero exit status 4294967295."
     ]
    }
   ],
   "source": [
    "%%bash\n",
    "cd models/research/\n",
    "protoc object_detection/protos/*.proto --python_out=."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "s62yJyQUcYbp"
   },
   "outputs": [],
   "source": [
    "%%bash \n",
    "cd models/research\n",
    "pip install ."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "LBdjK2G5ywuc"
   },
   "source": [
    "### Imports"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "hV4P5gyTWKMI"
   },
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import os\n",
    "import six.moves.urllib as urllib\n",
    "import sys\n",
    "import tarfile\n",
    "import tensorflow as tf\n",
    "import zipfile\n",
    "\n",
    "from collections import defaultdict\n",
    "from io import StringIO\n",
    "from matplotlib import pyplot as plt\n",
    "from PIL import Image\n",
    "from IPython.display import display"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "r5FNuiRPWKMN"
   },
   "source": [
    "Import the object detection module."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "4-IMl4b6BdGO"
   },
   "outputs": [],
   "source": [
    "from object_detection.utils import ops as utils_ops\n",
    "from object_detection.utils import label_map_util\n",
    "from object_detection.utils import visualization_utils as vis_util"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "RYPCiag2iz_q"
   },
   "source": [
    "Patches:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "mF-YlMl8c_bM"
   },
   "outputs": [],
   "source": [
    "# patch tf1 into `utils.ops`\n",
    "utils_ops.tf = tf.compat.v1\n",
    "\n",
    "# Patch the location of gfile\n",
    "tf.gfile = tf.io.gfile"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "cfn_tRFOWKMO"
   },
   "source": [
    "# Model preparation "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "X_sEBLpVWKMQ"
   },
   "source": [
    "## Variables\n",
    "\n",
    "Any model exported using the `export_inference_graph.py` tool can be loaded here simply by changing the path.\n",
    "\n",
    "By default we use an \"SSD with Mobilenet\" model here. See the [detection model zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md) for a list of other models that can be run out-of-the-box with varying speeds and accuracies."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "7ai8pLZZWKMS"
   },
   "source": [
    "## Loader"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "zm8xp-0eoItE"
   },
   "outputs": [],
   "source": [
    "def load_model(model_name):\n",
    "  base_url = 'http://download.tensorflow.org/models/object_detection/'\n",
    "  model_file = model_name + '.tar.gz'\n",
    "  model_dir = tf.keras.utils.get_file(\n",
    "    fname=model_name, \n",
    "    origin=base_url + model_file,\n",
    "    untar=True)\n",
    "\n",
    "  model_dir = pathlib.Path(model_dir)/\"saved_model\"\n",
    "\n",
    "  model = tf.saved_model.load(str(model_dir))\n",
    "\n",
    "  return model"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "_1MVVTcLWKMW"
   },
   "source": [
    "## Loading label map\n",
    "Label maps map indices to category names, so that when our convolution network predicts `5`, we know that this corresponds to `airplane`.  Here we use internal utility functions, but anything that returns a dictionary mapping integers to appropriate string labels would be fine"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "hDbpHkiWWKMX"
   },
   "outputs": [],
   "source": [
    "# List of the strings that is used to add correct label for each box.\n",
    "PATH_TO_LABELS = 'models/research/object_detection/data/mscoco_label_map.pbtxt'\n",
    "category_index = label_map_util.create_category_index_from_labelmap(PATH_TO_LABELS, use_display_name=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "oVU3U_J6IJVb"
   },
   "source": [
    "For the sake of simplicity we will test on 2 images:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "jG-zn5ykWKMd"
   },
   "outputs": [],
   "source": [
    "# If you want to test the code with your images, just add path to the images to the TEST_IMAGE_PATHS.\n",
    "PATH_TO_TEST_IMAGES_DIR = pathlib.Path('models/research/object_detection/test_images')\n",
    "TEST_IMAGE_PATHS = sorted(list(PATH_TO_TEST_IMAGES_DIR.glob(\"*.jpg\")))\n",
    "TEST_IMAGE_PATHS"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "H0_1AGhrWKMc"
   },
   "source": [
    "# Detection"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "f7aOtOlebK7h"
   },
   "source": [
    "Load an object detection model:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "1XNT0wxybKR6"
   },
   "outputs": [],
   "source": [
    "model_name = 'ssd_mobilenet_v1_coco_2017_11_17'\n",
    "detection_model = load_model(model_name)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "yN1AYfAEJIGp"
   },
   "source": [
    "Check the model's input signature, it expects a batch of 3-color images of type uint8:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "CK4cnry6wsHY"
   },
   "outputs": [],
   "source": [
    "print(detection_model.signatures['serving_default'].inputs)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "Q8u3BjpMJXZF"
   },
   "source": [
    "And returns several outputs:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "oLSZpfaYwuSk"
   },
   "outputs": [],
   "source": [
    "detection_model.signatures['serving_default'].output_dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "FZyKUJeuxvpT"
   },
   "outputs": [],
   "source": [
    "detection_model.signatures['serving_default'].output_shapes"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "JP5qZ7sXJpwG"
   },
   "source": [
    "Add a wrapper function to call the model, and cleanup the outputs:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "ajmR_exWyN76"
   },
   "outputs": [],
   "source": [
    "def run_inference_for_single_image(model, image):\n",
    "  image = np.asarray(image)\n",
    "  # The input needs to be a tensor, convert it using `tf.convert_to_tensor`.\n",
    "  input_tensor = tf.convert_to_tensor(image)\n",
    "  # The model expects a batch of images, so add an axis with `tf.newaxis`.\n",
    "  input_tensor = input_tensor[tf.newaxis,...]\n",
    "\n",
    "  # Run inference\n",
    "  model_fn = model.signatures['serving_default']\n",
    "  output_dict = model_fn(input_tensor)\n",
    "\n",
    "  # All outputs are batches tensors.\n",
    "  # Convert to numpy arrays, and take index [0] to remove the batch dimension.\n",
    "  # We're only interested in the first num_detections.\n",
    "  num_detections = int(output_dict.pop('num_detections'))\n",
    "  output_dict = {key:value[0, :num_detections].numpy() \n",
    "                 for key,value in output_dict.items()}\n",
    "  output_dict['num_detections'] = num_detections\n",
    "\n",
    "  # detection_classes should be ints.\n",
    "  output_dict['detection_classes'] = output_dict['detection_classes'].astype(np.int64)\n",
    "   \n",
    "  # Handle models with masks:\n",
    "  if 'detection_masks' in output_dict:\n",
    "    # Reframe the the bbox mask to the image size.\n",
    "    detection_masks_reframed = utils_ops.reframe_box_masks_to_image_masks(\n",
    "              output_dict['detection_masks'], output_dict['detection_boxes'],\n",
    "               image.shape[0], image.shape[1])      \n",
    "    detection_masks_reframed = tf.cast(detection_masks_reframed > 0.5,\n",
    "                                       tf.uint8)\n",
    "    output_dict['detection_masks_reframed'] = detection_masks_reframed.numpy()\n",
    "    \n",
    "  return output_dict"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "z1wq0LVyMRR_"
   },
   "source": [
    "Run it on each test image and show the results:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "DWh_1zz6aqxs"
   },
   "outputs": [],
   "source": [
    "def show_inference(model, image_path):\n",
    "  # the array based representation of the image will be used later in order to prepare the\n",
    "  # result image with boxes and labels on it.\n",
    "  image_np = np.array(Image.open(image_path))\n",
    "  # Actual detection.\n",
    "  output_dict = run_inference_for_single_image(model, image_np)\n",
    "  # Visualization of the results of a detection.\n",
    "  vis_util.visualize_boxes_and_labels_on_image_array(\n",
    "      image_np,\n",
    "      output_dict['detection_boxes'],\n",
    "      output_dict['detection_classes'],\n",
    "      output_dict['detection_scores'],\n",
    "      category_index,\n",
    "      instance_masks=output_dict.get('detection_masks_reframed', None),\n",
    "      use_normalized_coordinates=True,\n",
    "      line_thickness=8)\n",
    "\n",
    "  display(Image.fromarray(image_np))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "3a5wMHN8WKMh"
   },
   "outputs": [],
   "source": [
    "for image_path in TEST_IMAGE_PATHS:\n",
    "  show_inference(detection_model, image_path)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "DsspMPX3Cssg"
   },
   "source": [
    "## Instance Segmentation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "CzkVv_n2MxKC"
   },
   "outputs": [],
   "source": [
    "model_name = \"mask_rcnn_inception_resnet_v2_atrous_coco_2018_01_28\"\n",
    "masking_model = load_model(model_name)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "0S7aZi8ZOhVV"
   },
   "source": [
    "The instance segmentation model includes a `detection_masks` output:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "vQ2Sj2VIOZLA"
   },
   "outputs": [],
   "source": [
    "masking_model.output_shapes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "AS57rZlnNL7W"
   },
   "outputs": [],
   "source": [
    "for image_path in TEST_IMAGE_PATHS:\n",
    "  show_inference(masking_model, image_path)"
   ]
  }
 ],
 "metadata": {
  "accelerator": "GPU",
  "colab": {
   "collapsed_sections": [],
   "last_runtime": {
    "build_target": "//learning/brain/python/client:colab_notebook",
    "kind": "private"
   },
   "name": "object_detection_tutorial.ipynb",
   "private_outputs": true,
   "provenance": [
    {
     "file_id": "/piper/depot/google3/third_party/tensorflow_models/object_detection/colab_tutorials/object_detection_tutorial.ipynb",
     "timestamp": 1594335690840
    },
    {
     "file_id": "1LNYL6Zsn9Xlil2CVNOTsgDZQSBKeOjCh",
     "timestamp": 1566498233247
    },
    {
     "file_id": "/piper/depot/google3/third_party/tensorflow_models/object_detection/object_detection_tutorial.ipynb?workspaceId=markdaoust:copybara_AFABFE845DCD573AD3D43A6BAFBE77D4_0::citc",
     "timestamp": 1566488313397
    },
    {
     "file_id": "/piper/depot/google3/third_party/py/tensorflow_docs/g3doc/en/r2/tutorials/generative/object_detection_tutorial.ipynb?workspaceId=markdaoust:copybara_AFABFE845DCD573AD3D43A6BAFBE77D4_0::citc",
     "timestamp": 1566145894046
    },
    {
     "file_id": "1nBPoWynOV0auSIy40eQcBIk9C6YRSkI8",
     "timestamp": 1566145841085
    },
    {
     "file_id": "/piper/depot/google3/third_party/tensorflow_models/object_detection/object_detection_tutorial.ipynb?workspaceId=markdaoust:copybara_AFABFE845DCD573AD3D43A6BAFBE77D4_0::citc",
     "timestamp": 1556295408037
    },
    {
     "file_id": "1layerger-51XwWOwYMY_5zHaCavCeQkO",
     "timestamp": 1556214267924
    },
    {
     "file_id": "/piper/depot/google3/third_party/tensorflow_models/object_detection/object_detection_tutorial.ipynb?workspaceId=markdaoust:copybara_AFABFE845DCD573AD3D43A6BAFBE77D4_0::citc",
     "timestamp": 1556207836484
    },
    {
     "file_id": "1w6mqQiNV3liPIX70NOgitOlDF1_4sRMw",
     "timestamp": 1556154824101
    },
    {
     "file_id": "https://github.com/tensorflow/models/blob/master/research/object_detection/object_detection_tutorial.ipynb",
     "timestamp": 1556150293326
    }
   ]
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
