# pybot-hunter
Using a 3-node RPi Cluster to hunt and identify potential Twitter bots. :rotating_light: :traffic_light:

### __Scope of the project:__
The concept of pybot-hunter is a set of scripts designed to look for Twitter accounts with abnormal activity and analyze their online patterns ( sentiment, timing intervals, topic(s) / trend )
If an account meets all of the required categories, it's automatically reported. 

This project makes use of the [python-twitter](https://github.com/bear/python-twitter) wrapper to interact with Twitter's API. 

### __High level overview:__
1. **[Node][1]** streams / captures the initial data 
2. **[Node][2]** communicates with [Node][1] to extract detailed information about a suspicious account 
3. **[Node][3]** parses the extracted data for sentiment, timing intervals, irregular patterns

### __Where we're at:__
- [x] Stream tweets based on custom terms [__Node1__]
- [x] Store usernames in ```/tmp``` directory that raise flags [__Node1__]
- [x] Make use of sshpass from [__Node2__] into [__Node1__] to extract last 200 tweets per ```screen_name``` into ```/filtered/screen_name```
- [x] Remove extracted username from ```/tmp``` directly

###### Install dependencies on [__Nodes__][1][2][3]

```python
pip install -Ur requirements.txt
```

###### Run setup.py on [__Nodes__][1]
```python
python setup.py
```

###### Update config.py with your Twitter App information [__Nodes__][1]
```python
consumer_key = '<consumer-key>'
consumer_secret = '<consumer-secret>'
access_key = '<access-key>'
access_secret = '<access-secret>'
```

###### Start the stream on [Node][1] :earth_americas:
```python
python capture-stream.py
```

###### Setup [Node][2]
1. Make sure ```pybot-muncher.py``` is copied to ```/home/pi ```
2. Edit the file to include the ip address of [Node][1] 
```python 
$ nano pybot-muncher.py
```
```python
# Change <node1-ip-address> to 192.x.x.x
# Change <password> to the password of your [Node][1] RPi
subprocess.call("sshpass -p <password> ssh pi@<node1-ip-address> 'cd ~ && python pybot-twitter/process_stream_data.py > /home/pi/pybot-twitter/runlog.txt'", shell=True)

```
