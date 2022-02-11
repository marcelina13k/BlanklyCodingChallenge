# BigBoiDatabase API Documentation

To begin, clone this repo. Initialize a new python configuration (i.e. anaconda, venv, etc.) and install the proper dependencies with `pip install -r requirements.txt`.

Then, run ```flask run``` to begin the API.

## Routes

---

```GET /get_one``` 

Returns the first message in the database

---

```POST /get_x```

| Arguments | type |
| --------- | ---- |
| num       | int  |

Return the first "num" messages of the database.

---

```GET /get```

Returns all the messages currently in the database

---

```POST /add```

| Arguments | type   |
| --------- | ------ |
| message   | string |
| timestamp | int    |

Adds the current message and timstamp to the database and encrypts the message
