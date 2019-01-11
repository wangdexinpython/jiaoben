


import hashlib

def md5(arg):
    md5_pwd = hashlib.md5(bytes('abd',encoding='utf-8'))
    md5_pwd.update(bytes(arg,encoding='utf-8'))
    return md5_pwd.hexdigest()

def log(user,pwd):
    with open('db','r',encoding='utf-8') as f:
        for line in f:
            u,p=line.strip().split('|')
            if u ==user and p == md5(pwd):
                return True






