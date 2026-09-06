status_code=44
if status_code==100:
    print("information")
elif status_code==200:
    print("success")
elif status_code==300:
    print("redirectional")
elif status_code==400:
    print("client side errors")
elif status_code==500:
    print("server side errors")
else:
    print("unknown status code")