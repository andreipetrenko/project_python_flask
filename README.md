# project_python_flask
# for flask start
set FLASK_APP=manage.py
python -m flask db init
python -m flask db migrate
python -m flask db upgrade
python -m flask run

# for docker start
docker-compose up -d
