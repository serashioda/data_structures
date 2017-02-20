"""Setup data-structures module."""


from setuptools import setup

setup(
    name="data-structures",
    description="Python implementations of classic data structures",
    version=0.2,
    author=["Sera Smith", "Amos Boldor"],
    install_requires=['scikit-learn==0.18.1'],
    licencse="MIT",
    package_dir={'': 'src'},
    py_modules=["insertion_sort", "bin_heap", "bst", "deque", "dll", "graph", "linked_list", "priority_queue", "merge_sort", "my_queue", "quick_sort", "shortest_path", "simple_graph", "stack", "trie", "weighted_graph"],
    extras_require={
        "test": ["pytest", "pytest-cov", "tox"]
    }
)
