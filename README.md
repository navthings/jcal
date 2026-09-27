# jcal

a simple, fast inline calculator for the terminal.


https://github.com/user-attachments/assets/87c9eae5-1300-4b94-875b-20eb5a534e7d


built it to play with jax numpy (`jnp`) arrays, so every number you type becomes a `jnp.array` before calculating

## requirements

- python 3.11+
- git

## install

each option clones jcal into `~/.jcal`, sets up its own venv, and adds a `jcal` command to your shell.

### zsh

```zsh
git clone https://github.com/navthings/jcal.git ~/.jcal
python3 -m venv ~/.jcal/.venv
~/.jcal/.venv/bin/pip install -r ~/.jcal/requirements.txt
echo "alias jcal='$HOME/.jcal/.venv/bin/python $HOME/.jcal/main.py'" >> ~/.zshrc
source ~/.zshrc
```

### bash

```bash
git clone https://github.com/navthings/jcal.git ~/.jcal
python3 -m venv ~/.jcal/.venv
~/.jcal/.venv/bin/pip install -r ~/.jcal/requirements.txt
echo "alias jcal='$HOME/.jcal/.venv/bin/python $HOME/.jcal/main.py'" >> ~/.bashrc
source ~/.bashrc
```

on macOS bash reads `~/.bash_profile` instead, so swap that in for `~/.bashrc`.

### powershell

```powershell
git clone https://github.com/navthings/jcal.git $HOME\.jcal
python -m venv $HOME\.jcal\.venv
& $HOME\.jcal\.venv\Scripts\pip.exe install -r $HOME\.jcal\requirements.txt
if (!(Test-Path $PROFILE)) { New-Item -ItemType File -Force $PROFILE }
Add-Content $PROFILE "function jcal { & `"$HOME\.jcal\.venv\Scripts\python.exe`" `"$HOME\.jcal\main.py`" }"
. $PROFILE
```

## usage

```
$ jcal
simple calculator using jnp arrays. Type 'q' to quit.
type 'clear' to clear the screen.
enter expressions in the format: a op b (e.g., 2 + 3)
> 2 + 3
5.0
> 10 / 4
2.5
> q
```

supports `+`, `-`, `*` and `/`. put spaces around the operator.

clear clears the screen, q quits the program


## uninstall

delete `~/.jcal` and remove the `jcal` line from your shell config (`~/.zshrc`, `~/.bashrc` or `$PROFILE`).
