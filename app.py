import os
import json
from datetime import datetime
from flask import Flask, render_template, request, jsonify, send_from_directory
import openai
import tweepy
from PIL import Image, ImageDraw, ImageFont
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET_KEY = os.getenv("TWITTER_API_SECRET_KEY")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/test_twitter_credentials")
def test_twitter_credentials():
    try:
        user_profile = api.verify_credentials()
        return f"Authenticated user: {user_profile.screen_name}"
    except Exception as e:
        return f"Error: {e}"


@app.route("/generate_post", methods=["POST"])
def generate_post():
    post_subject = request.form.get("post_subject")

    # Call the OpenAI API to generate the post content based on the post_subject
    prompt = f"Create a viral Twitter post about {post_subject} with popular and relevant hashtags."
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.8,
    )

    generated_post = response.choices[0].text.strip()

    return jsonify({"generated_post": generated_post})

def post_to_twitter(text):
    try:
        print(f"Posting to Twitter: {text}")
        api.update_status(text)
        print(f"Successfully posted to Twitter: {text}")
        return "success"
    except Exception as e:
        print(f"Error posting to Twitter: {e}")
        return str(e)


@app.route("/publish_post", methods=["POST"])
def publish_post():
    content = request.form.get("content", "")
    print(f"Content before posting to Twitter: {content}")  # Add this print statement
    result = post_to_twitter(content)
    if result == "success":
        return "success"
    else:
        return result


if __name__ == "__main__":
    app.run(debug=True)

