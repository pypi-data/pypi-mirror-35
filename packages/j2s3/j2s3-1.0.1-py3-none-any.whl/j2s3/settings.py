template = """<settings xmlns="http://maven.apache.org/SETTINGS/1.0.0"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.0.0 http://maven.apache.org/xsd/settings-1.0.0.xsd">
  <servers>
    <server>
      <id>s3.artifacts.release</id>
      <username>{aws_access_key_id}</username>
      <password>{aws_secret_key}</password>
      <filePermissions>AuthenticatedRead</filePermissions>
    </server>
    <server>
      <id>s3.artifacts.snapshot</id>
      <username>{aws_access_key_id}</username>
      <password>{aws_secret_key}</password>
      <filePermissions>AuthenticatedRead</filePermissions>
    </server>
  </servers>
</settings>"""


class Settings:

    def __init__(self, aws_access_key_id, aws_secret_key):
        self.rendered = template.format(aws_access_key_id=aws_access_key_id, aws_secret_key=aws_secret_key)

    def tostring(self):
        return self.rendered
