cy
##

Setup development environment
-----------------------------

We keep things simple.

1. create and activate virtualenv, upgrade pip:

    ```
    virtualenv -p `which python3` ~/.virtualenvs/cy
    ~/.virtualenvs/cy/bin/activate
    pip install -U pip
    ```

2. install dependencies:

    ```
    make install
    ```

3. verify everything's OK:

    ```
    make test
    ```

4. run!

    ```
    make run
    ```

Help yourself with `make` and `./manage.py --help`.