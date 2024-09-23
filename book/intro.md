# Python

Python es un lenguaje de programación de propósito general que a menudo se aplica en *scripting*, secuencia de comandos. Comúnmente se define como un lenguaje de *scripting* orientado a objetos.

## Características de Python

- Multipropósito
- Interpretado
- Interactivo
- De alto nivel
- Orientado a objetos

## ¿Por qué Python?

- Es un lenguaje multiplataforma
- Es un lenguaje open-source
- Tiene una comunidad muy grande
- Tiene capacidades de desarrollo back-end y front-end
- Posee infinidad de paquetes (pip y conda)
- Pocas y simples líneas de código

## ¿Cómo conseguir Python?

- Instalador oficial de la [Python Software Foundation](https://www.python.org/) (Windows, Linux y macOS)
- Mediante gestor de paquetes en distribuciones Linux: `apt`, `rpm`, `dnf`, `pacman`, and `zypper`.
- Gestor de paquetes Homebrew (MacOS)
- Utilizando Anaconda/Miniconda (Windows, Linux y macOS)

## ¿Cómo utilizar Python?

- A través del intérprete
  - Sesión REPL (*Read–eval–print loop*) interactiva de python también llamada *python shell* (`>>>`)
  - Utilizando el intérprete en terminal (*scripting mode*): `python hello.py`
- Utilizando "Interactive Python"
  - Una sesión interactiva `IPython` en terminal (`In[1]:`)
  - Un IPython notebook, Jupyter Lab, Jupyter Notebook
- A través de una editor/IDE
  - [VS Code](https://code.visualstudio.com)
  - [Pycharm](https://www.jetbrains.com/pycharm/)
  - [Spyder](https://www.spyder-ide.org)
  - [Rstudio](https://www.rstudio.com) 😂
  - Editores de texto: Vim, Emacs

```{admonition} ATG Workshop
Para este curso vamos a utilizar tres elementos del ecosistema de Python:

- `pyenv`
- `jupyter lab`
- `pip`
```

## Instalación de micromamba

```bash
"${SHELL}" <(curl -L micro.mamba.pm/install.sh)
micromamba shell completion
```

```{admonition} ¡Recuerda!
:class: tip
Una instalación personalizada con la opción `-p` no permite utilizar `conda activate`, en su lugar habrá que utilizar `source activate`.
```

**Agregar Miniconda al $PATH**
```bash
cat <<"EOF" >> $HOME/.bash_profile
export PATH=$HOME/bin/miniconda3/bin:$PATH
EOF
```

**Recargar y revisar el $PATH**
```bash
source $HOME/.bash_profile

echo $PATH
```

```{admonition} ¡Recuerda!
:class: tip
El archivo de PATH por default para GNU/Linux es `~/.bashrc`.
```

**Agregar canales de Conda**
```bash
cat <<EOF >> $HOME/.condarc
channels:
  - conda-forge
  - bioconda
  - defaults
EOF
```

## Un minitutorial de micromamba

Verificar versión de conda**

```bash
conda info
```

Actualizar conda**

```bash
conda update conda
```

Listar todos los entornos de conda**

```bash
conda env list
```

Actualizar todos los paquetes de conda (base)**

```bash
conda update conda --all
```

Agregar canales**

```bash
conda config --add channels r
conda config --add channels conda-forge
conda config --add channels bioconda
```

Buscar un paquete**

```bash
conda search PACKAGE
```

Instalar un paquete en el entorno base**

```bash
conda install PACKAGE
```

Eliminar temporales y actualizar todo**

```bash
conda clean --all
conda update --all
```

Eliminar entorno**

```bash
conda remove -n qiime2 --all
```

Crear un entorno en un canal específico con una versión particular de python y con una versión específica de un paquete**

```bash
conda create -y -n test3.6 python=3.6 pandas=1.0
```
