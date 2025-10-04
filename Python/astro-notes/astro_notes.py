#!/usr/bin/env python3
"""
Astro-Notes: tiny CLI notes with tags stored in SQLite.
One-PR: add a sample note or a helper function.
"""
import sqlite3, sys, os
DB = os.path.expanduser("~/.astronotes.db")

def get_conn():
    c = sqlite3.connect(DB)
    c.execute("CREATE TABLE IF NOT EXISTS notes(id INTEGER PRIMARY KEY, body TEXT, tags TEXT, created TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
    c.commit()
    return c

def add(body, tags=""):
    c = get_conn()
    c.execute("INSERT INTO notes(body, tags) VALUES(?,?)", (body, tags))
    c.commit()
    print("Added note.")

def list_notes(tag=None):
    c = get_conn()
    if tag:
        q = f"SELECT id,body,tags,created FROM notes WHERE tags LIKE ? ORDER BY created DESC"
        rows = c.execute(q, (f"%{tag}%",)).fetchall()
    else:
        rows = c.execute("SELECT id,body,tags,created FROM notes ORDER BY created DESC").fetchall()
    for r in rows:
        print(f"[{r[0]}] {r[3]} | tags:{r[2]}\n  {r[1]}\n")

def delete(id):
    c = get_conn()
    c.execute("DELETE FROM notes WHERE id=?", (id,))
    c.commit()
    print("Deleted.", id)

def help_msg():
    print("Usage: astro-notes add \"note body\" tag1,tag2")
    print("       astro-notes list [tag]")
    print("       astro-notes delete <id>")

def main(argv):
    if len(argv)<2:
        help_msg(); return
    cmd = argv[1]
    if cmd=="add" and len(argv)>=3:
        body = argv[2]
        tags = argv[3] if len(argv)>3 else ""
        add(body,tags)
    elif cmd=="list":
        tag = argv[2] if len(argv)>2 else None
        list_notes(tag)
    elif cmd=="delete" and len(argv)>2:
        delete(argv[2])
    else:
        help_msg()

if __name__=="__main__":
    main(sys.argv)
