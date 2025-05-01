from sqlmodel import Session, select

from src.models.platform_model import Platform


def get_platform_by_name(db: Session, name: str):
    query = select(Platform).where(Platform.name == name)
    result = db.exec(query).first()
    print(result)
    return result


def create_platform(db: Session, game_info: Platform):
    db.add(game_info)
    db.commit()
    db.refresh(game_info)
    return game_info


def delete_platform_by_id(db: Session, id: int):
    query = select(Platform).where(Platform.id == id)
    result = db.exec(query).first()
    db.delete(result)
    db.commit()
    return result


# GET PLATFORM_BY_ID
def get_platform_by_id(db: Session, platform_id: int):
    return db.get(Platform, platform_id)


def update_platform(db: Session, new_platform: Platform):
    query = select(Platform).where(Platform.id == new_platform.id)
    old_platform = db.exec(query).first()

    old_platform.name = new_platform.name if new_platform.name else old_platform.name
    db.commit()
    db.refresh(old_platform)
    return old_platform
