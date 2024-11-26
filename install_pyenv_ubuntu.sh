sudo apt update
sudo apt upgrade

# Dependencies from https://github.com/pyenv/pyenv/wiki#suggested-build-environment
sudo apt install build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev curl git libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

# Installation
curl https://pyenv.run | bash
git clone https://github.com/pyenv/pyenv.git $HOME/.pyenv
cd $HOME/.pyenv && src/configure && make -C src

# Add environment variables to PATH
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> $HOME/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> $HOME/.bashrc
echo 'eval "$(pyenv init -)"' >> $HOME/.bashrc

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> $HOME/.profile
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> $HOME/.profile
echo 'eval "$(pyenv init -)"' >> $HOME/.profile

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> $HOME/.bash_profile
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> $HOME/.bash_profile
echo 'eval "$(pyenv init -)"' >> $HOME/.bash_profile

# Restart shell
exec "$SHELL"
