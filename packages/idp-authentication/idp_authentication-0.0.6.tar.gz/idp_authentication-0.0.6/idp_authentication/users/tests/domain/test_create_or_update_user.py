def test_create_user(container):
    data = {
        "username": "test0",
        "email": "test0@gmail.com",
        "first_name": "test",
        "last_name": "test",
    }
    create_user = container.users_module().use_cases().create_or_update_user_use_case()
    created_user = create_user.execute(data=data)
    assert created_user.username == data["username"]


def test_update_user(container, user):
    data = {
        "username": "test1",
        "email": "test@cardoai.com",
        "first_name": "test",
        "last_name": "test",
    }
    previous_user_email = user.email
    create_user = container.users_module().use_cases().create_or_update_user_use_case()
    updated_user = create_user.execute(data=data)
    assert previous_user_email != updated_user.email
