import boto3
import os
import json
from demography.conf import settings


def get_bucket():
    session = boto3.session.Session(
        region_name=settings.AWS_REGION,
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    )
    s3 = session.resource("s3")
    return s3.Bucket(settings.AWS_S3_BUCKET)


class UploadData(object):
    @staticmethod
    def upload_division(division, subdivision_level, data):
        bucket = get_bucket()

        for series in data.keys():
            for year in data[series].keys():
                for table in data[series][year].keys():
                    key = os.path.join(
                        settings.AWS_S3_UPLOAD_ROOT, series, year, table
                    )

                    if division == "nation":
                        key = os.path.join(
                            key, "{}.json".format(subdivision_level)
                        )
                    else:
                        key = os.path.join(
                            key,
                            division.code,
                            "{}.json".format(subdivision_level),
                        )

                    bucket.put_object(
                        Key=key,
                        ACL=settings.AWS_ACL,
                        Body=json.dumps(data[series][year][table]),
                        CacheControl=settings.AWS_CACHE_HEADER,
                        ContentType="application/json",
                    )
