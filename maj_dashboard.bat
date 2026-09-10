@echo off

cd /d C:\copper-dashboard

python export_json.py

git add .

git commit -m "Automatic update" || echo No change

git push