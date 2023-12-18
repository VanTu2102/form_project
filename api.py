from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from typing import Any
import mysql.connector
from mysql.connector import errorcode
import uuid
from datetime import datetime
from urllib.parse import urlparse, parse_qs
import matplotlib.pyplot as plt
import numpy as np
import io
import base64

config = {
    "user": "root",
    "password": "",
    "host": "127.0.0.1",
    "database": "form_project_db",
    "raise_on_warnings": True,
}
cnx = mysql.connector.connect(**config)
if cnx.is_connected():
    print("Connected to MySQL server")

    # Create a cursor object
    cursor = cnx.cursor()

    # Replace 'parts' and column definitions according to your requirements
    # create_table_query = '''
    #     CREATE TABLE IF NOT EXISTS parts (
    #         id INT AUTO_INCREMENT PRIMARY KEY,
    #         part TEXT NOT NULL
    #     )
    # '''
    # # Execute the CREATE TABLE query
    # cursor.execute(create_table_query)

    # print('Table parts created successfully')

    # # Replace 'questions' and column definitions according to your requirements
    # create_table_query = '''
    #     CREATE TABLE IF NOT EXISTS questions (
    #         id INT AUTO_INCREMENT PRIMARY KEY,
    #         question TEXT NOT NULL,
    #         part_id INT NOT NULL,
    #         FOREIGN KEY (part_id) REFERENCES parts(id)
    #     )
    # '''
    # # Execute the CREATE TABLE query
    # cursor.execute(create_table_query)

    # print('Table questions created successfully')

    # # Replace 'answers' and column definitions according to your requirements
    # create_table_query = '''
    #     CREATE TABLE IF NOT EXISTS answers (
    #         id INT PRIMARY KEY,
    #         answer TEXT NOT NULL,
    #         question_id INT NOT NULL,
    #         value INT NOT NULL,
    #         FOREIGN KEY (question_id) REFERENCES questions(id)
    #     );
    # '''
    # # Execute the CREATE TABLE query
    # cursor.execute(create_table_query)

    # print('Table answers created successfully')

    # # Replace 'forms' and column definitions according to your requirements
    # create_table_query = '''
    #     CREATE TABLE IF NOT EXISTS forms (
    #         session_id TEXT NOT NULL,
    #         answer_id INT NOT NULL,
    #         last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    #         FOREIGN KEY (answer_id) REFERENCES answers(id)
    #     );
    # '''
    # # Execute the CREATE TABLE query
    # cursor.execute(create_table_query)

    # print('Table forms created successfully')

    # insert_data_query = '''
    #     INSERT INTO parts (id, part) VALUES
    #       (1, 'Income Sources'),
    #       (2, 'Budget Allocation - Spending'),
    #       (3, 'Savings – Tech – Crisis handling'),
    #       (4, 'Final question');
    #     INSERT INTO questions (id, part_id, question) VALUES
    #       (1, 1, 'From where do you derive your income'),
    #       (2, 2, 'Which of the following best describes your approach to budget allocation'),
    #       (3, 2, 'How do you prioritize spending your money'),
    #       (4, 2, 'What factors influence your budget decisions the most?'),
    #       (5, 2, 'How comfortable are you with differentiating between “wants” and “needs” in your budget?'),
    #       (6, 3, 'How do you describe your current saving habits?'),
    #       (7, 3, 'What percentage of your income do you typically allocate for your savings?'),
    #       (8, 3, 'What challenge do you face when it comes to saving money?'),
    #       (9, 3, 'Where do you usually keep your savings'),
    #       (10, 3, 'Do you have an emergency fund in place for unexpected expenses?'),
    #       (11, 3, 'How do you perceive the role of financial education in preparing for financial crises?'),
    #       (12, 4, 'Which year are you in?');
    #     INSERT INTO answers (id, question_id, answer, value) VALUES
    #       (1, 1, 'Family support', 1),
    #       (2, 1, 'Employed', 2),
    #       (3, 1, 'Employed and receive assistance from family as well', 3),
    #       (4, 2, 'Yes I have a well-defined plan for budget allocation', 1),
    #       (5, 2, 'I am still working on developing a strategy for budget allocation', 2),
    #       (6, 2, 'No, I currently don’t have a specific plan for budget allocation', 3),
    #       (7, 3, 'Essential needs like foods, rent, utilities …', 1),
    #       (8, 3, 'Entertainment and leisure activities', 2),
    #       (9, 3, 'Saving for the future', 3),
    #       (10, 3, 'I’m not sure', 4),
    #       (11, 4, 'Immediate needs', 1),
    #       (12, 4, 'Peer influence', 2),
    #       (13, 4, 'Long-term goals', 3),
    #       (15, 4, 'Random or impulsive purchases', 4),
    #       (16, 5, 'Very comfortable', 1),
    #       (17, 5, 'Somewhat comfortable', 2),
    #       (18, 5, 'Not very comfortable', 3),
    #       (19, 5, 'I struggle with this concept', 4),
    #       (20, 6, 'I consistently save a portion of my income', 1),
    #       (21, 6, 'I save occasionally when I have extra money', 2),
    #       (22, 6, 'I rarely save as I spend most of my income', 3),
    #       (23, 6, 'I don’t save at all', 4),
    #       (24, 7, '20% or more', 1),
    #       (25, 7, '10 – 20%', 2),
    #       (26, 7, 'Less than 10%', 3),
    #       (27, 7, 'I don’t allocate my income for savings', 4),
    #       (28, 8, 'Lack of income', 1),
    #       (29, 8, 'Impulse spending', 2),
    #       (30, 8, 'Lack of knowledge about saving options', 3),
    #       (31, 8, 'I don’t face any challenge', 4),
    #       (32, 9, 'Bank accounts', 1),
    #       (33, 9, 'E-wallet', 2),
    #       (34, 9, 'I keep my saving with me or hidden away', 3),
    #       (35, 9, 'Others (Specify)', 4),
    #       (36, 10, 'Yes I have a dedicated emergency fund', 1),
    #       (37, 10, 'I rely on credit cards or loan for emergencies', 2),
    #       (38, 10, 'I rely on family support to handle emergencies', 3),
    #       (39, 10, 'I don’t have a plan', 4),
    #       (40, 11, 'Extremely important', 1),
    #       (41, 11, 'Somewhat important', 2),
    #       (42, 11, 'Not very important', 3),
    #       (43, 11, 'I don’t see the relevance of financial	 education', 4),
    #       (44, 12, 'First year', 1),
    #       (45, 12, 'Second year', 2),
    #       (46, 12, 'Third year', 3),
    #       (47, 12, 'Fourth year+', 4);
    # '''
    # # Execute the INSERT TABLE query
    # cursor.execute(insert_data_query)

    # print('insert successfully')


class RequestHandler(BaseHTTPRequestHandler):
    def _send_response(self, status_code, data=None):
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

        if data:
            self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_GET(self):
        if self.path == "/api/dataquestion":
            cursor = cnx.cursor()
            data_parts = cursor.execute(
                """
              SELECT * FROM parts
            """
            )
            row_parts = cursor.fetchall()
            res = {}
            for row in row_parts:
                data_questions = cursor.execute(
                    """
                SELECT * FROM questions WHERE questions.part_id = """
                    + str(row[0])
                    + """
                """
                )
                row_questions = cursor.fetchall()
                question = {}
                for row_question in row_questions:
                    data_answers = cursor.execute(
                        """
                    SELECT * FROM answers WHERE answers.question_id = """
                        + str(row_question[0])
                        + """
                    """
                    )
                    row_answers = cursor.fetchall()
                    question[row_question[0]] = {
                        "question": row_question[1],
                        "answer": row_answers,
                    }
                res[row[0]] = {"part": row[1], "question": question}

            self._send_response(200, {"data": res})
        elif self.path == "/api/datasurvey":
            cursor = cnx.cursor()
            data = cursor.execute(
                """SELECT * FROM (
                        SELECT forms.session_id, forms.answer_id, forms.last_updated, answers.answer, answers.value, answers.question_id FROM forms JOIN
                        answers WHERE forms.answer_id = answers.id
                    ) AS fa
                    JOIN questions WHERE questions.id = fa.question_id
            """
            )
            res = cursor.fetchall()
            res_data = []
            for i in res:
                e = {
                    "id": i[1],
                    "session_id": i[0],
                    "question": i[7],
                    "answer": i[3],
                    "value": i[4],
                    "update_time": datetime.isoformat(i[2]),
                }
                res_data.append(e)
            self._send_response(200, {"data": res_data})
        elif self.path.find("/api/chartsurvey") >= 0:
            parsed_url = urlparse(self.path)
            query_params = parse_qs(parsed_url.query)
            if query_params["id"][0] == "1":
                cursor = cnx.cursor()
                data_label_answer = cursor.execute(
                    """SELECT answers.answer FROM `answers`
                            WHERE answers.question_id = 3"""
                )
                res_data_label_answer = cursor.fetchall()
                label_answer = [t[0] for t in res_data_label_answer]
                data_label_x = cursor.execute(
                    """SELECT answers.answer FROM `answers`
                            WHERE answers.question_id = 12"""
                )
                res_data_label_x = cursor.fetchall()
                label_x = [t[0] for t in res_data_label_x]
                data_x = cursor.execute(
                    """SELECT answers.answer, answers.id, COUNT(*) FROM `forms` JOIN answers
                            WHERE forms.answer_id = answers.id AND answers.question_id = 12
                            GROUP BY forms.answer_id"""
                )
                res_data_x = cursor.fetchall()
                expenses_7 = [0, 0, 0, 0]
                expenses_8 = [0, 0, 0, 0]
                expenses_9 = [0, 0, 0, 0]
                expenses_10 = [0, 0, 0, 0]
                for i in res_data_x:
                    cursor.execute(
                        """SELECT * FROM `forms` WHERE forms.answer_id = """ + str(i[1])
                    )
                    session_gr = cursor.fetchall()
                    query_count = """SELECT *, COUNT(forms.answer_id) FROM `forms` WHERE forms.answer_id BETWEEN 7 AND 10 AND ("""
                    for j in session_gr:
                        if session_gr.index(j) == 0:
                            query_count += " forms.session_id = '" + j[0] + "'"
                        else:
                            query_count += " OR forms.session_id = '" + j[0] + "'"
                    query_count += ") GROUP BY forms.answer_id"
                    cursor.execute(query_count)
                    count_gr = cursor.fetchall()
                    for j in count_gr:
                        if i[1] == 44:
                            expenses_7[j[1] - 7] += j[3]
                        if i[1] == 45:
                            expenses_8[j[1] - 7] += j[3]
                        if i[1] == 46:
                            expenses_9[j[1] - 7] += j[3]
                        if i[1] == 47:
                            expenses_10[j[1] - 7] += j[3]
                x = np.arange(len(label_x) if len(label_x) >= 4 else 4)

                # Độ rộng cột
                width = 0.2

                # Vẽ biểu đồ
                fig, ax = plt.subplots()
                rects1 = ax.bar(x - width, expenses_7, width, label=label_answer[0])
                rects2 = ax.bar(x, expenses_8, width, label=label_answer[1])
                rects3 = ax.bar(x + width, expenses_9, width, label=label_answer[2])
                rects4 = ax.bar(
                    x + 2 * width, expenses_10, width, label=label_answer[3]
                )

                # Thêm các thông tin khác cho biểu đồ
                ax.set_ylabel("Số lượng sinh viên")
                ax.set_title("Số lượng sinh viên mỗi năm theo từng tiêu chí tiêu tiền")
                ax.set_xticks(x)
                ax.set_xticklabels(label_x)
                ax.legend()
                plt.ylim(
                    0,
                    max(
                        [
                            max(expenses_7),
                            max(expenses_8),
                            max(expenses_9),
                            max(expenses_10),
                        ]
                    )
                    + 4,
                )
                # Save the figure to a BytesIO buffer
                buffer = io.BytesIO()
                plt.savefig(buffer, format="png")
                buffer.seek(0)

                # Convert the buffer to a Base64 string
                base64_image = base64.b64encode(buffer.read()).decode("utf-8")
                self._send_response(
                    200, {"data": "data:image/png;base64," + base64_image}
                )
        else:
            self._send_response(404, {"error": "Not Found"})

    def do_POST(self):
        if self.path == "/api/post_form":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length).decode("utf-8")
            json_data = json.loads(post_data)
            cursor = cnx.cursor()

            id = uuid.uuid4()

            insert_query = """
                INSERT INTO forms (session_id, answer_id)
                VALUES (%(session_id)s, %(answer_id)s)
            """

            for i in json_data["data"]:
                data_to_insert = {"session_id": str(id), "answer_id": i}
                cursor.execute(insert_query, data_to_insert)
            cnx.commit()

            self._send_response(200, {"message": "success", "id": str(id)})
        else:
            self._send_response(404, {"error": "Not Found"})


if __name__ == "__main__":
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print("Starting server on port 8000")
    httpd.serve_forever()
