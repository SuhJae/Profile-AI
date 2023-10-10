### 📜 Archived Repository
This repository has been archived, due to recent change in Twitter API policy.

![](https://img.shields.io/pypi/pyversions/tweepy?style=flat-square)
![](https://img.shields.io/pypi/pyversions/redis?style=flat-square)
![](https://img.shields.io/pypi/pyversions/openai?style=flat-square)
![](https://img.shields.io/github/release-date-pre/SuhJae/Profile_AI?style=flat-square)
![](https://img.shields.io/github/license/SuhJae/Profile_AI?style=flat-square)

# Profile_AI
An AI bot that utilizes GPT-3.5 to analyze user's Twitter profile.

## File Structure

### main.py
The `main.py` file contains the main code for the AI bot. It processes tweets, gets responses from GPT-3.5, and tweets the responses back to the users. The code also sets up authentication and streaming rules for the Twitter API.

### app.py
The `app.py` file contains the code for the Flask web app. It connects to Redis to store and retrieve AI-generated responses for each user.

## How to Run

### Prerequisites
Ensure you have the following installed on your system:

1. Python 3.6 or later
2. Redis

### Setup

1. Install redis on your system (For more information, see [Redis Installation](https://redis.io/topics/quickstart)).

2. Clone the repository:
    ```
    git clone https://github.com/SuhJae/Profile_AI.git
    cd Profile_AI
    ```

3. Create a virtual environment and activate it:
   ```
    python3 -m venv venv
    source venv/bin/activate
   ```
 
4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Configure your `config.ini` and `webapp/config.ini` file with your API keys and redis database:
   - Obtain the necessary API keys for OpenAI and Twitter.
   - Update the `config.ini` file with your keys, redis database and any additional settings.
   - For `webapp/config.ini`, just provide the redis database and certainly not needed if you don't want to run the web app.

### Running the Project

1. Start the Redis server on your system.

2. Run `run.sh` to start the AI bot and `webapp/run.sh` web app.

3. If you are going to use web app, make sure you install production server like `gunicorn` and run it with `gunicorn -w 4 app:app`


