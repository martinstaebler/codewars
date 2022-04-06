import re

def domain_name(url):
    re_pattern = '[\/.]'
    arr_domainname = re.split(re_pattern, url)
    for item in arr_domainname:

        if "http" not in item and "www" not in item and len(item) > 0:
            return item
            break


print(domain_name("http://github.com/carbonfive/raygun")) #== "github"
print(domain_name("http://www.zombie-bites.com")) #== "zombie-bites"
print(domain_name("https://www.cnet.com")) #== "cnet"

text = "python is# an% easy;language- to, learn."
print(re.split('; |, |# |% |- |;', text))