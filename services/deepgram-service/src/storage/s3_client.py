import logging
import boto3
from botocore.exceptions import ClientError
from pathlib import Path
from src.config import settings

logger = logging.getLogger(__name__)

class S3Storage:
    """S3-compatible storage client. Works w/ MiniO for local dev and AWS S3 for production."""

    def __init__(self):
        """Initialize S3 client with credentials from settings."""
        
        s3_config = {
            'aws_access_key_id': settings.s3_access_key,
            'aws_secret_access_key': settings.s3_secret_key,
        }

        if settings.s3_endpoint:
            s3_config['endpoint_url'] = settings.s3_endpoint
            logger.info(f"Using MinIO endpoint: {settings.s3_endpoint}")
        else:
            if settings.s3_region:
                s3_config['region_name'] = settings.s3_region
            logger.info(f"Using AWS S3 in region: {settings.s3_region}")

        self.s3 = boto3.client('s3', **s3_config)
        self.bucket = settings.s3_bucket

        if settings.s3_endpoint:
            self._ensure_bucket_exists()

    def _ensure_bucket_exists(self):
        """Create bucket if it doesn't exist and set public-read policy (MinIO only)."""
        import json

        try:
            self.s3.head_bucket(Bucket=self.bucket)
            logger.debug(f"Bucket {self.bucket} exists")
        except ClientError as e:
            error_code = e.response.get('Error', {}).get('Code')
            if error_code == '404':
                logger.info(f"Creating bucket {self.bucket}")
                self.s3.create_bucket(Bucket=self.bucket)
            else:
                logger.error(f"Error checking bucket: {e}")
                raise

        # Set public-read bucket policy (MinIO ignores ACL headers by default)
        policy = {
            "Version": "2012-10-17",
            "Statement": [{
                "Effect": "Allow",
                "Principal": {"AWS": ["*"]},
                "Action": ["s3:GetObject"],
                "Resource": [f"arn:aws:s3:::{self.bucket}/*"]
            }]
        }
        try:
            self.s3.put_bucket_policy(Bucket=self.bucket, Policy=json.dumps(policy))
            logger.debug(f"Public-read policy set on bucket {self.bucket}")
        except Exception as e:
            logger.warning(f"Could not set bucket policy (may already be set): {e}")

    def upload_file(self, local_path: str, s3_key: str, content_type: str = None) -> str:
        """Upload a file to S3."""

        try:
            if not content_type:
                if s3_key.endswith('.mp3'):
                    content_type = 'audio/mpeg'
                elif s3_key.endswith('.m4a'):
                    content_type = 'audio/mp4'
                else:
                    content_type = 'application/octet-stream'

            extra_args = {
                'ContentType': content_type,
            }

            self.s3.upload_file(
                local_path,
                self.bucket,
                s3_key,
                ExtraArgs=extra_args
            )

            # Build public URL
            url = self._build_public_url(s3_key)

            logger.debug(f"Uploaded {local_path} to {url}")
            return url

        except Exception as e:
            logger.error(f"Failed to upload {local_path} to S3: {e}")
            raise

    def upload_snippet(self, job_id: str, speaker_id: str, local_path: str) -> str:
        """Upload a speaker snippet to S3."""

        s3_key = f"snippets/{job_id}/{speaker_id}.mp3"
        return self.upload_file(local_path, s3_key, content_type='audio/mpeg')

    def upload_audio(self, job_id: str, local_path: str) -> str:
        """Upload original audio file to S3."""

        ext = Path(local_path).suffix  # .m4a, .mp3, .wav, etc.
        s3_key = f"uploads/{job_id}/audio{ext}"
        return self.upload_file(local_path, s3_key)

    def delete_file(self, s3_key: str) -> bool:
        """Delete a file from S3."""

        try:
            self.s3.delete_object(Bucket=self.bucket, Key=s3_key)
            logger.debug(f"Deleted {s3_key} from S3")
            return True
        except Exception as e:
            logger.error(f"Failed to delete {s3_key}: {e}")
            return False

    def delete_job_files(self, job_id: str) -> int:
        """Delete all files for a job (audio + snippets)."""

        count = 0

        prefixes = [
            f"uploads/{job_id}/",
            f"snippets/{job_id}/"
        ]

        for prefix in prefixes:
            try:
                response = self.s3.list_objects_v2(
                    Bucket=self.bucket,
                    Prefix=prefix
                )

                if 'Contents' in response:
                    for obj in response['Contents']:
                        self.s3.delete_object(
                            Bucket=self.bucket,
                            Key=obj['Key']
                        )
                        count += 1

            except Exception as e:
                logger.error(f"Failed to delete files with prefix {prefix}: {e}")

        logger.info(f"Deleted {count} file(s) for job {job_id}")
        return count

    def _build_public_url(self, s3_key: str) -> str:
        """Build public URL for an S3 object."""
        
        # MinIO (dev) - use configured endpoint
        if settings.s3_endpoint:
            return f"{settings.s3_public_url}/{self.bucket}/{s3_key}"

        # AWS S3 (prod) - use standard URL format
        if settings.s3_region:
            return f"https://{self.bucket}.s3.{settings.s3_region}.amazonaws.com/{s3_key}"
        else:
            return f"https://{self.bucket}.s3.amazonaws.com/{s3_key}"