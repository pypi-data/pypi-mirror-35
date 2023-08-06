# jenkenv

Virtualenvs for jenkinsfile-runner

## Overview

This tool uses a pre-built release of [kohsuke/jenkinsfile-runner](https://github.com/kohsuke/jenkinsfile-runner). It provides a set of commands that make it easy to test your code with Jenkins without jumping through the usual hoops. You can either set your preferred Jenkins version local to your project, or globally as a default. To get started:

```
pip install jenkenv
```

Once installed, if you don't know the version you want to use, run: `jenkenv install -l` or:

```sh
jenkenv install 2.121.3
jenkenv use local 2.121.3
```

Now you'll want to install your plugins. Just run: `jenkenv run-jenkins`. The administrator password will output to stdout. Once your plugins are installed (assuming you have a Jenkinsfile), run `jenkenv run Jenkinsfile`. All output pipes to stdout and `jenkenv` will exit with the builds return status. 
