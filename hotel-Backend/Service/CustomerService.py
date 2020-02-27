from wsgiref import headers

from flask import session, jsonify
from DAO.CustomerDAO import CustomerDAO
from Service.EmailService import EmailService
from Service.RoomService import RoomService


class CustomerService:
    customerDAO = CustomerDAO()
    emailService = EmailService()
    roomService = RoomService()

    @classmethod
    def getAllCustomers(cls):
        responseData = cls.customerDAO.getAllCustomersfromDB()
        return responseData

    @classmethod
    def createCustomer(cls, data):
        responseData = cls.customerDAO.createNewCustomer(data.get('name'), data.get('username'), data.get('password'),
                                                         data.get('email'),
                                                         data.get('contact_no'))

        cls.emailService.custCreateMail(responseData.get('customer_id'), responseData.get('email'))
        return responseData

    @classmethod
    def customerLogin(cls, data):
        customerData = cls.customerDAO.customerLogin(data.get('customer_id'), data.get('password'))
        session['loginData'] = customerData
        responseData = cls.roomService.getAllRooms()
        session['RoomsData'] = responseData
        return responseData

    @classmethod
    def checkCustomerFromSessionID(cls, headerData):
        responseData = cls.customerDAO.checkCustomerFromSessionID(headerData)

        if responseData is not None:
            return responseData
        else:
            return False
