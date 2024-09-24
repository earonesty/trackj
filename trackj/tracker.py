import re

MAP = {
    'ups': {
        'url': 'http://wwwapps.ups.com/WebTracking/track?track=yes&trackNums={tracking_number}',
        'patterns': [r'1Z[0-9A-Z]{16}', r'[\dT]\d{10}']
    },
    'fedex': {
        'url': 'https://www.fedex.com/apps/fedextrack/?tracknumbers={tracking_number}',
        'patterns': [r'96\d{20}', r'61\d{18}', r'\d{12}', r'\d{15}', r'(98\d+|98\d{2})\d{8}(\d{3})?']
    },
    'usps': {
        'url': 'https://tools.usps.com/go/TrackConfirmAction?qtc_tLabels1={tracking_number}',
        'patterns': [r'91\d+', r'9\d{15,21}', r'\d{20}', r'\d{26}', r'E\D{1}\d{9}\D{2}', r'[A-Za-z]{2}\d+US']
    },
    'dhl': {
        'url': 'http://www.dhl.com/en/express/tracking.html?AWB={tracking_number}&brand=DHL',
        'patterns': [r'\d{10,11}']
    },
    'canada_post': {
        'url': 'https://www.canadapost-postescanada.ca/track-reperage/en#/search?searchFor={tracking_number}',
        'patterns': [r'\d{16}', r'(91|71)\d{14}']
    },
    'royal_mail': {
        'url': 'https://www.royalmail.com/track-your-item#/tracking-results/{tracking_number}',
        'patterns': [r'[A-Z]{2}\d{9}GB']
    },
    'australia_post': {
        'url': 'https://auspost.com.au/mypost/track/#/details/{tracking_number}',
        'patterns': [r'(33|99)\d{8,12}']
    },
    'china_post': {
        'url': 'http://track-chinapost.com/?trackNumber={tracking_number}',
        'patterns': [r'[A-Z]{2}\d{9}CN']
    },
    'japan_post': {
        'url': 'https://trackings.post.japanpost.jp/services/srv/search/direct?reqCodeNo1={tracking_number}',
        'patterns': [r'[A-Z]{2}\d{9}JP']
    },
    'hermes_uk': {
        'url': 'https://www.myhermes.co.uk/track#/{tracking_number}/details',
        'patterns': [r'[PHL]\d{15}']
    },
    'gls': {
        'url': 'https://gls-group.com/track?match={tracking_number}',
        'patterns': [r'\d{11,12}']
    },
    'postnl': {
    'url': 'https://www.postnl.nl/tracktrace/?lang=en&barcodes={tracking_number}',
    'patterns': [r'3S\d{9}NL']
    },
    'correos_spain': {
        'url': 'https://www.correos.es/ss/Satellite/site/pagina-localizador_envios-sidioma=en_GB?numero={tracking_number}',
        'patterns': [r'[A-Z]{2}\d{9}ES']
    },
    'deutsche_post': {
        'url': 'https://www.deutschepost.de/sendung/simpleQuery.html?form.sendungsnummer={tracking_number}',
        'patterns': [r'[A-Z]{2}\d{9}DE']
    },
    'aramex': {
        'url': 'https://www.aramex.com/track/shipments/{tracking_number}',
        'patterns': [r'[23]\d{10,11}']
    },
    'sf_express': {
        'url': 'http://www.sf-express.com/cn/en/dynamic_functions/waybill/#search/bill-number/{tracking_number}',
        'patterns': [r'SF\d{10,12}', r'\d{12}']
    }
}

def match(tracking_number):
    tracking_number = tracking_number.replace(' ', '').upper()
    for carrier_id, data in MAP.items():
        for pattern in data['patterns']:
            if re.fullmatch(pattern, tracking_number):
                return {
                    'carrier': carrier_id,
                    'url': data['url'].format(tracking_number=tracking_number)
                }
    return None

def url(tracking_number):
    result = match(tracking_number)
    return result['url'] if result else None

def carrier(tracking_number):
    result = match(tracking_number)
    return result['carrier'] if result else None
