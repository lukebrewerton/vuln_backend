# Contribution guidelines
 **Working on your first Pull Request?** You can learn how from this *free* series [How to Contribute to an Open Source Project on GitHub](https://egghead.io/series/how-to-contribute-to-an-open-source-project-on-github)

First of all, thanks for thinking of contributing to this project. :smile:

Before sending a Pull Request, please make sure that you're assigned the task on a GitHub issue.

- If a relevant issue already exists, discuss on the issue and get it assigned to yourself on GitHub.
- If no relevant issue exists, open a new issue and get it assigned to yourself on GitHub.

Please proceed with a Pull Request only after you're assigned. It'd be sad if your Pull Request (and your hardwork) isn't accepted just because it isn't idealogically compatible.

# Developing the scripts

1. Install with

    ```sh
    git clone git@github.com:lukebrewerton/vuln_backend.git
    cd vuln_backend
    pip install -r requirements.txt
    ```

2. Make your changes in a different git branch (say, `add-new-flag`). These changes can be

    - adding extra features
    - fixing bugs
    - add tests

3. (Optional) To test whether `vuln_backend` scripts is working properly, do 
    ```sh
    python vuln_backend.py
    ```

4. (Required for script file changes) These are the specifications for the script files (/vuln_backend/) -

    - filenames must be descriptive of the functions inside
    - functions must also be descriptively named i.e. not MyFunction but something like download_all
    - adhere to PEP8 guidelines

5. (Required for new tests) Add command to `.travis.yml` file.
