from sqlalchemy import Column,Integer,String, Boolean,Date
from database import Base 

class CategoryModel(Base) :
    __tablename__ = "category_category"
    __table_args__ = {'extend_existing': True} # 

    id	= Column("id",Integer,primary_key=True, index=True)
    name	= Column("name",String(150))
    description	= Column("description",String(-1))
    status	= Column("status",Boolean)
    created_at	= Column("created_at",Date)
    category_image = Column("category_image",String(100))