import sqlite3

db_name = "logs.db"

def add(data):
    conn = sqlite3.connect('logs.db')
    c = conn.cursor()
    values = (data['request_time'], data['latency'], data['api_ip'], data['country'], data['city'],
              data['as'], data['lat'], data['lon'], data['duration'], data['distance'])
    c.execute("""INSERT INTO location_requests VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", values)
    conn.commit()
    conn.close()

def get_all():
    conn = sqlite3.connect('logs.db')
    c = conn.cursor()
    c.execute("SELECT * FROM location_requests")
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows

def get_all_json():
    data = get_all()
    if data:
        time_sum = 0
        for element in data:
            time_sum += float(element[1])
        time_avg = time_sum / len(data)
        html = "<div> Requests: {}, average response time: {} </div>".format(len(data), time_avg)

        html += "<table>"
        for i, element in enumerate(data):
            html += "<tr> <td>" + str(i) + "</td>"
            for j in range(10):
                html += "<td> " + element[j] + "</td>"
            
        html += "</table>"
        return html
    else:
        return "<div> No logs </div>"



def create():
    conn = sqlite3.connect('logs.db')
    c = conn.cursor()
    try:
        c.execute('''CREATE TABLE location_requests
                    (request_time text, api_ip text, latency text,
                    country text, city text, address text,
                    lat text, lon text, duration text, distance text)''')
        conn.commit()
    except sqlite3.OperationalError:
        pass
    conn.close()

if __name__ == "__main__":
    create()