import click
import utils
import pprint

@click.group()
def APISendr():
    pass

@APISendr.command()
@click.option('--method','-m',default='get',help='Method of request')
@click.option('--url','-u',required=True,help='Url for send request')
@click.option('--authorization','-a',help='authorized by JWT')
def query(method,url,authorization):
    if method != None and url != None:
        if authorization != None:
            r = utils.send_request(method,url,None,None,authorization)
        else:
            r = utils.send_request(method,url,None,None,None)
        if r.status_code == 200:
            pprint.pprint(r.json())
        else:
            print(r.status_code)
    else:
        print('ERR/(0x000): Url and Method is required.')

@APISendr.command()
@click.option('--path','-p',required=True,help='Path file to Request')
def file(path):
    if path != None:
        data = utils.read_json(path)
        if utils.extract_data(data) != False:
            method,url,body,headers,authorization = utils.extract_data(data)
            r = utils.send_request(method,url,body,headers,authorization)
            if r.status_code == 200:
                pprint.pprint(r.json())
            else:
                print(r.status_code)
        else:
            print('ERR/(0x004): The file should not be empty')
    else:
        print('ERR/(0x001): Path is required.')

if __name__ == '__main__':
    APISendr()
