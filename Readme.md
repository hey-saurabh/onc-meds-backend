#Create Python Environment Using following commands and activate it:

  ```
  python3 -m venv <env_name>
  ```
  ```
  source <env_name>/bin/activate
  ```

#Now Install requirements file using following commands:

  ```
  pip install -r requirements.txt
  ```

#Now create a settings.py file in config folder and have these variables:
  ```
  MONGO_URL: <YOUR MONGO URL HERE>
  PORT = 8000 default
  ```


#Now to run project -> Use following commands:

  ```
  uvicorn main:app --reload
  ```
