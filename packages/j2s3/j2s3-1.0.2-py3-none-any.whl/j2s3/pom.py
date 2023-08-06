from .xml_service import parse_xml_string
from lxml import etree

class Pom:
    # xmlns namespace
    tag_prefix = '{http://maven.apache.org/POM/4.0.0}'
    var_artifact_repo_url = 'artifactrepo.url'
    extension_group_id = 'org.kuali.maven.wagons'
    extension_artifact_id = 'maven-s3-wagon'
    extension_version = '1.2.1'

    def __init__(self, xmlstring, bucket_name):
        self.bucket_name = bucket_name
        self.root = parse_xml_string(xmlstring)

        self.set_artifact_repo_url(bucket_name)
        self.set_distribution_management()
        self.set_build_extensions()

    def set_build_extensions(self):
        build = self.get_or_create(self.root, 'build')
        extensions = self.get_or_create(build, 'extensions')
        # see if s3 wagen is already present, if not add it
        if True:
            extension = self.get_or_create(extensions, 'extension')
            # add the maven wagon to the extensions
            groupId = self.get_or_create(extension, 'groupId')
            groupId.text = self.extension_group_id
            artifactId = self.get_or_create(extension, 'artifactId')
            artifactId.text = self.extension_artifact_id
            version = self.get_or_create(extension, 'version')
            version.text = self.extension_version

    def set_distribution_management(self):
        distribution_management = self.get_or_create(self.root, 'distributionManagement')
        # set repository
        repository = self.get_or_create(distribution_management, 'repository')
        repository_id = self.get_or_create(repository, 'id')
        repository_id.text = 's3.artifacts.release'
        repository_url = self.get_or_create(repository, 'url')
        repository_url.text = 's3://${%s}/release' % self.var_artifact_repo_url
        # set snapshotRepository
        snapshot_repository = self.get_or_create(distribution_management, 'snapshotRepository')
        snapshot_repository_id = self.get_or_create(snapshot_repository, 'id')
        snapshot_repository_id.text = 's3.artifacts.snapshot'
        snapshot_repository_url = self.get_or_create(snapshot_repository, 'url')
        snapshot_repository_url.text = 's3://${%s}/snapshot' % self.var_artifact_repo_url

    def set_artifact_repo_url(self, bucket_name):
        properties = self.get_or_create(self.root, 'properties')
        artifactrepo_url = self.get_or_create(properties, self.var_artifact_repo_url)
        artifactrepo_url.text = bucket_name

    def get(self, root, tag):
        return root.find('.//' + self.tag_prefix + tag)

    def get_xpath(self, root, query):
        return root.xpath('.//' + query)

    def create(self, root, tag):
        return etree.SubElement(root, tag)

    def get_or_create(self, root, tag):
        elem = self.get(root, tag)
        return elem if elem is not None else self.create(root, tag)

    def tostring(self):
        return etree.tostring(self.root).decode()


