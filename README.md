# Spanner Utils

Command-line interface to perform basic spanner operations. 

**Requirements**
- Python 3.x
- gcloud


## Setup and install

Setup your gcloud stuff:
* Install the [google cloud sdk](https://cloud.google.com/sdk/downloads#apt-get).
* Authenticate: `gcloud auth login`
* Set the project: `gcloud config set project [PROJECT_ID]`

Now install the repo: 
1. Clone this repo. 
1. Install the requirements: `pip install -r requirements`
1. [Optional] Add to your profile (.rc) file with an alias: `alias spanner=python path/to/this/repo/main.py`

## Usage

### Import csv-files to spanner

To import a csv-file run the following:
```
spanner --instance_id [INSTANCE_ID] --database_id [DATABASE_ID] --table_id [TABLE_ID] --file_path [FILE_PATH] --format_path [FORMAT_PATH] --chunksize [CHUNKSIZE]
```

Where:

```
    INSTANCE_ID : Cloud Spanner instance id.
    DATABASE_ID : Cloud Spanner database id.
    TABLE_ID    : Cloud Spanner table id.
    FILE_PATH   : Cloud Spanner path to csv file (note that headers are required).
    FORMAT_PATH : JSON file that contains the dtype info e.g. {"STRING_COL": "object", "INT64_COL": "int64"}.
    CHUNKSIZE   : Number of lines to read per upload (use -1 to read the file in one iteration). 
```

### Download csv-files from spanner

Not available.

### Create/Delete spanner elements

Not available.

## Authors

* [Rodrigo Hernández Mota](https://www.linkedin.com/in/rhdzmota/)

## LICENSE


<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">
  <img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" />
</a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">spanner-utils
</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://github.com/rhdzmota/whatsapp-webdriving" property="cc:attributionName" rel="cc:attributionURL">Rodrigo Hernández Mota</a> 
is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">
Creative Commons Attribution-ShareAlike 4.0 International License</a>.

## Acknowledgements

Not so far.