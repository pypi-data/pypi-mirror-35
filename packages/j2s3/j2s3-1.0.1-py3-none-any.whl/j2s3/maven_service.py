import subprocess


def deploy(dir_path, settings_path):
    # maven deploy in dir
    cmd = ['mvn', '--settings', settings_path, 'deploy']
    deploy_process = subprocess.Popen(cmd, cwd=dir_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = deploy_process.communicate()
    if deploy_process.returncode > 0:
        msg = 'Command `%s` failed with `%s`\n\n%s\n\n`%s`' % (''.join(cmd), deploy_process.returncode, out, err)
        raise Exception(msg)



