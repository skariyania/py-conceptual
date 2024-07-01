## Redis installation

```sh
curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list

sudo apt-get update
sudo apt-get install redis
```
.. or follow original source documentation [here](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/install-redis-on-linux/)


## References
https://redis.io/docs/latest/develop/get-started/vector-database/
