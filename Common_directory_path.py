# https://www.codewars.com/kata/597f334f1fe82a950500004b/train/python

def get_common_directory_path(pathes): 

    shortest_str_len = len(min(pathes, key=len))
    for i in range(0, shortest_str_len):
        slice = pathes[0][:i]

        for y in pathes:
            if slice != y[:i]:
                substring = pathes[0][:i-1]
                return substring[:substring.rfind('/')+1]





print(get_common_directory_path(['/web/images/image1.png', '/web/images/image2.png']))#, '/web/images/')
print(get_common_directory_path(['/web/assets/style.css', '/web/scripts/app.js',  'home/setting.conf']))#, '')
print(get_common_directory_path(['/web/assets/style.css', '/.bin/mocha',  '/read.me']))#, '/')
print(get_common_directory_path(['/web/favicon.ico', '/web-scripts/dump', '/webalizer/logs']))#, '/')