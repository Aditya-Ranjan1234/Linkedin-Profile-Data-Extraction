from frontend import app

if __name__ == "__main__":
    app.secret_key = "your_secret_key_here"
    app.run(debug=True) 