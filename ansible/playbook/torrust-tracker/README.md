# Torrust Tracker

Torrust Tracker is a lightweight but incredibly high-performance and feature-rich BitTorrent tracker written in [Rust](https://www.rust-lang.org/).

It aims to provide a reliable and efficient solution for serving torrents to a vast number of peers while maintaining a high level of performance, robustness, extensibility, security, usability and with community-driven development.

[Github Repo](https://raw.githubusercontent.com/torrust/torrust-tracker) | [Official Page](https://torrust.com/)

## Installation
### Deploy service using Ansible

This application is heavily networked, so it is not deployed in the docker, but runs as a systemd-service on the host.

Check if ports 6971/tcp, 6971/udp are open in OS firewall

After installation create A or CNAME record "retracker-local.saber3d.net" in your local DNS server pointing to the server running torrust-tracker service

qBittorrent will be restarted after installation if found in running state

Check new retracker work in the qBittorrent WebUI

Enjoy!