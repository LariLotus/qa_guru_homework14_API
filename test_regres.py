import requests


def test_requested_page_number():
    page = 2
    response = requests.get('https://reqres.in/api/users', params={'page': page})

    assert response.status_code == 200
    assert response.json()['page'] == page


def test_users_list_default_length():
    default_users_count = 6

    response = requests.get('https://reqres.in/api/users')

    assert len(response.json()['data']) == default_users_count


def test_single_user_not_found():
    response = requests.get('https://reqres.in/api/users/23')

    assert response.status_code == 404
    assert response.text == '{}'


def test_create_user():
    name = "jane"
    job = "job"

    response = requests.post(
        url='https://reqres.in/api/users',
        json={
            "name": name,
            "job": job}
    )

    assert response.status_code == 201
    assert response.json()['name'] == name


def test_delete_user_returns_204():
    response = requests.delete(url='https://reqres.in/api/users/2')

    assert response.status_code == 204
    assert response.text == ''