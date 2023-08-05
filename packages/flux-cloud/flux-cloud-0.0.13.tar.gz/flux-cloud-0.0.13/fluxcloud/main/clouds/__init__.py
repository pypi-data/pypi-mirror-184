from .aws import AmazonCloud
from .google import GoogleCloud

# backends = {"aws": AmazonCloud}
clouds = {"google": GoogleCloud, "gcp": GoogleCloud, "aws": AmazonCloud}
cloud_names = list(clouds)


def get_cloud(name):
    return clouds.get(name)
