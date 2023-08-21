![Kedro Logo Banner - Light](.github/demo-dark.png#gh-dark-mode-only)
![Kedro Logo Banner - Dark](.github/demo-light.png#gh-light-mode-only)
[![Python version](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-blue.svg)](https://pypi.org/project/kedro/)
[![PyPI version](https://badge.fury.io/py/kedro.svg)](https://pypi.org/project/kedro/)
[![Conda version](https://img.shields.io/conda/vn/conda-forge/kedro.svg)](https://anaconda.org/conda-forge/kedro)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/kedro-org/kedro/blob/main/LICENSE.md)
[![Slack Organisation](https://img.shields.io/badge/slack-chat-blueviolet.svg?label=Kedro%20Slack&logo=slack)](https://slack.kedro.org)
[![Slack Archive](https://img.shields.io/badge/slack-archive-blueviolet.svg?label=Kedro%20Slack%20)](https://linen-slack.kedro.org/)
![CircleCI - Main Branch](https://img.shields.io/circleci/build/github/kedro-org/kedro/main?label=main)
![Develop Branch Build](https://img.shields.io/circleci/build/github/kedro-org/kedro/develop?label=develop)
[![Documentation](https://readthedocs.org/projects/kedro/badge/?version=stable)](https://docs.kedro.org/)
[![OpenSSF Best Practices](https://bestpractices.coreinfrastructure.org/projects/6711/badge)](https://bestpractices.coreinfrastructure.org/projects/6711)
[![Monthly downloads](https://static.pepy.tech/badge/kedro/month)](https://pepy.tech/project/kedro)
[![Total downloads](https://static.pepy.tech/badge/kedro)](https://pepy.tech/project/kedro)

## What is Kedro?

Kedro is a toolbox for production-ready data science. It uses software engineering best practices to help you create data engineering and data science pipelines that are reproducible, maintainable, and modular. You can find out more at [kedro.org](https://kedro.org).

Kedro is an open-source Python framework hosted by the [LF AI & Data Foundation](https://lfaidata.foundation/).
dwjfj
## How do I install Kedro?

To install Kedro from the Python Package Index (PyPI) run:

```
pip install kedro
```

It is also possible to install Kedro using `conda`:

```
conda install -c conda-forge kedro
```

Our [Get Started guide](https://docs.kedro.org/en/stable/get_started/install.html) contains full installation instructions, and includes how to set up Python virtual environments.

## What are the main features of Kedro?

![Kedro-Viz Pipeline Visualisation](https://github.com/kedro-org/kedro-viz/blob/main/.github/img/banner.png)
_A pipeline visualisation generated using [Kedro-Viz](https://github.com/kedro-org/kedro-viz)_

| Feature              | What is this?                                                                                                                                                                                                                                                                                                                                                                                  |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Project Template     | A standard, modifiable and easy-to-use project template based on [Cookiecutter Data Science](https://github.com/drivendata/cookiecutter-data-science/).                                                                                                                                                                                                                                        |
| Data Catalog         | A series of lightweight data connectors used to save and load data across many different file formats and file systems, including local and network file systems, cloud object stores, and HDFS. The Data Catalog also includes data and model versioning for file-based systems.                                                                                                              |
| Pipeline Abstraction | Automatic resolution of dependencies between pure Python functions and data pipeline visualisation using [Kedro-Viz](https://github.com/kedro-org/kedro-viz).                                                                                                                                                                                                                                  |
| Coding Standards     | Test-driven development using [`pytest`](https://github.com/pytest-dev/pytest), produce well-documented code using [Sphinx](http://www.sphinx-doc.org/en/master/), create linted code with support for [`flake8`](https://github.com/PyCQA/flake8), [`isort`](https://github.com/PyCQA/isort) and [`black`](https://github.com/psf/black) and make use of the standard Python logging library. |
| Flexible Deployment  | Deployment strategies that include single or distributed-machine deployment as well as additional support for deploying on Argo, Prefect, Kubeflow, AWS Batch and Databricks.                                                                                                                                                                                                                  |

## How do I use Kedro?

The [Kedro documentation](https://docs.kedro.org/en/stable/) first explains [how to install Kedro](https://docs.kedro.org/en/stable/get_started/install.html) and then introduces [key Kedro concepts](https://docs.kedro.org/en/stable/get_started/kedro_concepts.html).

You can then review the [spaceflights tutorial](https://docs.kedro.org/en/stable/tutorial/spaceflights_tutorial.html) to build a Kedro project for hands-on experience

For new and intermediate Kedro users, there's a comprehensive section on [how to visualise Kedro projects using Kedro-Viz](https://docs.kedro.org/en/stable/visualisation/index.html) and [how to work with Kedro and Jupyter notebooks](https://docs.kedro.org/en/stable/notebooks_and_ipython/index.html). We also recommend the [API reference documentation](/kedro) for additional information.


## Why does Kedro exist?

Kedro is built upon our collective best-practice (and mistakes) trying to deliver real-world ML applications that have vast amounts of raw unvetted data. We developed Kedro to achieve the following:

- To address the main shortcomings of Jupyter notebooks, one-off scripts, and glue-code because there is a focus on
  creating **maintainable data science code**
- To enhance **team collaboration** when different team members have varied exposure to software engineering concepts
- To increase efficiency, because applied concepts like modularity and separation of concerns inspire the creation of
  **reusable analytics code**

Find out more about how Kedro can answer your use cases from the [product FAQs on the Kedro website](https://kedro.org/#faq).

## The humans behind Kedro

The [Kedro product team](https://docs.kedro.org/en/stable/contribution/technical_steering_committee.html#kedro-maintainers) and a number of [open source contributors from across the world](https://github.com/kedro-org/kedro/releases) maintain Kedro.

## Can I contribute?

Yes! We welcome all kinds of contributions. Check out our [guide to contributing to Kedro](https://github.com/kedro-org/kedro/wiki/Contribute-to-Kedro).

## Where can I learn more?

There is a growing community around Kedro. We encourage you to ask and answer technical questions on [Slack](https://slack.kedro.org/) and bookmark the [Linen archive of past discussions](https://linen-slack.kedro.org/).

We keep a list of [technical FAQs in the Kedro documentation](https://docs.kedro.org/en/stable/faq/faq.html) and you can find a  growing list of blog posts, videos and projects that use Kedro over on the [`awesome-kedro` GitHub repository](https://github.com/kedro-org/awesome-kedro). If you have created anything with Kedro we'd love to include it on the list. Just make a PR to add it!

## How can I cite Kedro?

If you're an academic, Kedro can also help you, for example, as a tool to solve the problem of reproducible research. Use the "Cite this repository" button on [our repository](https://github.com/kedro-org/kedro) to generate a citation from the [CITATION.cff file](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files).
