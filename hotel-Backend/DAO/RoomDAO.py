import uuid

import pymysql
import json
from dbconfig import mysql
from flask import jsonify


class RoomDAO:

    @classmethod
    def checkRoomWithGivenID(cls, room_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute("SELECT * from room where room_id=%s",
                           room_id)
            rows = cursor.fetchone()
            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def checkRoomWithNumber(cls, room_number):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute("SELECT * from room where room_number=%s",
                           room_number)
            rows = cursor.fetchone()
            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def adminCheckFromSessionID(cls, session_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute("SELECT * from admin where session_id=%s",
                           session_id)
            rows = cursor.fetchone()
            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def adminLogin(cls, admin_id, password):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute("SELECT * from admin where admin_id = %s and password= %s",
                           (admin_id, password))
            rows = cursor.fetchone()
            if rows is not None:
                sessionId = str(uuid.uuid4())
                cursor.execute("update admin set session_id = %s where admin_id = %s",
                               (sessionId, admin_id))
                conn.commit()

                cursor.execute("SELECT * from admin where admin_id = %s and password= %s",
                               (admin_id, password))
                rows = cursor.fetchone()
                return rows
            else:
                return None
        except Exception as e:

            print(e)
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def getAllRooms(cls):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute("SELECT * from room where availibility='yes'")
            rows = cursor.fetchall()
            return rows
        except Exception as e:

            print(e)
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def getAllRoomsForAdmin(cls):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute("SELECT room_id,room_number,price,Average_Rating,availibility,facilities from room")
            rows = cursor.fetchall()
            return rows
        except Exception as e:

            print(e)
        finally:
            cursor.close()
            conn.close()


    @classmethod
    def addNewRoom(cls, room_number, price, Average_Rating, facilities,image):
        try:
            roomId = str(uuid.uuid4())
            isAvailable = 'Yes'
            EuroPrice = '€'
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute(
                "insert into room(room_id, room_number,price,Average_Rating,availibility,facilities,image) value (%s, %s, %s,%s, %s,%s,%s)",
                (roomId, room_number, price + EuroPrice, Average_Rating, isAvailable, facilities,image))
            conn.commit()
            cursor.execute("SELECT * from room r WHERE r.room_id = %s",
                           roomId)
            rows = cursor.fetchone()
            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()


    @classmethod
    def deleteRoomFromDB(cls, room_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute("DELETE from room where room_id=%s", room_id)
            conn.commit()
            cursor.execute("SELECT * from room")
            rows = cursor.fetchall()
            return rows
        except Exception as e:

            print(e)
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def checkRoomIsAvailable(cls, room_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute("SELECT * from room where availibility='Yes' and room_id=%s",
                           room_id)
            row = cursor.fetchone()
            return row
        except Exception as e:

            print(e)
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def adminLogoutDAO(cls, admin_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute("update admin set session_id = null where admin_id = %s",
                           admin_id)
            conn.commit()

            cursor.execute("SELECT * from admin where admin_id = %s",
                           admin_id)
            row = cursor.fetchone()
            return row
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()


    @classmethod
    def getCurrentRoomData(cls, room_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute("SELECT * from room where room_id=%s",
                           room_id)
            row = cursor.fetchone()
            return row
        except Exception as e:

            print(e)
        finally:
            cursor.close()
            conn.close()


    @classmethod
    def changeStatusToNo(cls, room_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute("UPDATE room set availibility = 'No' where room_id=%s",
                           room_id)
            conn.commit()
            cursor.execute("select * from room where room_id=%s",
                           room_id)
            row = cursor.fetchone()
            return row
        except Exception as e:

            print(e)
        finally:
            cursor.close()
            conn.close()


    @classmethod
    def changeStatusToYes(cls, room_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute("UPDATE room set availibility = 'Yes' where room_id=%r",
                           room_id)
            conn.commit()
            cursor.execute("select * from room where room_id=%s",
                           room_id)
            row = cursor.fetchone()
            return row
        except Exception as e:

            print(e)
        finally:
            cursor.close()
            conn.close()


    @classmethod
    def getAllImages(cls):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("select image from room")
            row = cursor.fetchall()
            print(row)
            return row
        except Exception as e:

            print(e)
        finally:
            cursor.close()


    @classmethod
    def addRoomFromtheForm(cls, image_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("insert into imagesTest(image_id) value(%s)",
                           image_id)
            conn.commit()
            cursor.execute("select * from imagesTest where image_id=%s",
                            image_id)
            row = cursor.fetchone()
            return row
        except Exception as e:

            print(e)
        finally:
            cursor.close()
            conn.close()