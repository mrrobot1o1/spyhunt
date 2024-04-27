from shutil import which
from colorama import Fore
import os
import subprocess

def commands(cmd):
    try:
        subprocess.check_call(cmd, shell=True)
    except Exception as e:
        print(Fore.RED + str(e))

def install_tool(command, tool_name):
    if which(tool_name):
        print(Fore.GREEN + f"{tool_name} already installed.")
    else:
        commands(command)
        if which(tool_name):
            print(Fore.GREEN + f"{tool_name} installed successfully.")

home = os.environ['HOME']
filepath = os.path.abspath(os.getcwd())

# Install required tools
install_tool("pip install colorama", "colorama")
install_tool("apt install golang -y", "go")
install_tool("apt install nodejs -y", "node")
install_tool("apt install npm -y", "npm")
install_tool("npm install broken-link-checker -g", "blc")
install_tool(f"wget -O aquatone.zip https://github.com/michenriksen/aquatone/releases/download/v1.7.0/aquatone_linux_amd64_1.7.0.zip && unzip aquatone.zip && rm aquatone.zip && mv aquatone {home}/go/bin && chmod +x {home}/go/bin/aquatone", "aquatone")
install_tool("apt install jq -y", "jq")

# Go-based tools installation
go_tools = {
    "dnsx": "github.com/projectdiscovery/dnsx/cmd/dnsx@latest",
    "subfinder": "github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest",
    "httprobe": "github.com/tomnomnom/httprobe@latest",
    "httpx": "github.com/projectdiscovery/httpx/cmd/httpx@latest",
    "anew": "github.com/tomnomnom/anew@latest",
    "gau": "github.com/lc/gau@latest",
    "gauplus": "github.com/bp0lr/gauplus@latest",
    "hakrawler": "github.com/hakluke/hakrawler@latest",
    "waybackurls": "github.com/tomnomnom/waybackurls@latest",
    "assetfinder": "github.com/tomnomnom/assetfinder@latest"
}

for tool, repo in go_tools.items():
    command = f"go install {repo} && mv {home}/go/bin/{tool} /usr/local/bin"
    install_tool(command, tool)

# Python-based tool installation
install_tool("easy_install shodan", "shodan")
install_tool("git clone https://github.com/devanshbatham/paramspider && cd paramspider && pip install . && cd ..", "paramspider")
