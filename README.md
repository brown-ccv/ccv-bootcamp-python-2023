# CCV Bootcamp Python

This repository contains Jupyter notebooks for a workshop by the for the [CCV Bootcamp]
(https://docs.ccv.brown.edu/bootcamp-2023/schuedule/wednesday-5-may-1), around an introduction 
to Python and data wrangling with Python. 

[Slides for Python Programming Basics](https://docs.google.com/presentation/d/1WYDiY4YUd78zdWkum3kkSNI6ZnTd6C_PMwNRZPCi37Y/edit?usp=sharing)

# Authors

Ellen Duong, George Dang, and John Holland

It was adapted from previous CCV's annual 
[summer Python workshop](https://github.com/brown-ccv/workshop-python-2020) and 
[Bootcamps](https://github.com/brown-ccv/ccv-bootcamp-python).

# Contact

For assistance, use the CCV-Share Slack channel for today's workshop: 
https://ccv-share.slack.com/archives/C0562DCNCD7

You may need to sign up here first: https://ccv-share.slack.com/signup#/

# Get Started with the project

This workshop will run on Jupyter Notebooks. If you're using Brown University Open On Demand, 
you need to:

- clone the repository using the "OSCAR Shell Access" app
- load the notebooks using the "Basic Jupyter Notebook with Anaconda" app

## Clone the Repo

Navigate to [ood.ccv.brown.edu](https://ood.ccv.brown.edu) and log in.

Select the Oscar Shell Access App:
![On ood.ccv.brown.edu, under the heading "Pinned Apps", selection: "OSCAR Shell access, System Installed App"](assets/ood-pinned-apps-oscar-shell-access-selected.png)

Then run the following commands. First, load the necessary modules:
```bash
module load "git/2.29.2"
```

Clone the repository using the command:
```bash
git clone https://github.com/brown-ccv/ccv-bootcamp-python-2023
```

Check you can enter the repository directory using the command:
```bash
cd ccv-bootcamp-python-2023
```

## Open the repository in Jupyter Notebook

To open the Jupyter Notebook in OpenOnDemand, first navigate to [ood.ccv.brown.edu](https://ood.ccv.brown.edu).

There select the Jupyter Notebook app:
![On ood.ccv.brown.edu, under the heading "Default GUIs", selection: "Basic Jupyter Notebook, System Installed App"](assets/ood-default-guis-jupyter-selected.png)

You should make the following selections:
- **Oscar Anaconda Module: `anaconda/2022.05`**
- Conda env: `/gpfs/data/datasci/bootcamp-python/venv`
- Modules: Leave empty
- Extra Jupyter args: Leave empty
- Number of cores: `1`
- Memory per job: `default`
- Number of GPUs: `1` (this will be ignored)
- Condo account: Leave empty
- Partition: Leave empty
- Reservation: Leave empty
- Number of hours: 8

Then click the "Launch" button.
![on ood.ccv.brown.edu, launch button](assets/ood-jupyter-launch-button.png)

On the next page, you will see a "Basic Jupyter Notebook" card with the current status, and once the notebook has been started, you can click on "Connect to Jupyter" to launch the Jupyter session.
![on ood.ccv.brown.edu, a card displaying a running "Basic Jupyter Notebook" with the "Connect to Jupyter" button visible](assets/ood-basic-jupyter-notebook-running.png)

In the notebook interface you can navigate to the `ccv-bootcamp-python-2023` directory and access the 
session notebooks.
