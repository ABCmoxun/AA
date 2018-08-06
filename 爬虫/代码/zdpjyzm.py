def parse_form(html):
    """extract all input properties from the form
    提取表单内所有的输入属性值对
    """
    tree = lxml.html.fromstring(html)
    data = {}
    for e in tree.cssselect('form input'):
        if e.get('name'):
            data[e.get('name')] = e.get('value')
    return data

def register(first_name, last_name, email, password, captcha_fn):
    ##自动化处理验证码，进而自动化的注册网站账号密码
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    html = opener.open(REGISTER_URL).read()
    form = parse_form(html)
    form['first_name'] = first_name
    form['last_name'] = last_name
    form['email'] = email
    form['password'] = form['password_two'] = password
    img = extract_image(html)##获取图像数据
    captcha = ocr(img)##利用OCR进行识别图像内文本
    form['recaptcha_response_field'] = captcha
    encoded_data = urllib.urlencode(form)
    request = urllib2.Request(REGISTER_URL, encoded_data)
    response = opener.open(request)


if __name__ == '__main__':
    print register('Test Account', 'Test Account', '1234567@webscraping.com', 'example', ocr)