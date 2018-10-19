# Config:

## SSH-KEY
 * Create SSH-Key
```
ssh-keygen -t rsa -b 4096 
```
 
 * Print Public-Key
```
cat /home/pi/.ssh/id_rsa.pub
```

## VI
 * Edit file .vimrc
```
set nocp
set backspace=indent,eol,start
```

## GIT
 * Edit file .gitconfig
```
[alias]
co = checkout
cp = cherry-pick
st = status -sb
cl = clone
ci = commit
co = checkout
br = branch
dc = diff --cached
lg = "log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %Cblue<%an>%Creset' --abbrev-commit --date=relative --all"
last = log -1 --stat
unstage = reset HEAD --
df = "difftool --tool=vimdiff"
dfy = "difftool --tool=vimdiff -y"
diffw = "diff --word-diff"
diffs = "diff --staged"
```
 
 * Add Git User
```
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```

## SAMBA
 * Install Samba
```
sudo apt-get update
sudo apt-get install samba
```

 * Create folder to share
```
cd /home/pi
mkdir pi-projects
``` 

 * Edit Samba Config /etc/samba/smb.conf
```
[global]
security = user

[Projects]
path = /home/pi/pi-projects
writeable = yes
public = yes
browsable = yes
available = yes
guest ok = no
valid users = pi
```

 * Set Password
```
sudo smbpasswd -a pi
```

 * Restart Samba Server
```
sudo /etc/init.d/samba restart
```

* Connect to Net Drive
```
smb://192.X.X.X
User: pi
PW: as defined
```


#### Check installation:  
  * $ docker --version  
  * $ docker-compose --version  
  * $ docker-machine --version  

 
# Run the application:
## Development
1. Clone / Pull the latest code from github 
  
2. Create docker container  
  * $ cd PATH-TO-APP  
  * $ docker-compose build
  
3. Start server  
  * $ cd PATH-TO-APP  
  * $ docker-compose up

4. Go to 
  * localhost:3000

## Ports
  * 3000 React

## Paths
  * :3000/xyz React


# Docker:
## Management
1. List all running docker container:  
  * $ docker ps 

2. Connect to a docker container bash:  
  * $ docker exec -it <CONTAINER-ID> bash
  * $ docker exec -it 142017e1571b bash

3. Stop all running docker containers:  
  * $ docker stop $(docker ps -a -q) 
  * $ docker rm $(docker ps -a -q) 

4. Remove all docker images:
  * $ docker rmi $(docker images -q)


# Tooling & Logging
## Connect to AWS Instance
  * ssh -i /path/file.pem ec2-user@ec2-00-00-000-00.eu-central-1.compute.amazonaws.com
  

# Tutorials:
  * NodeJS & Express: https://www.youtube.com/watch?v=4rF0tRxZ7Aw
  * React: https://www.youtube.com/watch?v=-AbaV3nrw6E&t=12s
  * Redux: https://www.youtube.com/watch?v=DiLVAXlVYR0
  * Observable: https://www.youtube.com/watch?v=AslncyG8whg&t=930s

