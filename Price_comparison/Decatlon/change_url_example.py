from urllib.parse import urlparse, ParseResult, parse_qs, urlencode

u = urlparse('http://example.com/?page=1&text=test#section')
params = parse_qs(u.query)
params['page'] = 22  #  change query param here
res = ParseResult(scheme=u.scheme, netloc=u.hostname, path=u.path, params=u.params, query=urlencode(params), fragment=u.fragment)
print (res.geturl())