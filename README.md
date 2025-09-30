# [Exercism Python Track](https://exercism.io/tracks/python)

[![Pytest Workflow](https://github.com/ikostan/python/actions/workflows/pytest.yml/badge.svg)](https://github.com/ikostan/python/actions/workflows/pytest.yml)
[![Pylint](https://github.com/ikostan/python/actions/workflows/pylint.yml/badge.svg)](https://github.com/ikostan/python/actions/workflows/pylint.yml)
[![Ruff Lint and Format](https://github.com/ikostan/python/actions/workflows/ruff.yml/badge.svg)](https://github.com/ikostan/python/actions/workflows/ruff.yml)
[![Flake8](https://github.com/ikostan/python/actions/workflows/flake8.yml/badge.svg)](https://github.com/ikostan/python/actions/workflows/flake8.yml)
[![codecov](https://codecov.io/github/ikostan/python/graph/badge.svg?token=G78RWJWJ38)](https://codecov.io/github/ikostan/python)

<div align="center"> 
<img width="9%" height="9%" src="https://github.com/ikostan/Exercism_Python_Track/blob/master/img/python-track.png" hspace="20">
</div>

## Exercism exercises in Python

### About Exercism

`Exercism` is an online platform designed to help you improve your coding
skills through practice and mentorship.

`Exercism` provides you with thousands of exercises spread across numerous
language tracks. Once you start a language track you are presented with a
core set of exercises to complete. Each one is a fun and interesting
challenge designed to teach you a little more about the features of a language.

You complete a challenge by downloading the exercise to your computer and
solving it in your normal working environment. Once you've finished you submit
it online and one of our mentors will give you feedback on how you could improve
it using features of the language that you may not be familiar with. After a
couple of rounds of refactoring, your exercise will be complete and you will
unlock both the next core exercise and also a series of related side-exercises
for you to practice with.

`Exercism` is entirely open source and relies on the contributions of thousands
of wonderful people.


### Local Docker-Based CI Test Environment

This setup provides a Docker container that replicates the GitHub Actions
environment (`Ubuntu 24.04`, `Python 3.12`) for running linting and testing
workflows locally. Use it to validate your code before pushing to GitHub.

#### Prerequisites

- Docker installed and running on your machine. Download from
  [docker.com](https://www.docker.com/get-started).
- Your repo cloned locally (e.g., `git clone https://github.com/ikostan/python.git`).
- Ensure `requirements.txt` exists in the repo root (even if empty).
  If you have a `.pylintrc`, it should be in the root as well.

#### Building and Using the Docker Container

1. **Place the files**:
   - Save the `Dockerfile` and `run_ci_tests.sh` in your repo root.
   - Make run_ci_tests.sh executable:
     - On Unix/macOS: ```chmod +x run_ci_tests.sh```
     - On Windows: No need, as it's run inside the Linux container.

2. **Build the Docker image**:
   ```bash
   docker build -t python-ci-env .
   ```
   This creates an image with `Python 3.12`, all linters (`Ruff`, `Flake8`, `Pylint`),
   and testers (`Pytest`, `pytest-cov`) installed.

3. **Run the container interactively** (for manual testing):
   * On Unix/macOS:
   ```bash
   docker run -it -v $(pwd):/app python-ci-env
   ```
   * On Windows PowerShell:
   ```bash
   docker run -it -v ${PWD}:/app python-ci-env
   ```
   * On Windows Command Prompt (cmd.exe):
   ```bash
   docker run -it -v %cd%:/app python-ci-env
   ```
   - This mounts your local repo to `/app` in the container and drops you into a bash shell.
   - Inside the container, you can run individual commands or the full script.

4. **Run all CI tests at once** (non-interactively):
   * On Unix/macOS:
   ```bash
   docker run -v $(pwd):/app python-ci-env /app/run_ci_tests.sh
   ```
   * On Windows PowerShell:
   ```bash
   docker run -v ${PWD}:/app python-ci-env /app/run_ci_tests.sh
   ```
   * On Windows Command Prompt (cmd.exe):
   ```bash
   docker run -v %cd%:/app python-ci-env /app/run_ci_tests.sh
   ```
   - This executes all linting and testing steps sequentially, mimicking the workflows.
   - Output will show results for `Ruff`, `Flake8`, `Pylint`, `Pytest`, and coverage generation.
   - If any step fails, the script exits early (like in CI).

5. **Run specific tests inside the container**:
   - Start the interactive container as in step 3.
   - Then run individual commands, e.g.:
     ```bash
     ruff check --output-format=github .
     pytest . --verbose --ignore=solutions --log-cli-level=INFO
     ```

#### Notes

- **Failures**: If tests fail, fix your code and rebuild/run again. The env matches GitHub,
  so issues should align.
- **Rebuilding**: If you update `requirements.txt` or add new deps, rebuild the image with
  `docker build -t python-ci-env .`.
- **Performance**: First build may take time to install packages; subsequent runs are faster.
- **Customization**: If your repo has no `requirements.txt`, the install step does nothing—that's
  fine for `Exercism` exercises.
- **Cleanup**: Use `docker image prune` to remove old images if needed.
- **Windows-Specific**: If mounting fails (e.g., permission issues), ensure your drive is shared
  in Docker Desktop settings. Use forward slashes in paths if needed, but Docker handles backslashes.

**This keeps things simple:** build once, run tests locally, catch issues early.
