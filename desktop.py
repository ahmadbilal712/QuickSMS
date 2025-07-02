from frappe import _

def get_data():
    return [
        {
            "module_name": "QuickSms",
            "type": "module",
            "label": _("QuickSms"),
            "icon": "octicon octicon-mail",  # You can change icon if needed
            "color": "blue",
            "link": "modules/QuickSms",
        }
    ]
