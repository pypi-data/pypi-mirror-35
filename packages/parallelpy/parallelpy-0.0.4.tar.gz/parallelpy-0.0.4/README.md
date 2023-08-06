<p align="center">
    <a href="https://pypi.org/project/parallelpy/">
        <img src="https://img.shields.io/badge/PyPI-0.0.4-brightgreen.svg?longCache=true&style=flat-square"/>
    </a>
</p>  

# parallelpy  

A minimal parallel processing module for data science applications  

+ pip install parallelpy  

```python
from parallelpy import Parallelizer

parallelizer = Parallelizer(
    target=print,
    args=[i for i in range(100)],
    enable_results=False,
    auto_proc_count=True,
    max_proc_count=8
)

parallelizer.run()
```
