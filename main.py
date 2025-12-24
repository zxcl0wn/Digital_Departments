import time
from datetime import datetime
import psycopg2
from generator import GameEvent
from decouple import config


def main():
    connect = psycopg2.connect(
        dbname=config("DATABASE_NAME"),
        user=config("DATABASE_USER"),
        password=config("DATABASE_PASSWORD"),
        host=config("DATABASE_HOST"),
        port=config("DATABASE_PORT")
    )

    cursor = connect.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS game_statistics (
        id SERIAL PRIMARY KEY,
        player VARCHAR(100) NOT NULL,
        action VARCHAR(100) NOT NULL,
        score INTEGER NOT NULL,
        level INTEGER NOT NULL,
        event_time TIMESTAMP NOT NULL
        );
    ''')


    for _ in range(20):
        event = GameEvent()
        event_time = datetime.now()
        cursor.execute(
            "INSERT INTO game_statistics (player, action, score, level, event_time) VALUES (%s, %s, %s, %s, %s);",
            (event.player, event.action, event.score, event.level, event_time)
        )
        print(f'Игрок {event.player} был добавлен в БД')
        connect.commit()
        time.sleep(2)


    connect.commit()
    cursor.close()
    connect.close()

if __name__ == "__main__":
    main()
