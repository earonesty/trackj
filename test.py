import pytest
import trackj

# Test data with tracking numbers for different carriers
test_cases = [
    ("1Z999AA10123456784", "ups", "http://wwwapps.ups.com/WebTracking/track?track=yes&trackNums=1Z999AA10123456784"),
    ("9611020987654312345671", "fedex", "https://www.fedex.com/apps/fedextrack/?tracknumbers=9611020987654312345671"),
    ("9400111899223197428490", "usps", "https://tools.usps.com/go/TrackConfirmAction?qtc_tLabels1=9400111899223197428490"),
    ("1234567890", "dhl", "http://www.dhl.com/en/express/tracking.html?AWB=1234567890&brand=DHL"),
    ("LS123456789CN", "china_post", "http://track-chinapost.com/?trackNumber=LS123456789CN"),
    ("EC123456789US", "usps", "https://tools.usps.com/go/TrackConfirmAction?qtc_tLabels1=EC123456789US"),
    ("RR123456789GB", "royal_mail", "https://www.royalmail.com/track-your-item#/tracking-results/RR123456789GB"),
    ("3S123456789NL", "postnl", "https://www.postnl.nl/tracktrace/?lang=en&barcodes=3S123456789NL")
]

@pytest.mark.parametrize("tracking_number, expected_carrier, expected_url", test_cases)
def test_match(tracking_number, expected_carrier, expected_url):
    result = trackj.match(tracking_number)
    assert result is not None, f"Expected a result for {tracking_number}"
    assert result['carrier'] == expected_carrier, f"Expected carrier {expected_carrier}, got {result['carrier']}"
    assert result['url'] == expected_url, f"Expected URL {expected_url}, got {result['url']}"

@pytest.mark.parametrize("tracking_number, expected_url", [(case[0], case[2]) for case in test_cases])
def test_url(tracking_number, expected_url):
    result = trackj.url(tracking_number)
    assert result == expected_url, f"Expected URL {expected_url}, got {result}"

@pytest.mark.parametrize("tracking_number, expected_carrier", [(case[0], case[1]) for case in test_cases])
def test_carrier(tracking_number, expected_carrier):
    result = trackj.carrier(tracking_number)
    assert result == expected_carrier, f"Expected carrier {expected_carrier}, got {result}"

def test_invalid_tracking_number():
    result = trackj.match("INVALID123")
    assert result is None, "Expected None for an invalid tracking number"
    assert trackj.url("INVALID123") is None, "Expected None for an invalid tracking number"
    assert trackj.carrier("INVALID123") is None, "Expected None for an invalid tracking number"

def test_map():
    assert isinstance(trackj.MAP, dict), "Expected MAP to be a dictionary"
    assert "ups" in trackj.MAP, "UPS should be in the carrier MAP"
    assert "fedex" in trackj.MAP, "FedEx should be in the carrier MAP"
    assert "dhl" in trackj.MAP, "DHL should be in the carrier MAP"
