until python3 app.py
until gunicorn3 --workers=3 app:app


do
    echo "It seems like there was a crash. Restarting in 3 seconds..."
    sleep 3
done
