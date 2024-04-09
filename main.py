import sqlite3

def create_tables():
    conn = sqlite3.connect('characters.db')

    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS personalities (
                            id INTEGER PRIMARY KEY,
                            pipeline_params TEXT,
                            name TEXT,
                            gender TEXT CHECK(gender IN ('Male', 'Female')),  -- Ограничение CHECK для гендера
                            main_description TEXT,
                            goals TEXT,
                            role TEXT,
                            age INTEGER,
                            hobbies_and_interests TEXT,
                            character_traits TEXT,
                            dialogue_style TEXT
                        )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS characters (
                           id INTEGER PRIMARY KEY,
                           personality_id INTEGER,
                           global_context TEXT,
                           mood TEXT,
                           knowledge INTEGER,
                           FOREIGN KEY (personality_id) REFERENCES personalities(id)
                       )''')

    conn.commit()

    conn.close()

def fill_tables_with_test_data():
    # Тестовые данные для персонажей
    characters_data = [
        (1, 'Some global context 1', 'Happy', 50, 1),
        (2, 'Some global context 2', 'Sad', 30, 2),
        (3, 'Some global context 3', 'Neutral', 40, 3)
    ]

    # Тестовые данные для личностей
    personalities_data = [
        (1, 'Some pipeline params 1', 'Tim', 'Male', 'Description 1', 'Goals 1', 'Role 1', 35, 'Hobbies 1', 'Traits 1', 'Dialogue style 1'),
        (2, 'Some pipeline params 2', 'Misha', 'Female', 'Description 2', 'Goals 2', 'Role 2', 28, 'Hobbies 2', 'Traits 2', 'Dialogue style 2'),
        (3, 'Some pipeline params 3', 'Leonid', 'Male', 'Description 3', 'Goals 3', 'Role 3', 42, 'Hobbies 3', 'Traits 3', 'Dialogue style 3')
    ]

    conn = sqlite3.connect('characters.db')
    cursor = conn.cursor()

    cursor.executemany('''INSERT INTO characters (id, global_context, mood, knowledge, personality_id) 
                          VALUES (?, ?, ?, ?, ?)''', characters_data)

    cursor.executemany('''INSERT INTO personalities (id, pipeline_params, name, gender, main_description, goals, role, age, hobbies_and_interests, character_traits, dialogue_style) 
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', personalities_data)

    conn.commit()

    conn.close()


if __name__ == "__main__":
    create_tables()
    fill_tables_with_test_data()
    print("Таблицы созданы и заполнены тестовыми данными.")
