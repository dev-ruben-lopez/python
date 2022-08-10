# Sum Of Squares in Python
### Solution by Ruben D. Lopez

## Run
This program is using venv (virtual environment) for python 3.8 and Flask as a local web server,  so please :

1- Go on terminal to this folder locationa and run: 

```python
>source .venv/bin/activate

>export FLASK_APP=webapp.py

>export FLASK_ENV=development

>flask run
```

Go to the address that is specified in:

In a second terminal window, execute the tester, or, if using POSTMAN go to the address:
http://127.0.0.1:5000/sumofsquares

Set Request Data to json, and enter in body:

```python
{"data": [5,4,6,1]}
```

Click GET or POST

Response should be

```python
{"output" : 8.77}
```

## Test

While running flask, run in another terminal window the file tester.py
You whould get the next results:

```python
(.venv)> SumSquares % python tester.py                                
{"output": 8.77}
{"output": 80.22}
"Error: List must contain at least 3 numbers."
"Error: List must contain only numbers."
```

