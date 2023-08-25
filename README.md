# Saber Delivery Deployment repo
Make your artifacts part of a larger system.


## Ansible deployment
[Official Docs](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)

If you don't have the Ansible service in your infrastructure, you can install it locally. If Ansible is already available and in use, you can skip this step.

```sh
# for debian <12
apt update
apt install -y \
  python3-all \
  python3-pip
pip install --upgrade pip
pip install --upgrade ansible 
# for debian >=12
pipx install --include-deps ansible

ansible --version
```


## Server 1. SD-Proxy

- Prepare new server

- Install Ansible as described above

### SD-Proxy deployment

We recommend set data_dir for directory mapped on the second data disk.

You need to get all tokens, urls, etc. before running these commands.

You need to generate password for qBittorrent > 14 chars or use your own.

In our example, Ansible is installed and run locally.

```sh
git clone https://github.com/saber-games/saber-delivery-deploy
cd ./saber-delivery-deploy/ansible
# Password generation example 
PASS=$(< /dev/urandom LANG= tr -dc a-zA-Z0-9 | head -c 16 && echo)
SERVER=127.0.0.1

# Install Docker Engine
ansible-playbook -i $SERVER, --connection=local playbook/docker/install/docker_install.yml

# Install SD-Proxy app and qBittorrent in docker-compose
ansible-playbook -i $SERVER, --connection=local playbook/proxy/install.yml --extra-vars  '{"api_token":"<provided token>", "api_url":"<provided api url>","data_dir":"/raid/proxy", "docker_proxy_repo":"", "qbt_password":'${PASS}'}'

# Optional: you can enable containers autoupdate on daily basis
ansible-playbook -i $SERVER, --connection=local playbook/docker/containers/dc_autoupdate_containers.yml

```


### Retracker-local based on torrust-tracker deployment

- Create DNS record as instructed

- Install torrust-tracker (it is assumed that you continue with the commands on the same server from the step above)

```sh
ansible-playbook -i $SERVER, --connection=local playbook/torrust-tracker/install.yml

# Check service
systemctl status torrust-tracker
```


## Server 2. SD-Cache

- Prepare new server

- Install Ansible as described above

### SD-Cache deployment

We recommend set data_dir_root for directory mapped on the second data disk.

You need to get all tokens, urls, etc. before running these commands.

You need to generate password for qBittorrent > 14 chars or use your own.

In our example, Ansible is installed and run locally.

```sh
git clone https://github.com/saber-games/saber-delivery-deploy
cd ./saber-delivery-deploy/ansible
# Password generation example 
PASS=$(< /dev/urandom LANG= tr -dc a-zA-Z0-9 | head -c 16 && echo)
SERVER=127.0.0.1

# Install Docker Engine
ansible-playbook -i $SERVER, --connection=local playbook/docker/install/docker_install.yml

# Install SD-Cache app and qBittorrent in docker-compose
ansible-playbook -i $SERVER, --connection=local playbook/cache/install.yml --extra-vars  '{"self_token":"<provided token>", "api_url":"<provided api url>", "data_dir_root":"/raid", "data_dir_name":"cache", "docker_proxy_repo":"", "qbt_password":'${PASS}'}'

# Optional: you can enable containers autoupdate on daily basis
ansible-playbook -i $SERVER, --connection=local playbook/docker/containers/dc_autoupdate_containers.yml
```