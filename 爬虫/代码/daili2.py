import requests

proxies = {
#见Requests库
  "http": "http://10.10.1.10:3128",
  #"https": "http://10.10.1.10:1080",
  #！！"https": "http://user:pass@10.10.1.10:3128/",
  #urllib--proxy
  #proxy_addr = "394996257:a1jnn6er@116.62.112.142:16816"
}



requests.get("http://example.org", proxies=proxies)