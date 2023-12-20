from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from typing import Any
import mysql.connector
from mysql.connector import errorcode
import uuid
from datetime import datetime, timedelta
from urllib.parse import urlparse, parse_qs
import matplotlib.pyplot as plt
import numpy as np
import io
import base64
import pandas as pd
import matplotlib.dates as mdates

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
                    query_count += (
                        ") AND forms.last_updated BETWEEN '"
                        ""
                        + query_params["year"][0]
                        + """-01-01 00:00:00' AND '"""
                        + query_params["year"][0]
                        + """-12-31 00:00:00'
                        GROUP BY forms.answer_id"""
                    )
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
                fig, ax = plt.subplots(layout="constrained")
                rects1 = ax.bar(
                    x - width,
                    [expenses_7[0], expenses_8[0], expenses_9[0], expenses_10[0]],
                    width,
                    label=label_answer[0],
                )
                rects2 = ax.bar(
                    x,
                    [expenses_7[1], expenses_8[1], expenses_9[1], expenses_10[1]],
                    width,
                    label=label_answer[1],
                )
                rects3 = ax.bar(
                    x + width,
                    [expenses_7[2], expenses_8[2], expenses_9[2], expenses_10[2]],
                    width,
                    label=label_answer[2],
                )
                rects4 = ax.bar(
                    x + 2 * width,
                    [expenses_7[3], expenses_8[3], expenses_9[3], expenses_10[3]],
                    width,
                    label=label_answer[3],
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
                plt.savefig(buffer, format="png", dpi=300, bbox_inches="tight")
                buffer.seek(0)

                # Convert the buffer to a Base64 string
                base64_image = base64.b64encode(buffer.read()).decode("utf-8")
                self._send_response(
                    200, {"data": "data:image/png;base64," + base64_image}
                )
                plt.clf()
            elif query_params["id"][0] == "2":
                cursor = cnx.cursor()
                data_label_answer = cursor.execute(
                    """SELECT answers.answer FROM `answers`
                            WHERE answers.question_id = 7"""
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
                line_7 = [0, 0, 0, 0]
                line_8 = [0, 0, 0, 0]
                line_9 = [0, 0, 0, 0]
                line_10 = [0, 0, 0, 0]
                for i in res_data_x:
                    cursor.execute(
                        """SELECT * FROM `forms` WHERE forms.answer_id = """ + str(i[1])
                    )
                    session_gr = cursor.fetchall()
                    query_count = """SELECT *, COUNT(forms.answer_id) FROM `forms` WHERE forms.answer_id BETWEEN 24 AND 27 AND ("""
                    for j in session_gr:
                        if session_gr.index(j) == 0:
                            query_count += " forms.session_id = '" + j[0] + "'"
                        else:
                            query_count += " OR forms.session_id = '" + j[0] + "'"
                    query_count += (
                        ") AND forms.last_updated BETWEEN '"
                        ""
                        + query_params["year"][0]
                        + """-01-01 00:00:00' AND '"""
                        + query_params["year"][0]
                        + """-12-31 00:00:00'
                        GROUP BY forms.answer_id"""
                    )
                    cursor.execute(query_count)
                    count_gr = cursor.fetchall()
                    for j in count_gr:
                        if i[1] == 44:
                            line_7[j[1] - 24] += j[3]
                        if i[1] == 45:
                            line_8[j[1] - 24] += j[3]
                        if i[1] == 46:
                            line_9[j[1] - 24] += j[3]
                        if i[1] == 47:
                            line_10[j[1] - 24] += j[3]
                x = np.arange(len(label_x) if len(label_x) >= 4 else 4)
                y_data = np.array(
                    [
                        np.array([line_7[0], line_8[0], line_9[0], line_10[0]]),
                        np.array([line_7[1], line_8[1], line_9[1], line_10[1]]),
                        np.array([line_7[2], line_8[2], line_9[2], line_10[2]]),
                        np.array([line_7[3], line_8[3], line_9[3], line_10[3]]),
                    ]
                )

                for i in range(len(label_answer)):
                    plt.plot(x, y_data[i], label=label_answer[i])

                # Add labels and title
                plt.ylabel("Số lượng")
                plt.xticks(x, label_x)
                plt.title("Mức tiết kiệm")

                # Add legend
                plt.legend()
                plt.ylim(
                    -1,
                    max(
                        [
                            max(line_7),
                            max(line_8),
                            max(line_9),
                            max(line_10),
                        ]
                    )
                    + 3,
                )

                # Save the figure to a BytesIO buffer
                buffer = io.BytesIO()
                plt.savefig(buffer, format="png", dpi=300, bbox_inches="tight")
                buffer.seek(0)

                # Convert the buffer to a Base64 string
                base64_image = base64.b64encode(buffer.read()).decode("utf-8")
                self._send_response(
                    200, {"data": "data:image/png;base64," + base64_image}
                )
                plt.clf()
            elif query_params["id"][0] == "3":
                cursor = cnx.cursor()
                data_label_answer = cursor.execute(
                    """SELECT answers.answer FROM `answers`
                            WHERE answers.question_id = 1"""
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
                pie_1 = [0, 0, 0]
                cursor.execute(
                    """SELECT * FROM `forms` WHERE forms.answer_id = """
                    + query_params["typesvid"][0]
                )
                session_gr = cursor.fetchall()
                query_count = """SELECT *, COUNT(forms.answer_id) FROM `forms` WHERE forms.answer_id BETWEEN 1 AND 3 AND ("""
                for j in session_gr:
                    if session_gr.index(j) == 0:
                        query_count += " forms.session_id = '" + j[0] + "'"
                    else:
                        query_count += " OR forms.session_id = '" + j[0] + "'"
                query_count += ") GROUP BY forms.answer_id"

                cursor.execute(query_count)
                count_gr = cursor.fetchall()
                for j in count_gr:
                    pie_1[j[1] - 1] += j[3]
                plt.subplot(1, 2, 1)
                plt.subplots(figsize=(4, 4))
                plt.pie(
                    pie_1,
                    autopct="%1.1f%%",
                    startangle=90,
                    colors=["lightblue", "lightgreen", "lightcoral"],
                )
                plt.title(label_x[int(query_params["typesvid"][0]) - 44])

                plt.tight_layout()

                # Add legend
                plt.legend(
                    loc="lower center", bbox_to_anchor=(0.5, -0.2), labels=label_answer
                )

                # Save the figure to a BytesIO buffer
                buffer = io.BytesIO()
                plt.savefig(buffer, format="png", dpi=300, bbox_inches="tight")
                buffer.seek(0)

                # Convert the buffer to a Base64 string
                base64_image = base64.b64encode(buffer.read()).decode("utf-8")
                self._send_response(
                    200, {"data": "data:image/png;base64," + base64_image}
                )
                plt.clf()
            elif query_params["id"][0] == "5":
                cursor = cnx.cursor()
                data_answer = cursor.execute(
                    """SELECT *, COUNT(forms.answer_id) FROM `forms` JOIN answers 
                        WHERE forms.answer_id = answers.id 
                        AND answers.question_id != 12 AND answers.id BETWEEN 1 AND 3 
                        AND forms.last_updated BETWEEN '"""
                    + query_params["year"][0]
                    + """-01-01 00:00:00' AND '"""
                    + query_params["year"][0]
                    + """-12-31 00:00:00'
                        GROUP BY forms.answer_id"""
                )
                res_data_answer = cursor.fetchall()
                pie_1 = [t[7] for t in res_data_answer]
                plt.subplot(1, 2, 1)
                plt.subplots(figsize=(4, 4))
                plt.pie(
                    pie_1,
                    autopct="%1.1f%%",
                    startangle=90,
                    colors=["lightblue", "lightgreen", "lightcoral"],
                )
                plt.title("From where do you derive your income?")

                plt.tight_layout()

                # Add legend
                plt.legend(
                    loc="lower center",
                    bbox_to_anchor=(0.5, -0.2),
                    labels=[t[4] for t in res_data_answer],
                )

                # Save the figure to a BytesIO buffer
                buffer = io.BytesIO()
                plt.savefig(buffer, format="png", dpi=300, bbox_inches="tight")
                buffer.seek(0)

                # Convert the buffer to a Base64 string
                base64_image = base64.b64encode(buffer.read()).decode("utf-8")
                self._send_response(
                    200, {"data": "data:image/png;base64," + base64_image}
                )
                plt.clf()
            elif query_params["id"][0] == "4":
                cursor = cnx.cursor()
                cursor.execute(
                    """SELECT * FROM `questions`
                            WHERE questions.id != 12"""
                )
                data_questions = cursor.fetchall()
                data_response_api = {}
                for ques in data_questions:
                    data_label_answer = cursor.execute(
                        """SELECT answers.answer FROM `answers`
                                WHERE answers.question_id = """
                        + str(ques[0])
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
                    pie_1 = [0 for t in range(0, len(res_data_label_answer))]
                    cursor.execute(
                        """SELECT * FROM `forms` WHERE forms.answer_id = """
                        + query_params["typesvid"][0]
                    )
                    session_gr = cursor.fetchall()
                    query_count = (
                        """SELECT *, COUNT(forms.answer_id) FROM `forms` JOIN answers WHERE forms.answer_id = answers.id AND answers.question_id ="""
                        + str(ques[0])
                        + """ AND ("""
                    )
                    for j in session_gr:
                        if session_gr.index(j) == 0:
                            query_count += " forms.session_id = '" + j[0] + "'"
                        else:
                            query_count += " OR forms.session_id = '" + j[0] + "'"
                    query_count += ") GROUP BY forms.answer_id"
                    cursor.execute(query_count)

                    count_gr = cursor.fetchall()
                    cursor.execute(
                        """SELECT MIN(answers.id) AS min FROM answers WHERE answers.question_id = """
                        + str(ques[0])
                    )
                    min_answer = cursor.fetchall()[0][0]
                    for j in count_gr:
                        pie_1[j[1] - min_answer] += j[3]
                    plt.subplots(figsize=(2, 2))
                    plt.pie(
                        pie_1,
                        autopct="%1.1f%%",
                        startangle=90,
                        colors=["lightblue", "lightgreen", "lightcoral", "lightcyan"],
                    )

                    plt.tight_layout()

                    # Add legend
                    plt.legend(
                        loc="lower center",
                        bbox_to_anchor=(0.5, -0.5),
                        labels=label_answer,
                    )

                    # Save the figure to a BytesIO buffer
                    buffer = io.BytesIO()
                    plt.savefig(buffer, format="png", dpi=300, bbox_inches="tight")
                    buffer.seek(0)

                    # Convert the buffer to a Base64 string
                    base64_image = base64.b64encode(buffer.read()).decode("utf-8")
                    data_response_api[ques[1]] = "data:image/png;base64," + base64_image
                    plt.clf()
                self._send_response(200, data_response_api)
            elif query_params["id"][0] == "6":
                cursor = cnx.cursor()
                label_answer = cursor.execute(
                    """SELECT * FROM answers 
                        WHERE answers.question_id = """
                    + query_params["question"][0]
                )
                res_label_answer = cursor.fetchall()
                value_y = {}
                times = []
                for i in res_label_answer:
                    value_y[i[1]] = [0]
                cursor.execute(
                    """SELECT * FROM `forms` WHERE forms.answer_id = """
                    + query_params["typesvid"][0]
                )
                session_gr = cursor.fetchall()
                query_count = (
                    """SELECT * FROM `forms` JOIN answers 
                        WHERE forms.answer_id = answers.id 
                        AND answers.question_id = """
                    + query_params["question"][0] +
                    """ AND forms.last_updated BETWEEN '"""
                    + query_params["fromyear"][0]
                    + """-01-01 00:00:00' AND '"""
                    + query_params["toyear"][0]
                    + """-12-31 00:00:00'""" + """ AND ("""
                )
                for j in session_gr:
                    if session_gr.index(j) == 0:
                        query_count += " forms.session_id = '" + j[0] + "'"
                    else:
                        query_count += " OR forms.session_id = '" + j[0] + "'"
                query_count = query_count + ")"
                data_answer = cursor.execute(query_count)
                res_data_answer = cursor.fetchall()
                times_series = pd.DataFrame()
                times_series = pd.DataFrame({
                    "date" : [t[2] for t in res_data_answer],
                    "data" : [t for t in res_data_answer]
                })
                times_series = times_series.sort_values(by='date').reset_index(drop=True)
                result = times_series.groupby(times_series['date'].dt.isocalendar().week).apply(lambda x: x[['date', 'data']].to_dict(orient='records')).to_dict()
                for j in result:
                    times.append(min(pd.to_datetime(times_series['date'])) - timedelta(days=30) if len(times) == 0 else times[-1] + timedelta(days=7))
                    for i in result[j]:
                        value_y[i["data"][4]][len(value_y[i["data"][4]]) - 1] += 1
                    for key, value in value_y.items():
                        value_y[key].append(0)
                for key, value in value_y.items():
                        value_y[key] = value_y[key][:-1]
                plt.figure(figsize=(10, 6))
                colors = ['r', 'g', 'b', 'y']
                for i in res_label_answer:
                    plt.plot(times, value_y[i[1]], marker='o', linestyle='-', color=colors[res_label_answer.index(i)])

                # Format the x-axis as dates
                plt.xticks(times, rotation=45, ha="right")
                plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
                plt.gca().xaxis.set_major_locator(mdates.YearLocator())

                # Add labels and title
                plt.xlabel('Date')
                plt.ylabel('Values')
                cursor.execute(
                    """SELECT * FROM `questions`
                            WHERE questions.id =""" + query_params["question"][0]
                )
                title_db = cursor.fetchall()
                title = str(title_db[0][0]) + ', ' + title_db[0][1]
                plt.title(title)

                # Rotate x-axis labels for better readability
                plt.gcf().autofmt_xdate()
                plt.legend(labels=[t[1] for t in res_label_answer], 
                    loc="lower center",
                    bbox_to_anchor=(0.5, -0.5))

                # Save the figure to a BytesIO buffer
                buffer = io.BytesIO()
                plt.savefig(buffer, format="png", dpi=300, bbox_inches="tight")
                buffer.seek(0)

                # Convert the buffer to a Base64 string
                base64_image = base64.b64encode(buffer.read()).decode("utf-8")
                self._send_response(
                    200, {"data": "data:image/png;base64," + base64_image}
                )
                plt.clf()
            elif query_params["id"][0] == "7":
                cursor = cnx.cursor()
                cursor.execute(
                    """SELECT * FROM `forms` WHERE forms.answer_id = """
                    + query_params["typesvid"][0]
                )
                session_gr = cursor.fetchall()
                query_count = (
                    """SELECT *, COUNT(forms.answer_id) FROM `forms` JOIN answers WHERE forms.answer_id = answers.id AND answers.question_id ="""
                    + query_params["question"][0]
                    + """ AND ("""
                )
                for j in session_gr:
                    if session_gr.index(j) == 0:
                        query_count += " forms.session_id = '" + j[0] + "'"
                    else:
                        query_count += " OR forms.session_id = '" + j[0] + "'"
                query_count = query_count + ") " + """ AND forms.last_updated BETWEEN '""" + query_params["fromyear"][0] + """-01-01 00:00:00' AND '""" + query_params["toyear"][0] + """-12-31 00:00:00' GROUP BY forms.answer_id"""
                cursor.execute(query_count)

                res_data_answer = cursor.fetchall()
                pie_1 = [t[7] for t in res_data_answer]
                plt.subplot(1, 2, 1)
                plt.subplots(figsize=(4, 4))
                plt.pie(
                    pie_1,
                    autopct="%1.1f%%",
                    startangle=90,
                    colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'],
                )
                cursor.execute(
                    """SELECT * FROM `questions`
                            WHERE questions.id =""" + query_params["question"][0]
                )
                title_db = cursor.fetchall()
                title = str(title_db[0][0]) + ', ' + title_db[0][1]
                plt.title(title[0:30] + '...?')

                plt.tight_layout()

                # Add legend
                plt.legend(
                    loc="lower center",
                    bbox_to_anchor=(0.5, -0.2),
                    labels=[(t[4][0:30] + ('...?' if len(t[4])>31 else '?')) for t in res_data_answer],
                )

                # Save the figure to a BytesIO buffer
                buffer = io.BytesIO()
                plt.savefig(buffer, format="png", dpi=300, bbox_inches="tight")
                buffer.seek(0)

                # Convert the buffer to a Base64 string
                base64_image = base64.b64encode(buffer.read()).decode("utf-8")
                self._send_response(
                    200, {"data": "data:image/png;base64," + base64_image}
                )
                plt.clf()
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
