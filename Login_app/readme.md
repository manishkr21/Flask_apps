### to create this do below steps
1. python3 -m venv venv
2. source venv/bin/activate
3. pip3 install Flask Flask-Login Flask-SQLAlchemy
4. create a structure like
 
 ```diff
   app-
      - instance
          - users.db
      - templates
          - css
              - style.css
          - index.html
          - login.html
          - signup.html
      - app.py
   venv - virtual environment
 ```
 
### to start the app
1. python3 -m venv venv
2. source venv/bin/activate
3. navigate to app_db.py
4. python3 app_db.py

### via flask run {to run the app}
1. python3 -m venv venv
2. source venv/bin/activate
3. export FLASK_APP=app_db.py {whatever your starting point is}
4. flask run

