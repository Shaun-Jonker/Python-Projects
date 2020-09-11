import sqlite3

conn = sqlite3.connect('org_count.sqlite')

cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = 'org.txt'

fh = open(fname)

for line in fh:
    if not line.startswith('From '): continue
    line_list = line.split()
    email = line_list[1]
    org = email.split('@')
    org = org[1]
    print(org)
    cur.execute('SELECT count FROM Counts WHERE org=?', (org,))
    row = cur.fetchone()
    print(row)
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org=?', (org,))

    conn.commit()