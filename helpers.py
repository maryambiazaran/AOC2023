import requests,configparser

def get_cookie():
    config = configparser.ConfigParser()
    config.read('secrets.txt')
    cookie = config['session_info']['cookie']
    return cookie

def get_inputs(day):
    cookie, day = get_cookie(), int(day)
    headers = {'session': cookie}
    url = f'https://adventofcode.com/2023/day/{day}/input'
    session = requests.Session()
    resp = session.get(url,cookies=headers)
    return resp.text.split('\n')[:-1]