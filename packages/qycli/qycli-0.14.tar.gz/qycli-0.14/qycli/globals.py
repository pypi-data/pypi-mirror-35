# coding: utf-8 2018/9/4 14:44

url = "https://api.qingcloud.com/iaas/"
prefix = "GET\n/iaas/\n"

api_version = 1
signature_version = 1
conf_file_name = "qy_config.yaml"

common_params = {
    "action": "",
    "zone": "",
    "time_stamp": "",
    "access_key_id": "",
    "version": api_version,
    "signature_method": "HmacSHA256",
    "signature_version": signature_version
}

