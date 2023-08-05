from django.db import models


class Attempt(models.Model):
    username = models.CharField(max_length=255, verbose_name='Username', blank=False, null=False)
    useragent = models.CharField(max_length=255, verbose_name='Useragent', blank=False, null=False)
    ipaddress = models.GenericIPAddressField(verbose_name='IP Address', null=False, blank=False)
    get_data = models.TextField(verbose_name='GET Data', blank=False, null=False)
    post_data = models.TextField(verbose_name='POST Data', blank=False, null=False)
    http_accept = models.CharField('HTTP Accept', max_length=255)
    path_info = models.CharField(verbose_name='Path', max_length=255)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Attempt created time')

    def __str__(self):
        return u'Attempt on: %s' % self.created

    class Meta:
        ordering = ['-created']
