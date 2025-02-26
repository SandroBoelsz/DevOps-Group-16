from app import init_app

app = init_app()
if app is None:
    print("Failed to initialize the app. Exiting.")
else:
    app.run(host='0.0.0.0', port=5000, debug=True)