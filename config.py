
from pyrogram import filters
import os

class Config:
    API_ID = "23812672"
    API_HASH = "297d47a5510f124e7f58387c0682e7ef"
    TOKEN = "8359190940:AAG8GJZzpDMhls3mjkzaYH3XLpWrUP3pn_k"
    TOKEN = os.environ.get("TOKEN", None)
    MONGO_URL = "mongodb+srv://balloonflame7:jatin@#0212@cluster0.7hal6uy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    START_PIC = "https://files.catbox.moe/pvj6h7.mp4"
    SUDOERS = filters.user(["8143754205"])
