from flask import Flask, jsonify, request
import requests
import dotenv
import os

dotenv.load.dotenv()

app = Flask(__name__)
OMDB_API_KEY = os.getenv("OMDB_API_KEY")

@app.route("/")
def index():
    return "fuck you"

@app.route("/search")
def search():
    movie = request.args.get("movie")

    if not movie:
        return jsonify({"error" : "movie query is required"}), 400

    response = requests.get(f"`http://www.omdbapi.com/?s=${movie}&apikey=${OMDB_API_KEY}")
    return jsonify(response.json()), 200

if __name__ == "__main__":
    app.run(
        debug=True, 
        port=1000
    )