import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS
import base64


def connect_to_db():
    conn = sqlite3.connect('database.db')
    return conn

def imageToBase64(file_path):
    try:
        with open(file_path, "rb") as file:
            file_data = file.read()
            encoded_data = base64.b64encode(file_data).decode('utf-8')
            return encoded_data
    except Exception as e:
        print("Error:", e)
        return None
def create_db_table():
    try:
        conn = connect_to_db()
        conn.execute('''DROP TABLE IF EXISTS images''')
        conn.execute('''
            CREATE TABLE images (
                image_id INTEGER PRIMARY KEY NOT NULL,
                species TEXT NOT NULL,
                timestamp TEXT NOT NULL,
                image TEXT NOT NULL
            );
        ''')

        conn.commit()
        print("image table created successfully")
    except Exception as e:
        print(e)
    finally:
        conn.close()


def insert_image(image):
    inserted_image = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO images (species, timestamp, image) VALUES (?, ?, ?)", (image['species'], image['timestamp'], image['image']) )
        conn.commit()
        inserted_image = get_image_by_id(cur.lastrowid)
    except:
        conn().rollback()

    finally:
        conn.close()

    return inserted_image


def get_images():
    images = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM images")
        rows = cur.fetchall()

        for i in rows:
            image = {}
            image["image_id"] = i["image_id"]
            image["species"] = i["species"]
            image["timestamp"] = i["timestamp"]
            image["image"] = i["image"]
            images.append(image)

    except:
        images = []

    return images


def get_image_by_id(image_id):
    image = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM images WHERE image_id = ?", (image_id,))
        row = cur.fetchone()

        # convert row object to dictionary
        image["image_id"] = row["image_id"]
        image["species"] = i["species"]
        image["timestamp"] = i["timestamp"]
        image["image"] = i["image"]
    except:
        image = {}

    return image

def delete_image(image_id):
    message = {}
    try:
        conn = connect_to_db()
        conn.execute("DELETE from images WHERE image_id = ?", (image_id,))
        conn.commit()
        message["status"] = "image deleted successfully"
    except:
        conn.rollback()
        message["status"] = "Cannot delete image"
    finally:
        conn.close()

    return message

images = [
    {
        "species": "antelope",
        "timestamp": "00000",
        "image": imageToBase64("0b1a3af197.jpg"),
    }
]

create_db_table()

for i in images:
    print(insert_image(i))




app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/api/images', methods=['GET'])
def api_get_images():
    return jsonify(get_images())

@app.route('/api/images/<image_id>', methods=['GET'])
def api_get_image(image_id):
    return jsonify(get_image_by_id(image_id))

@app.route('/api/images/add',  methods = ['POST'])
def api_add_image():
    image = request.get_json()
    return jsonify(insert_image(image))

@app.route('/api/images/update',  methods = ['PUT'])
def api_update_image():
    image = request.get_json()
    return jsonify(update_image(image))

@app.route('/api/images/delete/<image_id>',  methods = ['DELETE'])
def api_delete_image(image_id):
    return jsonify(delete_image(image_id))


if __name__ == "__main__":
    #app.debug = True
    #app.run(debug=True)
    app.run()