import uuid

import pymysql
import json
from dbconfig import mysql
from flask import jsonify

class BookingDAO:

    @classmethod
    def addRoomBooking(cls, customer_id, room_id,email):
        try:
            bookingId = str(uuid.uuid4())
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute(
                "insert into booking (booking_id, customer_id,room_id,email) value (%s, %s, %s,%s)",
                (bookingId, customer_id, room_id,email))
            conn.commit()
            cursor.execute("UPDATE room set availibility='No' where room_id=%s ",
                           room_id)
            conn.commit()
            cursor.execute("SELECT * from booking r WHERE r.booking_id = %s",
                           bookingId)
            rows = cursor.fetchone()
            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def contactUS(cls, customer_id, username,description):
        try:
            incidentId = str(uuid.uuid4())
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute(
                "insert into incident(incident_id,customer_id, username,description) value (%s,%s, %s, %s)",
                (incidentId,customer_id, username,description))
            conn.commit()

            cursor.execute("SELECT * from incident WHERE incident_id = %s",
                           incidentId)
            rows = cursor.fetchone()
            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()