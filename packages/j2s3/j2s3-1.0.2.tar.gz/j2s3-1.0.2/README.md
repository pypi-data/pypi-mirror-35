# Java 2 S3
Python library for publishing maven projects to an S3 maven repository. Requires maven installed in your path.

## Example

```python
from j2s3.main import publish
# project_directory is a dir containing Java code and a pom.xml file
publish(project_directory, aws_access_key_id, aws_secret_access_key, s3_bucket_name)
```

## Contributing
Pull requests and bug reports welcome on the github repository.