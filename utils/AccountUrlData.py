'''
get different environment mapping account, mapping urls
'''

test_accounts = {'UAT_RU':'stest56056 ',
                 'UAT_SOCN':'stest56703 ', #'stest56049',
                 'QA_RU':'',
                 'QA_SOCN':'stest140400'}

env_domain = {'UAT':'https://smartuat2.englishtown.com',
              'QA':'https://qa.englishtown.com'}

ru_product_url = {
'home': '/ecplatform/page/shopping?icid=buymoreclick&lng=en#/',
'grammer':'/ecplatform/page/shopping/detail?lng=en#/93',
'pronu':'/ecplatform/page/shopping/detail?lng=en#/92',
'online_ru':'/ecplatform/page/shopping/detail?lng=en#/7',
'center_ru': '/ecplatform/page/shopping/detail?lng=en#/6'

}

socn_product_url = {
'home': '/ecplatform/page/shopping?icid=buymoreclick&lng=en#/',
'grammer':'/ecplatform/page/shopping/detail?lng=en#/53',
'vacabu':'/ecplatform/page/shopping/detail?lng=en#/52',
'pronu':'/ecplatform/page/shopping/detail?lng=en#/54',
'hybrid_socn':'/ecplatform/page/shopping/detail?lng=en#/31',
'center_socn':'/ecplatform/page/shopping/detail?lng=en#/30',
'online_socn':'/ecplatform/page/shopping/detail?lng=en#/29'
}

# socn_product_url = {
# 'home': '/ecplatform/page/shopping?icid=buymoreclick&lng=en#/',
# 'grammer':'/ecplatform/page/shopping/detail?lng=en#/93',
# 'vacabu':'/ecplatform/page/shopping/detail?lng=en#/91',
# 'pronu':'/ecplatform/page/shopping/detail?lng=en#/92',
# 'hybrid_socn':'/ecplatform/page/shopping/detail?lng=en#/44',
# 'center_socn':'/ecplatform/page/shopping/detail?lng=en#/41',
# 'online_socn':'/ecplatform/page/shopping/detail?lng=en#/42'
# 'home_ru': '/ecplatform/page/shopping?icid=buymoreclick&lng=ru#/',
# 'grammer_ru':'/ecplatform/page/shopping/detail?lng=ru#/93',
# 'vacabu_ru':'/ecplatform/page/shopping/detail?lng=ru#/91',
# 'pronu_ru':'/ecplatform/page/shopping/detail?lng=ru#/92',
# 'hybrid_socn_ru':'/ecplatform/page/shopping/detail?lng=ru#/44',
# 'center_socn_ru':'/ecplatform/page/shopping/detail?lng=ru#/41',
# 'online_socn_ru':'/ecplatform/page/shopping/detail?lng=ru#/42',
# 'home_cs': '/ecplatform/page/shopping?icid=buymoreclick&lng=cs#/',
# 'grammer_cs':'/ecplatform/page/shopping/detail?lng=cs#/93',
# 'vacabu_cs':'/ecplatform/page/shopping/detail?lng=cs#/91',
# 'pronu_cs':'/ecplatform/page/shopping/detail?lng=cs#/92',
# 'hybrid_socn_cs':'/ecplatform/page/shopping/detail?lng=cs#/44',
# 'center_socn_cs':'/ecplatform/page/shopping/detail?lng=cs#/41',
# 'online_socn_cs':'/ecplatform/page/shopping/detail?lng=cs#/42',

# }

class GetRelatedUrls(object):
    def __init__(self, env, partner):
        self.env = env
        self.partner = partner
        self.account = ''
        self.url_list = {}

    def get_related_urls(self):
        if self.env == 'UAT':
            if self.partner == 'RU':
                self.account = test_accounts['UAT_RU']
                product_url = ru_product_url

            elif self.partner == 'SOCN':
                self.account = test_accounts['UAT_SOCN']
                product_url = socn_product_url

        elif self.env == 'QA':
            if self.partner == 'RU':
                self.account = test_accounts['QA_RU']
                product_url = ru_product_url
            elif self.partner == 'SOCN':
                self.account = test_accounts['QA_SOCN']
                product_url = socn_product_url

        for section, path in product_url.items():
            url = env_domain[self.env] + path
            self.url_list[section] = url

if __name__ == '__main__':
    env = 'UAT'
    partner = 'SOCN'
    g = GetRelatedUrls(env, partner)
    g.get_related_urls()
    print(g.account)
    print(g.url_list)

