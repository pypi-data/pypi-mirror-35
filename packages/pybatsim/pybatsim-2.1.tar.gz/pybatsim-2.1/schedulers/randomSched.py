from batsim.batsim import BatsimScheduler

from random import sample


class RandomSched(BatsimScheduler):

    def __init__(self, options):
        self.options = options

    def onAfterBatsimInit(self):
        self.res = [x for x in range(self.bs.nb_res)]
        self.jobs_res = {}
        self.openJobs = set()
        self.sched_delay = 0

    def scheduleJobs(self):
        scheduledJobs = []

        for job in self.openJobs:
            res = sample(self.res, job.requested_resources)

        # Iterating over all open jobs
        for job in set(self.openJobs):
            self.jobs_res[job.id] = res
            scheduledJobs.append(job)

        # Clearing open jobs
        self.openJobs = set()

        # update time
        self.bs.consume_time(self.sched_delay)

        # send to uds
        if len(scheduledJobs) > 0:
            self.bs.start_jobs(scheduledJobs, self.jobs_res)

    def onJobSubmission(self, job):
        self.openJobs.add(job)
        self.scheduleJobs()

    def onJobCompletion(self, job):
        pass
