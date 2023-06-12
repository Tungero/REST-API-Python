import sqlite3


connection = sqlite3.connect("database.db")
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS movies (
	id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	title VARCHAR(50),
	description VARCHAR(1024),
	release_year SMALLINT unsigned
);
''')

connection.commit()
connection.close()


def list_to_dict(array, keys):
	new_array = []

	for row in array:
		temp = {}
		for i in range(len(row)):
			temp[keys[i]] = row[i]
		new_array.append(temp)
	
	return new_array


def get(id=None):
	connection = sqlite3.connect("database.db")
	cursor = connection.cursor()

	where_clause = f' WHERE id={id}' if id != None else ''
	res = cursor.execute('''SELECT * FROM movies''' + where_clause).fetchall()

	column_names = [desc[0] for desc in cursor.description]

	connection.commit()
	connection.close()

	if len(res) == 0:
		return None
	
	if id == None:
		return list_to_dict(res, column_names)
	return list_to_dict(res, column_names)[0]


def add(title, description, release_year):
	connection = sqlite3.connect("database.db")
	cursor = connection.cursor()

	global res
	res_id = cursor.execute(f"INSERT INTO movies (title, description, release_year) VALUES ('{title}', '{description}', {release_year}) RETURNING id;").fetchone()[0]

	connection.commit()
	connection.close()

	return get(res_id)

def update(id, title, description, release_year):
	connection = sqlite3.connect("database.db")
	cursor = connection.cursor()
	
	description = f", description = '{description}'" if description != None else ""
	cursor.execute(f'''UPDATE movies
		SET title = '{title}', release_year = {release_year} {description}
		WHERE id = {id}''')

	connection.commit()
	connection.close()

	return get(id)
