![POLITICO](https://rawgithub.com/The-Politico/src/master/images/logo/badge.png)

# django-politico-civic-demography

Gather U.S. Census data for elections, the POLITICO way.

### Quickstart

1. Install the app.

  ```
  $ pip install django-politico-civic-demography
  ```

2. Add the app to your Django project and configure settings.

  ```python
  INSTALLED_APPS = [
      # ...
      'rest_framework',
      'geography',
      'demography',
  ]

  #########################
  # demography settings

  CENSUS_API_KEY = ''
  DEMOGRAPHY_AWS_ACCESS_KEY_ID = ''
  DEMOGRAPHY_AWS_SECRET_ACCESS_KEY = ''
  DEMOGRAPHY_AWS_S3_BUCKET = ''
  DEMOGRAPHY_AWS_REGION = 'us-east-1' # default
  DEMOGRAPHY_AWS_S3_UPLOAD_ROOT = 'elections' # default
  DEMOGRAPHY_AWS_ACL = 'public-read' # default
  DEMOGRAPHY_AWS_CACHE_HEADER = 'max-age=31536000' # default
  DEMOGRAPHY_API_AUTHENTICATION_CLASS = 'rest_framework.authentication.BasicAuthentication' # default
  DEMOGRAPHY_API_PERMISSION_CLASS = 'rest_framework.permissions.IsAdminUser' # default
  DEMOGRAPHY_API_PAGINATION_CLASS = 'demography.pagination.ResultsPagination' # default
  ```

### Developing

##### Running a development server

Move into the example directory, install dependencies and run the development server with pipenv.

  ```
  $ cd example
  $ pipenv install
  $ pipenv run python manage.py runserver
  ```

##### Setting up a PostgreSQL database

1. Run the make command to setup a fresh database.

  ```
  $ make database
  ```

2. Add a connection URL to `example/.env`.

  ```
  DATABASE_URL="postgres://localhost:5432/geography"
  ```

3. Run migrations from the example app.

  ```
  $ cd example
  $ pipenv run python manage.py migrate
  ```

### Baking Data

This app will bake multi-level census data files to the s3 bucket configured in your settings. The files will bake in the following structure:

```javascript
{ DEMOGRAPHY_AWS_S3_UPLOAD_ROOT }
  ├── { series } // each census series (e.g. acs5) has its own directory
  │ ├── { year } // each series has a directory for each year
  │ │ ├── { table } // each year has a directory for each table by table code
  │ │ │ ├── districts.json  // national-level data broken up by districts
  │ │ │ ├── states.json  // national-level data broken up by states by district
  │ │ │ ├── { state_fips } // each table has a directory for each state by FIPS code
  │ │ │ │   ├── districts.json // state-level data broken up district
  │ │ │ │   └── counties.json  // state-level data broken up county
  │ │ │ └── ...
  │ │ └── ...
  │ └── ...
  └── ...
```

The data structure will differ depending on the type of file and the setup of your census tables in the admin. Here are four samples for a data table of "median age" with a "total" code of `001E`. In our sample admin we have the code inputted twice: once with a label of `total` and once with no label.

##### National Districts File
```python
# upload_root/series/year/table/districts.json
{
  "10": { # state FIPS code
    "00": { # district number
      "001E": 39.6, # census variable without a label
      "total": 39.6, # census variable with an aggregate variable
    }
  },
  "11": {
    "98": {
      "001E": 33.8,
      "total": 33.8,
    }
  },
  "12": {
    "10": {
      "001E": 35,
      "total": 35,
    },
    "11": {
      "001E": 55,
      "total": 55,
    },
    "12": {
      "001E": 46.3,
      "total": 46.3,
    },
    ... # more districts here
  },
  ... # more states here
}
```

##### National States File
```python
# upload_root/series/year/table/states.json
{
  "10": {
    "001E": 39.6,
    "total": 39.6,
  },
  "11": {
    "001E": 33.8,
    "total": 33.8,
  },
  "12": {
    "001E": 41.6,
    "total": 41.6,
  },
  ... # more states here
}
```

##### State Districts File
```python
# upload_root/series/year/table/state/districts.json
{
  "10": {
    "001E": 35,
    "total": 35,
  },
  "11": {
    "001E": 55,
    "total": 55,
  },
  "12": {
    "001E": 46.3,
    "total": 46.3,
  },
  ... # more districts here
}
```

##### State County File
```python
# upload_root/series/year/table/state/counties.json
{
  "12001": { # county FIPS code
    "001E": 31,
    "total": 31,
  },
  "12003": {
    "001E": 36.5,
    "total": 36.5,
  },
  "12005": {
    "001E": 39.7,
    "total": 39.7,
  },
  "12007": {
    "001E": 41,
    "total": 41,
  },
  ... # more counties here
}
```
