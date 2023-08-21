# Saber Delivery Deployment repo
Make your artifacts part of a larger system.


## Ansible Installation
[Official Docs](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)

If you don't have the Ansible service in your infrastructure, you can install it locally on each server - proxy and cache. If Ansible is already available and in use, you can skip this step

```sh
apt update
apt install -y \
  python3-all \
  python3-pip

pip3 install --upgrade pip
# check
python3 -m pip -V

pip install --upgrade ansible
ansible --version
```


## Proxy deployment

We recommend set data_dir for directory mapped on the second drive.

You should get all tokens, urls before running these commands.

You should generate password for qBittorrent > 14 chars

```sh
SERVER=localhost
git clone <this repo>
cd ./ansible

# Installing Docker
ansible-playbook -i $SERVER, playbook/docker/install/docker_install.yml

# Installing torrust-tracker (retracker-local)
ansible-playbook -i $SERVER, playbook/torrust-tracker/install.yml
# After this step create A or CNAME record "retracker-local.saber3d.net" in your local DNS server pointing to the server running torrust-tracker service

# Installing Proxy with qBittorrent in docker-compose
ansible-playbook -i $SERVER, playbook/proxy/install.yml --extra-vars  '{"target":"$SERVER", "api_token":"<provided token>", "data_dir":"</you/data/dir>", "docker_proxy_repo":"", "api_url":"<provided api url>", "qbt_password":"<password generated by you>"}'
```
