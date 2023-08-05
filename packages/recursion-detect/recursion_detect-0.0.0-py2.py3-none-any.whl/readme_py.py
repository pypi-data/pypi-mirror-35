#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import mdown
import readme_md
from public import public
import runcmd
import setupcfg

# path/to/repo/
# path/to/repo/.edit/README/section/text.md
# path/to/repo/.edit/README/section/body.md

# output:
# path/to/repo/REAME.md
# path/to/repo/.tmp/pypi.org/REAME.md


@public
class Readme(readme_md.Readme):
    def validate(self):
        for path in ["setup.py", "setup.cfg"]:
            if not os.path.exists(path):
                raise OSError("%s NOT EXISTS" % path)
        return self

    @property
    def pip_install(self):
        return """```bash
$ [sudo] pip install %s
```""" % self.name

    @property
    def install(self):
        return self.pip_install

    @property
    def name(self):
        return setupcfg.get("metadata", "name")

    @property
    def packages(self):
        return setupcfg.get("options", "packages", [])

    @property
    def py_modules(self):
        return setupcfg.get("options", "py_modules", [])

    @property
    def scripts(self):
        return setupcfg.get("options", "scripts", [])

    @property
    def usage(self):
        usages = []
        for path in self.scripts:
            if os.path.basename(path)[0] == ".":
                continue
            src = open(path).read()
            if "--help" not in src:
                continue
            runcmd.run(["chmod", "+x", path])._raise()
            cmd = [path, "--help"]
            r = runcmd.run(cmd)
            r._raise()
            if not r.text:
                raise ValueError("'%s' - EMPTY OUTPUT" % cmd)
            code = mdown.code(r.text, "bash")
            usages.append(code)
        for module in self.py_modules:
            path = "%s.py" % module
            src = open(path).read()
            # module must contains: if __name__ == "__main__"
            if "__name__" in src and "__main__" in src:
                cmd = ["python", path, "--help"]
                r = runcmd.run(cmd)
                r._raise()
                if not r.out:
                    raise ValueError("'%s' - EMPTY OUTPUT" % cmd)
                code = mdown.code(r.out, "bash")
                usages.append(code)
        return "\n".join(usages)


USAGE = 'usage: python -m %s' % __file__.split("/")[-1].split(".")[0]


def _cli():
    for path in ["setup.py", "setup.cfg"]:
        if not os.path.exists(path):
            raise OSError("%s NOT EXISTS" % path)
    print(Readme().render())


if __name__ == '__main__':
    if sys.argv[-1] == "--help":
        print(USAGE)
        sys.exit(0)
    _cli()
