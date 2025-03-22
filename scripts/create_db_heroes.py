from pathlib import Path

from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select


class Hero(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    secret_name: str
    age: int
    team_id: int = Field(foreign_key="team.id")
    team: "Team" = Relationship(back_populates="members")


class Team(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    members: list[Hero] = Relationship(back_populates="team")


engine = create_engine("sqlite:///database.db")


def create_tables():
    SQLModel.metadata.create_all(engine)


def create_heroes():
    hero_1 = Hero(id=1, name="Paco", secret_name="El chocolate", age=42, team_id=1)
    hero_2 = Hero(id=2, name="Miguel", secret_name="El cobra kai", age=20, team_id=2)
    hero_3 = Hero(id=3, name="Mariano", secret_name="El pensador", age=65, team_id=1)

    team_1 = Team(id=1, name="Equipo 1")
    team_2 = Team(id=2, name="Equipo 2")
    with Session(engine) as session:
        session.add(hero_1)
        session.add(hero_2)
        session.add(hero_3)
        session.add(team_1)
        session.add(team_2)
        session.commit()


def execute_querys():
    with Session(engine) as session:
        query = select(Hero).where(Hero.team_id == 1)
        result = session.exec(query)
        print(result.all())


def execute_querys_2():
    with Session(engine) as session:
        query = select(Team.name)
        result = session.exec(query)
        print(result.all())


def main():
    if not Path("database.db").exists():
        create_tables()
        create_heroes()

    execute_querys()
    execute_querys_2()


if __name__ == "__main__":
    main()
