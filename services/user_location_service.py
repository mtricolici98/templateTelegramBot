from db.database import Session
from models.models import UserLocation


class NoLocationDataError(Exception):
    pass


def get_user_location(uid):
    with Session() as session:
        try:
            return session.query(UserLocation).filter(UserLocation.user_id == uid).one()
        except Exception as ex:
            raise NoLocationDataError("User doesn't have location data configured.")


def _create_user_location(uid, lat, lon):
    with Session() as session:
        ul = UserLocation(user_id=uid, lat=lat, lon=lon)
        session.add(ul)
        session.commit()
        return ul


def create_or_update_user_location(uid, lat, lon):
    try:
        loc = get_user_location(uid)
    except NoLocationDataError:
        loc = None
    if not loc:
        loc = _create_user_location(uid, lat, lon)
    return loc
