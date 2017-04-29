from __future__ import unicode_literals
from frappe import _

def get_data():
        return [
                {
                        "label": _("Docs"),
                        "items": [
                                {
                                        "type": "doctype",
                                        "name": "Fabric Checking Report"
                                },{
                                        "type": "doctype",
                                        "name": "Fabric Packing List"
                                }
                        ]
                },
                {
                        "label": _("Masters"),
                        "items": [
                                {
                                        "type": "doctype",
                                        "name": "Pining"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Taka Shade"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Taka Width"
                                }
                        ]
                }
        ]
