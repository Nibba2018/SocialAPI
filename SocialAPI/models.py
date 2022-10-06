from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP

from SocialAPI.db import Base


class Post(Base):
    __tablename__ = "Posts"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, default=datetime.now)

