# my-first-repo

## Setup

Create and activiate a virtual environment: 

```sh
conda create -n my-first-env-2025 python=3.11

conda activate my-first-env-2025
```

Install packages: 
```sh
#pip install pytest 

pip install -r requirements.txt
```


## Usage 

Play a game of rock, paper, scissors: 

``` sh 
#only works if this file does not import from other local py files 
python app/rps.py

#if this file imports from other local py files: 
python -m app.rps 
```

## Tests 

Run the tests: 

```sh
#find all the tests and run them: 
pytest
```

### Web App
Run the web app

```sh
FLASK_APP=web_app flask run
```

Visit in the browser, either:
+ http://127.0.0.1:5000
  + http://localhost:5000/


