from datetime import datetime
import pytz
from django.utils import timezone
from main.models import User, Property, Booking, Experience

prop1 = Property(name="Small Vintage Villa",
                 beds=1,
                 price=55.50,
                 roomType="Double",
                 rating=5,
                 address="23 Earl St, Glasgow, G14 0BA, UK",
                 lat=55.876885,
                 lng=-4.347243,
                 maxGuests=2,
                 rooms=1,
                 details="This small villa in the country side of Fife provides all the amenities you need to have a relaxed and care-free holiday.",
                 imgUrl="https://via.placeholder.com/300/0000FF/808080?text=Raymond"
                 )
prop1.save()

prop2 = Property(name="Modern City Flat",
                 beds=2,
                 price=120.00,
                 roomType="Double",
                 rating=4,
                 address="23 Earl St, Glasgow, G14 0BA, UK",
                 lat=55.876885,
                 lng=-4.347243,
                 maxGuests=4,
                 rooms=2,
                 details="Spend you weekend in the liveliest city in Scotland!.",
                 imgUrl="https://via.placeholder.com/300/0000FF/808080?text=Rique"
                 )
prop2.save()

prop3 = Property(name="Downton Fucking Abbey",
                 beds=40,
                 price=3500.00,
                 roomType="Master",
                 rating=5,
                 address="23 Earl St, Glasgow, G14 0BA, UK",
                 lat=55.876885,
                 lng=-4.347243,
                 maxGuests=80,
                 rooms=40,
                 details="Biggest mansion you'll find on this website.",
                 imgUrl="https://via.placeholder.com/300/0000FF/808080?text=Mansion"
                 )
prop3.save()

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

experience1 = Experience(title='Tour bus in the city!',
                         location='Glasgow',
                         category='Tour',
                         description='Tour the city with our experienced guides. We can speak 8 different languages!',
                         price=59.99,
                         imgUrl="https://via.placeholder.com/300/0000FF/808080?text=BusTour"
                         )

experience1.save()

experience2 = Experience(title='Mountain climbing!',
                         location='Loch Lomond',
                         category='Outdoors',
                         description='Enjoy the scenery with our group of outdoor enthusiasts!',
                         price='0.00',
                         imgUrl="https://via.placeholder.com/300/0000FF/808080?text=Mountains"
                         )

experience2.save()
