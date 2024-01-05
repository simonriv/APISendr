import click
import requests

@click.group()
def APISendr():
    pass

@APISendr.command()
@click.option('--method','-m',default='get',help='Method of request')
@click.option('--url','-u',required=True,help='Url for send request')
def query(method,url):
    if method != None and url != None:
        r = ''
        if method == 'get':
            try:
                r = requests.get(url)
            except requests.exceptions.HTTPError as errh:
                raise errh
            except requests.exceptions.ConnectionError as errc:
                raise errc
            except requests.exceptions.Timeout as errt:
                raise errt
            except requests.exceptions.RequestException as err:
                raise err
            if r.status_code == 200:
                print(r.json())
            else:
                print(r.status_code)
        else:
            print('WAR/(0X000): Only use method get in query instruction')
    else:
        print('ERR/(0x000): Url and Method is required.')

@APISendr.command()
def file():
    print('API Send Request file')

if __name__ == '__main__':
    APISendr()
