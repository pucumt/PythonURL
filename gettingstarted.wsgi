import GetURLMain

def application(environ, start_response):
    start_response('200 ok', [('content-type', 'text/plain')])
    return GetURLMain.printme()