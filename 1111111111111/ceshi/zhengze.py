import re
kwarg = {
    "regex":".*",
    "data":"2室1厅1卫                                  75                                平  简单装修"
}

def regular(self, *args, **kwarg):
    return [value for value in kwarg.get("data", []) if not re.match(kwarg.get("regex"), value)]





regular(kwarg)