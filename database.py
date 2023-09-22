from flask import Flask, request, jsonify
import pyodbc
import uuid
app = Flask(__name__)

class DatabaseManager:
    def __init__(self):
        server = 'DESKTOP-U2OOKJP'
        database = 'nayaysetu'
        trusted_connection = 'Trusted_Connection=yes;'
        try:
            self.conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';'+trusted_connection)
        except:
            print("Error connecting to database")

db_manager = DatabaseManager()

# Create operation for Prisoner_dashboard table
@app.route('/create_prisoner_dashboard', methods=['POST'])
def create_prisoner_dashboard_endpoint():
    try:
        data = request.json
        case_filed = data['case_filed']
        lawyer = data['lawyer']
        legal_information = data['legal_information']
        case_status = data['case_status']
        rehab_schedule = data['rehab_schedule']

        cursor = db_manager.conn.cursor()
        cursor.execute("INSERT INTO Prisoner_dashboard (Case_filed, lawyer, legal_information, Case_status, Rehabilatation_schedule) VALUES (?, ?, ?, ?, ?)",
                       (case_filed, lawyer, legal_information, case_status, rehab_schedule))
        db_manager.conn.commit()
        cursor.close()
        return jsonify({"message": "Prisoner_dashboard created successfully"})
    except pyodbc.Error as e:
        return jsonify({"error": f"Error creating Prisoner_dashboard: {str(e)}"}), 500

# Read operation for Prisoner_dashboard table
@app.route('/get_prisoner_dashboard/<int:prisoner_id>', methods=['GET'])
def get_prisoner_dashboard_by_id_endpoint(prisoner_id):
    try:
        cursor = db_manager.conn.cursor()
        cursor.execute("SELECT * FROM Prisoner_dashboard WHERE Id = ?", (prisoner_id,))
        data = cursor.fetchone()
        cursor.close()
        if data:
            return jsonify({"prisoner_dashboard": data})
        else:
            return jsonify({"message": "Prisoner_dashboard not found"}), 404
    except pyodbc.Error as e:
        return jsonify({"error": f"Error querying Prisoner_dashboard: {str(e)}"}), 500

# Update operation for Prisoner_dashboard table
@app.route('/update_prisoner_dashboard/<int:prisoner_id>', methods=['PUT'])
def update_prisoner_dashboard_endpoint(prisoner_id):
    try:
        data = request.json
        case_filed = data['case_filed']
        lawyer = data['lawyer']
        legal_information = data['legal_information']
        case_status = data['case_status']
        rehab_schedule = data['rehab_schedule']

        cursor = db_manager.conn.cursor()
        cursor.execute("UPDATE Prisoner_dashboard SET Case_filed = ?, lawyer = ?, legal_information = ?, Case_status = ?, Rehabilatation_schedule = ? WHERE Id = ?",
                       (case_filed, lawyer, legal_information, case_status, rehab_schedule, prisoner_id))
        db_manager.conn.commit()
        cursor.close()
        return jsonify({"message": "Prisoner_dashboard updated successfully"})
    except pyodbc.Error as e:
        return jsonify({"error": f"Error updating Prisoner_dashboard: {str(e)}"}), 500

# Delete operation for Prisoner_dashboard table
@app.route('/delete_prisoner_dashboard/<int:prisoner_id>', methods=['DELETE'])
def delete_prisoner_dashboard_endpoint(prisoner_id):
    try:
        cursor = db_manager.conn.cursor()
        cursor.execute("DELETE FROM Prisoner_dashboard WHERE Id = ?", (prisoner_id,))
        db_manager.conn.commit()
        cursor.close()
        return jsonify({"message": "Prisoner_dashboard deleted successfully"})
    except pyodbc.Error as e:
        return jsonify({"error": f"Error deleting Prisoner_dashboard: {str(e)}"}), 500

# Create operation for Case_Filed table
@app.route('/create_case_filed', methods=['POST'])
def create_case_filed_endpoint():
    try:
        data = request.json
        name_of_prisoner = data['name_of_prisoner']
        case_type = data['case_type']
        court_name = data['court_name']
        stage = data['stage']
        name_of_party = data['name_of_party']
        year = data['year']

        cursor = db_manager.conn.cursor()
        cursor.execute("INSERT INTO Case_Filed (Id,Name_of_prisoner, Case_type, Court_name, Stage, Name_of_party, Year) VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (1,name_of_prisoner, case_type, court_name, stage, name_of_party, year))
        db_manager.conn.commit()
        cursor.close()
        return jsonify({"message": "Case_Filed created successfully"})
    except pyodbc.Error as e:
        return jsonify({"error": f"Error creating Case_Filed: {str(e)}"}), 500

# Read operation for Case_Filed table
@app.route('/get_case_filed/<int:case_id>', methods=['GET'])
def get_case_filed_by_id_endpoint(case_id):
    try:
        cursor = db_manager.conn.cursor()
        cursor.execute("SELECT * FROM Case_Filed WHERE Id = ?", (case_id,))
        data = cursor.fetchone()
        cursor.close()
        if data:
            return jsonify({"case_filed": data})
        else:
            return jsonify({"message": "Case_Filed not found"}), 404
    except pyodbc.Error as e:
        return jsonify({"error": f"Error querying Case_Filed: {str(e)}"}), 500

# Update operation for Case_Filed table
@app.route('/update_case_filed/<int:case_id>', methods=['PUT'])
def update_case_filed_endpoint(case_id):
    try:
        data = request.json
        name_of_prisoner = data['name_of_prisoner']
        case_type = data['case_type']
        court_name = data['court_name']
        stage = data['stage']
        name_of_party = data['name_of_party']
        year = data['year']

        cursor = db_manager.conn.cursor()
        cursor.execute("UPDATE Case_Filed SET Name_of_prisoner = ?, Case_type = ?, Court_name = ?, Stage = ?, Name_of_party = ?, Year = ? WHERE Id = ?",
                       (name_of_prisoner, case_type, court_name, stage, name_of_party, year, case_id))
        db_manager.conn.commit()
        cursor.close()
        return jsonify({"message": "Case_Filed updated successfully"})
    except pyodbc.Error as e:
        return jsonify({"error": f"Error updating Case_Filed: {str(e)}"}), 500

# Delete operation for Case_Filed table
@app.route('/delete_case_filed/<int:case_id>', methods=['DELETE'])
def delete_case_filed_endpoint(case_id):
    try:
        cursor = db_manager.conn.cursor()
        cursor.execute("DELETE FROM Case_Filed WHERE Id = ?", (case_id,))
        db_manager.conn.commit()
        cursor.close()
        return jsonify({"message": "Case_Filed deleted successfully"})
    except pyodbc.Error as e:
        return jsonify({"error": f"Error deleting Case_Filed: {str(e)}"}), 500


# Create operation for Legal_information table
@app.route('/create_legal_information', methods=['POST'])
def create_legal_information_endpoint():
    try:
        data = request.json
        name = data['name']
        case_type = data['case_type']
        case_no = data['case_no']
        name_of_party = data['name_of_party']
        court_name = data['court_name']

        cursor = db_manager.conn.cursor()
        cursor.execute("INSERT INTO Legal_information (Name, Case_type, Case_no, Name_of_party, court_name) VALUES (?, ?, ?, ?, ?)",
                       (name, case_type, case_no, name_of_party, court_name))
        db_manager.conn.commit()
        cursor.close()
        return jsonify({"message": "Legal_information created successfully"})
    except pyodbc.Error as e:
        return jsonify({"error": f"Error creating Legal_information: {str(e)}"}), 500

# Read operation for Legal_information table
@app.route('/get_legal_information/<int:legal_info_id>', methods=['GET'])
def get_legal_information_by_id_endpoint(legal_info_id):
    try:
        cursor = db_manager.conn.cursor()
        cursor.execute("SELECT * FROM Legal_information WHERE Id = ?", (legal_info_id,))
        data = cursor.fetchone()
        cursor.close()
        if data:
            return jsonify({"legal_information": data})
        else:
            return jsonify({"message": "Legal_information not found"}), 404
    except pyodbc.Error as e:
        return jsonify({"error": f"Error querying Legal_information: {str(e)}"}), 500

# Update operation for Legal_information table
@app.route('/update_legal_information/<int:legal_info_id>', methods=['PUT'])
def update_legal_information_endpoint(legal_info_id):
    try:
        data = request.json
        name = data['name']
        case_type = data['case_type']
        case_no = data['case_no']
        name_of_party = data['name_of_party']
        court_name = data['court_name']

        cursor = db_manager.conn.cursor()
        cursor.execute("UPDATE Legal_information SET Name = ?, Case_type = ?, Case_no = ?, Name_of_party = ?, court_name = ? WHERE Id = ?",
                       (name, case_type, case_no, name_of_party, court_name, legal_info_id))
        db_manager.conn.commit()
        cursor.close()
        return jsonify({"message": "Legal_information updated successfully"})
    except pyodbc.Error as e:
        return jsonify({"error": f"Error updating Legal_information: {str(e)}"}), 500

# Delete operation for Legal_information table
@app.route('/delete_legal_information/<int:legal_info_id>', methods=['DELETE'])
def delete_legal_information_endpoint(legal_info_id):
    try:
        cursor = db_manager.conn.cursor()
        cursor.execute("DELETE FROM Legal_information WHERE Id = ?", (legal_info_id,))
        db_manager.conn.commit()
        cursor.close()
        return jsonify({"message": "Legal_information deleted successfully"})
    except pyodbc.Error as e:
        return jsonify({"error": f"Error deleting Legal_information: {str(e)}"}), 500
# Create operation for Case_status table
@app.route('/create_case_status', methods=['POST'])
def create_case_status_endpoint():
    try:
        data = request.json
        case_progress = data['case_progress']

        cursor = db_manager.conn.cursor()
        cursor.execute("INSERT INTO Case_status (case_progress) VALUES (?)", (case_progress,))
        db_manager.conn.commit()
        cursor.close()
        return jsonify({"message": "Case_status created successfully"})
    except pyodbc.Error as e:
        return jsonify({"error": f"Error creating Case_status: {str(e)}"}), 500

# Read operation for Case_status table
@app.route('/get_case_status/<int:case_status_id>', methods=['GET'])
def get_case_status_by_id_endpoint(case_status_id):
    try:
        cursor = db_manager.conn.cursor()
        cursor.execute("SELECT * FROM Case_status WHERE Id = ?", (case_status_id,))
        data = cursor.fetchone()
        cursor.close()
        if data:
            return jsonify({"case_status": data})
        else:
            return jsonify({"message": "Case_status not found"}), 404
    except pyodbc.Error as e:
        return jsonify({"error": f"Error querying Case_status: {str(e)}"}), 500

# Update operation for Case_status table
@app.route('/update_case_status/<int:case_status_id>', methods=['PUT'])
def update_case_status_endpoint(case_status_id):
    try:
        data = request.json
        case_progress = data['case_progress']

        cursor = db_manager.conn.cursor()
        cursor.execute("UPDATE Case_status SET case_progress = ? WHERE Id = ?", (case_progress, case_status_id))
        db_manager.conn.commit()
        cursor.close()
        return jsonify({"message": "Case_status updated successfully"})
    except pyodbc.Error as e:
        return jsonify({"error": f"Error updating Case_status: {str(e)}"}), 500

# Delete operation for Case_status table
@app.route('/delete_case_status/<int:case_status_id>', methods=['DELETE'])
def delete_case_status_endpoint(case_status_id):
    try:
        cursor = db_manager.conn.cursor()
        cursor.execute("DELETE FROM Case_status WHERE Id = ?", (case_status_id,))
        db_manager.conn.commit()
        cursor.close()
        return jsonify({"message": "Case_status deleted successfully"})
    except pyodbc.Error as e:
        return jsonify({"error": f"Error deleting Case_status: {str(e)}"}), 500

# Create operation for Lawyer table
@app.route('/create_lawyer', methods=['POST'])
def create_lawyer_endpoint():
    try:
        data = request.json
        search_lawyer = data['search_lawyer']
        insert_lawyer_data = data['insert_lawyer_data']

        cursor = db_manager.conn.cursor()
        cursor.execute("INSERT INTO Lawyer (search_lawyer, Insert_lawyer_data) VALUES (?, ?)", (search_lawyer, insert_lawyer_data))
        db_manager.conn.commit()
        cursor.close()
        return jsonify({"message": "Lawyer created successfully"})
    except pyodbc.Error as e:
        return jsonify({"error": f"Error creating Lawyer: {str(e)}"}), 500

# Read operation for Lawyer table
@app.route('/get_lawyer/<int:lawyer_id>', methods=['GET'])
def get_lawyer_by_id_endpoint(lawyer_id):
    try:
        cursor = db_manager.conn.cursor()
        cursor.execute("SELECT * FROM Lawyer WHERE Id = ?", (lawyer_id,))
        data = cursor.fetchone()
        cursor.close()
        if data:
            return jsonify({"lawyer": data})
        else:
            return jsonify({"message": "Lawyer not found"}), 404
    except pyodbc.Error as e:
        return jsonify({"error": f"Error querying Lawyer: {str(e)}"}), 500

# Update operation for Lawyer table
@app.route('/update_lawyer/<int:lawyer_id>', methods=['PUT'])
def update_lawyer_endpoint(lawyer_id):
    try:
        data = request.json
        search_lawyer = data['search_lawyer']
        insert_lawyer_data = data['insert_lawyer_data']

        cursor = db_manager.conn.cursor()
        cursor.execute("UPDATE Lawyer SET search_lawyer = ?, Insert_lawyer_data = ? WHERE Id = ?", (search_lawyer, insert_lawyer_data, lawyer_id))
        db_manager.conn.commit()
        cursor.close()
        return jsonify({"message": "Lawyer updated successfully"})
    except pyodbc.Error as e:
        return jsonify({"error": f"Error updating Lawyer: {str(e)}"}), 500

# Delete operation for Lawyer table
@app.route('/delete_lawyer/<int:lawyer_id>', methods=['DELETE'])
def delete_lawyer_endpoint(lawyer_id):
    try:
        cursor = db_manager.conn.cursor()
        cursor.execute("DELETE FROM Lawyer WHERE Id = ?", (lawyer_id,))
        db_manager.conn.commit()
        cursor.close()
        return jsonify({"message": "Lawyer deleted successfully"})
    except pyodbc.Error as e:
        return jsonify({"error": f"Error deleting Lawyer: {str(e)}"}), 500
# Create a route to add data to the Undertrial_prisoner table
@app.route('/add_undertrial_prisoner', methods=['POST'])
def add_undertrial_prisoner():
    try:
        data = request.json
        name = data['name']
        username = data['username']
        password = data['password']

        cursor = db_manager.conn.cursor()
        cursor.execute("INSERT INTO Undertrial_prisoner (Name, Username, password) VALUES (?, ?, ?)",
                       (name, username, password))
        db_manager.conn.commit()
        cursor.close()

        return jsonify({"message": "Undertrial prisoner added successfully"})
    except pyodbc.Error as e:
        return jsonify({"error": f"Error adding undertrial prisoner: {str(e)}"}), 500
# Read operation for Undertrial_prisoner table
@app.route('/get_undertrial_prisoner/<int:prisoner_id>', methods=['GET'])
def get_undertrial_prisoner_by_id_endpoint(prisoner_id):
    try:
        cursor = db_manager.conn.cursor()
        cursor.execute("SELECT * FROM Undertrial_prisoner WHERE Id = ?", (prisoner_id,))
        data = cursor.fetchone()
        cursor.close()
        if data:
            return jsonify({"undertrial_prisoner": data})
        else:
            return jsonify({"message": "Undertrial prisoner not found"}), 404
    except pyodbc.Error as e:
        return jsonify({"error": f"Error querying Undertrial prisoner: {str(e)}"}), 500

# Update operation for Undertrial_prisoner table
@app.route('/update_undertrial_prisoner/<int:prisoner_id>', methods=['PUT'])
def update_undertrial_prisoner_endpoint(prisoner_id):
    try:
        data = request.json
        name = data['name']
        username = data['username']
        password = data['password']

        cursor = db_manager.conn.cursor()
        cursor.execute("UPDATE Undertrial_prisoner SET Name = ?, Username = ?, password = ? WHERE Id = ?", (name, username, password, prisoner_id))
        db_manager.conn.commit()
        cursor.close()
        return jsonify({"message": "Undertrial prisoner updated successfully"})
    except pyodbc.Error as e:
        return jsonify({"error": f"Error updating Undertrial prisoner: {str(e)}"}), 500

# Delete operation for Undertrial_prisoner table
@app.route('/delete_undertrial_prisoner/<int:prisoner_id>', methods=['DELETE'])
def delete_undertrial_prisoner_endpoint(prisoner_id):
    try:
        cursor = db_manager.conn.cursor()
        cursor.execute("DELETE FROM Undertrial_prisoner WHERE Id = ?", (prisoner_id,))
        db_manager.conn.commit()
        cursor.close()
        return jsonify({"message": "Undertrial prisoner deleted successfully"})
    except pyodbc.Error as e:
        return jsonify({"error": f"Error deleting Undertrial prisoner: {str(e)}"}), 500

# Create operation for Legal_aid table
@app.route('/create_legal_aid', methods=['POST'])
def create_legal_aid_endpoint():
    try:
        data = request.json
        name = data['name']
        govt_id = data['govt_id']
        phone_no = data['phone_no']
        select_role = data['select_role']

        cursor = db_manager.conn.cursor()
        cursor.execute("INSERT INTO Legal_aid (Name, Govt_id, Phone_no, select_role) VALUES (?, ?, ?, ?)",
                       (name, govt_id, phone_no, select_role))
        db_manager.conn.commit()
        cursor.close()
        return jsonify({"message": "Legal aid created successfully"})
    except pyodbc.Error as e:
        return jsonify({"error": f"Error creating Legal aid: {str(e)}"}), 500

# Read operation for Legal_aid table
@app.route('/get_legal_aid/<int:legal_aid_id>', methods=['GET'])
def get_legal_aid_by_id_endpoint(legal_aid_id):
    try:
        cursor = db_manager.conn.cursor()
        cursor.execute("SELECT * FROM Legal_aid WHERE Id = ?", (legal_aid_id,))
        data = cursor.fetchone()
        cursor.close()
        if data:
            return jsonify({"legal_aid": data})
        else:
            return jsonify({"message": "Legal aid not found"}), 404
    except pyodbc.Error as e:
        return jsonify({"error": f"Error querying Legal aid: {str(e)}"}), 500

# Update operation for Legal_aid table
@app.route('/update_legal_aid/<int:legal_aid_id>', methods=['PUT'])
def update_legal_aid_endpoint(legal_aid_id):
    try:
        data = request.json
        name = data['name']
        govt_id = data['govt_id']
        phone_no = data['phone_no']
        select_role = data['select_role']

        cursor = db_manager.conn.cursor()
        cursor.execute("UPDATE Legal_aid SET Name = ?, Govt_id = ?, Phone_no = ?, select_role = ? WHERE Id = ?",
                       (name, govt_id, phone_no, select_role, legal_aid_id))
        db_manager.conn.commit()
        cursor.close()
        return jsonify({"message": "Legal aid updated successfully"})
    except pyodbc.Error as e:
        return jsonify({"error": f"Error updating Legal aid: {str(e)}"}), 500

# Delete operation for Legal_aid table
@app.route('/delete_legal_aid/<int:legal_aid_id>', methods=['DELETE'])
def delete_legal_aid_endpoint(legal_aid_id):
    try:
        cursor = db_manager.conn.cursor()
        cursor.execute("DELETE FROM Legal_aid WHERE Id = ?", (legal_aid_id,))
        db_manager.conn.commit()
        cursor.close()
        return jsonify({"message": "Legal aid deleted successfully"})
    except pyodbc.Error as e:
        return jsonify({"error": f"Error deleting Legal aid: {str(e)}"}), 500

# Create operation for Prison_authority table
@app.route('/create_prison_authority', methods=['POST'])
def create_prison_authority_endpoint():
    try:
        data = request.json
        name = data['name']
        govt_id = data['govt_id']
        phone_no = data['phone_no']
        select_role = data['select_role']

        cursor = db_manager.conn.cursor()
        cursor.execute("INSERT INTO Prison_authority (Name, Govt_id, Phone_no, select_role) VALUES (?, ?, ?, ?)",
                       (name, govt_id, phone_no, select_role))
        db_manager.conn.commit()
        cursor.close()
        return jsonify({"message": "Prison authority created successfully"})
    except pyodbc.Error as e:
        return jsonify({"error": f"Error creating Prison authority: {str(e)}"}), 500

# Read operation for Prison_authority table
@app.route('/get_prison_authority/<int:prison_authority_id>', methods=['GET'])
def get_prison_authority_by_id_endpoint(prison_authority_id):
    try:
        cursor = db_manager.conn.cursor()
        cursor.execute("SELECT * FROM Prison_authority WHERE Id = ?", (prison_authority_id,))
        data = cursor.fetchone()
        cursor.close()
        if data:
            return jsonify({"prison_authority": data})
        else:
            return jsonify({"message": "Prison authority not found"}), 404
    except pyodbc.Error as e:
        return jsonify({"error": f"Error querying Prison authority: {str(e)}"}), 500

# Update operation for Prison_authority table
@app.route('/update_prison_authority/<int:prison_authority_id>', methods=['PUT'])
def update_prison_authority_endpoint(prison_authority_id):
    try:
        data = request.json
        name = data['name']
        govt_id = data['govt_id']
        phone_no = data['phone_no']
        select_role = data['select_role']

        cursor = db_manager.conn.cursor()
        cursor.execute("UPDATE Prison_authority SET Name = ?, Govt_id = ?, Phone_no = ?, select_role = ? WHERE Id = ?",
                       (name, govt_id, phone_no, select_role, prison_authority_id))
        db_manager.conn.commit()
        cursor.close()
        return jsonify({"message": "Prison authority updated successfully"})
    except pyodbc.Error as e:
        return jsonify({"error": f"Error updating Prison authority: {str(e)}"}), 500

# Delete operation for Prison_authority table
@app.route('/delete_prison_authority/<int:prison_authority_id>', methods=['DELETE'])
def delete_prison_authority_endpoint(prison_authority_id):
    try:
        cursor = db_manager.conn.cursor()
        cursor.execute("DELETE FROM Prison_authority WHERE Id = ?", (prison_authority_id,))
        db_manager.conn.commit()
        cursor.close()
        return jsonify({"message": "Prison authority deleted successfully"})
    except pyodbc.Error as e:
        return jsonify({"error": f"Error deleting Prison authority: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(debug=True)