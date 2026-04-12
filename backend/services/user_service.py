from .. import models

def create_user_service(db, name, email):
    user = models.User(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_users_service(db, skip, limit, name=None):
    query = db.query(models.User)

    if name:
        query = query.filter(models.User.name.contains(name))

    return query.offset(skip).limit(limit).all()