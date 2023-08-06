import os
import shutil

from libensemble.register import Register
from libensemble.controller import Job, JobController, JobControllerException

def setup_module(module):
    print ("setup_module      module:%s" % module.__name__)
    if JobController.controller is not None:
        ctrl = JobController.controller
        del ctrl
        JobController.controller = None
    if Register.default_registry:
        defreg = Register.default_registry
        del defreg
        Register.default_registry = None

def setup_function(function):
    print ("setup_function    function:%s" % function.__name__)
    if JobController.controller is not None:
        ctrl = JobController.controller
        del ctrl
        JobController.controller = None
    if Register.default_registry:
        defreg = Register.default_registry
        del defreg
        Register.default_registry = None

def teardown_module(module):
    print ("teardown_module   module:%s" % module.__name__)
    if JobController.controller is not None:
        ctrl = JobController.controller
        del ctrl
        JobController.controller = None
    if Register.default_registry:
        defreg = Register.default_registry
        del defreg
        Register.default_registry = None


def test_job_funcs():
    dummyappname = os.getcwd() + '/myapp.x'
    registry = Register()
    jobctrl = JobController(registry = registry, auto_resources = False)
    registry.register_calc(full_path=dummyappname, calc_type='gen', desc='A dummy calc')
    registry.register_calc(full_path=dummyappname, calc_type='sim', desc='A dummy calc')

    dirname = 'dir_jobc_tests'
    if os.path.exists(dirname):
        shutil.rmtree(dirname)
    os.mkdir(dirname)
    os.chdir(dirname)
    myworkdir=os.getcwd()

    #First try no app - check exception raised?
    jc_triggered = False
    try:
        job = Job(workdir = myworkdir, stdout = 'stdout.txt')
    except JobControllerException:
        jc_triggered = True
    assert jc_triggered, "Failed to raise exception if create job with no app"

    #Now with no workdir specified
    dummyapp = registry.gen_default_app
    job1 = Job(app = dummyapp, stdout = 'stdout.txt')
    wd_exist = job1.workdir_exists()
    assert not wd_exist #, "No workdir specified, yet workdir_exists does not return False"
    stdout_exist = job1.stdout_exists()
    assert not stdout_exist
    f_exist = job1.file_exists_in_workdir('running_output.txt')
    assert not f_exist

    #Create job properly specified
    job2 = Job(app = dummyapp, workdir = myworkdir ,stdout = 'stdout.txt')

    #Workdir does exist
    wd_exist = job2.workdir_exists()
    assert wd_exist

    #Files do not exist
    stdout_exist = job2.stdout_exists()
    assert not stdout_exist
    f_exist = job2.file_exists_in_workdir('running_output.txt')
    assert not f_exist

    valerr_triggered = False
    try:
        job2.read_stdout()
    except ValueError:
        valerr_triggered = True
    assert valerr_triggered

    valerr_triggered = False
    try:
        job2.read_file_in_workdir('running_output.txt')
    except ValueError:
        valerr_triggered = True
    assert valerr_triggered

    #Now create files and check positive results
    with open("stdout.txt","w") as f:
        f.write('This is stdout')
    with open("running_output.txt","w") as f:
        f.write('This is running output')

    #job2 = Job(app = dummyapp, workdir = myworkdir ,stdout = 'stdout.txt')
    #wd_exist = job2.workdir_exists()
    #assert wd_exist
    stdout_exist = job2.stdout_exists()
    assert stdout_exist
    f_exist = job2.file_exists_in_workdir('running_output.txt')
    assert f_exist
    assert 'This is stdout' in job2.read_stdout()
    assert 'This is running output' in job2.read_file_in_workdir('running_output.txt')

    #Check if workdir does not exist
    job2.workdir = job2.workdir + '/bubbles'
    wd_exist = job2.workdir_exists()
    assert not wd_exist

    os.chdir('../')
    shutil.rmtree(dirname)

if __name__ == "__main__":
    test_job_funcs()

