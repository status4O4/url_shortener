def test_shorten_and_resolve(service):
    code = service.shorten("https://example.com")
    url = service.resolve(code)
    assert url == "https://example.com"


def test_same_url_returns_same_code(service):
    code1 = service.shorten("https://example.com")
    code2 = service.shorten("https://example.com")

    assert code1 == code2
