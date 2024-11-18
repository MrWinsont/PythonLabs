from peewee import *

db = SqliteDatabase('orders.db')


class Sender(Model):
    sender_id = IntegerField(primary_key=True, null=False)
    surname = CharField()
    name = CharField()
    middle_name = CharField()
    birth_date = CharField()
    Ind = CharField()
    city = CharField()
    street = CharField()
    house = CharField()
    flat = CharField()
    phone = CharField()

    class Meta:
        database = db


class Courier(Model):
    courier_id = IntegerField(primary_key=True, null=False)
    surname = CharField()
    name = CharField()
    middle_name = CharField()
    passport_id = CharField()
    birth_date = CharField()
    hiring_date = CharField()
    start_work_day = CharField()
    end_work_day = CharField()
    city = CharField()
    street = CharField()
    house = CharField()
    flat = CharField()
    phone = CharField()

    class Meta:
        database = db


class Transport(Model):
    car_num = CharField(primary_key=True, null=False)
    brand = CharField()
    registration_date = CharField()
    color = CharField()

    class Meta:
        database = db


Transport.create_table()


class Receiver(Model):
    receiver_id = IntegerField(primary_key=True, null=False)
    surname = CharField()
    name = CharField()
    middle_name = CharField()
    birth_date = CharField()
    Ind = CharField()
    city = CharField()
    street = CharField()
    house = CharField()
    flat = CharField()
    phone = CharField()

    class Meta:
        database = db


Receiver.create_table()


class Order(Model):
    order_id = IntegerField(primary_key=True, null=False)
    sender_id = ForeignKeyField(Sender, related_name='sender_id', null=False)
    receiver_id = ForeignKeyField(Receiver, related_name='receiver_id', null=False)
    order_date = CharField()
    delivery_date = CharField()
    delivery_price = CharField()
    courier_id = ForeignKeyField(Courier, related_name='courier_id', null=False)
    transport_id = ForeignKeyField(Transport, related_name='transport_id', null=False)

    class Meta:
        database = db


Order.create_table()

car1 = Transport.create(
    car_num='A000AA',
    brand='BMW',
    registration_date='12.01.1999',
    color='black'
)

car1.save()

car2 = Transport.create(
    car_num='М777УН',
    brand='toyota',
    registration_date='12.01.2024',
    color='black'
)

car2.save()

receiver1 = Receiver.create(
    receiver_id=3,
    surname='Sidorov',
    name='Igor',
    middle_name='Romanovich',
    birth_date='29.11.2004',
    Ind='6010',
    city='Moscow',
    street='Kolotuskina',
    house='29',
    flat='2',
    phone='+7911123454'
)
receiver1.save()

receiver2 = Receiver.create(
    receiver_id=4,
    surname='Sidorova',
    name='Alina',
    middle_name='Romanovna',
    birth_date='29.11.2018',
    Ind='6011',
    city='Moscow',
    street='Kolotuskina',
    house='49',
    flat='5',
    phone='+7911129483'
)
receiver2.save()

oreder1 = Order.create(
    order_id=1,
    sender_id=1,
    receiver_id=3,
    order_date='10.10.2020',
    delivery_date='10.10.2021',
    delivery_price='2500',
    courier_id=1,
    transport_id='A000AA'
)
oreder1.save()

oreder2 = Order.create(
    order_id=2,
    sender_id=1,
    receiver_id=4,
    order_date='10.10.2020',
    delivery_date='15.12.2020',
    delivery_price='50000',
    courier_id=1,
    transport_id='М777УН'
)
oreder2.save()