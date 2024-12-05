from src.models.db.settings.db_connection_handler import db_connection_handler

class PeopleRepository:
  def __init__(self) -> None:
    self.__conn = db_connection_handler.get_connection()

  def get_person_by_name(self, person_name: str) -> tuple:
    cursor = self.__conn.cursor()
    cursor.execute("SELECT name, age FROM people WHERE name = ?", (person_name,))
    person = cursor.fetchone()
    cursor.close()
    return person
  
  def registry_person(self, person_name: str, person_age: int) -> None:
    cursor = self.__conn.cursor()
    cursor.execute("INSERT INTO people (name, age) VALUES (?, ?)", (person_name, person_age))
    self.__conn.commit()
    cursor.close()