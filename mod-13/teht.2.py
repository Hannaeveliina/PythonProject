from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    connection = mysql.connector.connect(
        host='127.0.0.1',
        user='hanna',
        password='hannevk',
        database='flight_game'
    )
    return connection

@app.route('/kenttä/<icao>', methods=['GET'])
def hae_kenttä(icao):
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        sql = "SELECT ident, name, municipality FROM airport WHERE ident = %s"
        cursor.execute(sql, (icao.upper(),))
        result = cursor.fetchone()

        if result:
            response = {
                "ICAO": result["ident"],
                "Name": result["name"],
                "Municipality": result["municipality"]
            }
        else:
            response = {
                "Error": f"No airport found with ICAO code {icao.upper()}"
            }

        cursor.close()
        connection.close()
        return jsonify(response)

    except mysql.connector.Error as err:
        return jsonify({"Error": str(err)})


if __name__ == '__main__':
    app.run(debug=True, port=3000)
