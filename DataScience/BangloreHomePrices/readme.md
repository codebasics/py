![](BHP_website.PNG)

This data science project series walks through step by step process of how to build a real estate price prediction website. We will first build a model using sklearn and linear regression using Bangalore home prices dataset from kaggle.com. Second step would be to write a python flask server that uses the saved model to serve http requests. Third component is the website built in html, css and javascript that allows user to enter home square ft area, bedrooms etc and it will call python flask server to retrieve the predicted price. During model building we will cover almost all data science concepts such as data load and cleaning, outlier detection and removal, feature engineering, dimensionality reduction, gridsearchcv for hyperparameter tuning, k fold cross validation etc. Technology and tools wise this project covers,

1. Python
2. Numpy and Pandas for data cleaning
3. Matplotlib for data visualization
4. Sklearn for model building
5. Jupyter notebook, visual studio code and pycharm as IDE
6. Python flask for http server
7. HTML/CSS/Javascript for UI

# Deploy this app to cloud (AWS EC2)

1. Create EC2 instance using amazon console, also in security group add a rule to allow HTTP incoming traffic
2. Now connect to your instance using a command like this,
```
ssh -i "C:\Users\Viral\.ssh\Banglore.pem" ubuntu@ec2-3-133-88-210.us-east-2.compute.amazonaws.com
```
3. nginx setup
   1. Install nginx on EC2 instance using these commands,
   ```
   sudo apt-get update
   sudo apt-get install nginx
   ```
   2. Above will install nginx as well as run it. Check status of nginx using
   ```
   sudo service nginx status
   ```
   3. Here are the commands to start/stop/restart nginx
   ```
   sudo service nginx start
   sudo service nginx stop
   sudo service nginx restart
   ```
   4. Now when you load cloud url in browser you will see a message saying "welcome to nginx" This means your nginx is setup and running.
4. Now you need to copy all your code to EC2 instance. You can do this either using git or copy files using winscp. We will use winscp. You can download winscp from here: https://winscp.net/eng/download.php
5. Once you connect to EC2 instance from winscp (instruction in a youtube video), you can now copy all code files into /home/ubuntu/ folder. The full path of your root folder is now: **/home/ubuntu/BangloreHomePrices**
6.  After copying code on EC2 server now we can point nginx to load our property website by default. For below steps,
    1. Create this file /etc/nginx/sites-available/bhp.conf. The file content looks like this,
    ```
    server {
	    listen 80;
            server_name bhp;
            root /home/ubuntu/BangloreHomePrices/client;
            index app.html;
            location /api/ {
                 rewrite ^/api(.*) $1 break;
                 proxy_pass http://127.0.0.1:5000;
            }
    }
    ```
    2. Create symlink for this file in /etc/nginx/sites-enabled by running this command,
    ```
    sudo ln -v -s /etc/nginx/sites-available/bhp.conf /etc/nginx/sites-enabled/bhp.conf
    ```
    3. Remove symlink for default file in /etc/nginx/sites-enabled directory,
    ```
    sudo unlink default
    ```
    4. Restart nginx,
    ```
    sudo service nginx restart
    ```
7. Now install python packages and start flask server
```
sudo apt-get install python3-pip
sudo pip3 install -r /home/ubuntu/BangloreHomePrices/server/requirements.txt
python3 /home/ubuntu/BangloreHomePrices/server/server.py
```
Running last command above will prompt that server is running on port 5000.
8. Now just load your cloud url in browser (for me it was http://ec2-3-133-88-210.us-east-2.compute.amazonaws.com/) and this will be fully functional website running in production cloud environment





## Run locally

From the `server` directory, install the dependencies and start the Flask API:

```bash
cd BangloreHomePrices/server
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python server.py
```

The API is available at `http://localhost:5000`. The `/health` endpoint can be
used to verify that the server is running. The saved model artifacts must be
placed in `server/artifacts/` before starting the API.

## API example

```bash
curl -X POST http://localhost:5000/predict_home_price ^
  -d "total_sqft=1000" -d "location=1st Phase JP Nagar" -d "bhk=2" -d "bath=2"
```

## Contributing

Bug fixes, documentation improvements, tests, and small usability improvements
are welcome. Please keep changes focused and explain the motivation in your
pull request.
