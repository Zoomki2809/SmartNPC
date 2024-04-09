import gradio as gr
import sqlite3


def add_character_info(name, gender, main_description, goals, role, age, hobbies_and_interests, character_traits,
                       dialogue_style):
    conn = sqlite3.connect('characters.db')
    cursor = conn.cursor()

    cursor.execute('''INSERT INTO personalities (pipeline_params, name, gender, main_description, goals, role, age, hobbies_and_interests, character_traits, dialogue_style) 
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   ('Some pipeline params', name, gender, main_description, goals, role, age, hobbies_and_interests,
                    character_traits, dialogue_style))

    conn.commit()
    conn.close()

    return "Информация о персонаже успешно добавлена в базу данных."


iface = gr.Interface(fn=add_character_info,
                     inputs=["text", "text", "text", "text", "text", "number", "text", "text", "text"],
                     outputs="text",
                     title="Добавление информации о персонаже в базу данных")

iface.launch()
