from goodlens_db.database import DataBase

class Keywords(DataBase):
  def __init__(self):
    super().__init__()
    self.keywords = self.db.keywords

  def get_keywords(self, offset=0, limit=500):
    query = {}

    try:
      r = self.keywords.find(query).skip(offset).limit(limit)
    except Exception as e:
      print(e)

    return list(r)
