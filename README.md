GIT REPO: https://github.com/elthran/software-architecture-patterns-for-big-data-week-1

NOTE: This was tested on Python 3.11 only

NEW MODELS: `Alphabetical` and ` Random Forest`

TEST OUTPUT:

```angular2html
==============================
 Barclays Premier League 2021 
==============================

 Predictor                      | Accuracy | Elapsed   
--------------------------------+----------+-----------
 Home                           | 0.428947 | 0.000132s
 Alphabetical                   | 0.400000 | 0.000112s
 Random Forest                  | 0.481579 | 1.566916s
 Points                         | 0.539474 | 0.000128s
 Offense simulator (fast)       | 0.510526 | 1.264674s
 Offense simulator              | 0.507895 | 12.515870s
 Full simulator (fast)          | 0.550000 | 1.608165s
 Full simulator                 | 0.539474 | 15.879606s


==================================
 English League Championship 2021 
==================================

 Predictor                      | Accuracy | Elapsed   
--------------------------------+----------+-----------
 Home                           | 0.443447 | 0.000188s
 Alphabetical                   | 0.378815 | 0.000159s
 Random Forest                  | 0.396768 | 2.173275s
 Points                         | 0.368043 | 0.000169s
 Offense simulator (fast)       | 0.402154 | 1.818487s
 Offense simulator              | 0.402154 | 18.226634s
 Full simulator (fast)          | 0.412926 | 2.327827s
 Full simulator                 | 0.414722 | 23.791529s


====================
 Italy Serie A 2021 
====================

 Predictor                      | Accuracy | Elapsed   
--------------------------------+----------+-----------
 Home                           | 0.389474 | 0.000129s
 Alphabetical                   | 0.400000 | 0.000107s
 Random Forest                  | 0.492105 | 1.403932s
 Points                         | 0.507895 | 0.000118s
 Offense simulator (fast)       | 0.489474 | 1.245366s
 Offense simulator              | 0.497368 | 12.421952s
 Full simulator (fast)          | 0.518421 | 1.573830s
 Full simulator                 | 0.518421 | 15.926504s

```

# Match predictor

The Match Predictor codebase contains an app with several predictors for football results.

## Local development

Follow the instructions below to get the app up and running on your machine.

1.  Install Python 3.10 and a recent version of NPM.
1.  Install dependencies and run tests.
    ```shell
    make install test
    ```
1.  View the list of available tasks
    ```shell
    make
    ```

## Backend

Here are a few tasks that are useful when running the backend app.
Make sure they all run on your machine.

1.  Run tests
    ```shell
    make backend/test

1.  Run model measurement tests
    ```shell
    make backend/measure
    ```

1.  Run server
    ```shell
    make backend/run
    ```

1.  Run an accuracy report
    ```shell
    make backend/report
    ```

## Frontend

Here are a few tasks that are useful when running the frontend app.
Make sure they all run on your machine.

1.  Run tests
    ```shell
    make frontend/test
    ```

1.  Run server
    ```shell
    make frontend/run
    ```

## Integration tests

If it's helpful, you may want to run integration tests during development.
Do so with the tasks below.

1.  Run tests
    ```shell
    make integration/test
    ```

1.  Interactive mode
    ```shell
    make integration/run
    ```
