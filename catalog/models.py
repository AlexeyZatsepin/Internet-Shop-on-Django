from django.db import models
from datetime import *
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Category(models.Model):
    class Meta():
        db_table = "Category"
        ordering = ['category_title']

    def __str__(self):
        return self.category_title

    category_title = models.CharField(max_length=20)

    def get_absolute_url(self):
        return "/categories/%i/" % self.id


class Product(models.Model):
    distributors = (
        ('Apple', 'Apple'),
        ('HTC', 'HTC'),
        ('Lenovo', 'Lenovo'),
        ('Samsung', 'Samsung'),
        ('Meizu', 'Meizu'),
        ('Xiaomi', 'Xiaomi'),
        ('Sony', 'Sony'),
        ('HP', 'HP'),
        ('Acer', 'Acer'),
        ('Microsoft', 'Microsoft'),
        ('LG', 'LG'),
        ('Transend', 'Transend'),
        ('Impression', 'Impression'),
    )
    product_category = models.ForeignKey(Category)
    product_distributor = models.CharField(max_length=10, choices=distributors)
    product_title = models.CharField(max_length=20)
    product_short_discription = models.TextField()
    product_img = models.ImageField(upload_to="images")
    product_cost = models.PositiveIntegerField(default=0)
    product_presence = models.BooleanField()
    release_date = models.DateTimeField(default=datetime.now)

    def is_available(self):
        if self.product_presence:
            return 'Exists'
        else:
            return 'Not exist'

    def __str__(self):
        return self.product_title
        # class Meta():
        #    abstract = True

    def get_absolute_url(self):
        return "/product/%i/" % self.id


class Comment(models.Model):
    class Meta():
        db_table = "Comments"
        ordering = ['comment_date']

    def __str__(self):
        return self.comment_text

    comment_text = models.TextField("recall", help_text="Leave a comment")
    comment_date = models.DateTimeField(default=datetime.now)
    comment_product = models.ForeignKey(Product)
    comment_author = models.ForeignKey(User)


class Cart(models.Model):
    class Meta():
        db_table = "cart"

    owner = models.ForeignKey(User)
    product = models.ForeignKey(Product, null=True, default=None)
    quantity = models.PositiveIntegerField(null=True)



class SmartPhone(Product):
    class Meta():
        db_table = "smatphone"

    SIM_CHOICES = (
        ('1', 'one'),
        ('2', 'two'),
    )
    yn_choises = (
        ('+', 'yes'),
        ('-', 'no'),
    )
    os_choises = (
        ('Android 5.1', 'Android 5.1'),
        ('Android 5.0', 'Android 5.0'),
        ('Android 4.4', 'Android 4.4'),
        ('IOS 9', 'IOS 9'),
        ('IOS 8', 'IOS 8'),
        ('Ubuntu Touch', 'Ubuntu Touch'),
        ('Windows Phone', 'Windows Phone'),
    )
    color_choises = (
        ('grey', 'grey'),
        ('white', 'white'),
        ('black', 'black'),
        ('red', 'red'),
        ('orange', 'orange'),
        ('blue', 'blue'),
    )
    ram_choises = (
        ('512Mb', '512Mb'),
        ('1024MB', '1Gb'),
        ('2048MB', '2Gb'),
        ('3Gb', '3Gb')
    )
    hdd_choises = (
        ('8GB', '8Gb'),
        ('16GB', '16Gb'),
        ('32GB', '32Gb'),
    )
    resolution_choises = (
        ('not exist', 'null'),
        ('1Mp', '1Mp'),
        ('2Mp', '2Mp'),
        ('5MP', '5Mp'),
        ('8Mp', '8Mp'),
        ('13Mp', '13Mp'),
        ('22Mp', '22Mp'),
    )
    diagonal = models.DecimalField(max_digits=5, decimal_places=1)
    display_resolution = models.CharField(max_length=10)
    operating_system = models.CharField(max_length=20, choices=os_choises)
    processor = models.CharField(max_length=20)
    cpu_frequency = models.DecimalField(max_digits=3, decimal_places=1)
    ram = models.CharField(max_length=6, choices=ram_choises)
    hdd = models.CharField(max_length=5, choices=hdd_choises)
    sim_quantity = models.CharField(max_length=1, choices=SIM_CHOICES)
    support_4g = models.BooleanField(default=False)
    resolution_main = models.CharField(max_length=5, choices=resolution_choises)
    resolution_front = models.CharField(max_length=9, choices=resolution_choises)
    wifi = models.CharField(max_length=1, choices=yn_choises, default='yes')
    bluetooth = models.CharField(max_length=1, choices=yn_choises, default='yes')
    color = models.CharField(max_length=6, choices=color_choises)


class Notebook(Product):
    class Meta():
        db_table = "notebook"

    os_choises = (
        ('Mac OS X', 'Mac OS X'),
        ('Windows 10', 'Windows 10'),
        ('Windows 8.1', 'Windows 8.1'),
        ('Windows 7 SP1', 'Windows 7 SP1'),
        ('Ubuntu', 'Ubuntu'),
        ('Linix Mint', 'Linux Mint'),
        ('UEFI', 'FreeDOS'),
        ('no OS', 'BIOS'),
        ('Chrome OS', 'Chrome OS'),
        ('Steam OS', 'Steam OS'),
    )
    color_choises = (
        ('grey', 'grey'),
        ('white', 'white'),
        ('black', 'black'),
        ('red', 'red'),
        ('orange', 'orange'),
        ('blue', 'blue'),
    )
    surface_choises = (
        ('glossy', 'glossy'),
        ('matt', 'matt'),
    )
    ram_choises = (
        ('512', '512Mb'),
        ('1024', '1Gb'),
        ('2048', '2Gb'),
        ('3Gb', '3Gb'),
        ('4Gb', '4Gb'),
        ('8Gb', '8Gb'),
        ('16Gb', '16Gb'),
    )
    hdd_choises = (
        ('500Gb', '500Gb'),
        ('750Gb', '750Gb'),
        ('1000Gb', '1Tb'),
    )
    diagonal = models.DecimalField(max_digits=5, decimal_places=2)
    display_resolution = models.CharField(max_length=10)
    surface = models.CharField(max_length=10, choices=surface_choises)
    operating_system = models.CharField(max_length=20, choices=os_choises)
    processor = models.CharField(max_length=20)
    cpu_frequency = models.DecimalField(max_digits=3, decimal_places=1)
    ram = models.CharField(max_length=6, choices=ram_choises)
    hdd = models.CharField(max_length=5, choices=hdd_choises)
    color = models.CharField(max_length=6, choices=color_choises)
    video_card = models.CharField(max_length=30)
    video_memory = models.CharField(max_length=10)


class FlashMemory(Product):
    class Meta():
        db_table = "flash"

    type_choises = (
        ('microSD', 'microSD'),
        ('usb', 'USB'),
    )
    memory_ch = (
        ('1', '1Gb'),
        ('2', '2Gb'),
        ('4', '4Gb'),
        ('8', '8Gb'),
        ('16', '16Gb'),
        ('32', '32Gb'),
        ('64', '64Gb'),
        ('128', '128Gb'),
    )
    type = models.CharField(max_length=8, choices=type_choises)
    memory = models.CharField(max_length=4, choices=memory_ch)


class TV(Product):
    class Meta():
        db_table = "tv"

    surface_choises = (
        ('glossy', 'glossy'),
        ('matt', 'matt'),
    )
    diagonal = models.DecimalField(max_digits=5, decimal_places=2)
    display_resolution = models.CharField(max_length=10)
    surface = models.CharField(max_length=10, choices=surface_choises)
    smartTV = models.BooleanField()


class Email(models.Model):
    email = models.EmailField()
