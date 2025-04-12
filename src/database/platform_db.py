from sqlmodel import Session, select

from src.models.platform_model import Platform


def get_platform_by_name(db: Session, name: str):
    query = select(Platform).where(Platform.name == name)
    result = db.exec(query).first()
    print(result)
    return result


def create_platform(db: Session, name: str):
    platform = Platform(name=name)
    db.add(platform)
    db.commit()
    db.refresh(platform)
    print(platform)


def delete_platform_by_id(db: Session, id: int):
    query = select(Platform).where(Platform.id == id)
    result = db.exec(query).first()
    db.delete(result)
    db.commit()
