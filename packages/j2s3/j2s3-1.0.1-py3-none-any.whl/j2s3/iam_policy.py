template = """
{{
  "Version": "2012-10-17",
  "Statement": [
    {{
      "Sid": "",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": [
        "arn:aws:s3:::{bucket_name}/snapshot/*",
        "arn:aws:s3:::{bucket_name}/release/*"
      ]
    }}
  ]
}}"""


def get_iam_policy(bucket_name):
    return template.format(bucket_name=bucket_name)
