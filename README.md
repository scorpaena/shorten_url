## shorten_url
Don't hold back, make it shorter (your url of course)

This utility can be used for shortening long urls. Whole project is packed in Docker environment. For testing it's recommended to use Postman.
1. Clone the repository to your computer.
2. Run `docker-compose up --build -d`
3. Send payload using `POST` method to `http://0.0.0.0:8080/api/generate`. Example of the payload: 
`{"original_url": "https://someurl.com", "days_available": 5}`. Note: field `days_available` is optional, default value is 90 days.
4. Obtained `shortened_url` value can be used within input value of `days_available`. To retrieve original url, send `GET` request to `shortened_url` link.
See video how to use it: 
https://user-images.githubusercontent.com/25688041/210088165-2abb30e4-47aa-404f-9141-eed0e6f47f03.mp4

For generating `id` of the short urls `ShortUUID` library has been utilized, since it uses 57 different characters to generate unique uuid. The length of characters has been reduced to 8 to keep at least 1 million urls in database unique. Theoretically, 5 symbols should be enough, but practically collisions are subject to happen.<br />
Used this formula as a first approach to estimate theoretically, that 5 symbols should be enough: <br />
![image](https://user-images.githubusercontent.com/25688041/210089030-53acb3fc-9c78-4329-bbd3-e25857eef6aa.png) <br />
However, practically for `length=5`: <br />
```python
s = set()
for i in range(1000000):
    s.add(ShortUUID().random(length=5))
    
len(s)
998528
``` 
<br />

For `length=8`: <br />
```python
s = set()
for i in range(3000000):
    s.add(ShortUUID().random(length=8))    
    
len(s)
3000000
```


