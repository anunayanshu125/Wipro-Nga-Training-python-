from flask import Flask
app=Flask(__name__)
@app.route('/')
def home():
    return "Welcome to Anunay's Flask API"
if __name__ == '__main__':
    app.run(debug=True)