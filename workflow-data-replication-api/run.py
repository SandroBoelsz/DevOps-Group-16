from app import init_app

app = init_app()

if app is None:
    print("Failed to initialize the app. Exiting.")
else:
    if __name__ == "__main__":
        app.run(host='0.0.0.0', port=5000, debug=True)  # Only run if executed directly
