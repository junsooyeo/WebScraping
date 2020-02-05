from indeed import get_indeed_jobs
from saramin import get_saramin_jobs
from save import save_to_file

indeed_jobs = get_indeed_jobs()
saramin_jobs = get_saramin_jobs()
jobs = indeed_jobs+saramin_jobs
save_to_file(jobs)

