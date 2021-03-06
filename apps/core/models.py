from django.db import models
from django.contrib.auth.models import AbstractUser
from phone_field import PhoneField


class Person(AbstractUser):
    qualifications = models.ManyToManyField(
        'Qualification',
        blank=True,
        verbose_name="Qualifikation",
    )
    qualification_specific = models.CharField(
        max_length=60,
        null=True,
        blank=True,
        verbose_name="Qualif. Details",
    )
    restrictions = models.ManyToManyField(
        'Restriction',
        blank=True,
        verbose_name="Einschränkung",
    )
    restriction_specific = models.CharField(
        max_length=60,
        null=True,
        blank=True,
        verbose_name="Einschränkung Details",
    )
    occupation = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Beruf",
    )
    street = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Straße",
    )
    number = models.CharField(
        max_length=8,
        null=True,
        blank=True,
        verbose_name="Hausnr.",
    )
    postal_code = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="PLZ",
    )
    city = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name="Ort",
    )
    remark = models.CharField(
        max_length=1000,
        null=True,
        blank=True,
        verbose_name="Anmerkungen",
    )

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    class Meta:
        verbose_name = "Registrierter Helfer"
        verbose_name_plural = "Registrierte Helfer"


class ActionCategory(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    
    def __str__(self):
        return '%s' % self.name

    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = "Einsatzkategorie"
        verbose_name_plural = "Einsatzkategorien"


class Qualification(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return '%s' % self.name

    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = "Qualifikation"
        verbose_name_plural = "Qualifikationen"


class Restriction(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return '%s' % self.name

    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = "Einschränkung"
        verbose_name_plural = "Einschränkungen"


class EquipmentProvided(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return '%s' % self.name

    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = "Ausstattung durch HiOrg"
        verbose_name_plural = "Ausstattungen durch HiOrg"


class EquipmentSelf(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return '%s' % self.name

    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = "Ausstattung mitzubringen"
        verbose_name_plural = "Ausstattungen mitzubringen"


class PublicationCategory(models.Model):
    title = models.CharField(max_length=30, null=True, blank=True)
    slug = models.CharField(max_length=30, unique=True, null=False, blank=False)
    
    def __str__(self):
        return '%s' % self.title

    def __unicode__(self):
        return '%s' % self.title

    class Meta:
        verbose_name = "Artikelkategorie"
        verbose_name_plural = "Artikelkategorien"


class MixinPublication(models.Model):
    title = models.CharField(max_length=60, unique=True, null=False, blank=False, default="none")
    slug = models.CharField(max_length=60, unique=True, null=False, blank=False)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    #topic = models.ForeignKey(PublicationCategory, on_delete=models.SET_NULL, null=True, blank=False)


class MulticastMessage(MixinPublication, models.Model):
    combined_and_or = models.CharField(max_length=60, null=False, blank=False)
    qualifications = models.ManyToManyField(Qualification)
    restrictions_excluded = models.ManyToManyField(Restriction)
    equipment_provided = models.ManyToManyField(EquipmentProvided)
    equipment_self = models.ManyToManyField(EquipmentSelf)

    def __str__(self):
        return '%s' % self.title

    def __unicode__(self):
        return '%s' % self.title

    class Meta:
        verbose_name = "Mitteilungsversand"
        verbose_name_plural = "Mitteilungsversand"


class BlogEntry(MixinPublication, models.Model):
    def __unicode__(self):
        return '%s' % self.title

    def __str__(self):
        return '%s' % self.title

    class Meta:
        verbose_name = "Webseiteneintrag"
        verbose_name_plural = "Webseiteneinträge"


class SentArchive(models.Model):
    person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, blank=True)
    current_email = models.EmailField(max_length=50, null=False, blank=False, unique=True)
    multicast_message = models.ManyToManyField(MulticastMessage)
    confirmed = models.CharField(max_length=60, null=False, blank=False)

    class Meta:
        verbose_name = "Einzelversandarchiv"
        verbose_name_plural = "Einzelversandarchive"
