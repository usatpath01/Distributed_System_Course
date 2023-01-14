# Distributed_System_Course
Framework: FastAPI
1. Install virtualenv (Optional) - If you do not want to install dependencies globally on to the computer.
```
pip3 install virtualenv
```

2. To make a virtual env
```
python3 -m venv env
source env/bin/activate
```

3. Install other dependencies
FastAPI
UviCorn - to create fast asgi server which basically run the fastapi application
```
pip3 install fastapi
pip3 install uvicorn 
```

4. Write the main application (main.py)

5. Run the server
```
uvicorn main:app --reload
```

6. Browse
```
http://127.0.0.1:8000
```

7. To go to the FastAPI swagger API go to 
```
http://127.0.0.1:8000/docs
```

