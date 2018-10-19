from django.db import models
from django.utils import timezone


class Show(models.Model):
    # Monday, Tuesday, Wednesday...
    day = models.CharField(max_length=50, default="  ")
    # Friday, October 19th, 2018
    date = models.DateTimeField(default="  ")
    # Percussionist Adam Lion
    title = models.CharField(max_length=200, default="  ")
    # Percussionist Adam Lion performs works on vibraphone by John Cage, Alvin Lucier, Mark Applebaum, and Sarah Hennies.
    description = models.CharField(max_length=1000, default="  ")
    # 9:00pm
    time = models.CharField(max_length=10, default="  ")
    # 18+
    age = models.CharField(max_length=5, default="  ")
    # $5
    price = models.CharField(max_length=5, default="  ")
    # https://www.freshtix.com/events/bob-log-iii-2018-08-20
    freshtix = models.CharField(max_length=200, default="n/a")

    def __str__(self):
        return self.day + " " + self.date.strftime("%m-%d-%Y %H:%M") + " " + self.title

    def next_seven(self):
        return self.date >= timezone.now() - datetime.timedelta(days=7)


class Band(models.Model):
    # Adam Faucett
    name = models.CharField(max_length=50, default="  ")
    # Rock, Indie
    genre = models.CharField(max_length=50, default="  ")
    # References Show records in DB from above
    shows = models.ManyToManyField(Show)
    # http://bandcamp/adam-faucett
    bandcamp_name = models.CharField(max_length=200, default="  ")
    # 5
    shows_played = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Press(models.Model):
    # Metro Pulse
    name = models.CharField(max_length=50, default="  ")
    # Knoxville, Tennessee's local website...
    description = models.CharField(max_length=1000, default="  ")
    # http://metropulse.com/
    website = models.CharField(max_length=500, default="  ")

    def __str__(self):
        return self.name


class Contact(models.Model):
    # Bob Loblaw
    name = models.CharField(max_length=50, default="  ")
    # 123 Main Street
    address_street = models.CharField(max_length=100, default="  ")
    # Knoxville, TN
    address_city_state = models.CharField(max_length=100, default="  ")
    # bobloblaw@law.blog.com
    email = models.CharField(max_length=50, default="  ")
    # Reference Press Model Above
    press = models.ForeignKey(Press, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " " + self.press.name
