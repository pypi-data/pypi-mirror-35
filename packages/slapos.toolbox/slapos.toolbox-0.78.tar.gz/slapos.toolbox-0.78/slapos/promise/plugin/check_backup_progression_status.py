from zope import interface as zope_interface
from slapos.grid.promise import interface
from slapos.grid.promise.generic import GenericPromise
import os

class RunPromise(GenericPromise):

  zope_interface.implements(interface.IPromise)

  def __init__(self, config):
    GenericPromise.__init__(self, config)
    self.setPeriodicity(minute=5)

  def sense(self):
    partition_folder = self.getPartitionFolder()
    status_path = self.getConfig('status-path')

    if not status_path or not os.path.exists(status_path):
      self.logger.info("Promise status is not present yet.")
      self.logger.info("Status path is: %r" % status_path)
      return
    with open(status_path) as f:
      try:
        date, statistic_path, message = f.read().split(',')
      except ValueError, e:
        self.logger.error("Status content is not valid: %s" % e)
        return
 
      if 'failed' not in message:
        # this backup failed
        stat_message = ""
        if os.path.exists(statistic_path):
          with open(statistic_path) as stat_f:
            stat_message = stat_f.read()
        self.logger.info("%s, %s. \n\n%s" % (date, message, stat_message))
      else:
        self.logger.error("%s, %s" % (date, message))

  def test(self):
    # we skip cheking backup status promise in slapgrid mode
    return TestResult(problem=False, message="")

  def anomaly(self):
    return self._test(result_count=2, failure_amount=2)
