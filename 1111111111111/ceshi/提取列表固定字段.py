import re
import string

value_handle = {
    "name":"",
    "data":"[[2,3],[2,4],5]",
    "regex":"a",
    "value":"ab.acd.aer.ag"
}
# r = value_handle.get('value').split('.')
# print(r)
def fetch_list_fix(value):
    data = ''

    key_list = value.get("value").split('.')
    # print(key_list)
    for i in value.get('data'):
        for y in i:
            if value.get("regex") in y.get(key_list[0], ''):
                data = y.get(key_list[1], '')
    print data
    #



fetch_list_fix({
    "name":"",
    "data":"",
    "regex":"a",
    "value":"ab.acd.aer.ag"
})

