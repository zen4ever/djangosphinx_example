from django.core.management import setup_environ
import settings

setup_environ(settings)

from jobs.models import Job

Job.objects.create(title="Programmer Needed",
                   description="Django Developer",
                   tags="django, job",
                   latitude=34.018003,
                   longitude=-118.474725)

import math

def to_radians(lat, long):
    return (math.radians(lat),math.radians(long))

lat, long = to_radians(34.095259, -118.347997)

mi = 1609.344

job_list = (
     Job.search.geoanchor('lat', 'long', lat, long)
               .filter(**{'@geodist__lt':10*mi})
               .order_by('-@geodist')
)

print [x.sphinx.values() for x in job_list]
