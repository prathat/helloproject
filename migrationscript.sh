#!/bin/sh
echo "Starting ..."

echo ">> Deleting old migrations"
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete


# Optional
echo ">> Deleting sqlite  (if exists) database"
find . -name "db.sqlite3" -delete

echo ">> Running manage.py makemigrations"
python manage.py makemigrations

echo ">> Running manage.py migrate"
python manage.py migrate

echo ">> Done"
read -p "If any error persists, Proceed to reinstall django? y/n :" status
if [ $status=='y' ]
then
echo status
echo ">> Deleting Django"
pip uninstall django
echo ">> Reinsralling Django"
pip install django
echo "Done"
else 
echo "-----Not reinstalling django------"
fi
