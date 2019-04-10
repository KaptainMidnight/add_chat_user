import requests

try:
    url = "https://api.vk.com/method/friends.get?"
    url_add = "https://api.vk.com/method/messages.addChatUser?"
    access_token = "token"  # Сюда свой токен
    v = "5.92"
    user_id = "user_id"  # Сюда надо вставить СВОЙ id для получения друзей
    response = requests.get(url, params={  # Получаем друзей
        'access_token': access_token,
        'v': v,
        'user_id': user_id
    })
    friends = response.json()['response']['items']  # Берем id друзей
    for i in friends:
        a = requests.get(url_add, params={  # Добавляем их в чат
            'access_token': access_token,
            'v': v,
            'user_id': str(i),
            'chat_id': '111'
        })
except Exception as e:
    print(f"Error: {e}")
