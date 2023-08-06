ClutchGen is CLI tool for generating new projects structures. Developed on python.
Using `.yaml` config files you can create structures any complexity

For example with config like:

```yaml
$root:
  - app:
    - src:
      - services:
          - some_service.py
      - settings.py
    - main.py
  - Makefile
  - README.md
```

You will get structure like this:

![img.png](docs/images/example_of_project.png)

More info about usage you can find on [WIKI pages](https://gitlab.com/AlexeyReket/clutchgen/-/wikis/home)
