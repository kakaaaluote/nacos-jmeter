import sys
sys.path.append("../nacos-jmeter")

from nacos import Nacos
import settings


stage = sys.argv[1]
snapshot_dir = sys.argv[2]
if stage == "ci":
    host = settings.HOST_CI
elif stage == "testonline":
    host = settings.HOST_TESTONLINE
elif stage == "predeploy":
    host = settings.HOST_PREDEPLOY
else:
    raise ValueError("stage error")
nacos_new = Nacos(host, settings.PORT)
nacos_new.make_snapshot(snapshot_dir)
