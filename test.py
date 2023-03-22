import redis
import configparser
import time

# Load config file
config = configparser.ConfigParser()
config.read('config.ini')

# Connect to Redis
r = redis.Redis(
    host=config['REDIS']['host'],
    port=int(config['REDIS']['port']),
    db=int(config['REDIS']['db'])
)

# Function to make all keys lowercase and preserve expiry
def make_keys_lowercase(r):
    # Get all keys
    keys = r.keys('*')

    for key in keys:
        lower_key = key.decode().lower()

        # Check if the key is already lowercase
        if key.decode() == lower_key:
            continue

        # Get the remaining time to live (TTL) for the key
        ttl = r.ttl(key)

        # Dump and delete the original key
        value_dump = r.dump(key)
        r.delete(key)

        # Restore the key with lowercase name and the original TTL
        if ttl == -1:  # Key doesn't have an expiry
            r.restore(lower_key, 0, value_dump)
        else:
            r.restore(lower_key, int(ttl * 1000), value_dump)

# Call the function to update keys
make_keys_lowercase(r)
