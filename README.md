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