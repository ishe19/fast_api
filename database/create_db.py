import db

print("creating database!")

db.Base.metadata.create_all(db.engine)
