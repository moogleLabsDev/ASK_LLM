from sqlalchemy import Column, Integer, String, Boolean, ForeignKey,JSON,Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class LlmTable(Base):
    __tablename__ = "llm_table"
    id = Column(Integer, primary_key=True)
    llm_type = Column(String(255), index=True)
    chat_histories = relationship("ChatHistory", back_populates="llm")

class Users(Base):
    __tablename__ = "users"  # Changed to lowercase for consistency
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, index=True)
    phone_number = Column(String(20),unique=True,index=True)
    name = Column(String(255), index=True)
    payment_type = Column(Integer, default=0)
    balance = Column(Integer, default=5)
    user_type = Column(Integer, default=0)  # 0,1
    is_active = Column(Integer)
    is_paid = Column(Boolean, default=False)
    mobile_type = Column(Integer, default=0)
    OTP_verification = Column(String(255))
    hashed_password = Column(String(255))
    llm_use = Column(JSON, default=list)
    transactions = relationship("Transaction", back_populates="owner")
    chat_histories = relationship("ChatHistory", back_populates="owner")

class Transaction(Base):
    __tablename__ = "transaction"
    id = Column(Integer, primary_key=True)
    title = Column(String(255), index=True)
    transaction_id = Column(String(255), index=True)
    payment_id = Column(String(255), index=True)
    user_id = Column(Integer, ForeignKey("users.id"))  # Corrected to lowercase
    owner = relationship("Users", back_populates="transactions")

class ChatHistory(Base):
    __tablename__ = "chat_history"
    id = Column(Integer, primary_key=True)
    in_msg = Column(Text)  # Changed to Text for long messages
    out_msg = Column(Text)  # Changed to Text for long messages
    llm_id = Column(Integer, ForeignKey("llm_table.id"))
    user_id = Column(Integer, ForeignKey("users.id"))  # Corrected to lowercase
    owner = relationship("Users", back_populates="chat_histories")
    llm = relationship("LlmTable", back_populates="chat_histories")
    
    
class BlacklistedToken(Base):
    __tablename__ = "blacklisted_tokens"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer,unique=True,index=True)

