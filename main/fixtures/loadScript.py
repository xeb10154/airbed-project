from datetime import datetime
import pytz
from django.utils import timezone
from main.models import User, Property, Booking, \
    Experience, Location, Rating, Review, Gallery


user1 = User(firstName="Raymond",
             lastName="Yau",
             email="raymond@test.com",
             )
user1.save()


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

location3 = Location(city='Highclere',
                     country='UK',
                     imgUrl="https://via.placeholder.com/300/0000FF/808080?text=StirlingCityImage"
                     )

location3.save()


prop1 = Property(name="Family Scotstoun flat",
                 beds=3,
                 price=55.50,
                 roomType="Double",
                 address="23 Earl St, Glasgow, G14 0BA, UK",
                 location=location1,
                 lat=55.876885,
                 lng=-4.347243,
                 maxGuests=3,
                 rooms=1,
                 tagline="This small villa in the country side of Fife provides all the amenities you need to have a relaxed and care-free holiday.",
                 info="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sed nisl non libero tristique tincidunt ac ultricies quam. Donec ut justo congue, sodales tellus sit amet, accumsan dui. Nulla vel quam sed metus luctus sagittis nec vel ante. Fusce eu nisl eu quam tempus lobortis. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus id augue posuere dolor placerat sagittis. Aliquam at dui sit amet massa hendrerit pulvinar sit amet nec quam. Pellentesque efficitur tempus arcu, in pharetra tortor sodales a. Nulla facilisi."
                 )
prop1.save()

prop2 = Property(name="Milngavie walker's flat",
                 beds=2,
                 price=120.00,
                 roomType="Double",
                 address="38 Castle Terrace, Edinburgh, EH3 9DZ, UK",
                 location=location2,
                 lat=55.947178,
                 lng=-3.201734,
                 maxGuests=2,
                 rooms=2,
                 tagline="The starting point for the West Highland Way! Perfect for outdoor lovers.",
                 info="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sed nisl non libero tristique tincidunt ac ultricies quam. Donec ut justo congue, sodales tellus sit amet, accumsan dui. Nulla vel quam sed metus luctus sagittis nec vel ante. Fusce eu nisl eu quam tempus lobortis. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus id augue posuere dolor placerat sagittis. Aliquam at dui sit amet massa hendrerit pulvinar sit amet nec quam. Pellentesque efficitur tempus arcu, in pharetra tortor sodales a. Nulla facilisi."
                 )
prop2.save()

prop3 = Property(name="Downton Bloody Abbey",
                 beds=40,
                 price=3500.00,
                 roomType="Master",
                 address="32D Cowane St, Stirling, FK8 1JR, UK",
                 location=location3,
                 lat=55.876885,
                 lng=-4.347243,
                 maxGuests=80,
                 rooms=40,
                 tagline="Biggest mansion you'll find on this website.",
                 info="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sed nisl non libero tristique tincidunt ac ultricies quam. Donec ut justo congue, sodales tellus sit amet, accumsan dui. Nulla vel quam sed metus luctus sagittis nec vel ante. Fusce eu nisl eu quam tempus lobortis. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus id augue posuere dolor placerat sagittis. Aliquam at dui sit amet massa hendrerit pulvinar sit amet nec quam. Pellentesque efficitur tempus arcu, in pharetra tortor sodales a. Nulla facilisi."
                 )
prop3.save()

prop4 = Property(name="Glasgow trendy flat",
                 beds=2,
                 price=70.00,
                 roomType="Double",
                 address="32D Cowane St, Stirling, FK8 1JR, UK",
                 location=location3,
                 lat=55.876885,
                 lng=-4.347243,
                 maxGuests=2,
                 rooms=2,
                 tagline="Central location in Glasgow. Ideal for young professionals and students.",
                 info="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sed nisl non libero tristique tincidunt ac ultricies quam. Donec ut justo congue, sodales tellus sit amet, accumsan dui. Nulla vel quam sed metus luctus sagittis nec vel ante. Fusce eu nisl eu quam tempus lobortis. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus id augue posuere dolor placerat sagittis. Aliquam at dui sit amet massa hendrerit pulvinar sit amet nec quam. Pellentesque efficitur tempus arcu, in pharetra tortor sodales a. Nulla facilisi."
                 )
prop4.save()

prop5 = Property(name="Pagination Test Property",
                 beds=2,
                 price=200.00,
                 roomType="Double",
                 address="32D Cowane St, Stirling, FK8 1JR, UK",
                 location=location2,
                 lat=55.876885,
                 lng=-4.347243,
                 maxGuests=2,
                 rooms=2,
                 tagline="Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                 info="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sed nisl non libero tristique tincidunt ac ultricies quam. Donec ut justo congue, sodales tellus sit amet, accumsan dui. Nulla vel quam sed metus luctus sagittis nec vel ante. Fusce eu nisl eu quam tempus lobortis. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus id augue posuere dolor placerat sagittis. Aliquam at dui sit amet massa hendrerit pulvinar sit amet nec quam. Pellentesque efficitur tempus arcu, in pharetra tortor sodales a. Nulla facilisi."
                 )
prop5.save()

prop6 = Property(name="Pagination Test Property",
                 beds=3,
                 price=200.00,
                 roomType="Double",
                 address="32D Cowane St, Stirling, FK8 1JR, UK",
                 location=location2,
                 lat=55.876885,
                 lng=-4.347243,
                 maxGuests=3,
                 rooms=3,
                 tagline="Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                 info="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sed nisl non libero tristique tincidunt ac ultricies quam. Donec ut justo congue, sodales tellus sit amet, accumsan dui. Nulla vel quam sed metus luctus sagittis nec vel ante. Fusce eu nisl eu quam tempus lobortis. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus id augue posuere dolor placerat sagittis. Aliquam at dui sit amet massa hendrerit pulvinar sit amet nec quam. Pellentesque efficitur tempus arcu, in pharetra tortor sodales a. Nulla facilisi."
                 )
prop6.save()

prop7 = Property(name="Pagination Test Property",
                 beds=4,
                 price=200.00,
                 roomType="Master",
                 address="32D Cowane St, Stirling, FK8 1JR, UK",
                 location=location2,
                 lat=55.876885,
                 lng=-4.347243,
                 maxGuests=4,
                 rooms=4,
                 tagline="Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                 info="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sed nisl non libero tristique tincidunt ac ultricies quam. Donec ut justo congue, sodales tellus sit amet, accumsan dui. Nulla vel quam sed metus luctus sagittis nec vel ante. Fusce eu nisl eu quam tempus lobortis. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus id augue posuere dolor placerat sagittis. Aliquam at dui sit amet massa hendrerit pulvinar sit amet nec quam. Pellentesque efficitur tempus arcu, in pharetra tortor sodales a. Nulla facilisi."
                 )
prop7.save()


gallery1 = Gallery(name="highclere4_r8mdr4.jpg", property=prop3)
gallery1.save()
gallery2 = Gallery(name="highclere3_hzm90e.jpg", property=prop3)
gallery2.save()
gallery3 = Gallery(name="highclere2_oh7ium.jpg", property=prop3)
gallery3.save()
gallery4 = Gallery(name="highclere1_ayb6yc.jpg", property=prop3)
gallery4.save()
prop3.img = gallery1
prop3.save()

gallery5 = Gallery(name="scotstoun4_po0shu.jpg", property=prop1)
gallery5.save()
gallery6 = Gallery(name="scotstoun3_ccbzyc.jpg", property=prop1)
gallery6.save()
gallery7 = Gallery(name="scotstoun2_wurxvi.jpg", property=prop1)
gallery7.save()
gallery8 = Gallery(name="scotstoun1_wwq8db.jpg", property=prop1)
gallery8.save()
prop1.img = gallery5
prop1.save()

gallery9 = Gallery(name="glasgow4_mzjvry.jpg", property=prop4)
gallery9.save()
gallery10 = Gallery(name="glasgow3_xxtpdl.jpg", property=prop4)
gallery10.save()
gallery11 = Gallery(name="glasgow2_fpkmet.jpg", property=prop4)
gallery11.save()
gallery12 = Gallery(name="glasgow1_sflq1u.jpg", property=prop4)
gallery12.save()
prop4.img = gallery9
prop4.save()

gallery13 = Gallery(name="eglasgow4_unoivs.jpg", property=prop5)
gallery13.save()
gallery13a = Gallery(name="eglasgow4_unoivs.jpg", property=prop6)
gallery13a.save()
gallery13b = Gallery(name="eglasgow4_unoivs.jpg", property=prop7)
gallery13b.save()
gallery14 = Gallery(name="eglasgow3_hume03.jpg", property=prop5)
gallery14.save()
gallery14a = Gallery(name="eglasgow3_hume03.jpg", property=prop6)
gallery14a.save()
gallery14b = Gallery(name="eglasgow3_hume03.jpg", property=prop7)
gallery14b.save()
gallery15 = Gallery(name="eglasgow2_elhdsa.jpg", property=prop5)
gallery15.save()
gallery15a = Gallery(name="eglasgow2_elhdsa.jpg", property=prop6)
gallery15a.save()
gallery15b = Gallery(name="eglasgow2_elhdsa.jpg", property=prop7)
gallery15b.save()
gallery16 = Gallery(name="eglasgow1_edga3x.jpg", property=prop5)
gallery16.save()
gallery16a = Gallery(name="eglasgow1_edga3x.jpg", property=prop6)
gallery16a.save()
gallery16b = Gallery(name="eglasgow1_edga3x.jpg", property=prop7)
gallery16b.save()
prop5.img = gallery13
prop6.img = gallery13
prop7.img = gallery13
prop5.save()
prop6.save()
prop7.save()

gallery17 = Gallery(name="milngavie4_m2dtqt.jpg", property=prop2)
gallery17.save()
gallery18 = Gallery(name="milngavie3_memqjg.jpg", property=prop2)
gallery18.save()
gallery19 = Gallery(name="milngavie2_bdt0r4.jpg", property=prop2)
gallery19.save()
gallery20 = Gallery(name="milngavie1_cazxmk.jpg", property=prop2)
gallery20.save()
prop2.img = gallery17
prop2.save()


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

review1 = Review(
    rating=rating1, user='Raymond Yau',
    description='Very poor experience. The accomodation provided lacked general hygiene. Food was OK though, I just wish there was more.')
review1.save()

review2 = Review(
    rating=rating5, user='Henrique Batista',
    description='Exceptional stay at this accomodation! The host was friendly and the room as well equipped. Highly Recommended!')
review2.save()

review3 = Review(
    rating=rating4, user='John Doe',
    description='Great wee place to stay. It is a very convenient location (close to the public transport) and really good value for the price. We just found the place a bit noisy at night. A+++')
review3.save()

booking1 = Booking(user=user1,
                   property=prop1,
                   review=review1,
                   startDate=datetime(
                       2020, 9, 1, 15, 0, 0, 127325, tzinfo=pytz.UTC),
                   endDate=datetime(
                       2020, 9, 5, 15, 0, 0, 127325, tzinfo=pytz.UTC)
                   )
booking1.save()

booking2 = Booking(user=user1,
                   property=prop2,
                   review=review2,
                   startDate=datetime(
                       2020, 8, 24, 15, 0, 0, 127325, tzinfo=pytz.UTC),
                   endDate=datetime(
                       2020, 8, 30, 15, 0, 0, 127325, tzinfo=pytz.UTC)
                   )
booking2.save()

booking3 = Booking(user=user1,
                   property=prop7,
                   review=None,
                   startDate=datetime(
                       2020, 11, 1, 15, 0, 0, 127325, tzinfo=pytz.UTC),
                   endDate=datetime(
                       2020, 11, 10, 15, 0, 0, 127325, tzinfo=pytz.UTC)
                   )
booking3.save()

booking4 = Booking(user=user1,
                   property=prop2,
                   review=review3,
                   startDate=datetime(
                       2020, 3, 1, 15, 0, 0, 127325, tzinfo=pytz.UTC),
                   endDate=datetime(
                       2020, 3, 10, 15, 0, 0, 127325, tzinfo=pytz.UTC)
                   )
booking4.save()


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
