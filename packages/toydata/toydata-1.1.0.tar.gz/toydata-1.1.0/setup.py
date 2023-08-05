# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['toydata']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'toydata',
    'version': '1.1.0',
    'description': 'Data Structures in Python',
    'long_description': '\n<p align="center" style="font-size:40px; margin:0px 10px 0px 10px">\n    <em>ToyData</em>\n</p>\n<p align="center">\n    <em>Learning Data Structures with toy code</em>\n</p>\n\n<p align="center">\n<a href="https://codecov.io/gh/shenxiangzhuang/toydata" target="_blank">\n    <img src="https://codecov.io/gh/shenxiangzhuang/toydata/branch/master/graph/badge.svg" alt="Coverage">\n</a>\n<a href="https://pypi.org/project/toydata" target="_blank">\n    <img src="https://badge.fury.io/py/toydata.svg" alt="PyPI Package">\n</a>\n</p>\n\n\n![](https://github.com/shenxiangzhuang/toydata/raw/master/toydata.png)\n\n\nThere are some simple implementations(in Python3.7.6) of classic data structrues.\n\nI am trying to do this with an easy-to-read style.\n\nAnd, I add some extra functions beyond the ADTs, which are used mostly for printing and testing purposes.\n\n### Install\n[ToyData 1.0 in pypi](https://pypi.org/project/toydata/1.0/)\nJust run:`pip install ToyData==1.0` in your cmd.\n\n>Note that: If you had change the default mirror of pip to another one,\n>such as *https://pypi.tuna.tsinghua.edu.cn/simple* or *http://pypi.douban.com/simple* , you may have to install with `pip install ToyData -i https://pypi.org/simple`\n\n\n### Books\n\n[*Data Structures and Algorithms in Python, Michael T. Goodrich*](https://www.amazon.com/Structures-Algorithms-Python-Michael-Goodrich/dp/1118290275/ref=sr_1_4?qid=1580122939&refinements=p_27%3AMichael+T.+Goodrich&s=books&sr=1-4&text=Michael+T.+Goodrich)\nis the **main reference** of the implementations.\n\nNote that there is a book named [*Data Structures and Algorithms in C++, Michael T. Goodrich*](https://www.amazon.com/Data-Structures-Algorithms-Michael-Goodrich/dp/0470383275/ref=sr_1_2?qid=1580122957&refinements=p_27%3AMichael+T.+Goodrich&s=books&sr=1-2&text=Michael+T.+Goodrich) which use C++ to implement these data structures.\n\nAnd [*Data Structures Using C, Reema Thareja*](https://www.amazon.in/Data-Structures-Using-Reema-Thareja/dp/0198099304/ref=sr_1_1?qid=1580122713&refinements=p_27%3AReema+Thareja&s=books&sr=1-1) is also a great book that implement these data structures using C.\n\n\n\n### Documentation\n[ToyData](http://datahonor.com/toydata/)\n\n\n### API\n\n- [x] Stack: ArrayStack, LinkedStack\n- [x] Queue: ArrayQueue, ArrayDeque\n- [x] Deque: LinkedDeque\n- [x] Positional List: PositionalList\n- [x] Prority Queues: UnsortedPriorityQueue, SortedPriorityQueue, HeapPriorityQueue\n- [x] LinkedLists: Singlellist, Doublellist\n- [x] Hash Tables: ChainHashMap, ProbeHashMap, SortedTableMap\n- [x] Trees: LinkedBinaryTree\n- [x] Search Trees: AVLTreeMap, SplayTreeMap, RedBlackTreeMap\n- [x] Graph: Adjacency Map, DFS/BFS, Floyd-Warshall\n\n\n\n### Courses\nThere some courses that use the book(*Data Structures and Algorithms in Python*) as textbook.(Tell me please, if you know other courses use it:-)\n\n1. [数据结构与算法-Python (2019秋季)，武汉大学](http://xpzhang.me/)\n   >Great lecture notes.\n\n\n### References:\n\n1. [Jenny\'s lectures CS/IT NET&JRF](https://www.youtube.com/channel/UCM-yUTYGmrNvKOCcAl21g3w/playlists)\n   >Jenny makes everything clear！\n',
    'author': 'Xiangzhuang Shen',
    'author_email': 'datahonor@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
