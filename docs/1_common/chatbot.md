
# Make Environment

  conda create --name words_nlp python=3.12
  conda activate words_nlp
  conda install conda-forge::nltk
  conda install conda-forge::spacy
  conda install pip
  pip install -U pip setuptools wheel
  pip install benepar

  #conda deactivate;
  #conda remove --name words_nlp --all

# Install Python Natural Language Tool Kit (nltk) 

https://www.nltk.org/install.html
https://www.nltk.org/data.html
https://spacy.io/

  Pip Installations
    ```
    pip install nltk
    pip install -U pip setuptools wheel
    pip install spacy
    pip install benepar
    ```
  Downloads
    ```
    python
    import nltk
    nltk.download() # In the location put "/usr/share/nltk_data"
    import benepar, spacy
    benepar.download('benepar_en3')
    ```

# Hugging Face Models
  
  `pip install -q transformers`
  
  First Time Using Model
    
    ```
    from transformers import AutoModelForCausalLM, AutoTokenizer,AutoModel
    # Define Variables
    path = "~/downloads/large_language_models/model"
    model_path = "user/model"
    device = "cuda" # for GPU usage or "cpu" for CPU usage
    # Fetch
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path).to(device)
    # Save 
    tokenizer.save_pretrained(path)
    model.save_pretrained(path)
    ```
  Future Use of Model
    ```
    from transformers import AutoModelForCausalLM, AutoTokenizer,AutoModel
    # Define Variables
    path = "/home/tristin/downloads/large_language_models/DeciCoder-1b"
    device = "cuda" # for GPU usage or "cpu" for CPU usage
    # Fetch Local 
    tokenizer = AutoTokenizer.from_pretrained(path)
    model = AutoModelForCausalLM.from_pretrained(path).to(device)
    ```
    


# Private GPT
  Don't use this.
  ## Install Private GPT

      # Download
      cd ~/downloads/
      git clone https://github.com/imartinez/privateGPT.git
      
      # Set up PyEnv Environment: Check python version hasn't changed. 
      cd /opt/.pyenv_root/plugins/python-build/../.. && git pull && cd -
      pyenv install -v 3.10.10
      pyenv virtualenv 3.10.10 chat
      cd ~/downloads/privateGPT/
      pyenv activate chat
      pip3 install -r requirements.txt
      
      pip install sentence_transformers
      
  ## Download Language Model and Set-Up Env File

    I store language modes in: ~/downloads/large_language_models/
    So, I have to change the MODEL_PATH location in the .env file
    
  ## Place Link files into source directory

      ### Link files
      
      ### Ingest files 
      python ingest.py

  ## Ask Questions:
    cd ~/downloads/privateGPT/
    python privateGPT.py
    Enter a query: ...
    Enter a query: exit
