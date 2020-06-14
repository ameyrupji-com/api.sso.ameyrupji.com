from .settings import db
from datetime import datetime
from .models import User, Role

## Adding some dummy data!!!

# Create 'member@example.com' user with no roles
if not User.query.filter(User.email == 'member@example.com').first():
    user = User(
        email='member@example.com',
        email_confirmed_at=datetime.utcnow(),
        password='P@ssw0rd!',
    )
    db.session.add(user)
    db.session.commit()

# Create 'admin@example.com' user with 'Admin' and 'Agent' roles
if not User.query.filter(User.email == 'admin@example.com').first():
    user = User(
        email='admin@example.com',
        email_confirmed_at=datetime.utcnow(),
        password='P@ssw0rd!',
    )
    user.roles.append(Role(name='Admin'))
    user.roles.append(Role(name='Agent'))
    db.session.add(user)
    db.session.commit()
