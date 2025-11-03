1. Clone the repo and enter the project folder

```bash
git clone https://github.com/YounesBensafia/nashlab.git
cd nashlab
```

2. Check the required Python version

```bash
cat .python-version
```

3. Create and activate a virtual environment

```bash
# Create venv
python -m venv .venv
or
uv venv

# Activate (Linux / macOS)
source .venv/bin/activate

4. Install dependencies (choose one of the two options below depending on your workflow)

**A. If you use Poetry (recommended, because the repo contains `pyproject.toml`)**

```bash
# install Poetry if not installed
pip install --upgrade pip
pip install poetry
or
uv add poetry

# Install project dependencies
poetry install
# To run commands inside poetry shell:
poetry shell
```

**B. If you prefer pip and there is no requirements.txt**

```bash
# If the project provides an installable package via pyproject.toml:
pip install --upgrade pip setuptools
pip install .

# OR (if the repo contains a requirements.txt)
pip install -r requirements.txt
```

5. Run the application entrypoint

```bash
# From the project root
python main.py
```
6. Troubleshooting checklist

* Confirm the Python version matches `.python-version`.
* If dependency installation fails
* Look at `pyproject.toml` for required packages and scripts.
* Inspect `main.py` and the `src/` folder to confirm the expected run command or additional setup steps.

