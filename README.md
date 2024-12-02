# quality-control-exercise

## Setup

Todo: create and activate a virtual environment

Todo: install packages


## Usage

Run the unemployment report:

```sh
#ALPHAVANTAGE_API_KEY="..." python app/unemployment.py

python app/unemployment.py

```
### Web App
Run the web app (then view in the browser at http://localhost:5000/):

```sh
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
```


## Setup

Create a virtual environment (first time only):

```sh
conda create -n reports-env-2024 python=3.10
```

Activate the environment (whenever you come back to this project):

```sh
conda activate reports-env-2024
```

Install packages:

```sh
pip install -r requirements.txt
```

[Obtain an API Key](https://www.alphavantage.co/support/#api-key) from AlphaVantage.

Create a ".env" file and add contents like the following (using your own AlphaVantage API Key):

```sh
# this is the ".env" file:
ALPHAVANTAGE_API_KEY="..."
```

```sh
#ALPHAVANTAGE_API_KEY="..." python app/unemployment.py

# python app/unemployment.py

python -m app.unemployment
```


Run the stocks report:

```sh
#python app/stocks.py

python -m app.stocks
```

Run the email sender:

```sh
python app/email_service
```

Run the RPS game:

```sh
python app/rps
```

## Testing

Run tests: 

```sh
pytest
```