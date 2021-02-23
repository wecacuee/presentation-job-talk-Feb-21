try:
    from bayes_cbf.unicycle_move_to_pose import unicycle_bayes_cbf_safe_obstacle_vis
except ImportError:
    import subprocess
    subprocess.run("pip install git+ssh://git@github.com/wecacuee/BayesCBF.git@v1.2.4".split())
    from bayes_cbf.unicycle_move_to_pose import unicycle_bayes_cbf_safe_obstacle_vis

import os.path
unicycle_bayes_cbf_safe_obstacle_vis(os.path.dirname(__file__) or ".")
