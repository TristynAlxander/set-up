# Git

## Set-Up Git

    # Set-Up Git Directories
    if [ ! -d $STORE/repos ]; then mkdir $STORE/repos; fi
    ln -s $STORE/repos ~/repos
    
    # Set-Up Settings
    git config --global user.email "you@email.com"
    git config --global user.name "UserName"
    
## Downloading a Repository

  - Use in `$STORE/repos` use `git clone URL` with URL as:
    - `https://Username`:`Password`@`github.com/Username/myRepo.git`
    - `https://Username`:`Personal_Access_Token`@`github.com/Username/myRepo.git`
    - Note: Personal_Access_Token can be found in configs
    - `git config --global --add safe.directory $STORE/repos/myRepo`
      - This is very picky about exactly how this is written, and I can't figure out what's wrong.
      - Seems like it only works if I copy/paste 
      git config --global --add safe.directory $STORE/repos/1_uploads/junkyard

## Create Respository

**Caution:** You probably want to create a Github Repo then download that. [link](https://docs.github.com/en/get-started/quickstart/create-a-repo)

For-Non-Github Repositories:
  - Create and Empty Repository `git init` make bare `git config --bool core.bare true`
  - https://packaging.python.org/en/latest/tutorials/packaging-projects/

