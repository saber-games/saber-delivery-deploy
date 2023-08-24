# Saber Delivery Deployment repo
Make your artifacts part of a larger system.


## Ansible deployment
[Official Docs](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)

If you don't have the Ansible service in your infrastructure, you can install it locally. If Ansible is already available and in use, you can skip this step

```sh
apt update
apt install -y \
  python3-all \
  python3-pip

pip install --upgrade pip
# check
pip -V

pip install --upgrade ansible
ansible --version
```


## Server 1. Proxy

### SD-Proxy deployment

We recommend set data_dir for directory mapped on the second disk.

You should get all tokens, urls before running these commands.

You should generate password for qBittorrent > 14 chars or use your own.

```sh
git clone https://github.com/saber-games/saber-delivery-deploy
cd ./saber-delivery-deploy/ansible
# password generation example 
PASS=$(< /dev/urandom LANG= tr -dc a-zA-Z0-9 | head -c 16 && echo)
SERVER=127.0.0.1

# Installing Docker
ansible-playbook -i $SERVER, --connection=local playbook/docker/install/docker_install.yml

# Installing Proxy with qBittorrent in docker-compose
ansible-playbook -i $SERVER, --connection=local playbook/proxy/install.yml --extra-vars  '{"target":"$SERVER", "api_token":"<provided token>", "api_url":"<provided api url>","data_dir":"</you/data/dir>", "docker_proxy_repo":"", "qbt_password":"$PASS"}'
```

### Retracker-local based on torrust-tracker deployment

- Create A or CNAME record "retracker-local.saber3d.net" in your local DNS server (domain based or caching) pointing to the server running torrust-tracker service. This is current proxy server in our case.

- Installing torrust-tracker (it is assumed that you continue with the commands from the step above)

```sh
ansible-playbook -i $SERVER, --connection=local playbook/torrust-tracker/install.yml
```


## Server 2. Cache

### SD-Cache deployment