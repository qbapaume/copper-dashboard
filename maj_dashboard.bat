@echo off

cd /d C:\copper-dashboard

python export_json.py

git add .

git commit -m "Daily update"

git push