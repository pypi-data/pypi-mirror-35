==========================
中文分词器集合
==========================


.. image:: https://img.shields.io/pypi/v/chinese_tokenzier_iterator.svg
        :target: https://pypi.python.org/pypi/tokenzier_iterator

.. image:: https://img.shields.io/travis/howl-anderson/chinese_tokenzier_iterator.svg
        :target: https://travis-ci.org/howl-anderson/tokenzier_iterator

.. image:: https://readthedocs.org/projects/chinese-tokenzier-iterator/badge/?version=latest
        :target: https://tokenzier-iterator.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




一些中文分词器的简单封装和集合


* Free software: MIT license
* Documentation: https://chinese-tokenzier-iterator.readthedocs.io.


Features
--------

* TODO

使用
----
.. code-block:: python

    from tokenizers_collection.config import tokenizer_registry
    for name, tokenizer in tokenizer_registry:
        print("Tokenizer: {}".format(name))
        tokenizer('input_file.txt', 'output_file.txt')

安装
----
.. code-block:: bash

    pip install tokenizers_collection

更新许可文件与下载模型
=======================
因为其中有些模型需要更新许可文件（比如：pynlpir）或者需要下载模型文件（比如：pyltp），因此安装后需要执行特定的命令完成操作，这里已经将所有的操作封装成了一个函数，只需要执行类似如下的指令即可

.. code-block:: bash

    python -m tokenizers_collection.helper


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
