
---
# LangChain

Langchain Tutorial

**This is how to set up this project**

# 0) Change the directory to `langchain_tut`

Run this code `cd langchain_tut`  


# 1) Create a Virtual Environment

Run:

```
python -m venv venv
```

This creates:

```
langchain_tut/
└── venv/
```

The `venv` folder should NOT be uploaded to GitHub.

It is already excluded through `.gitignore`.

**NOTE:** Change the python interpreter of the VS Code to the one in "venv". 


# 2) Activate the Virtual Environment

## Windows PowerShell

```
.\venv\Scripts\Activate.ps1
```

## Windows Command Prompt

```
venv\Scripts\activate
```

## Git Bash

```
source venv/Scripts/activate
```

After activation, you should see something similar to:

```
(venv)
```

at the beginning of your terminal.


# 3) Install the Dependencies

The project contains a `requirements.txt` file.

Install all dependencies with:

```
pip install -r requirements.txt
```

This is the preferred method because the project's dependencies are kept in one place.


# 4) Create the `.env` File

Inside:

```
langchain_tut/
```

create a file named:

```
.env
```

Example:

```
GOOGLE_API_KEY=your_google_api_key
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
```

Add other API keys only if a particular example requires them.

IMPORTANT:

`.env` is intentionally NOT included in GitHub.

Never commit your API keys.


# 5) Installing a Missing Package

If Python gives an error such as:

```
ModuleNotFoundError: No module named 'some_package'
```

install the missing package:

```
pip install some_package
```

Then update `requirements.txt` if the package is a real project dependency.
