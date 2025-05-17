# Windows 11 Deployment Guide

## Requirements
- Python 3.8+
- Nginx for Windows
- Cloudflare Account

## Setup Steps
1. Install Chocolatey
```ps1
Set-ExecutionPolicy Bypass -Scope Process -Force
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```

2. Run Deployment Scripts
```ps1
cd deployment
.\django_windows_service.ps1
```

3. Configure Cloudflare
- Import `cloudflare_rules.json`
- Update DNS records

## Verification
```ps1
Get-Process nginx
Get-Service DjangoProduction
curl http://localhost/api/health
```
