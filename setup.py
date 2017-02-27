"""Setup data-structures module."""


from setuptools import setup

setup(
    name="data-structures",
    description="Python implementations of classic data structures",
    version=0.2,
    author=["Sera Smith", "Amos Bolder", "Ford Fowler"],
    author_email=["seras37@gmail.com", "amosbolder@gmail.com", "fordjfowler@gmail.com"],
    licencse="MIT",
    package_dir={'': 'src'},
    py_modules=["bin_heap", "bst", "deque", "dll", "graph", "linked_list", "priority_queue", "my_queue", "shortest_path", "simple_graph", "stack", "trie", "weighted_graph"],
    extras_require={
        "test": ["pytest", "pytest-cov", "tox"]
    }
)
