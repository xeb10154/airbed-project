from datetime import datetime
import pytz
from django.utils import timezone
from main.models import User, Property, Booking, Experience, Location, Rating


location1 = Location(city='Glasgow',
                     country='UK',
                     imgUrl="https://via.placeholder.com/300/0000FF/808080?text=GlasgowCityImage"
                     )

location1.save()

location2 = Location(city='Edinburgh',
                     country='UK',
                     imgUrl="https://via.placeholder.com/300/0000FF/808080?text=EdinburghCityImage"
                     )

location2.save()

location3 = Location(city='Stirling',
                     country='UK',
                     imgUrl="https://via.placeholder.com/300/0000FF/808080?text=StirlingCityImage"
                     )

location3.save()

prop1 = Property(name="Small Vintage Villa",
                 beds=1,
                 price=55.50,
                 roomType="Double",
                 address="23 Earl St, Glasgow, G14 0BA, UK",
                 location=location1,
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
                 address="38 Castle Terrace, Edinburgh, EH3 9DZ, UK",
                 location=location2,
                 lat=55.947178,
                 lng=-3.201734,
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
                 address="32D Cowane St, Stirling, FK8 1JR, UK",
                 location=location3,
                 lat=55.876885,
                 lng=-4.347243,
                 maxGuests=80,
                 rooms=40,
                 details="Biggest mansion you'll find on this website.",
                 imgUrl="https://via.placeholder.com/300/0000FF/808080?text=Mansion"
                 )
prop3.save()

prop4 = Property(name="Pagination Test Thing",
                 beds=40,
                 price=3500.00,
                 roomType="Master",
                 address="32D Cowane St, Stirling, FK8 1JR, UK",
                 location=location3,
                 lat=55.876885,
                 lng=-4.347243,
                 maxGuests=80,
                 rooms=40,
                 details="Biggest mansion you'll find on this website.",
                 imgUrl="https://via.placeholder.com/300/0000FF/808080?text=Mansion"
                 )
prop4.save()

prop5 = Property(name="Pagination Test Thing",
                 beds=40,
                 price=3500.00,
                 roomType="Master",
                 address="32D Cowane St, Stirling, FK8 1JR, UK",
                 location=location3,
                 lat=55.876885,
                 lng=-4.347243,
                 maxGuests=80,
                 rooms=40,
                 details="Biggest mansion you'll find on this website.",
                 imgUrl="https://via.placeholder.com/300/0000FF/808080?text=Mansion"
                 )
prop5.save()

prop6 = Property(name="Pagination Test Thing",
                 beds=40,
                 price=3500.00,
                 roomType="Master",
                 address="32D Cowane St, Stirling, FK8 1JR, UK",
                 location=location3,
                 lat=55.876885,
                 lng=-4.347243,
                 maxGuests=80,
                 rooms=40,
                 details="Biggest mansion you'll find on this website.",
                 imgUrl="https://via.placeholder.com/300/0000FF/808080?text=Mansion"
                 )
prop6.save()

prop7 = Property(name="Pagination Test Thing",
                 beds=40,
                 price=3500.00,
                 roomType="Master",
                 address="32D Cowane St, Stirling, FK8 1JR, UK",
                 location=location3,
                 lat=55.876885,
                 lng=-4.347243,
                 maxGuests=80,
                 rooms=40,
                 details="Biggest mansion you'll find on this website.",
                 imgUrl="https://via.placeholder.com/300/0000FF/808080?text=Mansion"
                 )
prop7.save()

user1 = User(firstName="Raymond",
             lastName="Yau",
             email="raymond@test.com",
             )
user1.save()

rating1 = Rating(score=1)
rating1.save()
rating2 = Rating(score=2)
rating2.save()
rating3 = Rating(score=3)
rating3.save()
rating4 = Rating(score=4)
rating4.save()
rating5 = Rating(score=5)
rating5.save()

booking1 = Booking(user=user1,
                   property=prop1,
                   rating=rating3,
                   startDate=datetime(
                       2020, 9, 1, 15, 0, 0, 127325, tzinfo=pytz.UTC),
                   endDate=datetime(
                       2020, 9, 5, 15, 0, 0, 127325, tzinfo=pytz.UTC)
                   )
booking1.save()

booking2 = Booking(user=user1,
                   property=prop2,
                   rating=None,
                   startDate=datetime(
                       2020, 9, 24, 15, 0, 0, 127325, tzinfo=pytz.UTC),
                   endDate=datetime(
                       2020, 9, 30, 15, 0, 0, 127325, tzinfo=pytz.UTC)
                   )
booking2.save()

booking3 = Booking(user=user1,
                   property=prop7,
                   rating=None,
                   startDate=datetime(
                       2020, 11, 1, 15, 0, 0, 127325, tzinfo=pytz.UTC),
                   endDate=datetime(
                       2020, 11, 10, 15, 0, 0, 127325, tzinfo=pytz.UTC)
                   )
booking3.save()

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
