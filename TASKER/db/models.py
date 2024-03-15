from sqlalchemy.orm import Mapped, mapped_column, declarative_base
from sqlalchemy import BigInteger, func, VARCHAR, DateTime
from pydantic import field_validator
from datetime import datetime, timezone
from TASKER.api.schemas.users import Role

Base = declarative_base()


class UserDB(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(VARCHAR, unique=True, index=True)
    password: Mapped[str]
    online: Mapped[bool] = mapped_column(default=False)
    last_seen: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=func.now())
    role: Mapped[Role] = mapped_column(default=Role.user)

    @field_validator('last_seen')
    def set_online_status(cls, v):
        v = True
        cls.last_seen = datetime.now(timezone.utc)
        return v
