from datetime import datetime
import pytz
from django.utils import timezone
from main.models import User, Property, Booking

prop1 = Property(name="Small Vintage Villa",
                 beds=1,
                 price=55.50,
                 roomType="Double",
                 rating=5,
                 location="United Kingdom",
                 lat=55.876885,
                 lng=-4.347243,
                 maxGuests=2,
                 rooms=1,
                 details="This small villa in the country side of Fife provides all the amenities you need to have a relaxed and care-free holiday.",
                 imgUrl="https://via.placeholder.com/600/92c952"
                 )
prop1.save()

user1 = User(firstName="Raymond",
             lastName="Yau",
             email="raymond@test.com",
             )
user1.save()

booking1 = Booking(user=user1,
                   property=prop1,
                   startDate=datetime(
                       2019, 9, 1, 15, 0, 0, 127325, tzinfo=pytz.UTC),
                   endDate=datetime(
                       2019, 9, 25, 15, 0, 0, 127325, tzinfo=pytz.UTC)
                   )
booking1.save()
