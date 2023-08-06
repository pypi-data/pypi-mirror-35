# Payload WTF

simple payload with an easy format for building Python APIs (like Django).
As an alternative that frees you to render responses without DRF or something
that is full of rules.

## Quick Example
You can use this package is easy:

```python
payload = PayloadWTF()
payload.set_state(setter=PayloadWTF.SET_RESULT, data={"data": "Yes this is data from queryset"})
payload.set_state(setter=PayloadWTF.SET_LINKS, next="http://.../?page=1")
payload.set_state(setter=PayloadWTF.SET_META, data={'user_activated': {'username': 'yanzen'}})
print(payload.tojson()) # Or payload.todata() result is dictionary
```

Result:
```
{
    "results": {"data": "Yes this is data from queryset"},
    "meta": {"user_activated": {"username": "yanzen"}},
    "links": {"next": "http://.../?page=1", "prev": ""}
}
```

