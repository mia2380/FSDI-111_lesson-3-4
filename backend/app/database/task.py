from app.database import get_db


def output_formatter(results):
    out = []
    for result in results:
        formatted_result = {
            "id": result[0],
            "summary": result[1],
            "description": result[2],
            "is_active": result[3]
        }
        out.append(formatted_result)
    return out


def scan():
    conn = get_db()
    cursor = conn.execute(
        "SELECT * FROM task WHERE is_active=1", ()
    )
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def select_by_id(pk):
    conn = get_db()
    cursor = conn.execute(
        "SELECT * FROM task WHERE id=?", (pk, )
    )
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)[0]


def insert(raw_data):
    task_data = (
        raw_data.get("summary"),
        raw_data.get("description")
    )

    statement = """
        INSERT INTO task (
                summary,
                description
            ) VALUES (
                ?, ?
            )
        """

    conn = get_db()
    conn.execute(statement, task_data)
    conn.commit()
    conn.close()


def update(raw_data, pk):
    task_data = (
        raw_data.get("summary"),
        raw_data.get("description"),
        raw_data.get("is_active"),
        "pk"
    )

    statement = """
        UPDATE task
        SET summary=?,
            description=?,
            is_active=?
        WHERE id=?
    """
    conn = get_db()
    conn.execute(statement, task_data)
    conn.commit()
    conn.close()


def delete(pk):
    conn = get_db()
    conn.execute("DELETE FROM task WHERE id=?", (pk, ))
    conn.commit()
    conn.close()
