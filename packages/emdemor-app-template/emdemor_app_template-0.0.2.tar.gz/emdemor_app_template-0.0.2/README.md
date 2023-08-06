## Gerar Documentação

1. Instale sphinx

```bash
pip install sphinx
```

2. Crie e entre na pasta docs e rode sphinx-quickstart

```bash
mkdir docs
cd docs
sphinx-quickstart
```

3. Preencha as informações

```bash
> Separar os diretórios de origem e compilação (y/n) [n]: y
> Nome do projeto: Template de Python
> Nome(s) de autor(es): A. U. Thor
> Lançamento do projeto []: 2022-12-31
> Idioma do projeto [en]: en
```

Após isso, teremos duas pastas dentro de docs. A pasta source vai ser onde vamos trabalhar para gerar documentação. A pasta build será onde a documentação estará.

4. Editar o endereço do seus modulos (no template, é a pasta src) em relação ao arquivo `docs/source/conf.py`. No nosso caso, será:

```python
import os
import sys

sys.path.insert(0, os.path.abspath("../../src"))
```

5. Adicione extensões. No arquivo `docs/source/conf.py`, onde está

```python
# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = []
```

Substitua por:

```python
# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
]
```

6. Altere o thema html do arquivo

```python
# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
```

7. Adicione logo, favicon e estilos css à sua página. Para isso, adicione todos os arquivos dentro de `docs/source/_static`. Dentro do arquivo `docs/source/conf.py`, adicione as seguintes linhas:

```python
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_logo = "_static/logo.png"

html_css_files = ["custom-theme.css"]

html_favicon = "_static/favicon.ico"

html_theme_options = {
    "logo_only": True,
    "display_version": False,
}

```

8. Dentro da pasta docs, rode:

```bash
make html
```

A documentação estará em `docs/build/html`
