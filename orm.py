from .models import User

async def add_user(tg_id, username):
    user = await User.query.where(User.tg_id == tg_id).gino.first()

    if user is None:
        new_user = User(tg_id=tg_id, username=username)
        await new_user.create()


async def get_all_users():
    users = await User.query.gino.all()
    return users


async def get_all_users_filter():
    users = await User.query.order_by(User.id.desc()).gino.all()
    return users

async def get_first_user():
    user = await User.query.gino.first()
    return user