# PDF Extract

## Install

```bash
git clone https://github.com/ulisses-cruz/pdf_extract.git
cd pdf_extract
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

```


## Configure environment variables

```bash
cp .env.example .env
```

You will need to setup your `GEMINI_API_KEY`

## Database

The data is stored in a sqlite database for simplicity.
To create the database file and the table where the data is stored run the
migration.

### Run migration

```bash
python ./src/infrastructure/sqlite/migrations.py

```

## Serve pdf file

You can run a server in the `assets` folder in order to have a public pdf url
for testing.

```bash 
cd assets
python3 -m http.server
```

After running the server you will be able to access the pdf in [this url](http://localhost:8000/0809090-86.2024.8.12.0021.pdf).

## Run the Service

```bash
python src/main.py
```
