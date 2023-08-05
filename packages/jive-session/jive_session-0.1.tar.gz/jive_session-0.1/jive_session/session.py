def Session(req):
    info = req.environ
    prefix = info['wsgi.url_scheme']
    http_host = info['HTTP_HOST']
    hostname = http_host.split(":")[0]
    path = info['PATH_INFO']
    user_agent = info['HTTP_USER_AGENT']
    host = "%s://%s" % (prefix,hostname)
    caller = "%s://%s%s" % (prefix,http_host,path)
    session_key = user_agent+caller
    return host,session_key
